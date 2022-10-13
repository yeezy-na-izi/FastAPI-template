import uvicorn

from app.settings import get_settings


def main() -> None:
    """Entrypoint of the application."""
    settings = get_settings("config.toml")

    uvicorn.run(
        "app.application:get_app",
        workers=settings.api.workers_count,
        host=settings.api.host,
        port=settings.api.port,
        reload=settings.api.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()
