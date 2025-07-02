# 🤖 mass-invite-vk-bot

Автоматическое массовое приглашение всех друзей в групповой чат ВКонтакте по команде `!invite`.  
Скрипт работает через VK API, поддерживает все операционные системы и IDE: Windows, Linux, Termux, macOS, VS Code, PyCharm.

---

## Быстрый старт (одна команда установки)

> Подходит для **Linux**, **Termux**, **macOS**, **Git Bash (Windows)**:

sudo apt install git -y && sudo apt install python -y (Для всего что описано сверху кроме Termux)
pkg install git -y && pkg install python -y (Для Termux)

bash git clone https://github.com/Twix234/mass-invite-vk-bot.git && cd ~/mass-invite-vk-bot && pip install -r requirements.txt && python main.py (Это команда,Для всех ОС, что описаны сверху без исключений)




📦 Возможности

✅ Автоматическое приглашение всех друзей в чат

✅ Поддержка всех платформ

✅ Ожидает команду !invite от владельца аккаунта.

✅ Простая настройка через .env

✅ Защита от лимитов VK API

✅ Повторный запрос авторизации при ошибке



Установка в Windows вручную через CMD:
1. Установи Python (галочка “Add to PATH” при установке)
2. Установи Git for Windows
3. Открой CMD или PowerShell и выполни:

git clone https://github.com/Twix234/mass-invite-vk-bot.git
cd ~/mass-invite-vk-bot
pip install -r requirements.txt
python main.py



Установка в Termux вручную (Android):

pkg update && pkg install git python -y && git clone https://github.com/Twix234/mass-invite-vk-bot.git && cd ~/mass-invite-vk-bot  && pip install -r requirements.txt && python main.py

Установка вручную в Linux/macOS:

git clone https://github.com/Twix234/mass-invite-vk-bot.git
cd ~/mass-invite-vk-bot
pip install -r requirements.txt
python main.py


Использование в IDE на Windows

VS Code
1. Установи Visual Studio Code
2. Открой проект: File → Open Folder → mass-invite-vk-bot
3. Установи расширение Python
4. Выбери интерпретатор Python (справа внизу)
5. Открой main.py и нажми ▶️ (Run)

PyCharm
1. Установи PyCharm Community
2. Открой папку проекта
3. PyCharm предложит установить зависимости — подтверди
4. Открой main.py, нажми правой кнопкой → Run 'main'

🔐 Как получить VK токен страницы
Скрипт требует токен вашей страницы. Вот как его получить:
1. Перейди на сайт: vkhost.github.io
2. Выбери тип: VK Admin или Standalone
3. Подтверди разрешения
4. После этого в адресной строке появится ссылка:
https://oauth.vk.com/blank.html#access_token=vk1.a.xxxxxx&expires_in=0&user_id=12345678
5. Скопируй:
access_token=... → это VK_TOKEN
user_id=... → это USER_ID

Файл .env
Скрипт создаёт config.env (или .env) при первом запуске. Пример:
VK_TOKEN=vk1.a.твой_токен
USER_ID=12345678
DELAY_MIN=0.05
DELAY_MAX=0.7

💬 Как использовать
1. Запусти скрипт:
python main.py
2. В беседе ВКонтакте, куда нужно добавить пользователей, отправь команду:
"!invite"
3.Скрипт начнёт приглашать всех твоих друзей в эту беседу
4.В чат придёт отчёт вида:
"✅ Приглашено: 87 пользователей
🕒 Время: 14:36:41
👥 Всего обработано: 110"
📂 Структура проекта:

mass-invite-vk-bot/
├── main.py             # основной скрипт
├── config.env          # создаётся автоматически
├── requirements.txt    # зависимости
└── README.md           # документация

🧾 requirements.txt:

vk_api
python-dotenv

Установка:

pip install -r requirements.txt


---

❗ Возможные ошибки

❌ Неверный токен — проверь, не истёк ли и не обрезан ли

🕒 Rate limit exceeded — добавь больше задержки

❗ Нет прав в чате — в чатах где доступ приглашать людей ограничен,и доступен только администрации,ты должен быть администратором.

🧾 Лицензия

MIT License © 2025 — Twix234.
