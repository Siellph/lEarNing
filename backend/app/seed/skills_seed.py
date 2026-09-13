"""Original graded reading, listening, and dialogue content for lEarNinG.

All English texts and Russian glosses are written for this product.
Do not import plots or wording from Easy English or other publishers.
"""

from __future__ import annotations


def _q(kind: str, prompt: str, answer: str, **extra) -> dict:
    row = {"kind": kind, "prompt": prompt, "answer": answer, "explanation": extra.get("explanation", "")}
    if "options" in extra:
        row["options"] = extra["options"]
    if "accepted" in extra:
        row["accepted"] = extra["accepted"]
    if "speak" in extra:
        row["speak"] = extra["speak"]
    return row


def _choice(prompt: str, answer: str, options: list[str], explanation: str = "") -> dict:
    return _q("choice", prompt, answer, options=options, explanation=explanation)


def _dictation(prompt: str, answer: str, speak: str, accepted: list[str] | None = None, explanation: str = "") -> dict:
    return _q(
        "dictation",
        prompt,
        answer,
        speak=speak,
        accepted=accepted or [answer],
        explanation=explanation,
    )


def _gap(prompt: str, answer: str, accepted: list[str] | None = None, explanation: str = "") -> dict:
    return _q("fill_gap", prompt, answer, accepted=accepted or [answer], explanation=explanation)


# --- Graded reading (~22) ---------------------------------------------------

