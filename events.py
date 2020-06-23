from vk_api.bot_longpoll import VkBotEventType
from config import tg_bot, tg_channel
from utils import Console


def process_event(e):
    if e.t == VkBotEventType.WALL_POST_NEW:
        Console.sys("New post: {}".format(e.obj.text[:50]))
        process_new_post(e.obj)


def process_new_post(data):
    tg_bot.send_message(chat_id=tg_channel, text=data.text)
