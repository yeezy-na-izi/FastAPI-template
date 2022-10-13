from typing import Callable, Awaitable
from urllib.request import Request

from fastapi import FastAPI


def register_main_middleware(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Register main middleware.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.middleware("http")
    async def _main_middleware(request: Request, call_next):  # noqa: WPS430

        response = await call_next(request)

        return response

    return _main_middleware
