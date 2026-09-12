#!/usr/bin/env python3
"""Renders apps.ohayo.by from the templates in templates/ plus the copy below.

One structure, two locales: edit STRINGS (or the template), re-run, commit the
generated index.html / ru/index.html / ohayo-network/index.html /
ohayo-network/ru/index.html and sitemap.xml.

    python3 render.py
"""
from datetime import date
from pathlib import Path

APP_STORE_URL = "https://apps.apple.com/app/ohayo-network/id6787492543?mt=12"

# Per-locale plumbing. Everything that is a path, a file-name fragment or an
# attribute rather than prose lives here; prose lives in STRINGS.
LOCALES = {
    "en": {
        "LANG": "en",
        "OG_LOCALE": "en_US",
        "BADGE_LOCALE": "en-us",
        "SHOTS": "en",
        "HUB_PATH": "/",
        "NETWORK_PATH": "/ohayo-network",
        "EN_CURRENT": 'aria-current="true"',
        "RU_CURRENT": "",
        "home_out": "index.html",
        "network_out": "ohayo-network/index.html",
        "home_path": "/",
        "network_path": "/ohayo-network",
    },
    "ru": {
        "LANG": "ru",
        "OG_LOCALE": "ru_RU",
        "BADGE_LOCALE": "ru-ru",
        "SHOTS": "ru",
        "HUB_PATH": "/ru",
        "NETWORK_PATH": "/ohayo-network/ru",
        "EN_CURRENT": "",
        "RU_CURRENT": 'aria-current="true"',
        "home_out": "ru/index.html",
        "network_out": "ohayo-network/ru/index.html",
        "home_path": "/ru",
        "network_path": "/ohayo-network/ru",
    },
}

