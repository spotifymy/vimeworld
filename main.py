from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api

vk_implicit = vk_api.VkApi(token="aa55f0a6baca1eecdce996c3a079dfe4a2c1ee8d374f23c5d2d7fc4531f14dcdda7c0b8e0e567f31c4dfc")
vk_implicit._auth_token()

vk = vk_api.VkApi(token="d138473f347003bf5589494d0ccb34930405b9512f5d129fa943f815cb57b65d0c36d9a275220916249be")
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 195570123)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id == 598391185:
                userText = event.object.text
                textToWords = userText.split(" ")


                if textToWords[0] == "/server":
                    try:
                        if textToWords[1] == "add":
                            try:
                                text = vk_implicit.method("wall.get", {"owner_id": -195570123})["items"][0]["text"]
                                id = vk_implicit.method("wall.get", {"owner_id": -195570123})["items"][0]["id"]

                                vk_implicit.method("wall.delete", {"owner_id": -195570123, "post_id": id})
                                vk_implicit.method("wall.post", {"owner_id": -195570123, "from_group": 1, "message": text + "\n" + textToWords[2]})
                                vk.method("messages.send", {"peer_id": 598391185, "message": "Лицензия активирована", "random_id": 0})
                            except IndexError:
                                vk.method("messages.send", {"peer_id": 598391185,
                                                            "message": "Неверная команда. Используйте: /server add [HWID]",
                                                            "random_id": 0})
                                vk_implicit.method("wall.post", {"owner_id": -195570123, "from_group": 1, "message": text})
                        elif textToWords[1] == "remove":
                            try:
                                text = vk_implicit.method("wall.get", {"owner_id": -195570123})["items"][0]["text"]
                                id = vk_implicit.method("wall.get", {"owner_id": -195570123})["items"][0]["id"]

                                vk_implicit.method("wall.delete", {"owner_id": -195570123, "post_id": id})
                                vk_implicit.method("wall.post", {"owner_id": -195570123, "from_group": 1, "message": text.replace("\n" + textToWords[2], "")})
                                vk.method("messages.send", {"peer_id": 598391185, "message": "Лицензия удалена", "random_id": 0})
                            except IndexError:
                                vk.method("messages.send", {"peer_id": 598391185,
                                                            "message": "Неверная команда. Используйте: /server remove [HWID]",
                                                            "random_id": 0})
                        else:
                            vk.method("messages.send", {"peer_id": 598391185,
                                                        "message": "Неверная команда. Используйте: /server [add|remove] [HWID]",
                                                        "random_id": 0})
                    except IndexError:
                        vk.method("messages.send", {"peer_id": 598391185,
                                                    "message": "Неверная команда. Используйте: /server [add|remove] [HWID]",
                                                    "random_id": 0})

