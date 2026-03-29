from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
import logging
from pathlib import Path
from typing import Callable, List

from fasthtml.common import Redirect

BASE_DIR = Path(__file__).parent
logger = logging.getLogger(__name__)


@dataclass
class Application:
    slug: str
    title: str
    description: str
    icon: str
    route: str
    external_url: str | None = None
    view: Callable | None = None
    target: str = "_blank"

    def __post_init__(self) -> None:
        if self.view is None and self.external_url is None:
            raise ValueError(
                f"Application '{self.slug}' must define either 'view' or 'external_url'."
            )

    @property
    def normalized_route(self) -> str:
        return self.route if self.route.startswith("/") else f"/{self.route}"

    @property
    def href(self) -> str:
        return self.normalized_route

    def bind(self, rt: Callable) -> bool:
        handler = self.view or self._default_handler()
        if handler is None:
            logger.error("Skipping application '%s': no handler is available.", self.slug)
            return False
        rt(self.normalized_route)(handler)
        return True

    def _default_handler(self):
        if self.external_url:
            def _redirect():
                return Redirect(self.external_url)
            return _redirect
        return None


def load_applications(rt: Callable) -> List[Application]:
    """Discover application modules and register their routes."""
    applications: List[Application] = []
    for file in sorted(BASE_DIR.glob("*.py"), key=lambda path: path.stem):
        if file.stem.startswith("_"):
            continue
        try:
            module = import_module(f"app.applications.{file.stem}")
        except Exception:
            logger.exception("Failed to import application module '%s'.", file.stem)
            continue

        candidate = getattr(module, "application", None)
        if isinstance(candidate, Application):
            if candidate.bind(rt):
                applications.append(candidate)
    applications.sort(key=lambda app: app.title.lower())
    return applications