STRINGS = {
    "en": {
        # -- shared chrome -------------------------------------------------
        "SKIP": "Skip to content",
        "NAV_LABEL": "Main",
        "FOOTER_NAV_LABEL": "Footer",
        "FOOTER_TM": "Apple, Mac, macOS and Mac App Store are trademarks of Apple Inc., registered in the U.S. and other countries.",

        # -- hub -----------------------------------------------------------
        "HOME_TITLE": "Ohayo — apps from Ohayo Studio",
        "HOME_DESCRIPTION": "Apps from Ohayo Studio — what is out, what each one does and where to get it.",
        "NAV_LEGAL": "Legal",
        "H1": "Apps by Ohayo Studio",
        "SUB": "Everything released so far is below. Each app has its own page: what it does, how it looks and where to get it.",
        "CARD_META": "macOS · Utilities · Mac App Store",
        "CARD_TEXT": "Live speed, your real exit IP and the location of every VPN tunnel, right in the menu bar. Plus per-app traffic, read-only.",
        "CARD_MORE": "Take a look →",
        "SOON": "More Ohayo apps land here as they ship.",
        "HOME_FOOTER_TAG": "Apps by Ohayo Studio.",
        "FOOTER_LEGAL": "Legal & support",

        # -- network: head -------------------------------------------------
        "TITLE": "Ohayo Network — network monitor for the macOS menu bar",
        "DESCRIPTION": "Live speed, your real exit IP and the location of every VPN tunnel — right in the macOS menu bar. Opt-in per-app traffic. No account, no analytics.",
        "OG_IMAGE_ALT": "Ohayo Network running in the macOS menu bar",

        "NAV_FEATURES": "Features",
        "NAV_SCREENS": "Screens",
        "NAV_PRIVACY": "Privacy",
        "NAV_FAQ": "FAQ",
        "NAV_CTA": "Get it",

        # -- network: hero -------------------------------------------------
        "HERO_H1": "<span>Your connection,</span><span class='grad'>in the menu bar.</span>",
        "HERO_SUB": "Live download and upload speed, the country your traffic actually exits from, and — unusually — the location of every VPN tunnel separately. Split routing is visible at a glance.",
        "HERO_SECONDARY": "See what it can do",
        "HERO_NOTE": "macOS 14 or later · Apple silicon · one-time purchase, no subscription",
        "BADGE_ALT": "Download Ohayo Network on the Mac App Store",

        "TRUST_1": "No account, ever",
        "TRUST_2": "No analytics, no ads",
        "TRUST_3": "Your data stays on your Mac",

        # -- network: features ---------------------------------------------
        "FEATURES_KICKER": "What it does",
        "FEATURES_H2": "Eight capabilities behind one status-bar icon.",
        "FEATURES_SUB": "Everything is read locally and updates the moment it changes — no background service, no calls home, no waiting for a refresh.",

        "F1_H": "Throughput, straight from the kernel",
        "F1_P": "Download and upload come from the interface byte counters macOS keeps itself — no polling of other apps, no estimates. A live sparkline in the status bar, the full chart in the dashboard.",
        "F2_H": "Every tunnel, located separately",
        "F2_P": "utun, WireGuard, IPsec — each active tunnel is geolocated over that interface, not over the default route. Split routing is flagged the moment part of your traffic leaves the country you expect.",
        "F3_H": "Exit IP and region",
        "F3_P": "Country, city, ISP and ASN, with the flag in the status bar. Recent IP history, and your own labels: tag an exit as Home or Office VPN by country, city, ISP, ASN or IP.",
        "F4_H": "Per-app traffic",
        "F4_P": "Live up and down per app, session totals, connection counts and remote endpoints. Top five in the popover, a sortable table in the dashboard. It runs on a macOS content-filter extension you add from Settings.",
        "F5_H": "Latency and a real speed test",
        "F5_P": "Round-trip time and jitter for hosts you choose, plus an on-demand Cloudflare speed test with configurable duration, parallel streams and a data cap per phase.",
        "F6_H": "Wi-Fi, in detail",
        "F6_P": "Network name, signal, channel, 802.11 standard, security and transmit rate — next to your local IP, MAC address and the DNS servers actually in use.",
        "F7_H": "Data usage on your own schedule",
        "F7_P": "Cumulative totals for received and sent, with automatic resets — daily, weekly, monthly or never — and a manual reset whenever you want a clean count.",
        "F8_H": "The geolocation services are yours",
        "F8_P": "Three key-less providers by default — each editable, switchable or removable. Add your own HTTPS endpoint by URL and JSON key paths, and pick which one is authoritative.",

        # -- network: screens ----------------------------------------------
        "SCREENS_KICKER": "Screen by screen",
        "SCREENS_H2": "Four screens: popover, dashboard, per-app traffic and settings.",

        "S1_H": "The whole link, in one window",
        "S1_P": "The dashboard stacks everything that matters into a single scroll: what you are connected through, where it comes out, how fast it is right now, and what a proper test says.",
        "S1_L1": "Connection card: Wi-Fi, Ethernet or VPN — including the carrier underneath a tunnel",
        "S1_L2": "Active tunnels, each with its own flag and exit",
        "S1_L3": "Throughput chart and a Cloudflare speed test with ping, download and upload",
        "ALT_DASHBOARD": "The Ohayo Network dashboard: connection, active tunnels, throughput chart and speed test results",

        "S2_H": "See which apps use the network",
        "S2_P": "Every app that touches the network is listed live — with connection counts and the endpoints it talks to. It runs on a macOS content-filter system extension, installed from the app's own settings.",
        "S2_L1": "Read-only: every flow is allowed, untouched — nothing is blocked, redirected or modified",
        "S2_L2": "No payload is ever read; byte counts are aggregated in memory and written nowhere",
        "S2_L3": "Remove the extension whenever you like; the rest of the app keeps working",
        "ALT_PERAPP": "The per-app traffic table listing apps with live download and upload rates and session totals",

        "S3_H": "Every switch in one pane",
        "S3_P": "Monitoring settings keep the controls together: how data usage resets, whether Wi-Fi details are read, and whether traffic is counted per app.",
        "S3_L1": "Data usage resets daily, weekly, monthly or never — or clear it by hand right there",
        "S3_L2": "Wi-Fi details are their own switch; macOS gates network names behind Location access",
        "S3_L3": "The system extension installs and uninstalls here, with counting as a separate toggle",
        "ALT_SETTINGS": "The Monitoring settings pane with the system extension section and the per-app traffic toggle",

        "S4_H": "The status bar, your way",
        "S4_P": "Show a live sparkline, the two speeds, a compact label — with or without the flag of the country you are exiting from. It is a menu-bar app: no dock icon, no window in the way.",
        "ALT_MB_SPEED": "Menu-bar item showing download and upload speed",
        "ALT_MB_SPARK": "Menu-bar item showing a live throughput sparkline",
        "ALT_MB_LABEL": "Menu-bar item showing a compact label with the exit country flag",
        "ALT_POPOVER": "The Ohayo Network popover: connection, speed, map of the exit location, tunnels and top apps",

        # -- network: privacy ----------------------------------------------
        "PRIVACY_KICKER": "Privacy",
        "PRIVACY_H2": "We have no server. There is nothing for us to collect.",
        "PRIVACY_SUB": "Ohayo Network has no account, no sign-in and no backend — everything it shows is measured on your Mac, by your Mac.",
        "P1_H": "Stays on your Mac",
        "P1_P": "Throughput, per-app traffic, Wi-Fi details and your history of exits are computed and kept locally, in your own preferences.",
        "P2_H": "You choose who hears your IP",
        "P2_P": "Geolocation, latency probes, the speed test and the map reach only the services you enable, always over HTTPS. Disable one and it is never contacted again.",
        "P3_H": "The filter reads no traffic",
        "P3_P": "The content-filter extension allows every flow untouched, never inspects payload, and writes nothing to disk. It only counts bytes per app, in memory.",
        "PRIVACY_LINK": "Read the full privacy policy →",

        # -- network: faq --------------------------------------------------
        "FAQ_KICKER": "FAQ",
        "FAQ_H2": "Before you buy.",
        "Q1": "Do I need a VPN for this to be useful?",
        "A1": "No. Without a tunnel you get live speed, your exit IP and region, latency, Wi-Fi details, data usage and the speed test. If you do use one, each active tunnel is geolocated separately — that is the part no other menu-bar monitor does.",
        "Q2": "What is the system extension, and do I have to install it?",
        "A2": "Per-app traffic is the only feature that needs it, and it is entirely optional — everything else works without it. It is a macOS content-filter extension: read-only, never blocking, never inspecting payload. You install it yourself, approve it in System Settings, and can uninstall it from the same panel at any time.",
        "Q3": "Does it work on Intel Macs?",
        "A3": "No — Ohayo Network is built for Apple silicon and requires macOS 14 Sonoma or later. If you need an Intel build, write to feedback@ohayo.by.",
        "Q4": "Is it a subscription?",
        "A4": "No. It is a one-time purchase on the Mac App Store, and updates to the version you bought arrive the usual way.",
        "Q5": "Does monitoring slow my connection down?",
        "A5": "No. Speed is read from counters the kernel already maintains, once a second. The content filter allows every flow immediately and only asks the kernel for cumulative byte counts — your traffic never routes through user space.",
        "Q6": "What languages does it speak?",
        "A6": "English and Russian, following your system language. If you need another language, write to feedback@ohayo.by.",

        # -- network: closer + footer --------------------------------------
        "CLOSER_H2": "Know where your traffic goes.",
        "CLOSER_SUB": "One window, one status bar item, and no doubt about which country your packets left through.",
        "FOOTER_TAG": "A menu-bar network monitor for macOS.",
        "FOOTER_APPS": "All Ohayo apps",
        "FOOTER_SUPPORT": "Support",
        "FOOTER_PRIVACY": "Privacy Policy",
        "FOOTER_EULA": "EULA",
        "FOOTER_FINE": "Mac App Store copies are licensed under Apple's standard Licensed Application EULA; our own EULA covers directly distributed copies.",
    },

    "ru": {
        # -- shared chrome -------------------------------------------------
        "SKIP": "К содержимому",
        "NAV_LABEL": "Основная навигация",
        "FOOTER_NAV_LABEL": "Нижнее меню",
        "FOOTER_TM": "Apple, Mac, macOS и Mac App Store — товарные знаки Apple Inc., зарегистрированные в США и других странах.",

        # -- hub -----------------------------------------------------------
        "HOME_TITLE": "Ohayo — приложения Ohayo Studio",
        "HOME_DESCRIPTION": "Приложения Ohayo Studio — что вышло, что умеет каждое и где его взять.",
        "NAV_LEGAL": "Документы",
        "H1": "Приложения Ohayo Studio",
        "SUB": "Ниже — всё, что уже вышло. У каждого приложения своя страница: что оно делает, как выглядит и где его взять.",
        "CARD_META": "macOS · Утилиты · Mac App Store",
        "CARD_TEXT": "Скорость, реальный внешний IP и геолокация каждого VPN-туннеля прямо в строке меню. Плюс трафик по приложениям — только на чтение.",
        "CARD_MORE": "Посмотреть →",
        "SOON": "Здесь появятся остальные приложения Ohayo.",
        "HOME_FOOTER_TAG": "Приложения от Ohayo Studio.",
        "FOOTER_LEGAL": "Документы и поддержка",

        # -- network: head -------------------------------------------------
        "TITLE": "Ohayo Network — монитор сети в строке меню macOS",
        "DESCRIPTION": "Скорость, реальный внешний IP и геолокация каждого VPN-туннеля прямо в строке меню macOS. Трафик по приложениям — по желанию. Без аккаунта и аналитики.",
        "OG_IMAGE_ALT": "Ohayo Network в строке меню macOS",

        "NAV_FEATURES": "Возможности",
        "NAV_SCREENS": "Интерфейс",
        "NAV_PRIVACY": "Приватность",
        "NAV_FAQ": "Вопросы",
        "NAV_CTA": "Купить",

        # -- network: hero -------------------------------------------------
        "HERO_H1": "<span>Ваше подключение —</span><span class='grad'>в строке меню.</span>",
        "HERO_SUB": "Скорость приёма и отдачи в реальном времени, страна, из которой на самом деле выходит трафик, и — что редкость — геолокация каждого VPN-туннеля по отдельности. Раздельная маршрутизация видна сразу.",
        "HERO_SECONDARY": "Посмотреть возможности",
        "HERO_NOTE": "macOS 14 или новее · Apple silicon · разовая покупка, без подписки",
        "BADGE_ALT": "Загрузить Ohayo Network в Mac App Store",

        "TRUST_1": "Никаких аккаунтов",
        "TRUST_2": "Без аналитики и рекламы",
        "TRUST_3": "Данные остаются на вашем Mac",

        # -- network: features ---------------------------------------------
        "FEATURES_KICKER": "Что он умеет",
        "FEATURES_H2": "Восемь возможностей за одним значком в строке меню.",
        "FEATURES_SUB": "Всё считывается локально и обновляется в момент изменения — без фоновых служб, без обращений наружу и без ожидания обновления.",

        "F1_H": "Скорость — прямо из ядра",
        "F1_P": "Приём и отдача берутся из счётчиков интерфейсов, которые macOS ведёт сама: без опроса других приложений и без догадок. Живой спарклайн в строке меню, полный график — на панели.",
        "F2_H": "Каждый туннель — отдельно",
        "F2_P": "utun, WireGuard, IPsec: каждый активный туннель определяется через сам этот интерфейс, а не через маршрут по умолчанию. Раздельная маршрутизация отмечается, как только часть трафика уходит не в ту страну.",
        "F3_H": "Внешний IP и регион",
        "F3_P": "Страна, город, провайдер и ASN, флаг в строке меню. История недавних IP и свои метки: отметьте выход как «Дом» или «Офисный VPN» — по стране, городу, провайдеру, ASN или IP.",
        "F4_H": "Трафик по приложениям",
        "F4_P": "Скорость приёма и отдачи по каждому приложению, итоги за сессию, число соединений и удалённые адреса. Топ-5 во всплывающем окне, сортируемая таблица на панели. Работает через системное расширение macOS, которое подключается в настройках.",
        "F5_H": "Задержка и настоящий замер скорости",
        "F5_P": "Время отклика и джиттер до выбранных вами узлов плюс замер скорости Cloudflare по запросу: настраиваемая длительность, число потоков и лимит данных на каждую фазу.",
        "F6_H": "Wi-Fi во всех подробностях",
        "F6_P": "Имя сети, сигнал, канал, стандарт 802.11, тип защиты и скорость передачи — рядом с локальным IP, MAC-адресом и DNS-серверами, которые используются на самом деле.",
        "F7_H": "Расход данных по вашему графику",
        "F7_P": "Накопленные итоги приёма и отдачи с автосбросом — ежедневно, еженедельно, ежемесячно или никогда — и ручной сброс, когда нужен чистый счёт.",
        "F8_H": "Сервисы геолокации — ваши",
        "F8_P": "Три сервиса без ключей по умолчанию, каждый можно изменить, отключить или удалить. Свой добавляется по URL и путям к полям JSON, и вы сами решаете, какой из них главный.",

        # -- network: screens ----------------------------------------------
        "SCREENS_KICKER": "Как это выглядит",
        "SCREENS_H2": "Четыре экрана: всплывающее окно, панель, трафик по приложениям и настройки.",

        "S1_H": "Весь канал в одном окне",
        "S1_P": "Панель складывает всё важное в одну прокрутку: через что вы подключены, где трафик выходит наружу, какая скорость прямо сейчас и что показывает честный замер.",
        "S1_L1": "Карточка подключения: Wi-Fi, Ethernet или VPN — включая канал под туннелем",
        "S1_L2": "Активные туннели, у каждого свой флаг и своя точка выхода",
        "S1_L3": "График скорости и замер Cloudflare: пинг, загрузка, отдача",
        "ALT_DASHBOARD": "Панель Ohayo Network: подключение, активные туннели, график скорости и результаты замера",

        "S2_H": "Видно, какие приложения выходят в сеть",
        "S2_P": "Каждое приложение, которое выходит в сеть, видно вживую — вместе с числом соединений и адресами, с которыми оно общается. Работает через системное расширение macOS — контент-фильтр, который ставится из настроек приложения.",
        "S2_L1": "Только на чтение: каждое соединение пропускается нетронутым — ничего не блокируется, не перенаправляется и не изменяется",
        "S2_L2": "Содержимое трафика не читается никогда; байты считаются в памяти и никуда не записываются",
        "S2_L3": "Расширение можно удалить в любой момент — остальная часть приложения продолжит работать",
        "ALT_PERAPP": "Таблица трафика по приложениям со скоростями приёма и отдачи и итогами за сессию",

        "S3_H": "Все переключатели — в одной панели",
        "S3_P": "Настройки мониторинга держат управление в одном месте: как сбрасывается расход данных, читать ли подробности Wi-Fi и считать ли трафик по приложениям.",
        "S3_L1": "Расход данных сбрасывается ежедневно, еженедельно, ежемесячно или никогда — и вручную одной кнопкой",
        "S3_L2": "Подробности Wi-Fi — отдельный переключатель: имена сетей macOS отдаёт только при доступе к геопозиции",
        "S3_L3": "Системное расширение здесь же ставится и удаляется, а подсчёт включается отдельно",
        "ALT_SETTINGS": "Настройки мониторинга: раздел системного расширения и переключатель трафика по приложениям",

        "S4_H": "Строка меню — на ваш вкус",
        "S4_P": "Живой спарклайн, две скорости или компактная подпись — с флагом страны выхода или без него. Это приложение строки меню: без иконки в Dock и без окна на пути.",
        "ALT_MB_SPEED": "Элемент строки меню со скоростью приёма и отдачи",
        "ALT_MB_SPARK": "Элемент строки меню с живым спарклайном скорости",
        "ALT_MB_LABEL": "Элемент строки меню с компактной подписью и флагом страны выхода",
        "ALT_POPOVER": "Всплывающее окно Ohayo Network: подключение, скорость, карта точки выхода, туннели и топ приложений",

        # -- network: privacy ----------------------------------------------
        "PRIVACY_KICKER": "Приватность",
        "PRIVACY_H2": "У нас нет сервера. Собирать попросту нечем.",
        "PRIVACY_SUB": "В Ohayo Network нет ни аккаунта, ни входа, ни бэкенда — всё, что он показывает, измеряется на вашем Mac и остаётся на нём.",
        "P1_H": "Остаётся на вашем Mac",
        "P1_P": "Скорость, трафик приложений, данные Wi-Fi и история точек выхода считаются и хранятся локально, в ваших же настройках.",
        "P2_H": "Кто узнает ваш IP — решаете вы",
        "P2_P": "Геолокация, замеры задержки, тест скорости и карта обращаются только к включённым вами сервисам и только по HTTPS. Отключите сервис — обращений к нему больше не будет.",
        "P3_H": "Фильтр не читает трафик",
        "P3_P": "Расширение-контент-фильтр пропускает каждое соединение нетронутым, не заглядывает в содержимое и ничего не пишет на диск. Оно лишь считает байты по приложениям — в памяти.",
        "PRIVACY_LINK": "Полная политика конфиденциальности →",

        # -- network: faq --------------------------------------------------
        "FAQ_KICKER": "Вопросы",
        "FAQ_H2": "Перед покупкой.",
        "Q1": "Нужен ли VPN, чтобы это было полезно?",
        "A1": "Нет. Без туннеля вы получаете скорость, внешний IP и регион, задержку, данные Wi-Fi, расход трафика и замер скорости. А если туннель есть, каждый активный определяется отдельно — именно этого не делает ни один другой монитор в строке меню.",
        "Q2": "Что за системное расширение и обязательно ли его ставить?",
        "A2": "Оно нужно только для трафика по приложениям и полностью необязательно — всё остальное работает без него. Это контент-фильтр macOS: только на чтение, ничего не блокирует и не читает содержимое. Вы ставите его сами, подтверждаете в «Настройках системы» и в любой момент удаляете из той же панели.",
        "Q3": "Работает ли на Intel-маках?",
        "A3": "Нет — Ohayo Network собран под Apple silicon и требует macOS 14 Sonoma или новее. Если нужна версия для Intel, напишите на feedback@ohayo.by.",
        "Q4": "Это подписка?",
        "A4": "Нет. Разовая покупка в Mac App Store, обновления купленной версии приходят обычным образом.",
        "Q5": "Мониторинг замедляет соединение?",
        "A5": "Нет. Скорость читается раз в секунду из счётчиков, которые ядро ведёт и без нас. Контент-фильтр сразу пропускает каждое соединение и лишь запрашивает у ядра накопленные байты — трафик не проходит через пользовательское пространство.",
        "Q6": "На каких языках интерфейс?",
        "A6": "Английский и русский, по языку системы. Если вам нужен другой язык, напишите на feedback@ohayo.by.",

        # -- network: closer + footer --------------------------------------
        "CLOSER_H2": "Знайте, куда уходит ваш трафик.",
        "CLOSER_SUB": "Одно окно, один значок в строке меню — и никаких сомнений, через какую страну ушли ваши пакеты.",
        "FOOTER_TAG": "Монитор сети в строке меню macOS.",
        "FOOTER_APPS": "Все приложения Ohayo",
        "FOOTER_SUPPORT": "Поддержка",
        "FOOTER_PRIVACY": "Конфиденциальность",
        "FOOTER_EULA": "Лицензия",
        "FOOTER_FINE": "Копии из Mac App Store лицензируются по стандартному соглашению Apple (Licensed Application EULA); наша собственная лицензия относится к копиям, распространяемым напрямую.",
    },
}

