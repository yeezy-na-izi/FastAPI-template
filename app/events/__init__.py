"""Events of application."""

from app.events.shutdown import register_shutdown_event
from app.events.startup import register_startup_event

__models__ = [
    register_startup_event,
    register_shutdown_event,
]
