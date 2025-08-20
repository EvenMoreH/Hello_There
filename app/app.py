from fasthtml.common import * # type: ignore

app, rt = fast_app(
    hdrs=[
        Script(src="https://unpkg.com/htmx.org"),
        Link(rel="stylesheet", href="/css/output.css"),
        Link(rel="icon", href="/images/favicon.ico", type="image/x-icon"),
        Link(rel="icon", href="/images/favicon.png", type="image/png"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Title("Hello There - FastHTML App")
    ],
    pico=False,  # disable Pico CSS since we're using Tailwind
    static_path="app/static"  # serve static files from app/static
)

@rt("/")
def get():
    return Div(
        Header(
            Div(
                H1("Hello There! 👋", cls="hero-title"),
                P(
                    "I work in quality assurance and have a passion for software development. \
                    Outside of work, I enjoy building tools to boost productivity, \
                    exploring new technologies, \
                    and trying to learn something new every day.",
                  cls="hero-subtitle"
                  ),
                cls="hero-content"
            ),
            cls="hero-header"
        ),
        Main(
            Div(
                # feature cards
                Div(
                    H2("Features", cls="section-title"),
                    Div(
                        # card 1
                        Div(
                            Div(
                                H3("⚡ FastHTML", cls="card-title"),
                                P(
                                    "Built with FastHTML - the modern Python web framework that " \
                                    "combines the best of server-side rendering with reactive components.",
                                  cls="card-text")
                            ),
                            cls="card"
                        ),

                        # card 2
                        Div(
                            Div(
                                H3("🎨 Tailwind CSS", cls="card-title"),
                                P("Styled with Tailwind CSS for beautiful, responsive design with utility-first CSS classes.",
                                  cls="card-text")
                            ),
                            cls="card"
                        ),

                        # card 3
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
                            cls="btn mt-8"
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
                # apps section
                Div(
                    H2("Check out my other apps", cls="section-title"),
                    Div(
                        # alarm app
                        Div(
                            A(
                                Div(
                                    H3("⏰ Alarm Clock", cls="card-title"),
                                    P("Set alarms and manage your time with this simple alarm clock application.",
                                      cls="card-text")
                                ),
                                href="/alarm",
                                target="_blank",
                                cls="card hover:scale-105 transform transition-transform duration-200 block"
                            )
                        ),

                        # temperature converter
                        Div(
                            A(
                                Div(
                                    H3("🌡️ Temperature Converter", cls="card-title"),
                                    P("Convert temperatures between Celsius, Fahrenheit, and Kelvin with ease.",
                                      cls="card-text")
                                ),
                                href="/temperature",
                                target="_blank",
                                cls="card hover:scale-105 transform transition-transform duration-200 block"
                            )
                        ),

                        # qr generator
                        Div(
                            A(
                                Div(
                                    H3("📱 QR Code Generator", cls="card-title"),
                                    P("Generate QR codes for text, URLs, and other data quickly and easily.",
                                      cls="card-text")
                                ),
                                href="/qr-gen",
                                target="_blank",
                                cls="card hover:scale-105 transform transition-transform duration-200 block"
                            )
                        ),

                        # distance converter
                        Div(
                            A(
                                Div(
                                    H3("📏 Distance Converter", cls="card-title"),
                                    P("Convert between different units of distance in your TTRPGs.",
                                      cls="card-text")
                                ),
                                href="/distance_converter",
                                target="_blank",
                                cls="card hover:scale-105 transform transition-transform duration-200 block"
                            )
                        ),

                        # dice roller
                        Div(
                            A(
                                Div(
                                    H3("🎲 Dice Roller", cls="card-title"),
                                    P("Roll virtual dice for games, decisions, or random number generation in old-school way",
                                      cls="card-text")
                                ),
                                href="/dice_roller",
                                target="_blank",
                                cls="card hover:scale-105 transform transition-transform duration-200 block"
                            )
                        ),

                        # color converter
                        Div(
                            A(
                                Div(
                                    H3("🎨 Color Converter", cls="card-title"),
                                    P("Convert colors between different formats: HEX, RGB, Tailwind.",
                                      cls="card-text")
                                ),
                                href="/color_converter",
                                target="_blank",
                                cls="card hover:scale-105 transform transition-transform duration-200 block"
                            )
                        ),
                        cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
                    ),
                    cls="section-spacing"
                ),
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
            cls="w-full h-64 border rounded"
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

# app endpoints
@rt("/alarm")
def alarm():
    return Redirect("https://alarm.fastools.xyz")

@rt("/temperature")
def temperature():
    return Redirect("https://temperature.fastools.xyz")

@rt("/qr-gen")
def qr_generator():
    return Redirect("https://qr.fastools.xyz")

@rt("/distance_converter")
def distance_converter():
    return Redirect("https://distance.fastools.xyz")

@rt("/dice_roller")
def dice_roller():
    return Redirect("https://roll.fastools.xyz")

@rt("/color_converter")
def color_converter():
    return Redirect("https://color.fastools.xyz/")

def main():
    """Main entry point for the application"""
    serve(host='0.0.0.0', port=5071)

if __name__ == "__main__":
    main()
