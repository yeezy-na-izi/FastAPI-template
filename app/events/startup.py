from typing import Awaitable, Callable

from fastapi import FastAPI


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    inthe state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    async def _startup() -> None:
        pass

    return _startup
