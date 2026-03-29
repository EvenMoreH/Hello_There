from app.applications import Application

application = Application(
    slug="distance_converter",
    title="Distance Converter",
    description=(
        "Convert between different units of distance in your TTRPGs."
    ),
    icon="📏",
    route="/distance_converter",
    external_url="https://distance.fastools.xyz",
)
