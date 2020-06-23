import os
import dotenv

dotenv.load_dotenv()
env = os.getenv("ENV")

token = os.getenv("TOKEN")
secret_key = os.getenv("SECRET_KEY")
confirmation_token = os.getenv("CONFIRMATION_TOKEN")
group_id = os.getenv("GROUP_ID")
vk_api_version = "5.89"

from vk_api import VkApi
vk_session = VkApi(token=token, api_version=vk_api_version)
api = vk_session.get_api()

import telebot
tg_token = os.getenv("TG_TOKEN")
tg_channel = os.getenv("TG_CHANNEL")

tg_bot = telebot.TeleBot(tg_token)


class Config:
    SECRET_KEY = (
        "v\xab?\x82\x9f\x94\x8a~\x06\xd2\xdf\xceJ\xa3\x8d_\xe4\xf2\xbb\xd1h\x07\x86\x92"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Dev(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"


class Production(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="",
        password="",
        hostname="",
        databasename="",
    )
