from typing import Awaitable, Callable

from fastapi import FastAPI


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    async def _shutdown() -> None:
        pass

    return _shutdown
