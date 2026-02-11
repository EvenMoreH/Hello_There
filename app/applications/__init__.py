from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Callable, List

from fasthtml.common import Redirect

BASE_DIR = Path(__file__).parent


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

    @property
    def normalized_route(self) -> str:
        return self.route if self.route.startswith("/") else f"/{self.route}"

    @property
    def href(self) -> str:
        return self.normalized_route

    def bind(self, rt: Callable) -> None:
        handler = self.view or self._default_handler()
        if handler is None:
            return
        rt(self.normalized_route)(handler)

    def _default_handler(self):
        if self.external_url:
            def _redirect():
                return Redirect(self.external_url)
            return _redirect
        return None


def load_applications(rt: Callable) -> List[Application]:
    """Discover application modules and register their routes."""
    applications: List[Application] = []
    for file in BASE_DIR.glob("*.py"):
        if file.stem.startswith("_"):
            continue
        module = import_module(f"app.applications.{file.stem}")
        candidate = getattr(module, "application", None)
        if isinstance(candidate, Application):
            candidate.bind(rt)
            applications.append(candidate)
    applications.sort(key=lambda app: app.title.lower())
    return applications