# Placeholders a page needs that are not in STRINGS: the hub uses the home-page
# title/description keys, the app page its own.
PAGES = [
    ("home.tmpl.html", "home_out", "home_path",
     {"TITLE": "HOME_TITLE", "DESCRIPTION": "HOME_DESCRIPTION", "FOOTER_TAG": "HOME_FOOTER_TAG"}),
    ("network.tmpl.html", "network_out", "network_path", {}),
]

root = Path(__file__).parent


def render(template: str, values: dict) -> str:
    for key, value in values.items():
        template = template.replace("{{%s}}" % key, value)
    return template


written = []
for template_file, out_key, path_key, aliases in PAGES:
    template = (root / "templates" / template_file).read_text()
    for code, cfg in LOCALES.items():
        values = dict(STRINGS[code])
        values.update({k: values[v] for k, v in aliases.items()})
        values.update({k: v for k, v in cfg.items() if k.isupper()})
        values["SELF_PATH"] = cfg[path_key]
        values["APP_STORE_URL"] = APP_STORE_URL
        out = root / cfg[out_key]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(template, values))
        written.append((out.relative_to(root), cfg[path_key]))
        print(f"wrote {out.relative_to(root)}")

leftovers = set()
for rel, _ in written:
    text = (root / rel).read_text()
    if "{{" in text:
        leftovers.update(part.split("}}")[0] for part in text.split("{{")[1:])
if leftovers:
    raise SystemExit("unfilled placeholders: " + ", ".join(sorted(leftovers)))

today = date.today().isoformat()
urls = "\n".join(
    f"  <url><loc>https://apps.ohayo.by{path}</loc><lastmod>{today}</lastmod></url>"
    for _, path in written
)
(root / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f"{urls}\n</urlset>\n"
)
print("wrote sitemap.xml")
