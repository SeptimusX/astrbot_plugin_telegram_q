from astrbot.api.all import Context


class Main:
    def __init__(self, context: Context) -> None:
        from .tg_platform_adapter import TelegramPlatformAdapter # noqa