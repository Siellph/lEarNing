"""Enriched A1 grammar theory (Russian explanations, English examples)."""

from app.seed.helpers import ex, lesson, rule

A1_THEORY = {
    "to-be": lesson(
        "Глагол to be («быть, являться») — связка: он соединяет подлежащее с тем, кем или каким оно является, где находится и сколько ему лет. На A1 без to be почти нельзя собрать нормальное описание. В речи чаще звучат краткие формы: I'm, she's, they're.",
        [
            rule(
                "Формы в настоящем",
                "Три формы: I am; he/she/it is; you/we/they are. Краткие: I'm, he's, she's, it's, you're, we're, they're. Выбор формы зависит только от подлежащего, не от следующего слова.",
                [
                    ex("I am a student. / I'm a student.", "Я студент."),
                    ex("She is tired. / She's tired.", "Она устала."),
                    ex("They are at home.", "Они дома."),
                ],
            ),
            rule(
                "Отрицание",
                "Not ставится сразу после формы to be: am not, is not / isn't, are not / aren't. Отдельный don't/doesn't с to be не нужен и звучит как ошибка.",
                [
                    ex("I'm not hungry.", "Я не голоден."),
                    ex("It isn't cold today.", "Сегодня не холодно."),
                    ex("We aren't ready yet.", "Мы ещё не готовы."),
                ],
            ),
            rule(
                "Вопрос",
                "Форма to be выходит на первое место: Are you ready? Is he here? Вопросительное слово стоит ещё левее: Where is the station?",
                [
                    ex("Are they from Spain?", "Они из Испании?"),
                    ex("Where is the station?", "Где вокзал?"),
                    ex("Is this your bag?", "Это твоя сумка?"),
                ],
            ),
            rule(
                "Типичные смыслы",
                "Профессия и роль (She is a doctor), место (They are in the park), возраст (He is twenty), описание и настроение (It is cold / I am happy). Это не «действие», а состояние или характеристика.",
                [
                    ex("My brother is an engineer.", "Мой брат — инженер."),
                    ex("The shop is closed.", "Магазин закрыт."),
                ],
            ),
        ],
        compare=[
            {"left": "She is a teacher.", "right": "Does she teach maths?", "note": "To be описывает роль; действие с обычным глаголом строит вопрос через do/does."},
            {"left": "Are you ready?", "right": "Do you ready?", "note": "Со связкой to be никогда не ставят do/does."},
        ],
        watch_out=[
            "Не «Do you are?» и не «Does she is?» — только Are you? / Is she?",
            "После he/she/it только is, не are.",
            "I am, не I is и не I are.",
        ],
        remember="To be сам несёт лицо и число. Краткие формы нормальны в речи; do/does ему не нужны.",
    ),
    "articles-a1": lesson(
        "Артикль — служебное слово перед существительным. В русском его нет, поэтому выбор a/an, the или «нуля» нужно осознанно тренировать. Три опоры A1: впервые / любой → a/an; известный или единственный → the; общее понятие → без артикля.",
        [
            rule(
                "A / an — один из класса, впервые",
                "A/an называют один неопределённый экземпляр: I need a pen (любую). Выбор a или an зависит от звука, не от буквы: a book, a university (/j/), an apple, an hour (/aʊ/).",
                [
                    ex("I need a pen.", "Мне нужна ручка (любая)."),
                    ex("She is an engineer.", "Она инженер."),
                    ex("We waited an hour.", "Мы ждали час."),
                ],
            ),
            rule(
                "The — этот самый или единственный",
                "The ставят, когда собеседник уже понимает, о каком предмете речь, или предмет уникален в контексте: the sun, the door, the kitchen. После первого a car часто следует the car.",
                [
                    ex("Close the window, please.", "Закрой окно (то, которое мы оба видим)."),
                    ex("The moon is bright tonight.", "Луна сегодня яркая."),
                    ex("I bought a phone. The phone is black.", "Купил телефон. Телефон чёрный."),
                ],
            ),
            rule(
                "Нулевой артикль",
                "Без артикля: имена, большинство стран и городов; неисчисляемые в общем смысле (tea, music); множественное число «вообще» (dogs sleep a lot). Это не «забыли артикль», а отдельное решение.",
                [
                    ex("I like music.", "Я люблю музыку (как явление)."),
                    ex("Cats sleep a lot.", "Кошки много спят (вообще)."),
                    ex("Anna lives in Madrid.", "Анна живёт в Мадриде."),
                ],
            ),
            rule(
                "Профессии и еда — короткие ориентиры",
                "Перед профессией в роли «кто он» обычно a/an: She is a nurse. Перед едой и напитками в общем смысле — ноль: I like coffee. Конкретная порция на столе — the coffee.",
                [
                    ex("He is a pilot.", "Он пилот."),
                    ex("Pass me the salt.", "Передай соль (ту, что на столе)."),
                ],
            ),
        ],
        compare=[
            {"left": "I bought a car.", "right": "The car is blue.", "note": "Сначала любой экземпляр, затем уже известный."},
            {"left": "I love chocolate.", "right": "The chocolate on the table is melting.", "note": "Общее вещество vs конкретная плитка."},
        ],
        watch_out=[
            "Слушайте звук, не смотрите на букву: a university, an hour.",
            "Уникальные объекты часто с the: the Internet, the sky, the sun.",
            "Не ставьте a перед множественным: a books — ошибка.",
        ],
        remember="A/an = один из класса. The = этот самый. Ноль = общее имя, вещество или класс во множественном.",
    ),
    "nouns-plurals": lesson(
        "Существительное почти всегда имеет единственное и множественное число. База A1: регулярное +s/+es и короткий список особых форм (man—men, child—children). Без этого нельзя согласовать there is/are и this/these.",
        [
            rule(
                "Регулярное множественное",
                "Большинство слов: +s (book—books). После s, x, ch, sh и часто o — +es: boxes, watches, tomatoes. Y после согласной → ies: city—cities. Y после гласной просто +s: day—days.",
                [
                    ex("one bus — two buses", "один автобус — два автобуса"),
                    ex("a baby — babies", "малыш — малыши"),
                    ex("one day — two days", "один день — два дня"),
                ],
            ),
            rule(
                "Особые формы",
                "Их лучше выучить списком: man—men, woman—women, child—children, person—people, tooth—teeth, foot—feet, mouse—mice. Здесь правило +s не работает.",
                [
                    ex("There are three children in the garden.", "В саду трое детей."),
                    ex("People are waiting.", "Люди ждут."),
                    ex("My feet hurt.", "У меня болят ноги."),
                ],
            ),
            rule(
                "Одинаковая форма и «ложное» множественное",
                "Sheep, fish, deer часто не меняются. News выглядит как множественное, но согласуется как единственное: The news is good.",
                [
                    ex("Five sheep are in the field.", "В поле пять овец."),
                    ex("The news is good.", "Новости хорошие."),
                ],
            ),
        ],
        compare=[
            {"left": "one child — two children", "right": "one book — two books", "note": "Сначала проверьте особый список, иначе +s."},
        ],
        watch_out=[
            "Peoples — только «народы»; про людей говорят people.",
            "Childs и foots — ошибки: children, feet.",
            "This news are — ошибка: news + is.",
        ],
        remember="Сначала особый список, затем +s/+es. News — единственное по согласованию.",
    ),
    "pronouns-possessives": lesson(
        "Местоимения заменяют имена, чтобы не повторять их. Нужно различать роль в предложении: кто делает действие (I, she) и на кого оно направлено (me, her). Отдельно — принадлежность: my book vs This book is mine.",
        [
            rule(
                "Подлежащее и дополнение",
                "Подлежащее: I, you, he, she, it, we, they. Дополнение: me, you, him, her, it, us, them. После глагола и предлога — объектная форма: She likes him. Look at us.",
                [
                    ex("She likes him.", "Она любит его."),
                    ex("They called us.", "Они нам позвонили."),
                    ex("Can you help me?", "Можешь мне помочь?"),
                ],
            ),
            rule(
                "Притяжательные прилагательные",
                "My, your, his, her, its, our, their всегда стоят перед существительным и никогда не бывают «голыми»: my bag, their house. Форма its — без апострофа.",
                [
                    ex("This is her laptop.", "Это её ноутбук."),
                    ex("Our teacher is kind.", "Наш учитель добрый."),
                    ex("The dog wagged its tail.", "Собака вильнула хвостом."),
                ],
            ),
            rule(
                "Абсолютные формы",
                "Mine, yours, his, hers, ours, theirs заменяют всю группу «чей + существительное»: This seat is mine (= my seat). Its в этой роли почти не встречается.",
                [
                    ex("This seat is mine.", "Это место моё."),
                    ex("Is that car yours?", "Эта машина твоя?"),
                    ex("Their flat is bigger than ours.", "Их квартира больше нашей."),
                ],
            ),
        ],
        compare=[
            {"left": "This is my book.", "right": "This book is mine.", "note": "Перед словом — my; вместо группы — mine."},
            {"left": "its tail", "right": "it's raining", "note": "its = принадлежность; it's = it is / it has."},
        ],
        watch_out=[
            "Me book и I book — ошибки; нужно my book.",
            "This bag is my — неполно; без существительного говорите mine.",
            "Its ≠ it's.",
        ],
        remember="Роль: I/me. Перед словом: my/her. Вместо группы: mine/hers.",
    ),
    "demonstratives": lesson(
        "This, that, these, those указывают на предмет и одновременно показывают число и «дистанцию» (рядом / дальше, или «этот упомянутый»). Они согласуются с существительным и с глаголом to be.",
        [
            rule(
                "Единственное: this / that",
                "This — близко к говорящему или только что введённое «вот это». That — дальше в пространстве или «то, о чём уже говорили». После них глагол в единственном числе: This is… That was…",
                [
                    ex("This coffee is hot.", "Этот кофе горячий."),
                    ex("That building is the museum.", "То здание — музей."),
                    ex("That was a great idea.", "То была отличная идея."),
                ],
            ),
            rule(
                "Множественное: these / those",
                "These — близкие предметы во множественном числе; those — далёкие или «те». Глагол тоже множественный: These are my keys.",
                [
                    ex("These shoes are new.", "Эти туфли новые."),
                    ex("Those people are my neighbours.", "Те люди — мои соседи."),
                ],
            ),
            rule(
                "С существительным и без него",
                "Можно сказать this book или просто this, если предмет ясен из ситуации: What is this? Указательные слова часто стоят в начале представления: This is Anna.",
                [
                    ex("This is my friend, Anna.", "Это моя подруга Анна."),
                    ex("What are those?", "Что это там?"),
                ],
            ),
        ],
        compare=[
            {"left": "this book / these books", "right": "that car / those cars", "note": "Число и дистанция меняются вместе."},
        ],
        watch_out=[
            "This books — ошибка; нужно these books.",
            "Those is my bag — ошибка; одна сумка → That is my bag.",
            "Не путайте these (множ.) и this (един.).",
        ],
        remember="Близко: this/these. Далеко: that/those. Число должно совпасть с существительным и глаголом.",
    ),
    "present-simple": lesson(
        "Present Simple — каркас повседневности: привычки, факты, расписания и то, что верно «вообще». На A1 важно освоить две вещи: -s у he/she/it в утверждении и do/does в вопросе и отрицании.",
        [
            rule(
                "Утверждение и -s",
                "I/you/we/they + V1: I work. He/she/it + V-s: she works. После s/x/ch/sh/o часто -es (watches, goes); y после согласной → ies (studies). Без -s у 3-го лица утверждение звучит неправильно.",
                [
                    ex("I start work at nine.", "Я начинаю работу в девять."),
                    ex("She studies French.", "Она изучает французский."),
                    ex("He watches TV in the evening.", "Он смотрит телевизор вечером."),
                ],
            ),
            rule(
                "Отрицание и вопрос с do/does",
                "Вспомогательный do/does берёт на себя время и лицо. I don't work. Does he work? Смысловой глагол после do/does всегда без -s: Does she like tea? — не likes.",
                [
                    ex("They don't eat meat.", "Они не едят мясо."),
                    ex("Does it rain a lot here?", "Здесь часто идёт дождь?"),
                    ex("Do you speak German?", "Ты говоришь по-немецки?"),
                ],
            ),
            rule(
                "Когда выбирать Present Simple",
                "Привычки и рутина, общие истины, расписание транспорта и магазинов. Маркеры: always, usually, often, sometimes, never, every day, on Mondays, in the morning.",
                [
                    ex("He always takes the bus.", "Он всегда ездит на автобусе."),
                    ex("The shop opens at 8.", "Магазин открывается в 8."),
                    ex("Water boils at 100°C.", "Вода кипит при 100°C."),
                ],
            ),
        ],
        compare=[
            {"left": "She likes tea.", "right": "Does she like tea?", "note": "-s только в утверждении 3-го лица; в вопросе лицо уже выражает does, поэтому like без -s."},
            {"left": "I work in an office.", "right": "I'm working from home today.", "note": "Постоянная работа vs ситуация сегодня (Continuous)."},
        ],
        watch_out=[
            "He don't — ошибка; нужно He doesn't.",
            "Does she works? — ошибка; после does глагол без -s.",
            "Не путайте с Continuous: сейчас на глазах часто нужен be + -ing.",
        ],
        remember="Факт и привычка — Present Simple. He/she/it + -s в утверждении; иначе do/does + V1.",
    ),
    "present-continuous": lesson(
        "Present Continuous показывает действие, которое разворачивается сейчас или в текущий временный период. Формула: am/is/are + V-ing. Это не привычка «вообще», а процесс прямо сейчас или временная ситуация.",
        [
            rule(
                "Форма be + V-ing",
                "I'm working. She's reading. They are waiting. Орфография -ing: make→making (немое e уходит), sit→sitting (короткая гласная + одна согласная часто удваивается), lie→lying.",
                [
                    ex("I'm cooking dinner now.", "Я сейчас готовлю ужин."),
                    ex("They are waiting for a taxi.", "Они ждут такси."),
                    ex("The baby is sleeping.", "Малыш спит."),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "Not идёт после be: He isn't listening. В вопросе be выходит вперёд: Are you using this chair? What is she doing?",
                [
                    ex("He isn't listening.", "Он не слушает."),
                    ex("Are you using this chair?", "Ты пользуешься этим стулом?"),
                    ex("What are they doing?", "Что они делают?"),
                ],
            ),
            rule(
                "Сейчас и временно",
                "Маркеры: now, right now, at the moment, today, this week. She's staying with us this week — не навсегда, а на текущий отрезок.",
                [
                    ex("She's staying with us this week.", "На этой неделе она живёт у нас."),
                    ex("I'm reading a great book this month.", "В этом месяце я читаю отличную книгу."),
                ],
            ),
            rule(
                "Глаголы состояния",
                "Know, like, want, need, understand и have в значении «иметь» редко стоят в Continuous. На A1 безопаснее: I know the answer, не I'm knowing.",
                [
                    ex("I know the answer.", "Я знаю ответ."),
                    ex("She wants a new phone.", "Она хочет новый телефон."),
                ],
            ),
        ],
        compare=[
            {"left": "I work in an office.", "right": "I'm working from home today.", "note": "Постоянная работа vs ситуация сегодня."},
            {"left": "She usually drinks tea.", "right": "Today she is drinking coffee.", "note": "Привычка vs сегодняшний момент."},
        ],
        watch_out=[
            "I working — ошибка; нужен am/is/are.",
            "Не ставьте Continuous с know/like/want без особой причины.",
            "They is playing — ошибка: they are.",
        ],
        remember="Сейчас и временно — be + -ing. Привычка и факт — Present Simple.",
    ),
    "there-is-are": lesson(
        "There is / there are вводят новый объект в пространство: «в этом месте есть…». There здесь не значит «там»; это служебное начало конструкции. Число согласуется с первым существительным после there.",
        [
            rule(
                "Единственное и множественное",
                "There is + единственное / неисчисляемое: There is a lamp. There is some milk. There are + множественное: There are two chairs.",
                [
                    ex("There is a supermarket near here.", "Здесь рядом есть супермаркет."),
                    ex("There are some messages for you.", "Для тебя есть несколько сообщений."),
                    ex("There is a lot of noise.", "Много шума."),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "There isn't / there aren't. Вопросы: Is there…? Are there…? Вспомогательный be снова выходит вперёд.",
                [
                    ex("There isn't any milk.", "Молока нет."),
                    ex("Are there any tickets left?", "Остались билеты?"),
                    ex("Is there a bank here?", "Здесь есть банк?"),
                ],
            ),
            rule(
                "Some / any на A1",
                "Some чаще в утверждении: There are some apples. Any — в вопросах и отрицаниях: Are there any…? There aren't any… Этого правила достаточно для старта.",
                [
                    ex("There are some apples.", "Есть несколько яблок."),
                    ex("There aren't any apples.", "Яблок нет."),
                ],
            ),
        ],
        compare=[
            {"left": "There is a book on the table.", "right": "It is a book on the table.", "note": "Для «есть/находится» нужна конструкция there is, не it is."},
        ],
        watch_out=[
            "There is two windows — ошибка; two → there are.",
            "Не путайте there (конструкция) и their (их).",
            "После there is не ставьте сразу множественное без are.",
        ],
        remember="Сначала there is/are, затем объект, затем место. Число = первое существительное.",
    ),
    "can-ability": lesson(
        "Can — модальный глагол умения, возможности и простой просьбы/разрешения. Он не спрягается по лицам и всегда требует «голый» инфинитив без to: can swim, не can to swim и не cans.",
        [
            rule(
                "Умение: can + V1",
                "I can, she can, they can — одна форма на все лица. Отрицание: can't / cannot. Вопрос: Can you swim? Can выходит вперёд, do/does не нужен.",
                [
                    ex("I can speak Spanish.", "Я умею говорить по-испански."),
                    ex("He can't drive.", "Он не умеет водить."),
                    ex("Can she play the piano?", "Она умеет играть на пианино?"),
                ],
            ),
            rule(
                "Возможность и разрешение",
                "Can описывает то, что возможно в ситуации: I can see the sea from here. И вежливо просит/даёт разрешение: Can I open the window? You can leave early today.",
                [
                    ex("You can leave early today.", "Сегодня можешь уйти пораньше."),
                    ex("Can I use your phone?", "Можно взять твой телефон?"),
                    ex("I can hear music next door.", "Я слышу музыку за стеной."),
                ],
            ),
            rule(
                "Почему не do и не to",
                "Модальный can уже вспомогательный: вопросы и отрицания строятся им самим. После can никогда нет to. Формы cans не существует.",
                [
                    ex("Can you help me?", "Можешь мне помочь?"),
                    ex("Birds can fly.", "Птицы умеют летать."),
                ],
            ),
        ],
        compare=[
            {"left": "I can cook.", "right": "I cook every day.", "note": "Can — про умение/возможность; Present Simple — про привычку."},
            {"left": "Can you help?", "right": "Do you help?", "note": "Просьба/умение через can; do — про обычное действие."},
        ],
        watch_out=[
            "I can to cook и He cans run — ошибки.",
            "Don't can — невозможно; отрицание только can't/cannot.",
            "Could появится позже для прошлого; на A1 can — про настоящее.",
        ],
        remember="Can не спрягается. После него голый инфинитив. Вопросы и not — через сам can.",
    ),
    "imperatives": lesson(
        "Повелительное наклонение даёт инструкцию, просьбу или запрет. Подлежащее you обычно не называют: форма глагола уже обращена к слушателю. Вежливость часто добавляют please; совместное действие — Let's.",
        [
            rule(
                "Утвердительный императив",
                "Берут базовую форму глагола: Open the door. Turn left. Take a seat. Please может стоять в начале или в конце: Please sit down / Sit down, please.",
                [
                    ex("Take a seat, please.", "Присядьте, пожалуйста."),
                    ex("Turn left at the bank.", "Поверните налево у банка."),
                    ex("Switch off your phones.", "Выключите телефоны."),
                ],
            ),
            rule(
                "Запрет: Don't + V1",
                "Don't (do not) + базовая форма: Don't touch the paintings. Don't be late. Даже to be в императиве выглядит как Be careful / Don't be noisy.",
                [
                    ex("Don't touch the paintings.", "Не трогайте картины."),
                    ex("Don't be late.", "Не опаздывайте."),
                    ex("Be careful!", "Будьте осторожны!"),
                ],
            ),
            rule(
                "Let's — сделаем вместе",
                "Let's (= let us) + V1 предлагает общее действие: Let's start. Let's go to the café. После let's частицы to нет.",
                [
                    ex("Let's start.", "Давайте начнём."),
                    ex("Let's go to the café.", "Давайте зайдём в кафе."),
                ],
            ),
        ],
        compare=[
            {"left": "Open the window.", "right": "Can you open the window?", "note": "Императив прямее; can you… мягче как просьба."},
        ],
        watch_out=[
            "To sit down и Let's to eat — ошибки: без to.",
            "Подлежащее you в нейтральной инструкции обычно опускают.",
            "Doesn't forget — для запрета группе нужно Don't forget.",
        ],
        remember="Инструкция = V1. Запрет = Don't + V1. Вместе = Let's + V1.",
    ),
    "question-words": lesson(
        "Специальный вопрос начинается с вопросительного слова (who, what, where…), затем обычно идёт вспомогательный глагол и подлежащее. Сначала выберите смысл (где/кто/почему), потом соберите порядок слов.",
        [
            rule(
                "Базовый набор Wh-слов",
                "Who — кто; what — что/какой; where — где; when — когда; why — почему; how — как; whose — чей; which — который из ограниченного набора.",
                [
                    ex("Where do you live?", "Где ты живёшь?"),
                    ex("Whose bag is this?", "Чья это сумка?"),
                    ex("Which one do you prefer, tea or coffee?", "Какой выберешь — чай или кофе?"),
                ],
            ),
            rule(
                "Порядок: Wh + aux + subject + verb",
                "What does she want? Where are you from? How did they travel? Исключение: who/what как подлежащее — Who called you? (без do, если who само подлежащее).",
                [
                    ex("What does she want?", "Чего она хочет?"),
                    ex("Who is that man?", "Кто этот мужчина?"),
                    ex("Why is he sad?", "Почему он грустный?"),
                ],
            ),
            rule(
                "How + измерение",
                "How many + исчисляемые: How many apples? How much + неисчисляемые: How much water? How often / how long — про частоту и длительность.",
                [
                    ex("How many apples do you want?", "Сколько яблок тебе нужно?"),
                    ex("How much sugar is left?", "Сколько сахара осталось?"),
                    ex("How do you get to work?", "Как ты добираешься на работу?"),
                ],
            ),
        ],
        compare=[
            {"left": "Where do you live?", "right": "Where you live?", "note": "Без вспомогательного глагола вопрос на A1 обычно неверен."},
            {"left": "Who called you?", "right": "Who did you call?", "note": "Who-подлежащее vs who-дополнение."},
        ],
        watch_out=[
            "Where you live? / What you want? — нужны are/do/does.",
            "How much apples — ошибка; apples → how many.",
            "Whose ≠ who's (who is).",
        ],
        remember="Сначала Wh-смысл, затем вспомогательный глагол, затем подлежащее и смысловой глагол.",
    ),
    "prepositions-place": lesson(
        "Предлоги места отвечают на вопрос «где?». Ядро A1 — тройка in / on / at, плюс относительные under, behind, between, next to, opposite. Часто это фиксированные сочетания, которые лучше запоминать целиком.",
        [
            rule(
                "In — внутри объёма",
                "In a room, in a box, in a city, in a country. Мысленно: объект находится «в пространстве». They live in Tokyo. The cat is in the box.",
                [
                    ex("The cat is in the box.", "Кот в коробке."),
                    ex("They live in Tokyo.", "Они живут в Токио."),
                    ex("There is milk in the fridge.", "В холодильнике есть молоко."),
                ],
            ),
            rule(
                "On — на поверхности; at — точка",
                "On a table, on the wall, on the floor. At — точка на карте или место-назначение: at the door, at the station, at the bus stop. Запомните: at home, at work.",
                [
                    ex("The keys are on the desk.", "Ключи на столе."),
                    ex("She's at the airport.", "Она в аэропорту."),
                    ex("Meet me at the bus stop.", "Встретимся на остановке."),
                ],
            ),
            rule(
                "Относительные предлоги",
                "Under — под; behind — за; in front of — перед; between A and B — между; next to / beside — рядом; opposite — напротив (часто без to).",
                [
                    ex("The café is next to the cinema.", "Кафе рядом с кинотеатром."),
                    ex("Wait in front of the hotel.", "Подожди перед отелем."),
                    ex("The shop is opposite the park.", "Магазин напротив парка."),
                ],
            ),
        ],
        compare=[
            {"left": "in the box", "right": "on the table", "note": "Внутри объёма vs на поверхности."},
            {"left": "at home", "right": "in home", "note": "Фиксированное at home."},
        ],
        watch_out=[
            "In home — ошибка; нужно at home.",
            "The book is in the table — обычно on the table.",
            "Opposite to the park на A1 чаще лишнее; достаточно opposite the park.",
        ],
        remember="Внутри — in. На поверхности — on. Точка/home/work — at. Остальное — относительные предлоги.",
    ),
    "prepositions-time": lesson(
        "Та же тройка in / on / at работает со временем. Короткая схема: at — точные часы и некоторые «точки»; on — дни и даты; in — более длинные периоды и части дня (кроме night).",
        [
            rule(
                "At — часы и точки",
                "At 7 o'clock, at 8.15, at noon, at midnight, at night. В BrE часто at the weekend, at Christmas. Это «момент на шкале времени».",
                [
                    ex("The film starts at 8.15.", "Фильм начинается в 8:15."),
                    ex("He sleeps well at night.", "Ночью он хорошо спит."),
                    ex("See you at the weekend.", "Увидимся в выходные."),
                ],
            ),
            rule(
                "On — дни и даты",
                "On Monday, on Friday evening, on 12 May, on my birthday. Если назван день или календарная дата — почти всегда on.",
                [
                    ex("See you on Friday.", "Увидимся в пятницу."),
                    ex("My birthday is on 3 March.", "Мой день рождения — 3 марта."),
                    ex("We don't work on Sundays.", "По воскресеньям мы не работаем."),
                ],
            ),
            rule(
                "In — периоды длиннее дня",
                "In July, in 2019, in the morning / afternoon / evening, in two weeks («через две недели»). Части дня с in, но night — с at.",
                [
                    ex("I was born in 1998.", "Я родился в 1998."),
                    ex("She works in the morning.", "Она работает утром."),
                    ex("We'll leave in two weeks.", "Мы уедем через две недели."),
                ],
            ),
        ],
        compare=[
            {"left": "at 9.00", "right": "on Monday", "note": "Часы vs день."},
            {"left": "in the morning", "right": "at night", "note": "Утро/день/вечер — in; ночь — at."},
        ],
        watch_out=[
            "In Monday и on 8 p.m. — перепутаны слоты.",
            "On the weekend чаще AmE; в британском учебном стиле — at the weekend.",
            "In night — ошибка; нужно at night.",
        ],
        remember="Часы и night/weekend (BrE) — at. Дни и даты — on. Месяцы, годы, morning/afternoon/evening — in.",
    ),
    "have-got": lesson(
        "Have got в британском английском — главный способ сказать о владении, семье и внешности на A1. По смыслу это не Present Perfect: got здесь часть устойчивой конструкции. В привычках вроде have breakfast got не ставят.",
        [
            rule(
                "Утверждение",
                "I/you/we/they have got. He/she/it has got. Краткие формы: I've got, she's got, they've got. I've got two sisters. He has got brown eyes.",
                [
                    ex("I've got two sisters.", "У меня две сестры."),
                    ex("He has got brown eyes.", "У него карие глаза."),
                    ex("We've got a small flat.", "У нас небольшая квартира."),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "I haven't got / she hasn't got. Вопросы: Have you got…? Has she got…? Конструкция Do you have got? неверна: либо Have you got, либо Do you have (без got).",
                [
                    ex("I haven't got a car.", "У меня нет машины."),
                    ex("Has she got a minute?", "У неё есть минутка?"),
                    ex("Have you got any cash?", "Есть наличные?"),
                ],
            ),
            rule(
                "Have без got",
                "В устойчивых действиях got не нужен: have breakfast / lunch / dinner, have a shower, have a break. Здесь have — обычный глагол привычки.",
                [
                    ex("We have lunch at one.", "Мы обедаем в час."),
                    ex("I have a shower every morning.", "Я каждое утро принимаю душ."),
                ],
            ),
        ],
        compare=[
            {"left": "I've got a bike.", "right": "I have breakfast at 7.", "note": "Владение с got vs привычное действие без got."},
            {"left": "Have you got a pen?", "right": "Do you have a pen?", "note": "Оба про владение; got типичен для BrE."},
        ],
        watch_out=[
            "I have got hungry — ошибка; нужно I am hungry.",
            "Do you have got… — смешение двух схем.",
            "He haves got — формы haves нет; только has got.",
        ],
        remember="Владение и внешность: have/has got. Еда, душ, перерыв — have без got.",
    ),
    "past-simple-be": lesson(
        "В прошедшем to be имеет всего две формы: was и were. Вопросы и отрицания строятся без did — was/were сами работают как вспомогательные. Этот блок удобно освоить до Past Simple смысловых глаголов.",
        [
            rule(
                "Was и were",
                "I/he/she/it was. You/we/they were. I was at home yesterday. They were tired. Для you всегда were — и в единственном, и во множественном смысле.",
                [
                    ex("I was at home yesterday.", "Вчера я был дома."),
                    ex("They were tired.", "Они были усталыми."),
                    ex("You were right.", "Ты был прав."),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "Wasn't / weren't. Were you late? Where was she? Was he the manager? Did + were вместе не ставят.",
                [
                    ex("It wasn't expensive.", "Это было недорого."),
                    ex("Were they at the party?", "Они были на вечеринке?"),
                    ex("Was she at work on Monday?", "Она была на работе в понедельник?"),
                ],
            ),
            rule(
                "Маркеры прошлого",
                "Yesterday, last week / last year, in 2019, two days ago. С ними was/were описывают состояние или место в законченном прошлом.",
                [
                    ex("We were in Paris in 2019.", "В 2019 мы были в Париже."),
                    ex("The weather was terrible.", "Погода была ужасной."),
                ],
            ),
        ],
        compare=[
            {"left": "Were you at school?", "right": "Did you were at school?", "note": "С was/were вспомогательный did не нужен."},
            {"left": "I was ill.", "right": "I were ill.", "note": "I/he/she/it — только was."},
        ],
        watch_out=[
            "Did you were? — грубая ошибка.",
            "I were / He were — неверно вне особых конструкций уровнем выше.",
            "Was you… — нужно Were you…",
        ],
        remember="Прошедшее to be — was/were без did. I/he/she/it was; you/we/they were.",
    ),
    "past-simple-verbs": lesson(
        "Past Simple называет законченное действие в конкретном прошлом: yesterday, last week, in 2010, ago. Правильные глаголы берут -ed; неправильные — II форму (go—went). В вопросе и отрицании появляется did, а смысловой глагол возвращается к V1.",
        [
            rule(
                "Правильные глаголы + ed",
                "Work—worked, live—lived, play—played. Stop—stopped (удвоение), study—studied (y→ied). Произношение -ed бывает /t/, /d/ или /ɪd/, но на письме схема одна.",
                [
                    ex("I visited my aunt last Sunday.", "В прошлое воскресенье я навестил тётю."),
                    ex("They played football yesterday.", "Вчера они играли в футбол."),
                    ex("She studied French at school.", "В школе она учила французский."),
                ],
            ),
            rule(
                "Неправильные: II форма",
                "Частый минимум: be—was/were, have—had, go—went, do—did, get—got, make—made, take—took, come—came, see—saw, buy—bought, lose—lost. Их учат списком, не правилом.",
                [
                    ex("She went to Rome in May.", "В мае она ездила в Рим."),
                    ex("We bought a ticket.", "Мы купили билет."),
                    ex("I lost my keys.", "Я потерял ключи."),
                ],
            ),
            rule(
                "Did в вопросе и отрицании",
                "Did + подлежащее + V1: Did you call her? He didn't like the film. Did уже несёт прошлое, поэтому went/saw после did не повторяют: не Did you went?",
                [
                    ex("Did you call her?", "Ты ей звонил?"),
                    ex("He didn't like the film.", "Ему не понравился фильм."),
                    ex("Did they arrive late?", "Они опоздали?"),
                ],
            ),
        ],
        compare=[
            {"left": "She went home.", "right": "Did she go home?", "note": "Во II форме — утверждение; после did — снова V1."},
            {"left": "I saw the email yesterday.", "right": "I have seen the email.", "note": "Точная дата прошлого → Past Simple, не Perfect."},
        ],
        watch_out=[
            "Did you went? / He didn't went — частые ошибки; нужно go.",
            "После yesterday/last/ago не тяните Present Perfect.",
            "Не забывайте II форму у неправильных в утверждении.",
        ],
        remember="Факт в прошлом + маркер времени = Past Simple. Вопрос/not: did + V1.",
    ),
    "going-to": lesson(
        "Be going to + V — основной способ говорить о будущем на A1: есть намерение или будущее уже «видно» по приметам. Нужны две детали: форма to be согласуется с подлежащим, после going to стоит голый инфинитив.",
        [
            rule(
                "Намерение и план",
                "Говорящий уже решил: I'm going to call her tonight. We're going to move house. Это не спонтанная идея «прямо сейчас», а заранее сложившееся намерение.",
                [
                    ex("We're going to move house.", "Мы собираемся переезжать."),
                    ex("I'm going to start a course.", "Я собираюсь начать курс."),
                    ex("He's going to study medicine.", "Он собирается учиться на врача."),
                ],
            ),
            rule(
                "Предсказание по примете",
                "Есть сигнал в настоящем: Look at those clouds — it's going to rain. She's going to win — she's much faster. Вывод о будущем опирается на то, что уже видно.",
                [
                    ex("Look at the sky! It's going to snow.", "Смотри на небо! Сейчас пойдёт снег."),
                    ex("She's going to win — she's much faster.", "Она победит: она намного быстрее."),
                ],
            ),
            rule(
                "Формы, not и вопрос",
                "Am/is/are + going to + V. Отрицание: I'm not going to tell him. Вопрос: Are you going to cook tonight? Без be конструкция ломается: не She going to be late.",
                [
                    ex("Is he going to study medicine?", "Он собирается изучать медицину?"),
                    ex("I'm not going to stay.", "Я не собираюсь оставаться."),
                    ex("Are you going to cook tonight?", "Ты собираешься готовить сегодня вечером?"),
                ],
            ),
        ],
        compare=[
            {"left": "I'm going to the shop.", "right": "I'm going to buy milk.", "note": "Going to + место vs going to + глагол-намерение."},
            {"left": "We're going to visit Grandma.", "right": "We visit Grandma on Sundays.", "note": "План на будущее vs привычка Present Simple."},
        ],
        watch_out=[
            "I going to… — нужен am/is/are.",
            "They is going to help — they are.",
            "После going to не ставьте to ещё раз: going to to buy — ошибка.",
        ],
        remember="План и очевидное будущее — be going to + V1. Be обязателен.",
    ),
    "adjectives-a1": lesson(
        "Прилагательное описывает качество человека или вещи и в английском не меняется по роду, числу и падежу: a red car, red cars. Главное на A1 — место (перед существительным или после связки) и то, что прилагательное не получает -s.",
        [
            rule(
                "Перед существительным",
                "A new phone, an old house. Несколько прилагательных обычно идут в порядке: мнение → размер → возраст → цвет → материал: a lovely little old town, a small black bag.",
                [
                    ex("a lovely little old town", "милый маленький старый город"),
                    ex("a small black bag", "маленькая чёрная сумка"),
                    ex("They have a big house.", "У них большой дом."),
                ],
            ),
            rule(
                "После be / look / feel",
                "She is tall. I feel tired. The soup tastes good. Здесь прилагательное — часть сказуемого. Не путайте с наречием на -ly, если нужно именно качество.",
                [
                    ex("I feel tired.", "Я чувствую себя усталым."),
                    ex("She looks happy.", "Она выглядит счастливой."),
                    ex("He is a careful driver.", "Он аккуратный водитель."),
                ],
            ),
            rule(
                "Усилители very / really",
                "Very и really стоят перед прилагательным: very cold, really interesting, really sad. Порядок: усилитель → прилагательное → (существительное).",
                [
                    ex("It's really important.", "Это действительно важно."),
                    ex("The water is very cold.", "Вода очень холодная."),
                    ex("It's a really sad story.", "Это очень грустная история."),
                ],
            ),
        ],
        compare=[
            {"left": "a blue car", "right": "a car blue", "note": "В атрибутивной позиции прилагательное перед существительным."},
            {"left": "She looks happy.", "right": "She looks happily.", "note": "После look в значении «выглядеть» нужно прилагательное."},
        ],
        watch_out=[
            "A car red и greens books — типичные кальки.",
            "Прилагательное не получает множественное -s.",
            "Feel badly про самочувствие на A1 обычно заменяют на feel bad.",
        ],
        remember="Прилагательное неизменно. Место: перед словом или после be/look/feel. Усилитель — перед ним.",
    ),
}
