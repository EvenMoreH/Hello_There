from app.applications import Application

application = Application(
    slug="to_ico_converter",
    title="Image to .ICO Converter",
    description=(
        "Convert images (.png, .jpg, .jpeg, .webp, .bmp) to .ICO files in a browser."
    ),
    icon="🖼️",
    route="/to_ico_converter",
    external_url="https://ico.fastools.xyz/",
)
