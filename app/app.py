from fasthtml.common import * # type: ignore

app, rt = fast_app(
    hdrs=[
        Script(src="https://unpkg.com/htmx.org"),
        Link(rel="stylesheet", href="/css/output.css"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Title("Hello There - FastHTML App")
    ],
    pico=False,  # Disable Pico CSS since we're using Tailwind
    static_path="app/static"  # Serve static files from app/static
)

@rt("/")
def get():
    return Div(
        Header(
            Div(
                H1("Hello There! 👋", cls="hero-title"),
                P("Welcome to my FastHTML + Tailwind CSS app", cls="hero-subtitle"),
                cls="hero-content"
            ),
            cls="hero-header"
        ),
        Main(
            Div(
                # Feature cards
                Div(
                    H2("Features", cls="section-title"),
                    Div(
                        # Card 1
                        Div(
                            Div(
                                H3("⚡ FastHTML", cls="card-title"),
                                P("Built with FastHTML - the modern Python web framework that combines the best of server-side rendering with reactive components.", 
                                  cls="card-text")
                            ),
                            cls="card"
                        ),

                        # Card 2
                        Div(
                            Div(
                                H3("🎨 Tailwind CSS", cls="card-title"),
                                P("Styled with Tailwind CSS for beautiful, responsive design with utility-first CSS classes.",
                                  cls="card-text")
                            ),
                            cls="card"
                        ),

                        # Card 3
                        Div(
                            Div(
                                H3("🐳 Docker Ready", cls="card-title"),
                                P("Containerized and ready for deployment anywhere with Docker support.",
                                  cls="card-text")
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
                    Div(
                        Button(
                            "Click me! 🚀",
                            hx_get="/demo",
                            hx_target="#demo-result",
                            hx_swap="innerHTML",
                            cls="btn-with-margin"
                        ),
                        Div(
                            "Click the button above to see HTMX in action!",
                            id="demo-result",
                            cls="demo-result"
                        ),
                        cls="centered"
                    ),
                    cls="section-spacing"
                ),
                cls="container-section"
            ),
            cls="main-content"
        ),

        # Footer
        Footer(
            Div(
                P("Built with ❤️ using FastHTML and Tailwind CSS", cls="footer-text"),
                P("© 2025 Hello There App", cls="footer-text-small"),
                cls="container-footer"
            ),
            cls="footer"
        ),
        cls="page-wrapper"
    )

# HTMX demo endpoint
@rt("/demo")
def get():
    return Div(
        P("🎉 Great! FastHTML and Tailwind are working perfectly together!",
          cls="success-text"),
        cls="demo-success"
    )

# API endpoint example
@rt("/api/hello")
def get():
    return {"message": "Hello from FastHTML API!", "status": "success"}

def main():
    """Main entry point for the application"""
    serve(host='0.0.0.0', port=5071)

if __name__ == "__main__":
    main()
