# DEV
from config import env

if env == "DEV":
    from flask import Flask

    app = Flask(__name__)
    app.config.from_object("config.Dev")

    from config import group_id, vk_session
    from vk_api.bot_longpoll import VkBotLongPoll

    longpoll = VkBotLongPoll(vk_session, group_id)

    if __name__ == "__main__":
        from utils import Console
        Console.sys("Bot is active")

        from events import process_event

        for e in longpoll.listen():
            process_event(e)

elif env == "PROD":
    from flask import Flask, request, json
    from config import confirmation_token, secret_key

    app = Flask(__name__)
    app.config.from_object('config.Production')

    from events import process_event
    from vk_api.bot_longpoll import VkBotEvent

    @app.route('/')
    def hello():
        return 'Working!'

    @app.route('/', methods=['POST'])
    def processing():
        data = json.loads(request.data)
        e = VkBotEvent(data)

        if 'type' not in data.keys():
            return 'not vk'

        if data['type'] == 'confirmation':
            return confirmation_token
        else:
            if data['secret'] != secret_key:
                return 'not vk'

            process_event(e)
            return 'ok'