READING_ITEMS: list[dict] = [
    {
        "slug": "reading-a1-morning-bus",
        "title": "Утренний автобус",
        "description": "Короткий текст о дороге на работу.",
        "kind": "reading",
        "level_code": "A1",
        "body": (
            "Every morning Lena wakes up at seven. She drinks tea and eats bread with cheese. "
            "Then she takes the bus to work. The bus is often full, but she finds a seat near the window. "
            "She looks at the trees and feels calm before a busy day."
        ),
        "keywords": [
            {"en": "wake up", "ru": "просыпаться"},
            {"en": "bus", "ru": "автобус"},
            {"en": "seat", "ru": "место (сиденье)"},
            {"en": "calm", "ru": "спокойный"},
        ],
        "questions": [
            _choice("What does Lena drink?", "tea", ["coffee", "tea", "juice", "water"], "В тексте: drinks tea."),
            _choice("How does she go to work?", "by bus", ["by car", "by train", "by bus", "on foot"], "She takes the bus."),
            _choice("Where does she like to sit?", "near the window", ["near the door", "near the window", "at the back", "standing"], "a seat near the window"),
        ],
    },
    {
        "slug": "reading-a1-new-neighbour",
        "title": "Новый сосед",
        "description": "Знакомство в доме.",
        "kind": "reading",
        "level_code": "A1",
        "body": (
            "Omar moves into a small flat on Green Street. On the first day his neighbour Anna knocks on the door. "
            "She brings a cake and says hello. Omar smiles and invites her for coffee next week. "
            "He thinks the building feels friendly already."
        ),
        "keywords": [
            {"en": "neighbour", "ru": "сосед / соседка"},
            {"en": "flat", "ru": "квартира"},
            {"en": "knock", "ru": "стучать"},
            {"en": "invite", "ru": "приглашать"},
        ],
        "questions": [
            _choice("Where does Omar live now?", "on Green Street", ["on Park Road", "on Green Street", "near the river", "in a hotel"], "on Green Street"),
            _choice("What does Anna bring?", "a cake", ["flowers", "a cake", "books", "tea"], "She brings a cake."),
            _choice("What does Omar plan next week?", "coffee with Anna", ["a party", "coffee with Anna", "a trip", "painting"], "invites her for coffee next week"),
        ],
    },
    {
        "slug": "reading-a1-market-day",
        "title": "День на рынке",
        "description": "Покупки овощей и фруктов.",
        "kind": "reading",
        "level_code": "A1",
        "body": (
            "On Saturday Maya goes to the outdoor market. She buys tomatoes, apples, and fresh bread. "
            "The seller gives her a free orange because she is a regular customer. "
            "Maya puts everything in a cloth bag and walks home slowly."
        ),
        "keywords": [
            {"en": "market", "ru": "рынок"},
            {"en": "fresh", "ru": "свежий"},
            {"en": "regular", "ru": "постоянный (клиент)"},
            {"en": "cloth bag", "ru": "тканевая сумка"},
        ],
        "questions": [
            _choice("When does Maya go to the market?", "on Saturday", ["on Monday", "on Friday", "on Saturday", "every day"], "On Saturday"),
            _choice("What free thing does she get?", "an orange", ["an apple", "bread", "an orange", "tomatoes"], "a free orange"),
            _choice("How does she carry the food?", "in a cloth bag", ["in a box", "in a cloth bag", "in her pockets", "in a suitcase"], "cloth bag"),
        ],
    },
    {
        "slug": "reading-a2-library-card",
        "title": "Читательский билет",
        "description": "Первый визит в библиотеку.",
        "kind": "reading",
        "level_code": "A2",
        "body": (
            "Last month Denis got a library card. He wanted quiet books about travel and science. "
            "The librarian showed him how to search the catalogue and how long he could keep a book. "
            "Now he borrows two books every fortnight and returns them on time. "
            "He says the library saves him money and helps him learn new words."
        ),
        "keywords": [
            {"en": "library card", "ru": "читательский билет"},
            {"en": "catalogue", "ru": "каталог"},
            {"en": "borrow", "ru": "брать (на время)"},
            {"en": "fortnight", "ru": "две недели"},
        ],
        "questions": [
            _choice("What topics interest Denis?", "travel and science", ["sport and cooking", "travel and science", "art only", "music"], "travel and science"),
            _choice("How often does he borrow books?", "every fortnight", ["every day", "once a year", "every fortnight", "never"], "every fortnight"),
            _choice("Why does he like the library?", "it saves money and helps vocabulary", ["it is noisy", "it sells food", "it saves money and helps vocabulary", "it is closed"], "saves him money and helps him learn new words"),
        ],
    },
    {
        "slug": "reading-a2-rainy-picnic",
        "title": "Пикник под дождём",
        "description": "Планы меняются из‑за погоды.",
        "kind": "reading",
        "level_code": "A2",
        "body": (
            "The family planned a picnic by the lake. In the morning the sky was clear, so they packed sandwiches and a ball. "
            "At noon dark clouds arrived and cold rain started. They ran to the car and ate inside while listening to music. "
            "Nobody was angry. They joked that indoor picnics can be fun too."
        ),
        "keywords": [
            {"en": "picnic", "ru": "пикник"},
            {"en": "pack", "ru": "упаковывать / собирать"},
            {"en": "cloud", "ru": "облако"},
            {"en": "joke", "ru": "шутить"},
        ],
        "questions": [
            _choice("Where did they want to picnic?", "by the lake", ["in the park", "by the lake", "at school", "on a roof"], "by the lake"),
            _choice("What happened at noon?", "it started raining", ["the sun got hotter", "it started raining", "they swam", "they slept"], "cold rain started"),
            _choice("How did they feel about the change?", "they were not angry", ["they were furious", "they cancelled forever", "they were not angry", "they cried"], "Nobody was angry"),
        ],
    },
    {
        "slug": "reading-a2-office-plant",
        "title": "Растение в офисе",
        "description": "Коллеги ухаживают за цветком.",
        "kind": "reading",
        "level_code": "A2",
        "body": (
            "Someone left a small plant on the shared desk. At first nobody watered it. "
            "Then Irina brought a cup of water every Monday. Soon the leaves became greener, and people started smiling at the plant. "
            "Now the team takes turns caring for it. They call it 'Office Friend'."
        ),
        "keywords": [
            {"en": "shared", "ru": "общий"},
            {"en": "water (v.)", "ru": "поливать"},
            {"en": "leaf / leaves", "ru": "лист / листья"},
            {"en": "take turns", "ru": "делать по очереди"},
        ],
        "questions": [
            _choice("Where was the plant?", "on the shared desk", ["in the kitchen", "on the shared desk", "outside", "in a box"], "shared desk"),
            _choice("Who started watering it regularly?", "Irina", ["the boss", "Irina", "a guest", "nobody"], "Irina"),
            _choice("What nickname do they use?", "Office Friend", ["Green Boss", "Office Friend", "Quiet Leaf", "Desk King"], "Office Friend"),
        ],
    },
    {
        "slug": "reading-b1-night-shift",
        "title": "Ночная смена",
        "description": "Работа в больнице ночью.",
        "kind": "reading",
        "level_code": "B1",
        "body": (
            "Sofia works as a nurse on the night shift three times a week. The hospital corridor is quieter after midnight, "
            "but alarms still break the silence. She checks patients, writes short notes, and drinks strong tea to stay alert. "
            "On her free mornings she sleeps until noon and then walks in the park. "
            "She admits the schedule is hard, yet she likes helping people when few others are around."
        ),
        "keywords": [
            {"en": "night shift", "ru": "ночная смена"},
            {"en": "corridor", "ru": "коридор"},
            {"en": "alert", "ru": "бодрый / внимательный"},
            {"en": "admit", "ru": "признавать"},
        ],
        "questions": [
            _choice("How often does Sofia work nights?", "three times a week", ["every night", "once a month", "three times a week", "weekends only"], "three times a week"),
            _choice("What helps her stay awake?", "strong tea", ["loud music", "strong tea", "cold showers at work", "sugar only"], "strong tea"),
            _choice("Why does she keep the job?", "she likes helping when few others are around", ["the pay is endless", "she hates mornings", "she likes helping when few others are around", "she wants fame"], "helping people when few others are around"),
        ],
    },
    {
        "slug": "reading-b1-second-hand-bike",
        "title": "Велосипед с рук",
        "description": "Покупка б/у велосипеда.",
        "kind": "reading",
        "level_code": "B1",
        "body": (
            "After months of crowded buses, Pavel decided to buy a second-hand bike. "
            "He checked the brakes, the tyres, and the chain at a small workshop before paying. "
            "The seller explained a few maintenance tips and wished him safe rides. "
            "Now Pavel cycles to the office and arrives earlier — and less tired — than before."
        ),
        "keywords": [
            {"en": "second-hand", "ru": "подержанный / с рук"},
            {"en": "brake", "ru": "тормоз"},
            {"en": "maintenance", "ru": "обслуживание / уход"},
            {"en": "cycle (v.)", "ru": "ехать на велосипеде"},
        ],
        "questions": [
            _choice("Why did Pavel want a bike?", "buses were crowded", ["he lost his car", "buses were crowded", "he moved abroad", "he hates walking"], "crowded buses"),
            _choice("What did he check before buying?", "brakes, tyres, and chain", ["only the colour", "brakes, tyres, and chain", "the basket size", "the bell"], "brakes, tyres, and chain"),
            _choice("What changed after he started cycling?", "he arrives earlier and less tired", ["he is always late", "he arrives earlier and less tired", "he quit work", "he sold the bike"], "arrives earlier — and less tired"),
        ],
    },
    {
        "slug": "reading-b2-community-garden",
        "title": "Общий сад",
        "description": "Соседи выращивают овощи вместе.",
        "kind": "reading",
        "level_code": "B2",
        "body": (
            "Behind the apartment block there used to be an empty yard full of weeds. "
            "A group of residents asked the council for permission to start a community garden. "
            "They raised funds for soil and tools, then planted beans, herbs, and sunflowers. "
            "Children water the beds after school, and in late summer they share harvest baskets. "
            "The project has not removed every problem in the neighbourhood, but people talk to each other more often now."
        ),
        "keywords": [
            {"en": "weed", "ru": "сорняк"},
            {"en": "council", "ru": "муниципалитет / совет"},
            {"en": "raise funds", "ru": "собирать средства"},
            {"en": "harvest", "ru": "урожай"},
        ],
        "questions": [
            _choice("What was in the yard before?", "weeds", ["a pool", "weeds", "a shop", "cars only"], "full of weeds"),
            _choice("Who waters the plants after school?", "children", ["the council alone", "tourists", "children", "robots"], "Children water the beds"),
            _choice("What social effect is mentioned?", "neighbours talk more often", ["everyone moved away", "neighbours talk more often", "the block closed", "prices fell"], "people talk to each other more often"),
        ],
    },
    {
        "slug": "reading-b2-remote-week",
        "title": "Неделя удалёнки",
        "description": "Плюсы и минусы работы из дома.",
        "kind": "reading",
        "level_code": "B2",
        "body": (
            "For one week Nadia’s team worked entirely from home. Without the commute she gained almost two hours a day, "
            "which she spent cooking proper lunches and finishing a short online course. "
            "Still, she missed quick hallway chats that often solved small problems faster than long emails. "
            "On Friday the team agreed to keep two remote days and three office days — a compromise that felt practical rather than perfect."
        ),
        "keywords": [
            {"en": "commute", "ru": "дорога на работу"},
            {"en": "hallway", "ru": "коридор (в офисе)"},
            {"en": "compromise", "ru": "компромисс"},
            {"en": "practical", "ru": "практичный"},
        ],
        "questions": [
            _choice("What did Nadia gain without commuting?", "almost two hours a day", ["a new laptop", "almost two hours a day", "a promotion", "free parking"], "almost two hours a day"),
            _choice("What did she miss?", "quick hallway chats", ["long emails", "online courses", "quick hallway chats", "cooking"], "hallway chats"),
            _choice("What schedule did they choose?", "two remote + three office days", ["fully remote", "fully office", "two remote + three office days", "weekends only"], "two remote days and three office days"),
        ],
    },
    {
        "slug": "reading-a1-lost-keys",
        "title": "Потерянные ключи",
        "description": "Поиск ключей дома.",
        "kind": "reading",
        "level_code": "A1",
        "body": (
            "This morning Tim cannot find his keys. He looks under the sofa and in his jacket. "
            "His sister finds them on the kitchen table next to a bowl of fruit. "
            "Tim laughs and puts the keys on a small hook by the door."
        ),
        "keywords": [
            {"en": "keys", "ru": "ключи"},
            {"en": "sofa", "ru": "диван"},
            {"en": "hook", "ru": "крючок"},
            {"en": "find", "ru": "находить"},
        ],
        "questions": [
            _choice("What is Tim looking for?", "his keys", ["his phone", "his keys", "his bag", "his shoes"], "his keys"),
            _choice("Who finds the keys?", "his sister", ["his neighbour", "his sister", "a guest", "nobody"], "His sister finds them"),
            _choice("Where does he put the keys later?", "on a hook by the door", ["in the fridge", "under the sofa", "on a hook by the door", "in a bowl"], "on a small hook by the door"),
        ],
    },
    {
        "slug": "reading-a1-pet-goldfish",
        "title": "Золотая рыбка",
        "description": "Уход за питомцем.",
        "kind": "reading",
        "level_code": "A1",
        "body": (
            "Nora has a small goldfish in a glass bowl. Every evening she gives it a little food. "
            "She changes the water once a week and keeps the bowl away from the hot window. "
            "The fish swims slowly and Nora watches it after homework."
        ),
        "keywords": [
            {"en": "goldfish", "ru": "золотая рыбка"},
            {"en": "bowl", "ru": "аквариумная чаша / миска"},
            {"en": "change the water", "ru": "менять воду"},
            {"en": "homework", "ru": "домашнее задание"},
        ],
        "questions": [
            _choice("What pet does Nora have?", "a goldfish", ["a cat", "a dog", "a goldfish", "a bird"], "a small goldfish"),
            _choice("How often does she change the water?", "once a week", ["every day", "once a month", "once a week", "never"], "once a week"),
            _choice("When does she watch the fish?", "after homework", ["before breakfast", "at school", "after homework", "at midnight"], "after homework"),
        ],
    },
    {
        "slug": "reading-a1-birthday-card",
        "title": "Открытка на день рождения",
        "description": "Подарок для бабушки.",
        "kind": "reading",
        "level_code": "A1",
        "body": (
            "Tomorrow is Grandma's birthday. Rita buys a bright card and writes a short message. "
            "She also buys yellow flowers at the corner shop. "
            "In the evening the family sings and Grandma smiles for a long time."
        ),
        "keywords": [
            {"en": "birthday", "ru": "день рождения"},
            {"en": "card", "ru": "открытка"},
            {"en": "message", "ru": "сообщение / текст"},
            {"en": "corner shop", "ru": "магазин на углу"},
        ],
        "questions": [
            _choice("Whose birthday is it?", "Grandma's", ["Rita's", "Grandma's", "a teacher's", "a neighbour's"], "Grandma's birthday"),
            _choice("What colour are the flowers?", "yellow", ["red", "blue", "yellow", "white"], "yellow flowers"),
            _choice("What does the family do in the evening?", "sings", ["travels", "sings", "studies", "paints"], "the family sings"),
        ],
    },
    {
        "slug": "reading-a2-train-ticket",
        "title": "Билет на поезд",
        "description": "Покупка билета в кассе.",
        "kind": "reading",
        "level_code": "A2",
        "body": (
            "Anton needed a train ticket to visit his uncle. At the station he chose a morning seat by the window. "
            "The clerk asked for his ID and printed a paper ticket with a QR code. "
            "Anton saved the PDF on his phone as a backup and arrived twenty minutes early."
        ),
        "keywords": [
            {"en": "ticket", "ru": "билет"},
            {"en": "clerk", "ru": "кассир / служащий"},
            {"en": "backup", "ru": "запасной вариант / копия"},
            {"en": "QR code", "ru": "QR-код"},
        ],
        "questions": [
            _choice("Why did Anton need a ticket?", "to visit his uncle", ["to go to school", "to visit his uncle", "to buy food", "to work nights"], "visit his uncle"),
            _choice("What did he save on his phone?", "a PDF backup", ["music", "a PDF backup", "photos of the clerk", "a map of Europe"], "saved the PDF"),
            _choice("How early did he arrive?", "twenty minutes early", ["one hour late", "exactly on time", "twenty minutes early", "the next day"], "twenty minutes early"),
        ],
    },
    {
        "slug": "reading-a2-burnt-toast",
        "title": "Подгоревший тост",
        "description": "Маленькая кухонная неудача.",
        "kind": "reading",
        "level_code": "A2",
        "body": (
            "Lara wanted a quick breakfast before work. She put bread in the toaster and opened her emails. "
            "A minute later she smelled smoke. The toast was black, so she opened the window and made porridge instead. "
            "She set a louder timer on her phone for next time."
        ),
        "keywords": [
            {"en": "toaster", "ru": "тостер"},
            {"en": "smell", "ru": "чувствовать запах"},
            {"en": "porridge", "ru": "каша"},
            {"en": "timer", "ru": "таймер"},
        ],
        "questions": [
            _choice("What went wrong?", "the toast burned", ["she lost her phone", "the toast burned", "the window broke", "she missed the bus"], "toast was black"),
            _choice("What did she eat instead?", "porridge", ["eggs", "porridge", "cake", "nothing"], "made porridge instead"),
            _choice("What will she do next time?", "use a louder timer", ["buy a new fridge", "skip breakfast", "use a louder timer", "cook outside"], "set a louder timer"),
        ],
    },
    {
        "slug": "reading-a2-weekend-hike",
        "title": "Поход в выходные",
        "description": "Прогулка по тропе с друзьями.",
        "kind": "reading",
        "level_code": "A2",
        "body": (
            "On Sunday four friends hiked a forest trail near the river. They packed water, sandwiches, and a small first-aid kit. "
            "After two hours they reached a viewpoint and took photos of the valley. "
            "On the way down it got muddy, but nobody fell, and they promised to return in spring."
        ),
        "keywords": [
            {"en": "hike", "ru": "ходить в поход / пеший маршрут"},
            {"en": "trail", "ru": "тропа"},
            {"en": "viewpoint", "ru": "смотровая площадка"},
            {"en": "muddy", "ru": "грязный / слякотный"},
        ],
        "questions": [
            _choice("How many friends went hiking?", "four", ["two", "three", "four", "ten"], "four friends"),
            _choice("What did they see from the viewpoint?", "the valley", ["the ocean", "the valley", "a stadium", "a factory"], "photos of the valley"),
            _choice("When do they want to return?", "in spring", ["tonight", "in winter only", "in spring", "never"], "return in spring"),
        ],
    },
    {
        "slug": "reading-b1-language-exchange",
        "title": "Языковой обмен",
        "description": "Практика двух языков в кафе.",
        "kind": "reading",
        "level_code": "B1",
        "body": (
            "Once a week Katya meets Diego in a quiet café for a language exchange. "
            "For thirty minutes they speak only English; then they switch to Spanish. "
            "They correct each other gently and write useful phrases in a shared notebook. "
            "After three months Katya feels braver ordering food abroad, and Diego finally understands Russian jokes in class."
        ),
        "keywords": [
            {"en": "language exchange", "ru": "языковой обмен"},
            {"en": "switch", "ru": "переключаться"},
            {"en": "gently", "ru": "мягко / спокойно"},
            {"en": "abroad", "ru": "за границей"},
        ],
        "questions": [
            _choice("How often do they meet?", "once a week", ["every day", "once a week", "once a year", "only online"], "Once a week"),
            _choice("What do they use to save phrases?", "a shared notebook", ["sticky walls", "a shared notebook", "only memory", "a radio"], "shared notebook"),
            _choice("What improved for Katya?", "ordering food abroad", ["driving", "ordering food abroad", "cooking meat", "singing"], "braver ordering food abroad"),
        ],
    },
    {
        "slug": "reading-b1-thrift-jacket",
        "title": "Куртка из секонда",
        "description": "Находка в комиссионном магазине.",
        "kind": "reading",
        "level_code": "B1",
        "body": (
            "Masha prefers thrift shops because she likes unique clothes and lower prices. "
            "Last Saturday she found a warm wool jacket that fitted perfectly after a small repair to the zipper. "
            "She washed it carefully and wore it to a winter market. "
            "Two friends asked where she bought it, and she happily shared the shop's address."
        ),
        "keywords": [
            {"en": "thrift shop", "ru": "секонд-хенд / комиссионка"},
            {"en": "wool", "ru": "шерсть / шерстяной"},
            {"en": "zipper", "ru": "молния (застёжка)"},
            {"en": "fit", "ru": "сидеть (об одежде)"},
        ],
        "questions": [
            _choice("Why does Masha like thrift shops?", "unique clothes and lower prices", ["free food", "unique clothes and lower prices", "louder music", "longer queues"], "unique clothes and lower prices"),
            _choice("What needed repair?", "the zipper", ["the buttons only", "the zipper", "the colour", "the sleeves"], "repair to the zipper"),
            _choice("What did she share with friends?", "the shop's address", ["her salary", "the shop's address", "a secret recipe", "nothing"], "shared the shop's address"),
        ],
    },
    {
        "slug": "reading-b1-food-bank",
        "title": "Волонтёрство на складе",
        "description": "Помощь в продовольственном банке.",
        "kind": "reading",
        "level_code": "B1",
        "body": (
            "Every other Saturday Oleg volunteers at a local food bank. He sorts donated cans, checks expiry dates, and packs boxes for families. "
            "The work is physical, but the team chat is friendly and breaks include strong coffee. "
            "Oleg says the shift reminds him how small actions can reduce stress for neighbours who are short on time and money."
        ),
        "keywords": [
            {"en": "volunteer", "ru": "работать волонтёром"},
            {"en": "food bank", "ru": "продовольственный банк / склад помощи"},
            {"en": "expiry date", "ru": "срок годности"},
            {"en": "shift", "ru": "смена"},
        ],
        "questions": [
            _choice("How often does Oleg volunteer?", "every other Saturday", ["every day", "every other Saturday", "once a year", "only Mondays"], "Every other Saturday"),
            _choice("What does he check on cans?", "expiry dates", ["prices", "expiry dates", "colours", "brands only"], "checks expiry dates"),
            _choice("What does the shift remind him of?", "small actions helping neighbours", ["winning prizes", "small actions helping neighbours", "office politics", "long holidays"], "small actions can reduce stress for neighbours"),
        ],
    },
    {
        "slug": "reading-b2-podcast-habit",
        "title": "Привычка к подкастам",
        "description": "Как аудио помогает в дороге.",
        "kind": "reading",
        "level_code": "B2",
        "body": (
            "Instead of scrolling social media on the tram, Ilya started listening to short science podcasts. "
            "He chooses episodes under twenty minutes so he can finish one before his stop. "
            "At first the hosts spoke too quickly, so he lowered the speed to 0.9 and kept a notes app for new terms. "
            "After two months he notices he remembers more vocabulary and feels less restless during delays."
        ),
        "keywords": [
            {"en": "scroll", "ru": "листать (ленту)"},
            {"en": "episode", "ru": "выпуск / эпизод"},
            {"en": "restless", "ru": "беспокойный / нетерпеливый"},
            {"en": "vocabulary", "ru": "словарный запас"},
        ],
        "questions": [
            _choice("What did Ilya replace on the tram?", "scrolling social media", ["sleeping", "scrolling social media", "calling clients", "eating lunch"], "Instead of scrolling social media"),
            _choice("Why under twenty minutes?", "to finish before his stop", ["to skip learning", "to finish before his stop", "because Wi‑Fi dies", "host rules"], "finish one before his stop"),
            _choice("What changed after two months?", "more vocabulary, less restless in delays", ["he quit the tram", "more vocabulary, less restless in delays", "he stopped notes", "hosts got slower"], "remembers more vocabulary and feels less restless"),
        ],
    },
    {
        "slug": "reading-b2-coworking-trial",
        "title": "Пробная неделя коворкинга",
        "description": "Фрилансер тестирует общее пространство.",
        "kind": "reading",
        "level_code": "B2",
        "body": (
            "Vera tested a coworking space for one week because her flat felt too quiet for deep work. "
            "The day pass included a desk, fast Wi‑Fi, and unlimited tea. She liked the focus rooms but disliked the noisy kitchen at noon. "
            "On Friday she bought a part-time membership for three mornings a week — enough structure without losing her home office entirely."
        ),
        "keywords": [
            {"en": "coworking", "ru": "коворкинг"},
            {"en": "day pass", "ru": "дневной пропуск"},
            {"en": "focus room", "ru": "тихая комната для концентрации"},
            {"en": "membership", "ru": "членство / абонемент"},
        ],
        "questions": [
            _choice("Why did Vera try coworking?", "her flat felt too quiet", ["free lunch forever", "her flat felt too quiet", "she lost Wi‑Fi at home", "her boss required it"], "flat felt too quiet"),
            _choice("What did she dislike?", "the noisy kitchen at noon", ["the desk", "the tea", "the noisy kitchen at noon", "the Wi‑Fi"], "disliked the noisy kitchen"),
            _choice("What membership did she choose?", "part-time, three mornings", ["full nights only", "part-time, three mornings", "one year prepaid", "none"], "three mornings a week"),
        ],
    },
    {
        "slug": "reading-b2p-invoice-delay",
        "title": "Задержка счёта",
        "description": "Клиент и фрилансер решают платёжную путаницу.",
        "kind": "reading",
        "level_code": "B2+",
        "body": (
            "When a client's payment was five days late, Dana checked her sent folder before writing an angry message. "
            "She discovered the invoice had landed in spam and the purchase order number was missing from the subject line. "
            "She resent a clearer PDF, copied the accounts team, and proposed a 48-hour confirmation window. "
            "The money arrived the next morning; Dana later added a checklist so the same mix-up would be less likely."
        ),
        "keywords": [
            {"en": "invoice", "ru": "счёт"},
            {"en": "spam", "ru": "спам"},
            {"en": "purchase order", "ru": "заказ на закупку (PO)"},
            {"en": "mix-up", "ru": "путаница / накладка"},
        ],
        "questions": [
            _choice("Where had the invoice gone?", "into spam", ["to a rival", "into spam", "to a printer", "nowhere"], "landed in spam"),
            _choice("What was missing from the subject line?", "the purchase order number", ["Dana's name", "the purchase order number", "emojis", "the price"], "purchase order number was missing"),
            _choice("What did Dana add afterwards?", "a checklist", ["a lawsuit", "a checklist", "higher fees only", "silence"], "added a checklist"),
            _choice("How soon did payment arrive after the fix?", "the next morning", ["a year later", "the next morning", "never", "after a court case"], "arrived the next morning"),
        ],
    },
]


