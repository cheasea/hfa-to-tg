from vk_api.bot_longpoll import VkBotEventType
from config import tg_bot, tg_channel
from utils import Console
from telebot.types import InputMediaPhoto

def process_event(e):
    if e.t == VkBotEventType.WALL_POST_NEW:
        Console.sys("New post: {}".format(e.obj.text[:50]))
        process_new_post(e.obj)


def process_new_post(data):
    text = data.text
    link = 'https://vk.com/home_for_alchemists?w=wall-125350949_' + str(data.id)
    link_tag = '<a href="{url}">{text}</a>'.format(url=link, text="➡️ VK")
    text += "\n\n" + link_tag
    
    if data.attachments:
        media = []
        for m in data.attachments:
            if m['type'] == 'photo':
                last_size = m['photo']['sizes'][-1]
                media.append(last_size['url'])

        count = len(media)
        if count > 0:
            if count == 1:
                tg_bot.send_photo(tg_channel, media[0], caption=text, parse_mode="HTML")
                return
            elif count >= 2:
                media[0] = InputMediaPhoto(media[0], caption=text, parse_mode="HTML")
                media[1:] = [InputMediaPhoto(photo) for photo in media[1:]]
                tg_bot.send_media_group(tg_channel, media)
                return

    tg_bot.send_message(tg_channel, text, parse_mode="HTML", disable_web_page_preview=True)
