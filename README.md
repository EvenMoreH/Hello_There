# Hello There - FastHTML Portfolio App

A personal portfolio web application built with FastHTML and Tailwind CSS v4.1, showcasing interactive demos and links to utility applications. The app features HTMX demonstrations, iframe integration, and a fully responsive design with custom component-based styling.

## Features

- 🚀 **FastHTML**: Modern Python web framework with server-side rendering and reactive components
- 🎨 **Tailwind CSS v4.1**: Custom component-based styling with utility classes
- ⚡ **HTMX Integration**: Interactive demos showcasing dynamic content updates
- 🖼️ **iframe Demos**: API response integration within embedded frames
- 🐳 **Docker Ready**: Containerized for easy deployment
- 📱 **Responsive Design**: Mobile-first approach with automatic dark/light mode support
- 🔗 **App Showcase**: Links to external utility applications
- 🎮 **Coming Soon**: Game projects and testing methodologies showcase

## Live Demo

Visit the live application: [https://fastools.xyz/](https://fastools.xyz/)

## Quick Start

### Local Development (with uv)

1. Install dependencies using [uv](https://docs.astral.sh/uv/):
```bash
# Install uv (if you don't have it yet)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate a virtual environment (optional but recommended)
uv venv .venv
source .venv/bin/activate

# Install project dependencies from the lockfile
uv sync --frozen --no-dev --no-install-project
```

2. Run the application:
```bash
python -m app.app
```

3. Open your browser and visit: http://localhost:5050

4. Compile Tailwind CSS (in development):
```bash
# Watch mode (auto-rebuild on changes)
tailwindcss -i ./app/static/css/input.css -o ./app/static/css/output.css --watch

# Production build (minified)
tailwindcss -i ./app/static/css/input.css -o ./app/static/css/output.css --minify
```

### Docker Deployment

#### Using Docker directly:

```bash
# Build the image
docker build -t hello-there-app .

# Run the container
docker run -p 5050:5050 hello-there-app
```

## Interactive Features

### HTMX Demo
- Interactive button that demonstrates HTMX functionality
- Auto-reset after 5 seconds
- Shows dynamic content updates without page refresh

### iframe Integration
- API response loading into iframe
- Demonstrates `/api/hello` endpoint integration
- Auto-reset functionality

### External App Links
The app showcases links to various utility applications (registered via the app registry, see below):
- ⏰ **Alarm Clock**: https://alarm.fastools.xyz
- 🌡️ **Temperature Converter**: https://temperature.fastools.xyz
- 📱 **QR Code Generator**: https://qr.fastools.xyz
- 📏 **Distance Converter**: https://distance.fastools.xyz
- 🎲 **Dice Roller**: https://roll.fastools.xyz
- 🎨 **Color Converter**: https://color.fastools.xyz
- 🖼️ **ICO Converter**: https://ico.fastools.xyz

## Page Sections

The main page includes the following sections:

1. **Hero Header**: Introduction with gradient background
2. **Technologies Used**: Showcases FastHTML, Tailwind CSS v4.1, and Docker
3. **More From Me**: Links to upcoming game projects and testing methodologies
4. **Try It Out**: Interactive HTMX and iframe demonstrations
5. **Check out my other apps**: Links to 7 utility applications
6. **Footer**: Credits and social links

## Project Structure

```
Hello_There/
├── app/
│   ├── app.py          # Main FastHTML application
│   ├── __init__.py     # Makes app a package and re-exports the ASGI app
│   ├── applications/   # Registry-driven external/internal tools
│   │   ├── __init__.py           # Application dataclass + registry loader
│   │   ├── alarm.py              # Alarm app registration
│   │   ├── temperature.py        # Temperature converter registration
│   │   ├── qr_gen.py             # QR generator registration
│   │   ├── distance_converter.py # Distance converter registration
│   │   ├── dice_roller.py        # Dice roller registration
│   │   ├── color_converter.py    # Color converter registration
│   │   └── to_ico_converter.py   # ICO converter registration
│   ├── pages/
│   │   ├── __init__.py     # Package marker for page modules
│   │   ├── games.py        # Games page content
│   │   └── testing.py      # Testing page content
│   └── static/
│       ├── css/
│       │   ├── input.css    # Tailwind v4.1 source with custom components
│       │   └── output.css   # Compiled Tailwind CSS
│       └── images/
│           ├── favicon.ico
│           └── favicon.png
├── pyproject.toml      # Project configuration and dependencies (uv/Poetry compatible)
├── requirements.txt    # Compatibility dependency list for tools that still expect it
├── uv.lock             # Locked dependency graph used by Docker/CI/local sync
├── tailwind.config.js  # Tailwind CSS configuration
├── Dockerfile          # Docker configuration
├── README.md           # This file
└── LICENSE             # MIT License
```

## Application Registry Pattern

This project now uses a simple **registry pattern** for apps, so adding a new tool is just dropping in a new file.

- The main entry `app/app.py` imports `load_applications` and calls it once to:
	- discover all applications in `app/applications/`,
	- bind their routes to the FastHTML router,
	- and render homepage cards from that list.
- The folder `app/applications/` is a package (thanks to its `__init__.py`) that defines:
	- an `Application` dataclass (slug, title, description, icon, route, external_url/view, target),
	- `load_applications(rt)`, which scans all `*.py` files in that folder, imports them, finds `application` objects, and binds their routes.
- The top-level `app/__init__.py` makes `app` a proper package and re-exports the ASGI `app` so Uvicorn can run `app:app` cleanly.
- Each module in `app/applications/` (for example `alarm.py`, `temperature.py`, etc.) defines **one** `application = Application(...)` instance; no manual route wiring is needed in those files.

**Runtime flow:**
1. `python -m app.app` starts the FastHTML app and calls `load_applications(rt)`.
2. The loader imports every `app/applications/*.py` module (except names starting with `_`).
3. Each `application` instance registers its route with `rt` (redirect or custom view).
4. The homepage uses the returned list of applications to render the "Check out my other apps" grid.

**Adding a new app:**
1. Create `app/applications/my_tool.py`.
2. Define a single `application = Application(...)` with slug, title, description, icon, route, and either `external_url` or a `view`.
3. Restart the server; your new route is bound and appears automatically on the homepage.

For a more detailed, teaching-focused explanation (for juniors), see `registry_pattern_update.md`.

## API Endpoints

### Main Routes
- `GET /` - Main application page with title "Fastools Hub"
- `GET /games` - Coming soon page for game projects
- `GET /testing` - Coming soon page for testing methodologies

### Demo Endpoints
- `GET /demo/htmx` - HTMX demonstration endpoint
- `GET /demo/htmx/reset` - Reset HTMX demo
- `GET /demo/iframe` - iframe demonstration endpoint
- `GET /demo/iframe/reset` - Reset iframe demo
- `GET /api/hello` - Sample API endpoint returning JSON

### External App Redirects
- `GET /alarm` - Redirect to alarm app
- `GET /temperature` - Redirect to temperature converter
- `GET /qr-gen` - Redirect to QR generator
- `GET /distance_converter` - Redirect to distance converter
- `GET /dice_roller` - Redirect to dice roller
- `GET /color_converter` - Redirect to color converter

## Technologies Used

- **FastHTML**: Modern Python web framework with reactive components
- **Tailwind CSS v4.1**: Utility-first CSS framework with custom component classes
- **HTMX**: Interactive frontend without JavaScript frameworks
- **Docker**: Containerization with health checks
- **Python 3.12+**: Runtime environment
- **uv**: Fast Python dependency management (used locally and in Docker)

### Dependency Source Of Truth

The authoritative dependency definition is `pyproject.toml` plus `uv.lock`.

- Local development uses `uv sync --frozen`.
- Docker builds use `uv sync --frozen`.
- CI installs use `uv sync --frozen`.
- `requirements.txt` is retained only for compatibility with tools that still expect it.

### CSS Architecture

The app uses Tailwind CSS v4.1 with a custom component-based architecture:
- All inline utilities replaced with reusable component classes
- Custom classes for layout, typography, cards, buttons, and more
- Full dark/light mode support with media queries
- Responsive design with mobile-first approach

## Development

The application uses FastHTML's built-in development server with hot reloading. Any changes to `app.py` will automatically restart the server.

### Development Tools
- **uv**: For fast dependency management and virtual environments
- **Tailwind CSS**: For styling with watch mode support
- **Docker**: For containerized development and deployment
- **Health Checks**: Built-in Docker health monitoring

## Deployment

This app is ready for deployment on any platform that supports Docker:

- **Docker Hub**
- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure Container Instances**
- **Heroku**
- **DigitalOcean App Platform**
- **Railway**
- **Fly.io**

### Environment Variables

No environment variables are required for basic operation. The app runs on port 5050 by default.

## License

This project is open source and available under the MIT License.