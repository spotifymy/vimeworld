from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api

vk_implicit = vk_api.VkApi(token="2572dc16e8b567fb88d318b1033a73dc9f303aa1ad2e483092648f613dd7204c99bfeb6d95a910712e4de")
vk_implicit._auth_token()

vk = vk_api.VkApi(token="3e50516412587e272dcbd1f3210af23c3dc660bdc43f5ac0563d1473a94fe9552dd75f71558ff717cdb5f")
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 195573855)

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
                                text = vk_implicit.method("wall.get", {"owner_id": -195573855})["items"][0]["text"]
                                id = vk_implicit.method("wall.get", {"owner_id": -195573855})["items"][0]["id"]

                                vk_implicit.method("wall.delete", {"owner_id": -195573855, "post_id": id})
                                vk_implicit.method("wall.post", {"owner_id": -195573855, "from_group": 1, "message": text + "\n" + textToWords[2]})
                                vk.method("messages.send", {"peer_id": 598391185, "message": "Лицензия активирована", "random_id": 0})
                            except IndexError:
                                vk.method("messages.send", {"peer_id": 598391185,
                                                            "message": "Неверная команда. Используйте: /server add [HWID]",
                                                            "random_id": 0})
                                vk_implicit.method("wall.post", {"owner_id": -195573855, "from_group": 1, "message": text})
                        elif textToWords[1] == "remove":
                            try:
                                text = vk_implicit.method("wall.get", {"owner_id": -195573855})["items"][0]["text"]
                                id = vk_implicit.method("wall.get", {"owner_id": -195573855})["items"][0]["id"]

                                vk_implicit.method("wall.delete", {"owner_id": -195573855, "post_id": id})
                                vk_implicit.method("wall.post", {"owner_id": -195573855, "from_group": 1, "message": text.replace("\n" + textToWords[2], "")})
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

