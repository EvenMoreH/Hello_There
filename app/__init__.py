"""Package marker for app module.

Exposes the ASGI `app` instance so Uvicorn's auto-reloader can find it
when using the default import path `app:app`.
"""

from .app import app  # re-export for Uvicorn

__all__ = ["app"]
