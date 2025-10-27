import os

from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv

@dataclass
class BotLog:
    log_format: str
    log_level: str

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tgbot: TgBot
    log: BotLog


def load_bot() -> Config:
    return Config(
        tgbot=TgBot(
            token=os.getenv("TOKEN"),
        ),
        log=BotLog(
            log_format=os.getenv("LOG_FORMAT"),
            log_level=os.getenv("LOG_LEVEL"),
        )
    )
