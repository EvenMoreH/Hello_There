import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from fasthtml.common import * # type: ignore

from app.applications import load_applications
from app.content.homepage import (
    HERO_TITLE,
    HERO_PARAGRAPH,
    MORE_GAMES_TEXT,
    MORE_TESTING_TEXT,
    TECH_DOCKER_TEXT,
    TECH_FASTHTML_TEXT,
    TECH_TAILWIND_TEXT,
)

app, rt = fast_app(
    hdrs=[
        Script(src="https://unpkg.com/htmx.org"),
        Link(rel="stylesheet", href="/css/output.css"),
        Link(rel="icon", href="/images/favicon.ico", type="image/x-icon"),
        Link(rel="icon", href="/images/favicon.png", type="image/png"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0")
    ],
    pico=False,  # disable Pico CSS since we're using Tailwind
    static_path="app/static"  # serve static files
)

applications = load_applications(rt)

@rt("/")
def get():
    app_cards = [
        Div(
            A(
                Div(
                    H3(f"{application.icon} {application.title}", cls="card-title"),
                    P(application.description, cls="card-text")
                ),
                href=application.href,
                target=application.target,
                cls="app-card-link"
            )
        )
        for application in applications
    ]

    apps_section = Div(
        H2("Check out my other apps", cls="section-title"),
        Div(
            *(app_cards if app_cards else [P("No applications available yet.", cls="card-text")]),
            cls="app-grid"
        ),
        cls="section-spacing"
    )

    return Title("Fastools Hub"), \
    Div(
        Header(
            Div(
                H1(HERO_TITLE, cls="hero-title"),
                P(HERO_PARAGRAPH, cls="hero-subtitle"),
                cls="hero-content"
            ),
            cls="hero-header"
        ),
        Main(
            Div(
                # features section - tech stack
                Div(
                    H2("Technologies Used", cls="section-title"),
                    Div(
                        # card 1
                        Div(
                            Div(
                                H3("⚡ FastHTML", cls="card-title"),
                                P(TECH_FASTHTML_TEXT, cls="card-text"),
                            ),
                            cls="card"
                        ),

                        # card 2
                        Div(
                            Div(
                                H3("🎨 Tailwind CSS", cls="card-title"),
                                P(TECH_TAILWIND_TEXT, cls="card-text"),
                            ),
                            cls="card"
                        ),

                        # card 3
                        Div(
                            Div(
                                H3("🐳 Docker Ready", cls="card-title"),
                                P(TECH_DOCKER_TEXT, cls="card-text"),
                            ),
                            cls="card"
                        ),

                        cls="feature-grid"
                    ),
                    cls="section-spacing"
                ),
                # HTMX Interactive section
                Div(
                    H2("Try It Out", cls="section-title"),
                    # HTMX
                    Div(
                        Button(
                            "Click me!",
                            hx_get="/demo/htmx",
                            hx_target="#demo-result",
                            hx_swap="innerHTML",
                            cls="btn"
                        ),
                        Div(
                            "Click the button above to see HTMX in action!",
                            id="demo-result",
                            cls="demo-result"
                        ),
                        cls="centered"
                    ),
                    # API
                    Div(
                        Button(
                            "Click me!",
                            hx_get="/demo/iframe",
                            hx_target="#demo-iframe",
                            hx_swap="outerHTML",
                            cls="btn btn-spacing"
                        ),
                        Div(
                            "Click the button above to load API response into iframe!",
                            id="demo-iframe",
                            cls="demo-result"
                        ),
                        cls="centered"
                    ),
                    cls="section-spacing"
                ),
                 # projects section
                Div(
                    H2("More From Me", cls="section-title"),
                    Div(
                        # card 4
                        Div(
                            A(
                                Div(
                                    H3("← My Games (Coming Soon)", cls="card-title"),
                                    P(MORE_GAMES_TEXT, cls="card-text"),
                                ),
                                href="/games",
                                target="_blank",
                            ),
                            cls="app-card-link"
                        ),

                        # card 5
                        Div(
                            A(
                                Div(
                                    H3("Check Out How I Test Things →", cls="card-title"),
                                    P(MORE_TESTING_TEXT, cls="card-text"),
                                ),
                                href="/testing",
                                target="_blank",
                            ),
                            cls="app-card-link"
                        ),

                        cls="two-col-grid"
                    ),
                    cls="section-spacing"
                ),
                # adding all app cards from applications folder
                apps_section,
                cls="container-section"
            ),
            cls="main-content"
        ),

        # footer
        Footer(
            Div(
                P("Built with ❤️ using FastHTML and Tailwind CSS", cls="footer-text"),
                Div(
                    P(
                        "Created by ",
                        A("EvenMoreH",
                          href="https://github.com/EvenMoreH",
                          target="_blank",
                          rel="noopener noreferrer",
                          cls="footer-link"),
                        cls="footer-text-small"
                    ),
                    cls="footer-layout"
                ),
                cls="container-footer"
            ),
            cls="footer"
        ),
        cls="page-wrapper"
    )

# HTMX demo endpoint
@rt("/demo/htmx")
def get():
    return Div(
        P("🎉 Great! FastHTML and Tailwind are working perfectly together! Resetting in 5...",
          cls="success-text"),
          # reset after 5 seconds
          Div(
              hx_get="/demo/htmx/reset",
              hx_target="#demo-result",
              hx_swap="innerHTML",
              hx_trigger="load delay:5s"
          ),
        cls="demo-success"
    )

@rt("/demo/htmx/reset")
def get():
    return "Click the button above to see HTMX in action!"

# iframe endpoint
@rt("/demo/iframe")
def get():
    return Div(
        Iframe(
            src="/api/hello",
            cls="iframe-container"
        ),
        # reset after 10 seconds
        Div(
            hx_get="/demo/iframe/reset",
            hx_target="#demo-iframe",
            hx_swap="outerHTML",
            hx_trigger="load delay:5s"
        ),
        id="demo-iframe",
        cls="demo-result centered"
    )

@rt("/demo/iframe/reset")
def get():
    return Div(
        "Click the button above to load API response into iframe!",
        id="demo-iframe",
        cls="demo-result"
    )

# API endpoint example
@rt("/api/hello")
def get():
    return {"message": "Hello from FastHTML API!", "status": "200 OK"}

# more from me endpoints
@rt("/games")
def games():
    return """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Coming Soon!</title>
    </head>
    <body>
        Coming Soon!
    </body>
    </html>"""


@rt("/testing")
def games():
    return """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Coming Soon!</title>
    </head>
    <body>
        Coming Soon!
    </body>
    </html>"""


def main():
    """Main entry point for the application"""
    serve(host='0.0.0.0', port=5050)

if __name__ == "__main__":
    main()