# --- Listening / dictation (~22) --------------------------------------------

LISTENING_ITEMS: list[dict] = [
    {
        "slug": "listening-a1-weather-note",
        "title": "Заметка о погоде",
        "description": "Короткая фраза о погоде + диктант.",
        "kind": "listening",
        "level_code": "A1",
        "body": "It is cold today. Please wear a warm jacket.",
        "keywords": [
            {"en": "cold", "ru": "холодный"},
            {"en": "wear", "ru": "носить (одежду)"},
            {"en": "jacket", "ru": "куртка"},
        ],
        "questions": [
            _choice("What is the weather like?", "cold", ["hot", "cold", "rainy", "windy"], "It is cold today."),
            _dictation(
                "Напечатайте, что нужно надеть (второе предложение).",
                "Please wear a warm jacket.",
                "Please wear a warm jacket.",
                accepted=["Please wear a warm jacket", "please wear a warm jacket"],
                explanation="Вторая фраза аудио.",
            ),
        ],
    },
    {
        "slug": "listening-a1-shop-hours",
        "title": "Часы работы магазина",
        "description": "Информация у входа.",
        "kind": "listening",
        "level_code": "A1",
        "body": "The shop opens at nine and closes at eight. Sunday is closed.",
        "keywords": [
            {"en": "open", "ru": "открываться"},
            {"en": "close", "ru": "закрываться"},
            {"en": "Sunday", "ru": "воскресенье"},
        ],
        "questions": [
            _choice("When does the shop open?", "at nine", ["at eight", "at nine", "at ten", "at noon"], "opens at nine"),
            _choice("Which day is the shop closed?", "Sunday", ["Monday", "Friday", "Sunday", "Saturday"], "Sunday is closed"),
            _dictation(
                "Напечатайте время закрытия из первой фразы.",
                "closes at eight",
                "closes at eight",
                accepted=["closes at eight", "Closes at eight"],
            ),
        ],
    },
    {
        "slug": "listening-a1-meet-friend",
        "title": "Встреча с другом",
        "description": "Где и когда встретиться.",
        "kind": "listening",
        "level_code": "A1",
        "body": "Let's meet at the station at five. I will wait near the ticket office.",
        "keywords": [
            {"en": "meet", "ru": "встречаться"},
            {"en": "station", "ru": "станция / вокзал"},
            {"en": "ticket office", "ru": "билетная касса"},
        ],
        "questions": [
            _choice("Where will they meet?", "at the station", ["at school", "at the station", "at home", "in a café"], "at the station"),
            _choice("What time?", "at five", ["at four", "at five", "at six", "at seven"], "at five"),
            _dictation(
                "Напечатайте, где ждать.",
                "near the ticket office",
                "near the ticket office",
                accepted=["near the ticket office", "Near the ticket office"],
            ),
        ],
    },
    {
        "slug": "listening-a2-kitchen-tip",
        "title": "Совет на кухне",
        "description": "Как варить пасту.",
        "kind": "listening",
        "level_code": "A2",
        "body": "Boil the water first. Add salt, then put the pasta in. Stir it after two minutes.",
        "keywords": [
            {"en": "boil", "ru": "кипятить"},
            {"en": "add", "ru": "добавлять"},
            {"en": "stir", "ru": "мешать"},
        ],
        "questions": [
            _choice("What do you do first?", "boil the water", ["add salt", "stir", "boil the water", "eat"], "Boil the water first"),
            _choice("When should you stir?", "after two minutes", ["immediately", "after two minutes", "never", "after an hour"], "after two minutes"),
            _dictation(
                "Напечатайте шаг с солью.",
                "Add salt, then put the pasta in.",
                "Add salt, then put the pasta in.",
                accepted=["Add salt, then put the pasta in", "add salt, then put the pasta in"],
            ),
        ],
    },
    {
        "slug": "listening-a2-missed-call",
        "title": "Пропущенный звонок",
        "description": "Голосовое сообщение.",
        "kind": "listening",
        "level_code": "A2",
        "body": "Hi, it's Mark. I missed your call because I was in a meeting. Call me after lunch, please.",
        "keywords": [
            {"en": "miss a call", "ru": "пропустить звонок"},
            {"en": "meeting", "ru": "совещание"},
            {"en": "after lunch", "ru": "после обеда"},
        ],
        "questions": [
            _choice("Who is speaking?", "Mark", ["Tom", "Mark", "Anna", "the boss"], "it's Mark"),
            _choice("Why did he miss the call?", "he was in a meeting", ["the phone broke", "he was in a meeting", "he was sleeping", "he was abroad"], "in a meeting"),
            _dictation(
                "Напечатайте просьбу в конце.",
                "Call me after lunch, please.",
                "Call me after lunch, please.",
                accepted=["Call me after lunch, please", "call me after lunch please"],
            ),
        ],
    },
    {
        "slug": "listening-a2-bus-delay",
        "title": "Задержка автобуса",
        "description": "Объявление на остановке.",
        "kind": "listening",
        "level_code": "A2",
        "body": "Bus number twelve is delayed by fifteen minutes. We are sorry for the inconvenience.",
        "keywords": [
            {"en": "delayed", "ru": "задержан"},
            {"en": "inconvenience", "ru": "неудобство"},
            {"en": "sorry", "ru": "извините / жаль"},
        ],
        "questions": [
            _choice("Which bus is delayed?", "number twelve", ["number two", "number twelve", "number twenty", "all buses"], "Bus number twelve"),
            _choice("How long is the delay?", "fifteen minutes", ["five minutes", "fifty minutes", "fifteen minutes", "one hour"], "fifteen minutes"),
            _dictation(
                "Напечатайте извинение.",
                "We are sorry for the inconvenience.",
                "We are sorry for the inconvenience.",
                accepted=["We are sorry for the inconvenience", "we are sorry for the inconvenience"],
            ),
        ],
    },
    {
        "slug": "listening-b1-museum-rules",
        "title": "Правила музея",
        "description": "Краткий инструктаж у входа.",
        "kind": "listening",
        "level_code": "B1",
        "body": (
            "Please keep your bags in the lockers. Do not touch the exhibits. "
            "Photography without flash is allowed in most rooms."
        ),
        "keywords": [
            {"en": "locker", "ru": "ячейка / шкафчик"},
            {"en": "exhibit", "ru": "экспонат"},
            {"en": "flash", "ru": "вспышка"},
        ],
        "questions": [
            _choice("Where should bags go?", "in the lockers", ["on the floor", "in the lockers", "with a guide", "outside only"], "in the lockers"),
            _choice("Is photography allowed?", "yes, without flash in most rooms", ["never", "only with flash", "yes, without flash in most rooms", "only selfies"], "without flash… most rooms"),
            _dictation(
                "Напечатайте запрет про экспонаты.",
                "Do not touch the exhibits.",
                "Do not touch the exhibits.",
                accepted=["Do not touch the exhibits", "Don't touch the exhibits"],
            ),
        ],
    },
    {
        "slug": "listening-b1-project-update",
        "title": "Обновление по проекту",
        "description": "Короткий стендап на работе.",
        "kind": "listening",
        "level_code": "B1",
        "body": (
            "We finished the draft yesterday. Today we need feedback from the design team. "
            "The final version should be ready by Thursday."
        ),
        "keywords": [
            {"en": "draft", "ru": "черновик"},
            {"en": "feedback", "ru": "обратная связь"},
            {"en": "final version", "ru": "финальная версия"},
        ],
        "questions": [
            _choice("When was the draft finished?", "yesterday", ["today", "yesterday", "Thursday", "last month"], "yesterday"),
            _choice("Who should give feedback?", "the design team", ["clients only", "the design team", "security", "nobody"], "design team"),
            _dictation(
                "Напечатайте срок финальной версии.",
                "The final version should be ready by Thursday.",
                "The final version should be ready by Thursday.",
                accepted=["The final version should be ready by Thursday", "the final version should be ready by Thursday"],
            ),
        ],
    },
    {
        "slug": "listening-b2-city-survey",
        "title": "Опрос жителей",
        "description": "Сообщение о городском опросе.",
        "kind": "listening",
        "level_code": "B2",
        "body": (
            "The city is collecting opinions about new bike lanes. "
            "You can fill in the online form until the end of the month. "
            "Results will be published on the official website."
        ),
        "keywords": [
            {"en": "opinion", "ru": "мнение"},
            {"en": "bike lane", "ru": "велодорожка"},
            {"en": "publish", "ru": "публиковать"},
        ],
        "questions": [
            _choice("What is the survey about?", "new bike lanes", ["parking fees", "new bike lanes", "school exams", "museums"], "new bike lanes"),
            _choice("Where will results appear?", "on the official website", ["on TV only", "in shops", "on the official website", "nowhere"], "official website"),
            _dictation(
                "Напечатайте, до когда можно заполнить форму.",
                "until the end of the month",
                "until the end of the month",
                accepted=["until the end of the month", "Until the end of the month"],
            ),
        ],
    },
    {
        "slug": "listening-b2-apartment-viewing",
        "title": "Просмотр квартиры",
        "description": "Агент описывает квартиру по телефону.",
        "kind": "listening",
        "level_code": "B2",
        "body": (
            "The flat has two bedrooms and a bright kitchen. "
            "The rent includes heating but not electricity. "
            "We can show it tomorrow afternoon if that suits you."
        ),
        "keywords": [
            {"en": "rent", "ru": "аренда / плата за аренду"},
            {"en": "heating", "ru": "отопление"},
            {"en": "suit (v.)", "ru": "подходить (по времени)"},
        ],
        "questions": [
            _choice("How many bedrooms?", "two", ["one", "two", "three", "none"], "two bedrooms"),
            _choice("What does the rent include?", "heating", ["electricity", "heating", "internet only", "furniture"], "includes heating"),
            _dictation(
                "Напечатайте предложение про показ.",
                "We can show it tomorrow afternoon if that suits you.",
                "We can show it tomorrow afternoon if that suits you.",
                accepted=[
                    "We can show it tomorrow afternoon if that suits you",
                    "we can show it tomorrow afternoon if that suits you",
                ],
            ),
        ],
    },
    {
        "slug": "listening-a1-bakery-order",
        "title": "Заказ в пекарне",
        "description": "Что купить утром.",
        "kind": "listening",
        "level_code": "A1",
        "body": "I would like two fresh rolls and one apple pie, please.",
        "keywords": [
            {"en": "roll", "ru": "булочка"},
            {"en": "fresh", "ru": "свежий"},
            {"en": "apple pie", "ru": "яблочный пирог"},
        ],
        "questions": [
            _choice("How many rolls?", "two", ["one", "two", "three", "none"], "two fresh rolls"),
            _choice("What pie is ordered?", "apple pie", ["cherry pie", "apple pie", "meat pie", "no pie"], "one apple pie"),
            _dictation(
                "Напечатайте весь заказ.",
                "I would like two fresh rolls and one apple pie, please.",
                "I would like two fresh rolls and one apple pie, please.",
                accepted=[
                    "I would like two fresh rolls and one apple pie, please",
                    "I would like two fresh rolls and one apple pie please",
                ],
            ),
        ],
    },
    {
        "slug": "listening-a1-gym-hours",
        "title": "Часы работы зала",
        "description": "Информация на двери спортзала.",
        "kind": "listening",
        "level_code": "A1",
        "body": "The gym opens at six in the morning. It closes at ten at night.",
        "keywords": [
            {"en": "gym", "ru": "спортзал"},
            {"en": "morning", "ru": "утро"},
            {"en": "at night", "ru": "вечером / ночью (по контексту времени)"},
        ],
        "questions": [
            _choice("When does the gym open?", "at six in the morning", ["at eight", "at six in the morning", "at noon", "at ten"], "opens at six in the morning"),
            _choice("When does it close?", "at ten at night", ["at six", "at nine", "at ten at night", "never"], "closes at ten at night"),
            _dictation(
                "Напечатайте фразу про открытие.",
                "The gym opens at six in the morning.",
                "The gym opens at six in the morning.",
                accepted=["The gym opens at six in the morning", "the gym opens at six in the morning"],
            ),
        ],
    },
    {
        "slug": "listening-a1-phone-battery",
        "title": "Батарея телефона",
        "description": "Короткая просьба о зарядке.",
        "kind": "listening",
        "level_code": "A1",
        "body": "My phone battery is low. May I borrow your charger for ten minutes?",
        "keywords": [
            {"en": "battery", "ru": "батарея / заряд"},
            {"en": "borrow", "ru": "взять на время"},
            {"en": "charger", "ru": "зарядка"},
        ],
        "questions": [
            _choice("What is the problem?", "low battery", ["broken screen", "low battery", "no SIM", "lost phone"], "battery is low"),
            _choice("For how long is the charger needed?", "ten minutes", ["one hour", "ten minutes", "all day", "a second"], "for ten minutes"),
            _dictation(
                "Напечатайте просьбу.",
                "May I borrow your charger for ten minutes?",
                "May I borrow your charger for ten minutes?",
                accepted=["May I borrow your charger for ten minutes", "may I borrow your charger for ten minutes?"],
            ),
        ],
    },
    {
        "slug": "listening-a2-laundry-note",
        "title": "Записка про стирку",
        "description": "Сообщение соседу по квартире.",
        "kind": "listening",
        "level_code": "A2",
        "body": "Please move your clothes from the machine when it beeps. I need to start a new wash at seven.",
        "keywords": [
            {"en": "clothes", "ru": "одежда"},
            {"en": "machine", "ru": "машина (стиральная)"},
            {"en": "beep", "ru": "пищать / сигнал"},
            {"en": "wash", "ru": "стирка"},
        ],
        "questions": [
            _choice("When should clothes be moved?", "when the machine beeps", ["tomorrow", "when the machine beeps", "never", "at noon only"], "when it beeps"),
            _choice("What time is the new wash?", "at seven", ["at five", "at seven", "at nine", "midnight"], "at seven"),
            _dictation(
                "Напечатайте второе предложение.",
                "I need to start a new wash at seven.",
                "I need to start a new wash at seven.",
                accepted=["I need to start a new wash at seven", "i need to start a new wash at seven"],
            ),
        ],
    },
    {
        "slug": "listening-a2-parcel-pickup",
        "title": "Получение посылки",
        "description": "СМС от пункта выдачи.",
        "kind": "listening",
        "level_code": "A2",
        "body": "Your parcel is ready at locker B fourteen. Bring your code and ID card.",
        "keywords": [
            {"en": "parcel", "ru": "посылка"},
            {"en": "locker", "ru": "ячейка"},
            {"en": "code", "ru": "код"},
            {"en": "ID card", "ru": "удостоверение личности"},
        ],
        "questions": [
            _choice("Which locker?", "B fourteen", ["A one", "B fourteen", "C twenty", "desk only"], "locker B fourteen"),
            _choice("What should you bring?", "code and ID card", ["cash only", "code and ID card", "food", "a friend"], "code and ID card"),
            _dictation(
                "Напечатайте, где посылка.",
                "Your parcel is ready at locker B fourteen.",
                "Your parcel is ready at locker B fourteen.",
                accepted=["Your parcel is ready at locker B fourteen", "your parcel is ready at locker B fourteen"],
            ),
        ],
    },
    {
        "slug": "listening-a2-class-cancel",
        "title": "Отмена занятия",
        "description": "Сообщение от преподавателя.",
        "kind": "listening",
        "level_code": "A2",
        "body": "Today's evening class is cancelled because the teacher is ill. We will catch up next Monday at the same time.",
        "keywords": [
            {"en": "cancelled", "ru": "отменён"},
            {"en": "ill", "ru": "болен / больна"},
            {"en": "catch up", "ru": "нагнать / провести взамен"},
        ],
        "questions": [
            _choice("Why is the class cancelled?", "the teacher is ill", ["a holiday", "the teacher is ill", "no room", "exam week"], "teacher is ill"),
            _choice("When is the catch-up?", "next Monday at the same time", ["tonight", "next Monday at the same time", "next year", "Saturday morning"], "next Monday at the same time"),
            _dictation(
                "Напечатайте фразу про замену.",
                "We will catch up next Monday at the same time.",
                "We will catch up next Monday at the same time.",
                accepted=["We will catch up next Monday at the same time", "we will catch up next Monday at the same time"],
            ),
        ],
    },
    {
        "slug": "listening-b1-flight-gate",
        "title": "Выход на рейс",
        "description": "Объявление в аэропорту.",
        "kind": "listening",
        "level_code": "B1",
        "body": (
            "Passengers for flight four one nine to Berlin, please proceed to gate twenty-two. "
            "Boarding begins in fifteen minutes."
        ),
        "keywords": [
            {"en": "passenger", "ru": "пассажир"},
            {"en": "gate", "ru": "выход (на посадку)"},
            {"en": "boarding", "ru": "посадка (в самолёт)"},
            {"en": "proceed", "ru": "направляться / пройти"},
        ],
        "questions": [
            _choice("What is the destination?", "Berlin", ["Paris", "Berlin", "Rome", "Oslo"], "to Berlin"),
            _choice("Which gate?", "twenty-two", ["twelve", "twenty-two", "two", "thirty"], "gate twenty-two"),
            _dictation(
                "Напечатайте фразу про начало посадки.",
                "Boarding begins in fifteen minutes.",
                "Boarding begins in fifteen minutes.",
                accepted=["Boarding begins in fifteen minutes", "boarding begins in fifteen minutes"],
            ),
        ],
    },
    {
        "slug": "listening-b1-password-reset",
        "title": "Сброс пароля",
        "description": "Автоответ системы безопасности.",
        "kind": "listening",
        "level_code": "B1",
        "body": (
            "We received a request to reset your password. "
            "If this was you, tap the link in your email within one hour. "
            "If not, ignore this message and keep your current password."
        ),
        "keywords": [
            {"en": "reset", "ru": "сбросить / сброс"},
            {"en": "tap", "ru": "нажать"},
            {"en": "ignore", "ru": "игнорировать"},
            {"en": "current", "ru": "текущий"},
        ],
        "questions": [
            _choice("What was requested?", "a password reset", ["a new phone", "a password reset", "a refund", "a ticket"], "reset your password"),
            _choice("How long is the link valid?", "one hour", ["one minute", "one hour", "one week", "forever"], "within one hour"),
            _dictation(
                "Напечатайте совет, если запрос не ваш.",
                "If not, ignore this message and keep your current password.",
                "If not, ignore this message and keep your current password.",
                accepted=[
                    "If not, ignore this message and keep your current password",
                    "if not, ignore this message and keep your current password",
                ],
            ),
        ],
    },
    {
        "slug": "listening-b1-recycling-tip",
        "title": "Совет по сортировке",
        "description": "Короткий ролик ЖКХ.",
        "kind": "listening",
        "level_code": "B1",
        "body": (
            "Rinse plastic containers before recycling. "
            "Flatten cardboard boxes to save space. "
            "Please do not put batteries in the general bin."
        ),
        "keywords": [
            {"en": "rinse", "ru": "ополаскивать"},
            {"en": "flatten", "ru": "сплющивать / складывать плоско"},
            {"en": "cardboard", "ru": "картон"},
            {"en": "battery", "ru": "батарейка"},
        ],
        "questions": [
            _choice("What should you do with plastic containers?", "rinse them", ["burn them", "rinse them", "paint them", "hide them"], "Rinse plastic containers"),
            _choice("Where should batteries not go?", "in the general bin", ["to a shop", "in the general bin", "in cardboard", "outside only"], "do not put batteries in the general bin"),
            _dictation(
                "Напечатайте совет про коробки.",
                "Flatten cardboard boxes to save space.",
                "Flatten cardboard boxes to save space.",
                accepted=["Flatten cardboard boxes to save space", "flatten cardboard boxes to save space"],
            ),
        ],
    },
    {
        "slug": "listening-b2-standup-blocker",
        "title": "Блокер на стендапе",
        "description": "Короткий статус на созвоне.",
        "kind": "listening",
        "level_code": "B2",
        "body": (
            "Yesterday I finished the login tests. "
            "Today I'm stuck waiting for API access from the security team. "
            "If anyone has a spare sandbox key, please message me after the call."
        ),
        "keywords": [
            {"en": "stuck", "ru": "застрять / упереться"},
            {"en": "API access", "ru": "доступ к API"},
            {"en": "sandbox", "ru": "песочница / тестовая среда"},
            {"en": "spare", "ru": "запасной / лишний"},
        ],
        "questions": [
            _choice("What was finished yesterday?", "login tests", ["the whole product", "login tests", "hiring", "a picnic"], "finished the login tests"),
            _choice("What is the blocker?", "waiting for API access", ["no laptop", "waiting for API access", "too many meetings", "vacation"], "waiting for API access"),
            _dictation(
                "Напечатайте просьбу в конце.",
                "If anyone has a spare sandbox key, please message me after the call.",
                "If anyone has a spare sandbox key, please message me after the call.",
                accepted=[
                    "If anyone has a spare sandbox key, please message me after the call",
                    "if anyone has a spare sandbox key, please message me after the call",
                ],
            ),
        ],
    },
    {
        "slug": "listening-b2-rent-notice",
        "title": "Уведомление об аренде",
        "description": "Письмо от управляющей компании.",
        "kind": "listening",
        "level_code": "B2",
        "body": (
            "From next month the rent will rise by three percent. "
            "The increase covers higher heating costs. "
            "Contact the office before Friday if you need a payment plan."
        ),
        "keywords": [
            {"en": "rise", "ru": "повышаться"},
            {"en": "increase", "ru": "повышение / увеличение"},
            {"en": "cover", "ru": "покрывать (расходы)"},
            {"en": "payment plan", "ru": "план рассрочки / график платежей"},
        ],
        "questions": [
            _choice("By how much will rent rise?", "three percent", ["thirty percent", "three percent", "free", "double"], "rise by three percent"),
            _choice("What does the increase cover?", "higher heating costs", ["new furniture", "higher heating costs", "a party", "parking fines"], "higher heating costs"),
            _dictation(
                "Напечатайте срок для связи с офисом.",
                "Contact the office before Friday if you need a payment plan.",
                "Contact the office before Friday if you need a payment plan.",
                accepted=[
                    "Contact the office before Friday if you need a payment plan",
                    "contact the office before Friday if you need a payment plan",
                ],
            ),
        ],
    },
    {
        "slug": "listening-b2p-workshop-brief",
        "title": "Бриф воркшопа",
        "description": "Вступительное аудио для участников.",
        "kind": "listening",
        "level_code": "B2+",
        "body": (
            "Welcome to today's writing workshop. "
            "Please silence your phones and join the shared document with your real first name. "
            "We will draft for twenty minutes, then swap feedback in pairs."
        ),
        "keywords": [
            {"en": "workshop", "ru": "воркшоп / мастер-класс"},
            {"en": "silence", "ru": "выключать звук / соблюдать тишину"},
            {"en": "draft", "ru": "набрасывать черновик"},
            {"en": "swap feedback", "ru": "обменяться обратной связью"},
        ],
        "questions": [
            _choice("What should people use in the document?", "their real first name", ["a nickname only", "their real first name", "numbers", "silence"], "with your real first name"),
            _choice("How long is the drafting block?", "twenty minutes", ["two minutes", "twenty minutes", "two hours", "all day"], "draft for twenty minutes"),
            _choice("What happens after drafting?", "feedback in pairs", ["a test", "feedback in pairs", "lunch only", "going home"], "swap feedback in pairs"),
            _dictation(
                "Напечатайте просьбу про телефоны.",
                "Please silence your phones and join the shared document with your real first name.",
                "Please silence your phones and join the shared document with your real first name.",
                accepted=[
                    "Please silence your phones and join the shared document with your real first name",
                    "please silence your phones and join the shared document with your real first name",
                ],
            ),
        ],
    },
]


