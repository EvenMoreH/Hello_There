from app.applications import Application

application = Application(
    slug="color_converter",
    title="Color Converter",
    description=(
        "Convert colors between different formats: HEX, RGB, Tailwind."
    ),
    icon="🎨",
    route="/color_converter",
    external_url="https://color.fastools.xyz/",
)
