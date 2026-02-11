from app.applications import Application

application = Application(
    slug="alarm",
    title="Alarm Clock",
    description=(
        "Set alarms and manage your time with this simple alarm clock application."
    ),
    icon="⏰",
    route="/alarm",
    external_url="https://alarm.fastools.xyz",
)
