# Registry Pattern Update

This document explains the new app registry pattern to quickly understand how routes are discovered, bound, and shown on the homepage.

## Why the change?
- Remove hardcoded routes from the homepage and centralize them.
- Make adding a new tool a drop-in file, no edits to the main app.
- Keep Uvicorn/FastHTML imports clean by treating `app` as a package.

## What changed (high level)
- Main entry now loads applications dynamically and renders cards from that data: see app/app.py.
- Applications folder is now a real package with a loader that imports each module and binds its route: see app/applications/__init__.py.
- Top-level package exposes the ASGI `app` for Uvicorn: see app/__init__.py.
- Each tool lives in its own module declaring a single `application = Application(...)`: see files in app/applications/ (alarm.py, temperature.py, qr_gen.py, distance_converter.py, dice_roller.py, color_converter.py).

## File-by-file details

### app/app.py
- Adds sys.path bootstrap so `app` can be imported when running as a script.
- Imports `load_applications` and immediately calls it to bind routes and collect metadata for the homepage cards.
- Homepage now builds cards from the discovered `applications` list instead of hardcoded links.

### app/applications/__init__.py
- Marks `app/applications` as a package so we can import `app.applications.*` modules.
- Defines `Application` dataclass with metadata (slug, title, description, icon, route, external_url, view, target).
- `load_applications(rt)` scans every `.py` file in this folder (skips files starting with `_`), imports it, looks for `application`, and if it is an `Application`, binds the route via `rt` and returns the list (sorted by title).
- Default behavior: if `external_url` is set, a redirect handler is created; otherwise expect a custom `view` to be provided.

### app/__init__.py
- Marks the top-level `app` directory as a package.
- Re-exports the ASGI `app` object so Uvicorn can import `app:app` (fixes “Attribute app not found in module app” error when the reloader starts).

### app/applications/<name>.py (per-app modules)
- Each module defines one `application = Application(...)` instance.
- Current examples: alarm.py, temperature.py, qr_gen.py, distance_converter.py, dice_roller.py, color_converter.py.
- These modules do not need to register routes manually; the loader handles binding.

## How the registry flow works at runtime
1) app/app.py runs, creates the FastHTML app, and calls `load_applications(rt)`.
2) load_applications scans app/applications/*.py, imports each module, and collects `application` objects.
3) Each `application` binds its route to `rt` (either a redirect or a custom view).
4) The homepage renders cards from the collected `applications` list, so new tools appear automatically.
5) app/__init__.py makes `app` importable by Uvicorn as `app:app`.

## How to add a new app
1) Create a new file in app/applications/, e.g., `my_tool.py`.
2) Inside it, define one `application = Application(...)` with at least: slug, title, description, icon, route, and either `external_url` (for redirect) or `view` (for server-side handler).
3) Restart the server (or let the reloader pick it up). The route is bound automatically and the homepage card appears.

## Common pitfalls to avoid
- Forgetting `application = Application(...)` in the module: loader will skip it.
- Naming the file with a leading underscore: loader intentionally ignores those.
- Omitting `app/__init__.py`: Uvicorn cannot import `app:app` and will fail at startup.

## Quick reference
- Main entry and registry call: app/app.py
- Registry logic and dataclass: app/applications/__init__.py
- Package export for ASGI app: app/__init__.py
- Example app modules: app/applications/*.py
