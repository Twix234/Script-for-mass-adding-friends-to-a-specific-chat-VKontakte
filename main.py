import os
import sys
import time
import random
import subprocess
import asyncio
from datetime import datetime
from typing import Set

CONFIG_FILE = "config.env"
REQUIRED_MODULES = ['vk_api', 'python-dotenv']

def install_dependencies():
    """Установка зависимостей"""
    for module in REQUIRED_MODULES:
        try:
            __import__(module)
        except ImportError:
            print(f"Устанавливаю: {module}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

def load_config():
    from dotenv import load_dotenv
    if not os.path.exists(CONFIG_FILE):
        token = input("Введите VK токен: ").strip()
        user_id = input("Введите ваш VK ID: ").strip()
        with open(CONFIG_FILE, "w") as f:
            f.write(f"VK_TOKEN={token}\nUSER_ID={user_id}\nDELAY_MIN=0.01\nDELAY_MAX=0.5\n")
    load_dotenv(CONFIG_FILE)

async def invite_users(vk, chat_id: int, friends: list, delay_min: float, delay_max: float):
    from vk_api.exceptions import VkApiError
    invited: Set[int] = set()
    success = 0

    for user_id in friends:
        if user_id in invited:
            continue
        try:
            vk.messages.addChatUser(chat_id=chat_id, user_id=user_id)
            invited.add(user_id)
            success += 1
            print(f"[+] Приглашен: {user_id}")
            await asyncio.sleep(random.uniform(delay_min, delay_max))
        except VkApiError as e:
            if e.code in [15, 100]:  # уже в чате или нет доступа
                invited.add(user_id)
            elif e.code == 6:  # слишком много запросов
                print("⚠️ Rate limit. Ждём...")
                await asyncio.sleep(1)
            else:
                print(f"[!] Ошибка {e.code}: {e}")
        except Exception as ex:
            print(f"[!] Исключение: {ex}")
    return success, len(invited)

async def main():
    install_dependencies()
    load_config()

    import vk_api
    from dotenv import load_dotenv
    from vk_api.exceptions import VkApiError

    load_dotenv(CONFIG_FILE)

    token = os.getenv("VK_TOKEN")
    owner_id = int(os.getenv("USER_ID"))
    delay_min = float(os.getenv("DELAY_MIN", 0.01))
    delay_max = float(os.getenv("DELAY_MAX", 0.5))

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    last_id = None

    print("✅ Скрипт запущен. Введите команду !invite в нужный чат...")

    while True:
        try:
            dialogs = vk.messages.getConversations(count=20)['items']
            for d in dialogs:
                msg = d['last_message']
                if msg['text'].strip().lower() == '!invite' and msg['from_id'] == owner_id:
                    if msg['id'] == last_id:
                        continue
                    last_id = msg['id']
                    peer_id = msg['peer_id']
                    chat_id = peer_id - 2000000000
                    print(f"[!] Команда найдена в чате: {chat_id}")

                    try:
                        friends = vk.friends.get()['items']
                        print(f"[+] Друзей: {len(friends)}")
                        invited, total = await invite_users(vk, chat_id, friends, delay_min, delay_max)
                        report = (
                            f"✅ Приглашено: {invited} пользователей\n"
                            f"🕒 Время: {datetime.now().strftime('%H:%M:%S')}\n"
                            f"👥 Всего обработано: {total}"
                        )
                        vk.messages.send(peer_id=peer_id, message=report, random_id=0)
                    except VkApiError as e:
                        print(f"[!] VK API Ошибка: {e}")
            await asyncio.sleep(3)

        except VkApiError as e:
            if e.code in [5, 1110]:
                print("❌ Ошибка авторизации. Удаляем конфиг...")
                os.remove(CONFIG_FILE)
                load_config()
            else:
                print(f"[!] Ошибка VK API: {e}")
                await asyncio.sleep(5)
        except Exception as e:
            print(f"❗ Критическая ошибка: {e}")
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
