"""Middlewares of application."""

from app.web.middlewares.main import register_main_middleware

__models__ = [
    register_main_middleware,
]
