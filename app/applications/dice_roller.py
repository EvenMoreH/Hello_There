from app.applications import Application

application = Application(
    slug="dice_roller",
    title="Dice Roller",
    description=(
        "Roll virtual dice for games, decisions, or random number generation in an old-school way."
    ),
    icon="🎲",
    route="/dice_roller",
    external_url="https://roll.fastools.xyz",
)
