from app.applications import Application

application = Application(
    slug="qr-gen",
    title="QR Code Generator",
    description=(
        "Generate QR codes for text, URLs, and other data quickly and easily."
    ),
    icon="📱",
    route="/qr-gen",
    external_url="https://qr.fastools.xyz",
)
