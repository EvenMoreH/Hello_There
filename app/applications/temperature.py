from app.applications import Application

application = Application(
    slug="temperature",
    title="Temperature Converter",
    description=(
        "Convert temperatures between Celsius, Fahrenheit, and Kelvin with ease."
    ),
    icon="🌡️",
    route="/temperature",
    external_url="https://temperature.fastools.xyz",
)
