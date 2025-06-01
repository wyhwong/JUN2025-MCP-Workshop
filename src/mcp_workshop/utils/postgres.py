import logging
from typing import Any, Iterable, Optional

import pandas as pd
import psycopg2

from mcp_workshop import env


logger = logging.getLogger(__name__)


class PostgresClient:
    """A simple client to interact with a PostgreSQL database."""

    def __init__(
        self,
        host: str = env.POSTGRES_HOST,
        port: int = env.POSTGRES_PORT,
        database: str = env.POSTGRES_DATABASE,
        user: str = env.POSTGRES_USERNAME,
        password: str = env.POSTGRES_PASSWORD,
    ):
        """Initialize the PostgresClient with database connection parameters."""

        self._config = {
            "database": database,
            "user": user,
            "password": password,
            "host": host,
            "port": port,
        }

    def _execute(self, sql: str, values: Optional[Iterable[Any]] = None) -> None:
        """Execute a query"""

        with psycopg2.connect(**self._config) as conn:
            with conn.cursor() as cursor:
                if values:
                    cursor.execute(sql, tuple(values))
                else:
                    cursor.execute(sql)
                conn.commit()

        logger.debug("Executed SQL: \n%s \nValues: %s", sql, values)

    def query(self, sql: str) -> pd.DataFrame:
        """Execute a SQL query and return the results as a pandas DataFrame."""

        # Get columns for dataframe annotation
        after_select = sql.split("SELECT", 1)[1]
        before_from = after_select.split("FROM", 1)[0]

        if "*" in before_from:
            logger.warning("Querying all columns, not able to mark columns for dataframe.")
            columns = None
        else:
            columns = before_from.replace(" ", "").replace("\n", "").replace("\t", "").split(",")
            columns = [column.split(".")[-1] for column in columns]

        with psycopg2.connect(**self._config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                data = cursor.fetchall()

        df = pd.DataFrame(data=data, columns=columns)
        return df

    def insert(self, table: str, data: dict[str, Any]) -> None:
        """Insert values into table"""

        keys = ",".join(data.keys())
        annotations = ",".join(["%s"] * len(data.keys()))

        sql = f"INSERT INTO {table}({keys}) VALUES ({annotations})"
        self._execute(sql, data.values())
