from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from tortoise.contrib.fastapi import register_tortoise

from app.settings import get_settings
from app.web.api.router import api_router
from app.web.events import register_shutdown_event, register_startup_event
from app.web.middlewares import register_main_middleware


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    :return: FastAPI
    """

    settings = get_settings("config.toml")

    app = FastAPI(
        title=settings.info.name,
        description=settings.info.description,
        version='0.1.0',
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Adds main middleware.
    register_main_middleware(app)

    # Main router for the API.
    app.include_router(
        router=api_router,
        prefix="/api",
    )

    # Configures tortoise orm.
    register_tortoise(
        app,
        config=settings.database.get_tortoise_config(),
        add_exception_handlers=True,
        generate_schemas=True,
    )

    return app