# --- Mini-dialogues (~22) ---------------------------------------------------

DIALOGUE_ITEMS: list[dict] = [
    {
        "slug": "dialogue-a1-coffee-order",
        "title": "Заказ кофе",
        "description": "В кафе у стойки.",
        "kind": "dialogue",
        "level_code": "A1",
        "body": "Café counter",
        "lines": [
            {"speaker": "Clerk", "text": "Hi! What would you like?", "ru": "Здравствуйте! Что будете?"},
            {"speaker": "Customer", "text": "A large coffee, please.", "ru": "Большой кофе, пожалуйста."},
            {"speaker": "Clerk", "text": "To stay or to go?", "ru": "Здесь или с собой?"},
            {"speaker": "Customer", "text": "To go, thanks.", "ru": "С собой, спасибо."},
        ],
        "keywords": [
            {"en": "large", "ru": "большой"},
            {"en": "to go", "ru": "с собой"},
            {"en": "to stay", "ru": "здесь (в заведении)"},
        ],
        "questions": [
            _choice("What size coffee does the customer want?", "large", ["small", "large", "medium", "none"], "A large coffee"),
            _gap("Customer: A ___ coffee, please.", "large", explanation="Размер напитка."),
            _gap("Customer: To ___, thanks.", "go", accepted=["go", "to go"], explanation="С собой = to go."),
        ],
    },
    {
        "slug": "dialogue-a1-asking-time",
        "title": "Который час?",
        "description": "На улице у прохожего.",
        "kind": "dialogue",
        "level_code": "A1",
        "body": "Street",
        "lines": [
            {"speaker": "A", "text": "Excuse me, what time is it?", "ru": "Извините, который час?"},
            {"speaker": "B", "text": "It's half past three.", "ru": "Половина четвёртого."},
            {"speaker": "A", "text": "Thank you!", "ru": "Спасибо!"},
            {"speaker": "B", "text": "You're welcome.", "ru": "Пожалуйста."},
        ],
        "keywords": [
            {"en": "excuse me", "ru": "извините (привлечь внимание)"},
            {"en": "half past", "ru": "половина (часа)"},
            {"en": "you're welcome", "ru": "пожалуйста (в ответ на спасибо)"},
        ],
        "questions": [
            _choice("What time is it?", "half past three", ["two o'clock", "half past three", "noon", "midnight"], "half past three"),
            _gap("A: Excuse me, what ___ is it?", "time"),
            _gap("B: It's ___ past three.", "half"),
        ],
    },
    {
        "slug": "dialogue-a1-bus-stop",
        "title": "На остановке",
        "description": "Какой автобус нужен.",
        "kind": "dialogue",
        "level_code": "A1",
        "body": "Bus stop",
        "lines": [
            {"speaker": "Tourist", "text": "Does this bus go to the museum?", "ru": "Этот автобус идёт к музею?"},
            {"speaker": "Local", "text": "No, you need bus seven.", "ru": "Нет, вам нужен седьмой."},
            {"speaker": "Tourist", "text": "Where can I catch it?", "ru": "Где его поймать?"},
            {"speaker": "Local", "text": "At the next stop, two minutes from here.", "ru": "На следующей остановке, в двух минутах."},
        ],
        "keywords": [
            {"en": "catch a bus", "ru": "сесть на автобус"},
            {"en": "next stop", "ru": "следующая остановка"},
            {"en": "need", "ru": "нуждаться / нужен"},
        ],
        "questions": [
            _choice("Which bus goes to the museum?", "bus seven", ["this bus", "bus seven", "bus one", "a taxi"], "bus seven"),
            _gap("Local: No, you need bus ___.", "seven", accepted=["seven", "7"]),
            _gap("Local: At the ___ stop, two minutes from here.", "next"),
        ],
    },
    {
        "slug": "dialogue-a2-doctor-appointment",
        "title": "Запись к врачу",
        "description": "Звонок в клинику.",
        "kind": "dialogue",
        "level_code": "A2",
        "body": "Phone call",
        "lines": [
            {"speaker": "Reception", "text": "Good morning, City Clinic.", "ru": "Доброе утро, городская клиника."},
            {"speaker": "Patient", "text": "I'd like to book an appointment with Dr. Fox.", "ru": "Хочу записаться к доктору Фоксу."},
            {"speaker": "Reception", "text": "We have a slot on Tuesday at eleven.", "ru": "Есть окно во вторник в 11."},
            {"speaker": "Patient", "text": "Perfect. My name is Elena Volkova.", "ru": "Отлично. Меня зовут Елена Волкова."},
        ],
        "keywords": [
            {"en": "book an appointment", "ru": "записаться на приём"},
            {"en": "slot", "ru": "свободное время / слот"},
            {"en": "clinic", "ru": "клиника"},
        ],
        "questions": [
            _choice("When is the available slot?", "Tuesday at eleven", ["Monday at ten", "Tuesday at eleven", "Friday evening", "today"], "Tuesday at eleven"),
            _gap("Patient: I'd like to ___ an appointment with Dr. Fox.", "book"),
            _gap("Reception: We have a ___ on Tuesday at eleven.", "slot"),
        ],
    },
    {
        "slug": "dialogue-a2-returning-item",
        "title": "Возврат покупки",
        "description": "В магазине одежды.",
        "kind": "dialogue",
        "level_code": "A2",
        "body": "Clothes shop",
        "lines": [
            {"speaker": "Customer", "text": "I'd like to return this sweater. It's too small.", "ru": "Хочу вернуть свитер. Он мал."},
            {"speaker": "Staff", "text": "Do you have the receipt?", "ru": "Чек есть?"},
            {"speaker": "Customer", "text": "Yes, here it is.", "ru": "Да, вот."},
            {"speaker": "Staff", "text": "Would you like a refund or an exchange?", "ru": "Вернуть деньги или обменять?"},
            {"speaker": "Customer", "text": "An exchange for a larger size, please.", "ru": "Обмен на больший размер, пожалуйста."},
        ],
        "keywords": [
            {"en": "return", "ru": "возвращать (товар)"},
            {"en": "receipt", "ru": "чек"},
            {"en": "refund", "ru": "возврат денег"},
            {"en": "exchange", "ru": "обмен"},
        ],
        "questions": [
            _choice("Why is the sweater returned?", "it is too small", ["wrong colour", "it is too small", "torn", "too expensive"], "too small"),
            _gap("Staff: Do you have the ___?", "receipt"),
            _gap("Customer: An ___ for a larger size, please.", "exchange"),
        ],
    },
    {
        "slug": "dialogue-a2-group-project",
        "title": "Групповой проект",
        "description": "Студенты делят задачи.",
        "kind": "dialogue",
        "level_code": "A2",
        "body": "Campus",
        "lines": [
            {"speaker": "Sam", "text": "Can you prepare the slides?", "ru": "Можешь сделать слайды?"},
            {"speaker": "Nina", "text": "Sure. Who will write the short report?", "ru": "Конечно. Кто напишет короткий отчёт?"},
            {"speaker": "Sam", "text": "I will. Let's meet on Thursday to practise.", "ru": "Я. Встретимся в четверг порепетировать."},
            {"speaker": "Nina", "text": "Good idea. I'll send my draft by Wednesday.", "ru": "Хорошая идея. Пришлю черновик к среде."},
        ],
        "keywords": [
            {"en": "slides", "ru": "слайды"},
            {"en": "report", "ru": "отчёт"},
            {"en": "draft", "ru": "черновик"},
        ],
        "questions": [
            _choice("Who prepares the slides?", "Nina", ["Sam", "Nina", "the teacher", "nobody"], "Can you prepare… Sure"),
            _gap("Sam: Can you prepare the ___?", "slides"),
            _gap("Nina: I'll send my ___ by Wednesday.", "draft"),
        ],
    },
    {
        "slug": "dialogue-b1-job-interview",
        "title": "Собеседование",
        "description": "Короткий фрагмент интервью.",
        "kind": "dialogue",
        "level_code": "B1",
        "body": "Office",
        "lines": [
            {"speaker": "Interviewer", "text": "Tell me about a problem you solved at work.", "ru": "Расскажите о проблеме, которую вы решили на работе."},
            {
                "speaker": "Candidate",
                "text": "Our delivery was late, so I contacted the supplier and updated the clients the same day.",
                "ru": "Доставка опоздала, я связался с поставщиком и в тот же день сообщил клиентам.",
            },
            {"speaker": "Interviewer", "text": "What was the result?", "ru": "Какой был результат?"},
            {
                "speaker": "Candidate",
                "text": "We kept the clients and improved our checklist for future delays.",
                "ru": "Клиентов сохранили и улучшили чек-лист на будущее.",
            },
        ],
        "keywords": [
            {"en": "supplier", "ru": "поставщик"},
            {"en": "update", "ru": "информировать / обновлять"},
            {"en": "checklist", "ru": "контрольный список"},
        ],
        "questions": [
            _choice("What went wrong initially?", "a late delivery", ["lost money", "a late delivery", "a broken laptop", "no clients"], "delivery was late"),
            _gap("Candidate: I contacted the ___ and updated the clients.", "supplier"),
            _gap("Candidate: We kept the clients and improved our ___.", "checklist"),
        ],
    },
    {
        "slug": "dialogue-b1-flatmate-chores",
        "title": "Домашние обязанности",
        "description": "Соседи по квартире договариваются.",
        "kind": "dialogue",
        "level_code": "B1",
        "body": "Shared flat",
        "lines": [
            {"speaker": "Alex", "text": "The kitchen is a mess again. Can we set a cleaning schedule?", "ru": "Кухня снова в беспорядке. Составим график уборки?"},
            {"speaker": "Jordan", "text": "Sure. I'll wash the dishes on weekdays if you take the weekend floors.", "ru": "Ок. Я мою посуду в будни, ты — полы на выходных."},
            {"speaker": "Alex", "text": "Deal. Let's also buy more bin bags tomorrow.", "ru": "Договорились. Завтра купим ещё мешки для мусора."},
            {"speaker": "Jordan", "text": "I'll add it to the shared list.", "ru": "Добавлю в общий список."},
        ],
        "keywords": [
            {"en": "mess", "ru": "беспорядок"},
            {"en": "schedule", "ru": "расписание / график"},
            {"en": "bin bag", "ru": "мешок для мусора"},
        ],
        "questions": [
            _choice("What does Alex suggest?", "a cleaning schedule", ["moving out", "a cleaning schedule", "hiring a cook", "silence"], "cleaning schedule"),
            _gap("Alex: Can we set a cleaning ___?", "schedule"),
            _gap("Alex: Let's also buy more ___ bags tomorrow.", "bin"),
        ],
    },
    {
        "slug": "dialogue-b2-customer-complaint",
        "title": "Жалоба клиента",
        "description": "Служба поддержки по телефону.",
        "kind": "dialogue",
        "level_code": "B2",
        "body": "Support call",
        "lines": [
            {"speaker": "Client", "text": "I ordered a lamp last week, but the package arrived damaged.", "ru": "Заказывал лампу на прошлой неделе, посылка пришла повреждённой."},
            {"speaker": "Agent", "text": "I'm sorry about that. Could you send a photo of the damage?", "ru": "Извините. Можете прислать фото повреждения?"},
            {"speaker": "Client", "text": "Already done. I attached it to ticket 4821.", "ru": "Уже. Прикрепил к тикету 4821."},
            {
                "speaker": "Agent",
                "text": "Thank you. We'll ship a replacement tomorrow and arrange a pickup for the broken one.",
                "ru": "Спасибо. Завтра отправим замену и организуем забор сломанной.",
            },
        ],
        "keywords": [
            {"en": "damaged", "ru": "повреждённый"},
            {"en": "replacement", "ru": "замена"},
            {"en": "arrange a pickup", "ru": "организовать забор / вывоз"},
        ],
        "questions": [
            _choice("What is wrong with the order?", "the package arrived damaged", ["wrong colour", "the package arrived damaged", "never shipped", "late invoice"], "arrived damaged"),
            _gap("Agent: Could you send a photo of the ___?", "damage"),
            _gap("Agent: We'll ship a ___ tomorrow.", "replacement"),
        ],
    },
    {
        "slug": "dialogue-b2-travel-plan",
        "title": "План поездки",
        "description": "Друзья выбирают маршрут.",
        "kind": "dialogue",
        "level_code": "B2",
        "body": "Café planning",
        "lines": [
            {"speaker": "Mira", "text": "If we take the early train, we'll have a full day in the old town.", "ru": "Если сядем на ранний поезд, будет целый день в старом городе."},
            {"speaker": "Leo", "text": "True, but the evening tickets are cheaper. We could explore less and save money.", "ru": "Да, но вечерние билеты дешевле. Можно меньше гулять и сэкономить."},
            {"speaker": "Mira", "text": "I'd rather pay a bit more and avoid rushing.", "ru": "Лучше чуть доплатить и не торопиться."},
            {"speaker": "Leo", "text": "Fair enough. Let's book the morning seats tonight.", "ru": "Справедливо. Забронируем утренние места сегодня вечером."},
        ],
        "keywords": [
            {"en": "early train", "ru": "ранний поезд"},
            {"en": "explore", "ru": "осматривать / исследовать"},
            {"en": "rush", "ru": "спешить"},
            {"en": "fair enough", "ru": "справедливо / ладно"},
        ],
        "questions": [
            _choice("What does Mira prefer?", "pay more and avoid rushing", ["cheapest tickets only", "pay more and avoid rushing", "cancel the trip", "travel at night"], "pay a bit more and avoid rushing"),
            _gap("Mira: If we take the ___ train, we'll have a full day.", "early"),
            _gap("Leo: Let's book the morning ___ tonight.", "seats"),
        ],
    },
    {
        "slug": "dialogue-a1-hotel-checkin",
        "title": "Заезд в отель",
        "description": "У стойки регистрации.",
        "kind": "dialogue",
        "level_code": "A1",
        "body": "Hotel lobby",
        "lines": [
            {"speaker": "Guest", "text": "Hello. I have a reservation under Kim.", "ru": "Здравствуйте. Бронь на имя Ким."},
            {"speaker": "Reception", "text": "One moment. A single room for two nights?", "ru": "Минутку. Одноместный на две ночи?"},
            {"speaker": "Guest", "text": "Yes, that's right.", "ru": "Да, всё верно."},
            {"speaker": "Reception", "text": "Your key is for room twelve. Breakfast starts at seven.", "ru": "Ключ от комнаты двенадцать. Завтрак с семи."},
        ],
        "keywords": [
            {"en": "reservation", "ru": "бронь / резервация"},
            {"en": "single room", "ru": "одноместный номер"},
            {"en": "key", "ru": "ключ"},
        ],
        "questions": [
            _choice("How many nights?", "two", ["one", "two", "three", "seven"], "two nights"),
            _gap("Guest: I have a ___ under Kim.", "reservation"),
            _gap("Reception: Your key is for room ___.", "twelve", accepted=["twelve", "12"]),
        ],
    },
    {
        "slug": "dialogue-a1-buying-stamps",
        "title": "Марки на почте",
        "description": "Отправка открытки.",
        "kind": "dialogue",
        "level_code": "A1",
        "body": "Post office",
        "lines": [
            {"speaker": "Customer", "text": "I need stamps for a postcard to Italy.", "ru": "Нужны марки на открытку в Италию."},
            {"speaker": "Clerk", "text": "International stamps are on the left shelf.", "ru": "Международные — на левой полке."},
            {"speaker": "Customer", "text": "How much is one stamp?", "ru": "Сколько стоит одна марка?"},
            {"speaker": "Clerk", "text": "Two euros each.", "ru": "По два евро."},
        ],
        "keywords": [
            {"en": "stamp", "ru": "марка"},
            {"en": "postcard", "ru": "открытка (почтовая)"},
            {"en": "shelf", "ru": "полка"},
        ],
        "questions": [
            _choice("Where is the postcard going?", "to Italy", ["to Spain", "to Italy", "local only", "nowhere"], "to Italy"),
            _gap("Customer: I need ___ for a postcard to Italy.", "stamps"),
            _gap("Clerk: ___ euros each.", "Two", accepted=["Two", "two", "2"]),
        ],
    },
    {
        "slug": "dialogue-a1-finding-toilet",
        "title": "Где туалет?",
        "description": "В торговом центре.",
        "kind": "dialogue",
        "level_code": "A1",
        "body": "Shopping centre",
        "lines": [
            {"speaker": "Visitor", "text": "Excuse me, where is the toilet?", "ru": "Извините, где туалет?"},
            {"speaker": "Guard", "text": "Go straight and turn left after the café.", "ru": "Прямо и налево после кафе."},
            {"speaker": "Visitor", "text": "Is it free?", "ru": "Он бесплатный?"},
            {"speaker": "Guard", "text": "Yes. The code is on the receipt if you buy something.", "ru": "Да. Код на чеке, если что-то купите."},
        ],
        "keywords": [
            {"en": "toilet", "ru": "туалет"},
            {"en": "straight", "ru": "прямо"},
            {"en": "turn left", "ru": "повернуть налево"},
        ],
        "questions": [
            _choice("Where should the visitor turn?", "left after the café", ["right at the door", "left after the café", "upstairs only", "outside"], "turn left after the café"),
            _gap("Visitor: Excuse me, where is the ___?", "toilet"),
            _gap("Guard: Go ___ and turn left after the café.", "straight"),
        ],
    },
    {
        "slug": "dialogue-a2-allergy-order",
        "title": "Аллергия в ресторане",
        "description": "Заказ с уточнением ингредиентов.",
        "kind": "dialogue",
        "level_code": "A2",
        "body": "Restaurant",
        "lines": [
            {"speaker": "Guest", "text": "Does this soup contain nuts?", "ru": "В этом супе есть орехи?"},
            {"speaker": "Waiter", "text": "No nuts, but it has cream. Are you allergic to dairy?", "ru": "Орехов нет, но есть сливки. У вас аллергия на молочное?"},
            {"speaker": "Guest", "text": "Yes. Could I have the salad without cheese instead?", "ru": "Да. Можно салат без сыра?"},
            {"speaker": "Waiter", "text": "Of course. I'll note it for the kitchen.", "ru": "Конечно. Отмечу для кухни."},
        ],
        "keywords": [
            {"en": "contain", "ru": "содержать"},
            {"en": "allergic", "ru": "имеющий аллергию"},
            {"en": "dairy", "ru": "молочные продукты"},
            {"en": "note (v.)", "ru": "отметить / записать"},
        ],
        "questions": [
            _choice("What does the guest choose instead?", "salad without cheese", ["soup with cream", "salad without cheese", "nuts", "nothing"], "salad without cheese"),
            _gap("Guest: Does this soup ___ nuts?", "contain"),
            _gap("Waiter: Are you allergic to ___?", "dairy"),
        ],
    },
    {
        "slug": "dialogue-a2-library-fine",
        "title": "Штраф в библиотеке",
        "description": "Просроченная книга.",
        "kind": "dialogue",
        "level_code": "A2",
        "body": "Library desk",
        "lines": [
            {"speaker": "Librarian", "text": "This book is five days overdue.", "ru": "Книга просрочена на пять дней."},
            {"speaker": "Student", "text": "Oh no. How much is the fine?", "ru": "Ой. Какой штраф?"},
            {"speaker": "Librarian", "text": "Two pounds in total. You can pay by card.", "ru": "Всего два фунта. Можно картой."},
            {"speaker": "Student", "text": "I'll pay now and renew it for another week.", "ru": "Заплачу сейчас и продлю ещё на неделю."},
            {"speaker": "Librarian", "text": "Done. Please return it on time next time.", "ru": "Готово. В следующий раз верните вовремя."},
        ],
        "keywords": [
            {"en": "overdue", "ru": "просроченный"},
            {"en": "fine", "ru": "штраф"},
            {"en": "renew", "ru": "продлить"},
        ],
        "questions": [
            _choice("How many days overdue?", "five", ["two", "five", "seven", "one"], "five days overdue"),
            _gap("Librarian: This book is five days ___.", "overdue"),
            _gap("Student: I'll pay now and ___ it for another week.", "renew"),
        ],
    },
    {
        "slug": "dialogue-a2-gym-membership",
        "title": "Абонемент в зал",
        "description": "Вопросы о тарифе.",
        "kind": "dialogue",
        "level_code": "A2",
        "body": "Gym reception",
        "lines": [
            {"speaker": "Client", "text": "How much is a monthly membership?", "ru": "Сколько стоит месячный абонемент?"},
            {"speaker": "Staff", "text": "Thirty-five if you pay monthly, or three hundred for a year.", "ru": "Тридцать пять помесячно или триста за год."},
            {"speaker": "Client", "text": "Does it include group classes?", "ru": "Групповые занятия включены?"},
            {"speaker": "Staff", "text": "Yes, except the weekend yoga sessions.", "ru": "Да, кроме йоги по выходным."},
        ],
        "keywords": [
            {"en": "membership", "ru": "абонемент / членство"},
            {"en": "include", "ru": "включать"},
            {"en": "except", "ru": "кроме"},
        ],
        "questions": [
            _choice("What is not included?", "weekend yoga", ["all classes", "weekend yoga", "the locker", "water"], "except the weekend yoga"),
            _gap("Client: How much is a monthly ___?", "membership"),
            _gap("Staff: Yes, ___ the weekend yoga sessions.", "except"),
        ],
    },
    {
        "slug": "dialogue-b1-deadline-push",
        "title": "Перенос дедлайна",
        "description": "Коллеги согласовывают срок.",
        "kind": "dialogue",
        "level_code": "B1",
        "body": "Office chat",
        "lines": [
            {"speaker": "Priya", "text": "Can we move the report deadline to Wednesday?", "ru": "Можем сдвинуть дедлайн отчёта на среду?"},
            {"speaker": "Marcus", "text": "What's blocking you?", "ru": "Что мешает?"},
            {
                "speaker": "Priya",
                "text": "The sales numbers arrived late, and I still need to check two charts.",
                "ru": "Цифры продаж пришли поздно, ещё нужно проверить два графика.",
            },
            {"speaker": "Marcus", "text": "Wednesday works if you send a short status update today.", "ru": "Среда ок, если сегодня короткий статус."},
            {"speaker": "Priya", "text": "Deal. I'll post it in the channel by five.", "ru": "Договорились. Выложу в канал до пяти."},
        ],
        "keywords": [
            {"en": "deadline", "ru": "срок / дедлайн"},
            {"en": "block", "ru": "блокировать / мешать"},
            {"en": "status update", "ru": "статус / обновление"},
        ],
        "questions": [
            _choice("What does Marcus ask for today?", "a short status update", ["a new laptop", "a short status update", "vacation", "charts only"], "short status update today"),
            _gap("Priya: Can we move the report ___ to Wednesday?", "deadline"),
            _gap("Marcus: Wednesday works if you send a short status ___ today.", "update"),
        ],
    },
    {
        "slug": "dialogue-b1-lost-tourist",
        "title": "Заблудившийся турист",
        "description": "Как дойти до вокзала.",
        "kind": "dialogue",
        "level_code": "B1",
        "body": "City street",
        "lines": [
            {"speaker": "Tourist", "text": "Sorry, is the train station far from here?", "ru": "Извините, вокзал далеко?"},
            {
                "speaker": "Local",
                "text": "About twelve minutes on foot. Cross the bridge, then follow the tram tracks.",
                "ru": "Минут двенадцать пешком. Перейдите мост и идите вдоль трамвайных путей.",
            },
            {"speaker": "Tourist", "text": "Should I take a tram instead?", "ru": "Может, лучше на трамвае?"},
            {
                "speaker": "Local",
                "text": "Only if it starts raining. Walking is usually faster at this hour.",
                "ru": "Только если начнётся дождь. В этот час пешком обычно быстрее.",
            },
        ],
        "keywords": [
            {"en": "on foot", "ru": "пешком"},
            {"en": "bridge", "ru": "мост"},
            {"en": "tram tracks", "ru": "трамвайные пути"},
        ],
        "questions": [
            _choice("How long on foot?", "about twelve minutes", ["one hour", "about twelve minutes", "two days", "thirty seconds"], "About twelve minutes"),
            _gap("Local: Cross the ___, then follow the tram tracks.", "bridge"),
            _gap("Local: Walking is usually ___ at this hour.", "faster"),
        ],
    },
    {
        "slug": "dialogue-b1-phone-plan",
        "title": "Тариф на телефон",
        "description": "В салоне связи.",
        "kind": "dialogue",
        "level_code": "B1",
        "body": "Mobile shop",
        "lines": [
            {"speaker": "Customer", "text": "I need more mobile data for travel next month.", "ru": "Нужно больше мобильного интернета для поездки."},
            {
                "speaker": "Advisor",
                "text": "We can add a roaming pack or switch you to a higher local plan.",
                "ru": "Можем добавить роуминг-пакет или перевести на больший местный тариф.",
            },
            {"speaker": "Customer", "text": "Which option is cheaper for two weeks abroad?", "ru": "Что дешевле на две недели за границей?"},
            {
                "speaker": "Advisor",
                "text": "The roaming pack. It pauses automatically when you return.",
                "ru": "Роуминг-пакет. Он сам останавливается по возвращении.",
            },
        ],
        "keywords": [
            {"en": "mobile data", "ru": "мобильный интернет"},
            {"en": "roaming", "ru": "роуминг"},
            {"en": "abroad", "ru": "за границей"},
            {"en": "pause", "ru": "ставить на паузу"},
        ],
        "questions": [
            _choice("What is cheaper for two weeks abroad?", "the roaming pack", ["a new phone", "the roaming pack", "no plan", "higher local only"], "The roaming pack"),
            _gap("Customer: I need more mobile ___ for travel next month.", "data"),
            _gap("Advisor: It ___ automatically when you return.", "pauses"),
        ],
    },
    {
        "slug": "dialogue-b2-salary-talk",
        "title": "Разговор о зарплате",
        "description": "Мягкий запрос на пересмотр.",
        "kind": "dialogue",
        "level_code": "B2",
        "body": "Manager meeting",
        "lines": [
            {
                "speaker": "Employee",
                "text": "I'd like to discuss adjusting my salary based on the new responsibilities.",
                "ru": "Хочу обсудить пересмотр зарплаты с учётом новых обязанностей.",
            },
            {"speaker": "Manager", "text": "I've noticed the extra load. What range are you aiming for?", "ru": "Вижу допнагрузку. На какой диапазон ориентируетесь?"},
            {
                "speaker": "Employee",
                "text": "Around eight percent, or a clear path to that within two quarters.",
                "ru": "Около восьми процентов или понятный путь к этому за два квартала.",
            },
            {
                "speaker": "Manager",
                "text": "Let me check the budget this week and book a follow-up on Friday.",
                "ru": "Проверю бюджет на этой неделе и назначу продолжение в пятницу.",
            },
        ],
        "keywords": [
            {"en": "adjust", "ru": "корректировать / пересматривать"},
            {"en": "responsibilities", "ru": "обязанности"},
            {"en": "range", "ru": "диапазон"},
            {"en": "follow-up", "ru": "повторная встреча / продолжение"},
        ],
        "questions": [
            _choice("What percent does the employee mention?", "around eight percent", ["fifty percent", "around eight percent", "zero", "twenty"], "Around eight percent"),
            _gap("Employee: I'd like to discuss adjusting my ___.", "salary"),
            _gap("Manager: … book a ___ on Friday.", "follow-up", accepted=["follow-up", "follow up"]),
        ],
    },
    {
        "slug": "dialogue-b2-landlord-repair",
        "title": "Ремонт у арендодателя",
        "description": "Жалоба на протекающий кран.",
        "kind": "dialogue",
        "level_code": "B2",
        "body": "Phone call",
        "lines": [
            {"speaker": "Tenant", "text": "The kitchen tap has been dripping for three days.", "ru": "Кухонный кран капает уже три дня."},
            {"speaker": "Landlord", "text": "Have you tried tightening it? Sometimes that helps.", "ru": "Пробовали подтянуть? Иногда помогает."},
            {
                "speaker": "Tenant",
                "text": "I did. There's also a small puddle under the sink now.",
                "ru": "Пробовал. Под раковиной уже маленькая лужа.",
            },
            {
                "speaker": "Landlord",
                "text": "Understood. I'll send a plumber tomorrow morning between nine and eleven.",
                "ru": "Понял. Завтра утром пришлю сантехника с девяти до одиннадцати.",
            },
            {"speaker": "Tenant", "text": "Great. I'll be home then.", "ru": "Отлично. Я буду дома."},
        ],
        "keywords": [
            {"en": "drip", "ru": "капать"},
            {"en": "tighten", "ru": "подтягивать / затягивать"},
            {"en": "puddle", "ru": "лужа"},
            {"en": "plumber", "ru": "сантехник"},
        ],
        "questions": [
            _choice("Who will come tomorrow?", "a plumber", ["a painter", "a plumber", "a chef", "nobody"], "send a plumber"),
            _gap("Tenant: The kitchen tap has been ___ for three days.", "dripping"),
            _gap("Landlord: I'll send a ___ tomorrow morning.", "plumber"),
        ],
    },
    {
        "slug": "dialogue-b2p-mentor-feedback",
        "title": "Обратная связь ментора",
        "description": "Разбор черновика презентации.",
        "kind": "dialogue",
        "level_code": "B2+",
        "body": "Mentoring call",
        "lines": [
            {
                "speaker": "Mentee",
                "text": "Could you look at my draft slides before Thursday's pitch?",
                "ru": "Можете глянуть черновик слайдов до четвергового питча?",
            },
            {
                "speaker": "Mentor",
                "text": "Sure. The story is clear, but the third slide buries the key number.",
                "ru": "Конечно. История ясная, но на третьем слайде ключевая цифра теряется.",
            },
            {
                "speaker": "Mentee",
                "text": "Should I move it to the opening or add a callout box?",
                "ru": "Перенести в начало или добавить выноску?",
            },
            {
                "speaker": "Mentor",
                "text": "Open with it, then keep one simple chart. Cut two decorative animations.",
                "ru": "Начните с неё, оставьте один простой график. Уберите две декоративные анимации.",
            },
            {"speaker": "Mentee", "text": "Got it. I'll send a revised version tonight.", "ru": "Понял. Пришлю правку сегодня вечером."},
        ],
        "keywords": [
            {"en": "pitch", "ru": "питч / короткая презентация"},
            {"en": "bury", "ru": "хоронить / прятать (смысл)"},
            {"en": "callout", "ru": "выноска / акцент"},
            {"en": "revised", "ru": "исправленный / переработанный"},
        ],
        "questions": [
            _choice("What problem is on the third slide?", "the key number is buried", ["wrong font forever", "the key number is buried", "no title", "too short"], "buries the key number"),
            _gap("Mentor: … but the third slide ___ the key number.", "buries"),
            _gap("Mentee: I'll send a ___ version tonight.", "revised"),
            _choice("What should be cut?", "two decorative animations", ["the whole deck", "two decorative animations", "the mentor", "Thursday"], "Cut two decorative animations"),
        ],
    },
]


SKILL_ITEMS: list[dict] = READING_ITEMS + LISTENING_ITEMS + DIALOGUE_ITEMS
