from typing import Optional

from pydantic import AnyHttpUrl, AnyUrl, BaseSettings


class Settings(BaseSettings):
    env: str = "local"
    postgres_dsn: AnyUrl = "cockroachdb://root@localhost:29995/test_ci"
    postgres_dsn_test: AnyUrl = "cockroachdb://root@localhost:29995/test_ci_{}"
    sentry_dsn: Optional[AnyHttpUrl] = None

    # pagination
    default_limit: int = 10
    max_limit: int = 1000


settings = Settings()
