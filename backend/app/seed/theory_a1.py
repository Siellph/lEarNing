"""Enriched A1 grammar theory (Russian explanations, English examples).

Tone: impersonal / descriptive Russian. No direct address to the learner.
Examples keep {en, ru}. Body may use **…** for emphasis; rules may include
tables / callouts / wrong–right pairs for LessonView.
"""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

A1_THEORY = {
    "to-be": lesson(
        "Глагол **to be** («быть, являться») — связка: соединяет подлежащее с ролью, качеством, местом или возрастом. На A1 без to be почти нельзя собрать нормальное описание. В речи чаще звучат краткие формы: I'm, she's, they're.",
        [
            rule(
                "Формы в настоящем",
                "Выбор формы зависит только от подлежащего, не от следующего слова. Краткие формы в разговоре обычны и не считаются «ленивыми».",
                [
                    ex("I am a student. / I'm a student.", "Я студент."),
                    ex("She is tired. / She's tired.", "Она устала."),
                    ex("They are at home.", "Они дома."),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Полная форма", "Краткая"],
                        [
                            ["I", "am", "I'm"],
                            ["he / she / it", "is", "he's / she's / it's"],
                            ["you / we / they", "are", "you're / we're / they're"],
                        ],
                    ),
                ],
            ),
            rule(
                "Отрицание",
                "Частица **not** стоит сразу после формы to be. Отдельный don't / doesn't со связкой to be не нужен.",
                [
                    ex("I'm not hungry.", "Я не голоден."),
                    ex("It isn't cold today.", "Сегодня не холодно."),
                    ex("We aren't ready yet.", "Мы ещё не готовы."),
                ],
                tables=[
                    table(
                        ["Утверждение", "Отрицание"],
                        [
                            ["I am / I'm", "I am not / I'm not"],
                            ["she is / she's", "she is not / isn't"],
                            ["they are / they're", "they are not / aren't"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Does she is ready?", "Is she ready?", "Со связкой to be вспомогательный do/does не ставят."),
                ],
            ),
            rule(
                "Вопрос",
                "Форма to be выходит на первое место. Вопросительное слово стоит ещё левее: Where is the station?",
                [
                    ex("Are they from Spain?", "Они из Испании?"),
                    ex("Where is the station?", "Где вокзал?"),
                    ex("Is this your bag?", "Это твоя сумка?"),
                ],
            ),
            rule(
                "Типичные смыслы",
                "Профессия и роль, место, возраст, описание и настроение — это состояние или характеристика, а не «действие как процесс».",
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
            "После he/she/it только **is**, не are.",
            "**I am**, не I is и не I are.",
        ],
        remember="To be сам несёт лицо и число. Краткие формы нормальны в речи; do/does ему не нужны.",
    ),
    "articles-a1": lesson(
        "Артикль — служебное слово перед существительным. В русском его нет, поэтому выбор **a/an**, **the** или «нуля» нужно осознанно тренировать.\n\nТри опоры A1: впервые / любой → a/an; известный или единственный → the; общее понятие → без артикля.",
        [
            rule(
                "A / an — один из класса, впервые",
                "A/an называют один неопределённый экземпляр: I need a pen (любую ручку). Выбор a или an зависит от **звука**, не от буквы.",
                [
                    ex("I need a pen.", "Мне нужна ручка (любая)."),
                    ex("She is an engineer.", "Она инженер."),
                    ex("We waited an hour.", "Мы ждали час."),
                ],
                tables=[
                    table(
                        ["Звук", "Артикль", "Примеры"],
                        [
                            ["согласный", "**a**", "a book, a university (/j/)"],
                            ["гласный", "**an**", "an apple, an hour (/aʊ/)"],
                        ],
                    ),
                ],
                callouts=[
                    callout("University начинается с буквы u, но звук /j/ — согласный → **a** university. Hour начинается с немого h и звука гласного → **an** hour.", "tip"),
                ],
            ),
            rule(
                "The — этот самый или единственный",
                "The ставят, когда предмет уже понятен из ситуации или уникален в контексте: the sun, the door, the kitchen. После первого a car часто следует the car.",
                [
                    ex("Close the window, please.", "Закрой окно (то, которое оба видят)."),
                    ex("The moon is bright tonight.", "Луна сегодня яркая."),
                    ex("I bought a phone. The phone is black.", "Купил телефон. Телефон чёрный."),
                ],
            ),
            rule(
                "Нулевой артикль",
                "Без артикля: имена, большинство стран и городов; неисчисляемые в общем смысле (tea, music); множественное «вообще» (dogs sleep a lot). Это не «забытый артикль», а отдельное решение.",
                [
                    ex("I like music.", "Я люблю музыку (как явление)."),
                    ex("Cats sleep a lot.", "Кошки много спят (вообще)."),
                    ex("Anna lives in Madrid.", "Анна живёт в Мадриде."),
                ],
            ),
            rule(
                "Профессии и еда — короткие ориентиры",
                "Перед профессией в роли «кто это» обычно a/an: She is a nurse. Перед едой и напитками в общем смысле — ноль: I like coffee. Конкретная порция на столе — the coffee.",
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
            "Опора на звук, не на букву: **a** university, **an** hour.",
            "Уникальные объекты часто с the: the Internet, the sky, the sun.",
            "Не ставят a перед множественным: a books — ошибка.",
        ],
        remember="**A/an** = один из класса. **The** = этот самый. **Ноль** = общее имя, вещество или класс во множественном.",
    ),
    "nouns-plurals": lesson(
        "Существительное почти всегда имеет единственное и множественное число. База A1: регулярное **+s / +es** и короткий список особых форм (man—men, child—children). Без этого нельзя согласовать there is/are и this/these.",
        [
            rule(
                "Регулярное множественное",
                "Большинство слов получает окончание. Орфография зависит от конца слова.",
                [
                    ex("one bus — two buses", "один автобус — два автобуса"),
                    ex("a baby — babies", "малыш — малыши"),
                    ex("one day — two days", "один день — два дня"),
                ],
                tables=[
                    table(
                        ["Правило", "Единственное", "Множественное"],
                        [
                            ["обычно **+s**", "book", "books"],
                            ["после s / x / ch / sh (и часто o) → **+es**", "watch, box, tomato", "watches, boxes, tomatoes"],
                            ["**y** после согласной → **ies**", "city, baby", "cities, babies"],
                            ["**y** после гласной → **+s**", "day, key", "days, keys"],
                        ],
                    ),
                ],
            ),
            rule(
                "Особые формы",
                "Их выучивают списком: здесь правило +s не работает.",
                [
                    ex("There are three children in the garden.", "В саду трое детей."),
                    ex("People are waiting.", "Люди ждут."),
                    ex("My feet hurt.", "У меня болят ноги."),
                ],
                tables=[
                    table(
                        ["Единственное", "Множественное"],
                        [
                            ["man / woman", "men / women"],
                            ["child", "children"],
                            ["person", "people"],
                            ["tooth / foot", "teeth / feet"],
                            ["mouse", "mice"],
                        ],
                    ),
                ],
            ),
            rule(
                "Одинаковая форма и «ложное» множественное",
                "Sheep, fish, deer часто не меняются. News выглядит как множественное, но согласуется как единственное: The news **is** good.",
                [
                    ex("Five sheep are in the field.", "В поле пять овец."),
                    ex("The news is good.", "Новости хорошие."),
                ],
            ),
        ],
        compare=[
            {"left": "one child — two children", "right": "one book — two books", "note": "Сначала особый список, иначе +s."},
        ],
        watch_out=[
            "Peoples — только «народы»; про людей говорят **people**.",
            "Childs и foots — ошибки: children, feet.",
            "This news are — ошибка: news + **is**.",
        ],
        remember="Сначала особый список, затем **+s / +es**. News — единственное по согласованию.",
    ),
    "pronouns-possessives": lesson(
        "Местоимения заменяют имена, чтобы не повторять их. Нужно различать роль в предложении: кто делает действие (**I, she**) и на кого оно направлено (**me, her**). Отдельно — принадлежность: my book vs This book is mine.",
        [
            rule(
                "Подлежащее и дополнение",
                "После глагола и предлога нужна объектная форма: She likes him. Look at us.",
                [
                    ex("She likes him.", "Она любит его."),
                    ex("They called us.", "Они нам позвонили."),
                    ex("Can you help me?", "Можешь мне помочь?"),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Дополнение"],
                        [
                            ["I", "me"],
                            ["you", "you"],
                            ["he / she / it", "him / her / it"],
                            ["we", "us"],
                            ["they", "them"],
                        ],
                    ),
                ],
            ),
            rule(
                "Притяжательные прилагательные",
                "My, your, his, her, its, our, their всегда стоят **перед** существительным и никогда не бывают «голыми»: my bag, their house. Форма **its** — без апострофа.",
                [
                    ex("This is her laptop.", "Это её ноутбук."),
                    ex("Our teacher is kind.", "Наш учитель добрый."),
                    ex("The dog wagged its tail.", "Собака вильнула хвостом."),
                ],
                pairs=[
                    pair("This bag is my.", "This bag is mine.", "Без существительного нужна абсолютная форма."),
                    pair("it's tail", "its tail", "its = принадлежность; it's = it is / it has."),
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
                tables=[
                    table(
                        ["Перед словом", "Вместо группы"],
                        [
                            ["my", "mine"],
                            ["your", "yours"],
                            ["his / her", "his / hers"],
                            ["our / their", "ours / theirs"],
                        ],
                    ),
                ],
            ),
        ],
        compare=[
            {"left": "This is my book.", "right": "This book is mine.", "note": "Перед словом — my; вместо группы — mine."},
            {"left": "its tail", "right": "it's raining", "note": "its = принадлежность; it's = it is / it has."},
        ],
        watch_out=[
            "Me book и I book — ошибки; нужно **my** book.",
            "This bag is my — неполно; без существительного нужна форма **mine**.",
            "**Its** ≠ **it's**.",
        ],
        remember="Роль: I/me. Перед словом: my/her. Вместо группы: mine/hers.",
    ),
    "demonstratives": lesson(
        "This, that, these, those указывают на предмет и одновременно показывают число и «дистанцию» (рядом / дальше). Они согласуются с существительным и с глаголом to be.",
        [
            rule(
                "Число и дистанция",
                "This / that — единственное число. These / those — множественное. Ближе к говорящему — this/these; дальше или «уже упомянутое» — that/those.",
                [
                    ex("This coffee is hot.", "Этот кофе горячий."),
                    ex("Those people are my neighbours.", "Те люди — мои соседи."),
                    ex("That was a great idea.", "То была отличная идея."),
                ],
                tables=[
                    table(
                        ["", "Рядом / «вот»", "Дальше / «то»"],
                        [
                            ["1 предмет", "**this**", "**that**"],
                            ["несколько", "**these**", "**those**"],
                        ],
                    ),
                ],
            ),
            rule(
                "Согласование с глаголом",
                "После this/that глагол в единственном числе: This **is**…. После these/those — множественный: These **are**….",
                [
                    ex("This is my friend, Anna.", "Это моя подруга Анна."),
                    ex("These shoes are new.", "Эти туфли новые."),
                    ex("What are those?", "Что это там?"),
                ],
                pairs=[
                    pair("This books are new.", "These books are new.", "Множественное существительное → these/those."),
                    pair("Those is my bag.", "That is my bag.", "Одна сумка → that + is."),
                ],
            ),
        ],
        compare=[
            {"left": "this book / these books", "right": "that car / those cars", "note": "Число и дистанция меняются вместе."},
        ],
        watch_out=[
            "This books — ошибка; нужно **these** books.",
            "Those is my bag — ошибка; одна сумка → **That is** my bag.",
            "Не путают these (множ.) и this (един.).",
        ],
        remember="Близко: this/these. Далеко: that/those. Число должно совпасть с существительным и глаголом.",
    ),
    "present-simple": lesson(
        "Present Simple — каркас повседневности: привычки, факты, расписания и то, что верно «вообще».\n\nНа A1 критичны две опоры: окончание **-s** у he/she/it в утверждении и вспомогательные **do / does** в вопросе и отрицании.",
        [
            rule(
                "Утверждение: кто + какая форма глагола",
                "Для I / you / we / they берут базовую форму глагола (**V1**): I work.\n\nДля he / she / it к глаголу добавляют окончание: she work**s**. Без этого окончания утверждение о 3-м лице звучит неправильно.",
                [
                    ex("I start work at nine.", "Я начинаю работу в девять."),
                    ex("She studies French.", "Она изучает французский."),
                    ex("He watches TV in the evening.", "Он смотрит телевизор вечером."),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Форма", "Пример"],
                        [
                            ["I / you / we / they", "**V1** (без -s)", "I work · they live"],
                            ["he / she / it", "**V1 + -s / -es / -ies**", "she works · it rains"],
                        ],
                    ),
                    table(
                        ["Конец глагола", "Окончание", "Примеры"],
                        [
                            ["обычный случай", "**-s**", "work → works, play → plays"],
                            ["s / x / ch / sh / o", "**-es**", "watch → watches, go → goes"],
                            ["согласная + y", "**y → ies**", "study → studies"],
                        ],
                    ),
                ],
                pairs=[
                    pair("She work in an office.", "She works in an office.", "У he/she/it в утверждении окончание **-s** обязательно."),
                    pair("He go to school.", "He goes to school.", "После go / watch / finish чаще **-es**."),
                ],
                callouts=[
                    callout("Именно отсутствие **-s** у 3-го лица в утверждении — одна из самых частых ошибок A1: She like tea звучит неверно; нужно She like**s** tea.", "warn"),
                ],
            ),
            rule(
                "Отрицание и вопрос: do / does",
                "Вспомогательный **do / does** берёт на себя время и лицо. Смысловой глагол после do/does всегда возвращается к базовой форме **без -s**.",
                [
                    ex("They don't eat meat.", "Они не едят мясо."),
                    ex("Does it rain a lot here?", "Здесь часто идёт дождь?"),
                    ex("Do you speak German?", "Ты говоришь по-немецки?"),
                ],
                tables=[
                    table(
                        ["Тип", "I / you / we / they", "he / she / it"],
                        [
                            ["Отрицание", "don't + **V1**", "doesn't + **V1**"],
                            ["Вопрос", "Do … + **V1**?", "Does … + **V1**?"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Does she likes tea?", "Does she like tea?", "После does глагол без **-s**."),
                    pair("He don't work here.", "He doesn't work here.", "Для he/she/it — **doesn't**."),
                ],
            ),
            rule(
                "Когда выбирают Present Simple",
                "Привычки и рутина, общие истины, расписание транспорта и магазинов. Частые маркеры: always, usually, often, sometimes, never, every day, on Mondays, in the morning.",
                [
                    ex("He always takes the bus.", "Он всегда ездит на автобусе."),
                    ex("The shop opens at 8.", "Магазин открывается в 8."),
                    ex("Water boils at 100°C.", "Вода кипит при 100°C."),
                ],
            ),
        ],
        compare=[
            {"left": "She likes tea.", "right": "Does she like tea?", "note": "**-s** только в утверждении 3-го лица; в вопросе лицо уже выражает does, поэтому like без -s."},
            {"left": "I work in an office.", "right": "I'm working from home today.", "note": "Постоянная работа vs ситуация сегодня (Continuous)."},
        ],
        watch_out=[
            "**He don't** — ошибка; нужно He **doesn't**.",
            "**Does she works?** — ошибка; после does глагол без -s.",
            "Не путают с Continuous: действие «на глазах сейчас» часто требует be + **-ing**.",
        ],
        remember="Факт и привычка — Present Simple. В утверждении he/she/it + **-s**; в вопросе и отрицании — do/does + **V1** без -s.",
    ),
    "present-continuous": lesson(
        "Present Continuous показывает действие, которое разворачивается сейчас или в текущий временный период. Формула: **am / is / are + V-ing**. Это не привычка «вообще», а процесс прямо сейчас или временная ситуация.",
        [
            rule(
                "Форма be + V-ing",
                "Сначала согласуют форму to be с подлежащим, затем добавляют смысловой глагол с **-ing**.",
                [
                    ex("I'm cooking dinner now.", "Я сейчас готовлю ужин."),
                    ex("They are waiting for a taxi.", "Они ждут такси."),
                    ex("The baby is sleeping.", "Малыш спит."),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Форма"],
                        [
                            ["I", "am + **-ing** → I'm working"],
                            ["he / she / it", "is + **-ing** → she's reading"],
                            ["you / we / they", "are + **-ing** → they are waiting"],
                        ],
                    ),
                    table(
                        ["Орфография -ing", "Пример"],
                        [
                            ["немое e уходит", "make → making"],
                            ["короткая гласная + одна согласная часто удваивается", "sit → sitting"],
                            ["ie → y", "lie → lying"],
                        ],
                    ),
                ],
                pairs=[
                    pair("I working now.", "I'm working now.", "Без am/is/are Continuous не собирается."),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "Not идёт после be: He isn't listening. В вопросе be выходит вперёд: Are you using this chair?",
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
                callouts=[
                    callout("Если смысл — «вообще / обычно», чаще нужен Present Simple, даже если в русской фразе есть слово «сейчас».", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "I work in an office.", "right": "I'm working from home today.", "note": "Постоянная работа vs ситуация сегодня."},
            {"left": "She usually drinks tea.", "right": "Today she is drinking coffee.", "note": "Привычка vs сегодняшний момент."},
        ],
        watch_out=[
            "I working — ошибка; нужен **am/is/are**.",
            "Не ставят Continuous с know/like/want без особой причины.",
            "They is playing — ошибка: they **are**.",
        ],
        remember="Сейчас и временно — **be + -ing**. Привычка и факт — Present Simple.",
    ),
    "there-is-are": lesson(
        "There is / there are вводят новый объект в пространство: «в этом месте есть…». There здесь не значит «там»; это служебное начало конструкции. Число согласуется с **первым** существительным после there.",
        [
            rule(
                "Единственное и множественное",
                "There is — для одного предмета или неисчисляемого. There are — для множественного числа.",
                [
                    ex("There is a supermarket near here.", "Здесь рядом есть супермаркет."),
                    ex("There are some messages for you.", "Для тебя есть несколько сообщений."),
                    ex("There is a lot of noise.", "Много шума."),
                ],
                tables=[
                    table(
                        ["Конструкция", "Когда", "Пример"],
                        [
                            ["**There is**", "1 предмет / неисчисляемое", "There is a lamp. There is some milk."],
                            ["**There are**", "множественное", "There are two chairs."],
                        ],
                    ),
                ],
                pairs=[
                    pair("There is two windows.", "There are two windows.", "Число 2 и больше → there are."),
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
                "Some чаще в утверждении: There are some apples. Any — в вопросах и отрицаниях: Are there any…? There aren't any…",
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
            "There is two windows — ошибка; two → **there are**.",
            "Не путают there (конструкция) и their (их).",
            "После there is не ставят сразу множественное без are.",
        ],
        remember="Сначала there is/are, затем объект, затем место. Число = первое существительное.",
    ),
    "can-ability": lesson(
        "Can — модальный глагол умения, возможности и простой просьбы/разрешения. Он **не спрягается** по лицам и всегда требует «голый» инфинитив без to: can swim, не can to swim и не cans.",
        [
            rule(
                "Умение: can + V1",
                "Одна форма на все лица. Отрицание: can't / cannot. Вопрос: Can you swim? — can выходит вперёд, do/does не нужен.",
                [
                    ex("I can speak Spanish.", "Я умею говорить по-испански."),
                    ex("He can't drive.", "Он не умеет водить."),
                    ex("Can she play the piano?", "Она умеет играть на пианино?"),
                ],
                tables=[
                    table(
                        ["Тип", "Схема", "Пример"],
                        [
                            ["Утверждение", "can + **V1**", "She can swim."],
                            ["Отрицание", "can't + **V1**", "He can't drive."],
                            ["Вопрос", "Can + подлежащее + **V1**?", "Can you help?"],
                        ],
                    ),
                ],
                pairs=[
                    pair("He cans run.", "He can run.", "Формы cans не существует."),
                    pair("I can to cook.", "I can cook.", "После can частицы **to** нет."),
                ],
            ),
            rule(
                "Возможность и разрешение",
                "Can описывает то, что возможно в ситуации, и вежливо просит/даёт разрешение.",
                [
                    ex("You can leave early today.", "Сегодня можно уйти пораньше."),
                    ex("Can I use your phone?", "Можно взять твой телефон?"),
                    ex("I can hear music next door.", "Слышна музыка за стеной."),
                ],
            ),
        ],
        compare=[
            {"left": "I can cook.", "right": "I cook every day.", "note": "Can — про умение/возможность; Present Simple — про привычку."},
            {"left": "Can you help?", "right": "Do you help?", "note": "Просьба/умение через can; do — про обычное действие."},
        ],
        watch_out=[
            "I can to cook и He cans run — ошибки.",
            "Don't can — невозможно; отрицание только **can't / cannot**.",
            "Could появится позже для прошлого; на A1 can — про настоящее.",
        ],
        remember="Can не спрягается. После него голый инфинитив. Вопросы и not — через сам can.",
    ),
    "imperatives": lesson(
        "Повелительное наклонение даёт инструкцию, просьбу или запрет. Подлежащее you обычно не называют: форма глагола уже обращена к слушателю. Вежливость часто добавляют please; совместное действие — Let's.",
        [
            rule(
                "Утвердительный императив",
                "Берут базовую форму глагола. Please может стоять в начале или в конце.",
                [
                    ex("Take a seat, please.", "Присядьте, пожалуйста."),
                    ex("Turn left at the bank.", "Поверните налево у банка."),
                    ex("Switch off your phones.", "Выключите телефоны."),
                ],
                tables=[
                    table(
                        ["Смысл", "Схема", "Пример"],
                        [
                            ["Инструкция", "**V1** …", "Open the door."],
                            ["Запрет", "**Don't** + V1", "Don't touch."],
                            ["Вместе", "**Let's** + V1", "Let's start."],
                        ],
                    ),
                ],
            ),
            rule(
                "Запрет: Don't + V1",
                "Don't (do not) + базовая форма. Даже to be в императиве выглядит как Be careful / Don't be noisy.",
                [
                    ex("Don't touch the paintings.", "Не трогайте картины."),
                    ex("Don't be late.", "Не опаздывайте."),
                    ex("Be careful!", "Будьте осторожны!"),
                ],
            ),
            rule(
                "Let's — совместное действие",
                "Let's (= let us) + V1 предлагает общее действие. После let's частицы to нет.",
                [
                    ex("Let's start.", "Давайте начнём."),
                    ex("Let's go to the café.", "Давайте зайдём в кафе."),
                ],
                pairs=[
                    pair("Let's to eat.", "Let's eat.", "После let's нет to."),
                ],
            ),
        ],
        compare=[
            {"left": "Open the window.", "right": "Can you open the window?", "note": "Императив прямее; can you… мягче как просьба."},
        ],
        watch_out=[
            "To sit down и Let's to eat — ошибки: без to.",
            "Подлежащее you в нейтральной инструкции обычно опускают.",
            "Doesn't forget — для запрета нужно **Don't** forget.",
        ],
        remember="Инструкция = **V1**. Запрет = **Don't + V1**. Вместе = **Let's + V1**.",
    ),
    "question-words": lesson(
        "Специальный вопрос начинается с вопросительного слова (who, what, where…), затем обычно идёт вспомогательный глагол и подлежащее. Сначала выбирают смысл (где / кто / почему), потом собирают порядок слов.",
        [
            rule(
                "Базовый набор Wh-слов",
                "Каждое слово задаёт свой тип информации.",
                [
                    ex("Where do you live?", "Где ты живёшь?"),
                    ex("Whose bag is this?", "Чья это сумка?"),
                    ex("Which one do you prefer, tea or coffee?", "Какой вариант — чай или кофе?"),
                ],
                tables=[
                    table(
                        ["Слово", "Смысл"],
                        [
                            ["who", "кто"],
                            ["what", "что / какой"],
                            ["where", "где"],
                            ["when", "когда"],
                            ["why", "почему"],
                            ["how", "как"],
                            ["whose", "чей"],
                            ["which", "который из набора"],
                        ],
                    ),
                ],
            ),
            rule(
                "Порядок: Wh + aux + subject + verb",
                "What does she want? Where are you from?\n\nИсключение: who/what как подлежащее — Who called you? (без do, если who само подлежащее).",
                [
                    ex("What does she want?", "Чего она хочет?"),
                    ex("Who is that man?", "Кто этот мужчина?"),
                    ex("Why is he sad?", "Почему он грустный?"),
                ],
                pairs=[
                    pair("Where you live?", "Where do you live?", "Без вспомогательного глагола вопрос на A1 обычно неверен."),
                ],
            ),
            rule(
                "How + измерение",
                "How many + исчисляемые. How much + неисчисляемые. How often / how long — про частоту и длительность.",
                [
                    ex("How many apples do you want?", "Сколько яблок нужно?"),
                    ex("How much sugar is left?", "Сколько сахара осталось?"),
                    ex("How do you get to work?", "Как добираться на работу?"),
                ],
                tables=[
                    table(
                        ["Вопрос", "Тип существительного"],
                        [
                            ["**How many** …?", "исчисляемые (apples, tickets)"],
                            ["**How much** …?", "неисчисляемые (water, sugar, time)"],
                        ],
                    ),
                ],
            ),
        ],
        compare=[
            {"left": "Where do you live?", "right": "Where you live?", "note": "Без вспомогательного глагола вопрос на A1 обычно неверен."},
            {"left": "Who called you?", "right": "Who did you call?", "note": "Who-подлежащее vs who-дополнение."},
        ],
        watch_out=[
            "Where you live? / What you want? — нужны are/do/does.",
            "How much apples — ошибка; apples → **how many**.",
            "Whose ≠ who's (who is).",
        ],
        remember="Сначала Wh-смысл, затем вспомогательный глагол, затем подлежащее и смысловой глагол.",
    ),
    "prepositions-place": lesson(
        "Предлоги места отвечают на вопрос «где?». Ядро A1 — тройка **in / on / at**, плюс относительные under, behind, between, next to, opposite. Часто это фиксированные сочетания.",
        [
            rule(
                "In / on / at — короткая карта",
                "In — внутри объёма. On — на поверхности. At — точка на карте или место-назначение.",
                [
                    ex("The cat is in the box.", "Кот в коробке."),
                    ex("The keys are on the desk.", "Ключи на столе."),
                    ex("She's at the airport.", "Она в аэропорту."),
                ],
                tables=[
                    table(
                        ["Предлог", "Образ", "Типичные сочетания"],
                        [
                            ["**in**", "внутри", "in a room, in a city, in a box"],
                            ["**on**", "на поверхности", "on the table, on the wall, on the floor"],
                            ["**at**", "точка / место", "at the door, at the station, **at home**, **at work**"],
                        ],
                    ),
                ],
                pairs=[
                    pair("in home", "at home", "Фиксированное сочетание — at home."),
                    pair("in the table", "on the table", "На поверхности стола — on."),
                ],
            ),
            rule(
                "Относительные предлоги",
                "Under — под; behind — за; in front of — перед; between A and B — между; next to / beside — рядом; opposite — напротив.",
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
            "In home — ошибка; нужно **at home**.",
            "The book is in the table — обычно **on** the table.",
            "Opposite to the park на A1 чаще лишнее; достаточно opposite the park.",
        ],
        remember="Внутри — **in**. На поверхности — **on**. Точка / home / work — **at**.",
    ),
    "prepositions-time": lesson(
        "Та же тройка **in / on / at** работает со временем. Короткая схема: at — точные часы и некоторые «точки»; on — дни и даты; in — более длинные периоды и части дня (кроме night).",
        [
            rule(
                "Схема времени",
                "Слот предлога зависит от «размера» временного отрезка.",
                [
                    ex("The film starts at 8.15.", "Фильм начинается в 8:15."),
                    ex("See you on Friday.", "Увидимся в пятницу."),
                    ex("I was born in 1998.", "Я родился в 1998."),
                ],
                tables=[
                    table(
                        ["Предлог", "Когда", "Примеры"],
                        [
                            ["**at**", "часы и «точки»", "at 7.00, at noon, at midnight, **at night**, at the weekend (BrE)"],
                            ["**on**", "дни и даты", "on Monday, on 12 May, on my birthday"],
                            ["**in**", "периоды длиннее дня", "in July, in 2019, in the morning / afternoon / evening"],
                        ],
                    ),
                ],
                callouts=[
                    callout("Части дня с **in**, но **night** — с **at**: in the morning, at night.", "key"),
                ],
                pairs=[
                    pair("in Monday", "on Monday", "День недели → on."),
                    pair("on 8 p.m.", "at 8 p.m.", "Точное время → at."),
                    pair("in night", "at night", "Ночь — at night."),
                ],
            ),
        ],
        compare=[
            {"left": "at 9.00", "right": "on Monday", "note": "Часы vs день."},
            {"left": "in the morning", "right": "at night", "note": "Утро/день/вечер — in; ночь — at."},
        ],
        watch_out=[
            "In Monday и on 8 p.m. — перепутаны слоты.",
            "On the weekend чаще AmE; в британском учебном стиле — **at the weekend**.",
            "In night — ошибка; нужно **at night**.",
        ],
        remember="Часы и night/weekend (BrE) — **at**. Дни и даты — **on**. Месяцы, годы, morning/afternoon/evening — **in**.",
    ),
    "have-got": lesson(
        "Have got в британском английском — главный способ сказать о владении, семье и внешности на A1. По смыслу это не Present Perfect: got здесь часть устойчивой конструкции. В привычках вроде have breakfast got не ставят.",
        [
            rule(
                "Утверждение",
                "I/you/we/they **have got**. He/she/it **has got**. Краткие формы: I've got, she's got.",
                [
                    ex("I've got two sisters.", "У меня две сестры."),
                    ex("He has got brown eyes.", "У него карие глаза."),
                    ex("We've got a small flat.", "У нас небольшая квартира."),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Форма"],
                        [
                            ["I / you / we / they", "have got / 've got"],
                            ["he / she / it", "has got / 's got"],
                        ],
                    ),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "I haven't got / she hasn't got. Вопросы: Have you got…? Has she got…?\n\nСхема Do you have got? неверна: либо Have you got, либо Do you have (без got).",
                [
                    ex("I haven't got a car.", "У меня нет машины."),
                    ex("Has she got a minute?", "У неё есть минутка?"),
                    ex("Have you got any cash?", "Есть наличные?"),
                ],
                pairs=[
                    pair("Do you have got a pen?", "Have you got a pen?", "Не смешивают do-have и have got."),
                    pair("He haves got a bike.", "He has got a bike.", "Формы haves нет."),
                ],
            ),
            rule(
                "Have без got",
                "В устойчивых действиях got не нужен: have breakfast / lunch / dinner, have a shower, have a break.",
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
            "I have got hungry — ошибка; нужно **I am** hungry.",
            "Do you have got… — смешение двух схем.",
            "He haves got — формы haves нет; только **has got**.",
        ],
        remember="Владение и внешность: have/has got. Еда, душ, перерыв — have без got.",
    ),
    "past-simple-be": lesson(
        "В прошедшем to be имеет всего две формы: **was** и **were**. Вопросы и отрицания строятся без did — was/were сами работают как вспомогательные. Этот блок удобно освоить до Past Simple смысловых глаголов.",
        [
            rule(
                "Was и were",
                "Для you всегда were — и в единственном, и во множественном смысле.",
                [
                    ex("I was at home yesterday.", "Вчера я был дома."),
                    ex("They were tired.", "Они были усталыми."),
                    ex("You were right.", "Ты был прав."),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Прошедшее to be"],
                        [
                            ["I / he / she / it", "**was**"],
                            ["you / we / they", "**were**"],
                        ],
                    ),
                ],
                pairs=[
                    pair("I were ill.", "I was ill.", "I/he/she/it — только was."),
                    pair("Was you late?", "Were you late?", "Для you — were."),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "Wasn't / weren't. Were you late? Where was she? Did + were вместе не ставят.",
                [
                    ex("It wasn't expensive.", "Это было недорого."),
                    ex("Were they at the party?", "Они были на вечеринке?"),
                    ex("Was she at work on Monday?", "Она была на работе в понедельник?"),
                ],
                pairs=[
                    pair("Did you were at school?", "Were you at school?", "С was/were вспомогательный did не нужен."),
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
            "Was you… — нужно **Were you…**",
        ],
        remember="Прошедшее to be — **was/were** без did. I/he/she/it was; you/we/they were.",
    ),
    "past-simple-verbs": lesson(
        "Past Simple называет законченное действие в конкретном прошлом: yesterday, last week, in 2010, ago. Правильные глаголы берут **-ed**; неправильные — II форму (go—went). В вопросе и отрицании появляется **did**, а смысловой глагол возвращается к **V1**.",
        [
            rule(
                "Правильные глаголы + ed",
                "На письме схема одна; произношение -ed бывает /t/, /d/ или /ɪd/.",
                [
                    ex("I visited my aunt last Sunday.", "В прошлое воскресенье я навестил тётю."),
                    ex("They played football yesterday.", "Вчера они играли в футбол."),
                    ex("She studied French at school.", "В школе она учила французский."),
                ],
                tables=[
                    table(
                        ["Правило", "Пример"],
                        [
                            ["обычно **+ed**", "work → worked"],
                            ["немое e → **+d**", "live → lived"],
                            ["согласная + y → **ied**", "study → studied"],
                            ["удвоение согласной", "stop → stopped"],
                        ],
                    ),
                ],
            ),
            rule(
                "Неправильные: II форма",
                "Их учат списком, не правилом.",
                [
                    ex("She went to Rome in May.", "В мае она ездила в Рим."),
                    ex("We bought a ticket.", "Мы купили билет."),
                    ex("I lost my keys.", "Я потерял ключи."),
                ],
                tables=[
                    table(
                        ["V1", "II (Past)", "Смысл"],
                        [
                            ["go", "went", "идти / ехать"],
                            ["have", "had", "иметь"],
                            ["see", "saw", "видеть"],
                            ["buy", "bought", "покупать"],
                            ["make / take", "made / took", "делать / брать"],
                            ["come / get", "came / got", "приходить / получать"],
                        ],
                    ),
                ],
            ),
            rule(
                "Did в вопросе и отрицании",
                "Did уже несёт прошлое, поэтому went/saw после did не повторяют.",
                [
                    ex("Did you call her?", "Ты ей звонил?"),
                    ex("He didn't like the film.", "Ему не понравился фильм."),
                    ex("Did they arrive late?", "Они опоздали?"),
                ],
                tables=[
                    table(
                        ["Тип", "Схема"],
                        [
                            ["Утверждение", "V2 / V-ed"],
                            ["Отрицание", "didn't + **V1**"],
                            ["Вопрос", "Did + подлежащее + **V1**?"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Did you went home?", "Did you go home?", "После did снова базовая форма."),
                    pair("He didn't went.", "He didn't go.", "Didn't + V1, не II форма."),
                ],
                callouts=[
                    callout("Зеркало Present Simple: в утверждении — особая форма времени; в вопросе/отрицании время «переезжает» на вспомогательный глагол, а смысловой становится V1.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "She went home.", "right": "Did she go home?", "note": "Во II форме — утверждение; после did — снова V1."},
            {"left": "I saw the email yesterday.", "right": "I have seen the email.", "note": "Точная дата прошлого → Past Simple, не Perfect."},
        ],
        watch_out=[
            "Did you went? / He didn't went — частые ошибки; нужно **go**.",
            "После yesterday/last/ago не тянут Present Perfect.",
            "Не забывают II форму у неправильных в утверждении.",
        ],
        remember="Факт в прошлом + маркер времени = Past Simple. Вопрос/not: **did + V1**.",
    ),
    "going-to": lesson(
        "Be going to + V — основной способ говорить о будущем на A1: есть намерение или будущее уже «видно» по приметам. Нужны две детали: форма **to be** согласуется с подлежащим, после going to стоит голый инфинитив.",
        [
            rule(
                "Намерение и план",
                "Говорящий уже решил. Это не спонтанная идея «прямо сейчас», а заранее сложившееся намерение.",
                [
                    ex("We're going to move house.", "Мы собираемся переезжать."),
                    ex("I'm going to start a course.", "Я собираюсь начать курс."),
                    ex("He's going to study medicine.", "Он собирается учиться на врача."),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Схема"],
                        [
                            ["I", "am going to + **V1**"],
                            ["he / she / it", "is going to + **V1**"],
                            ["you / we / they", "are going to + **V1**"],
                        ],
                    ),
                ],
            ),
            rule(
                "Предсказание по примете",
                "Есть сигнал в настоящем: Look at those clouds — it's going to rain. Вывод о будущем опирается на то, что уже видно.",
                [
                    ex("Look at the sky! It's going to snow.", "Смотри на небо! Сейчас пойдёт снег."),
                    ex("She's going to win — she's much faster.", "Она победит: она намного быстрее."),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "I'm not going to tell him. Are you going to cook tonight? Без be конструкция ломается.",
                [
                    ex("Is he going to study medicine?", "Он собирается изучать медицину?"),
                    ex("I'm not going to stay.", "Я не собираюсь оставаться."),
                    ex("Are you going to cook tonight?", "Ты собираешься готовить сегодня вечером?"),
                ],
                pairs=[
                    pair("She going to be late.", "She's going to be late.", "Нужен am/is/are."),
                    pair("They're going to to buy milk.", "They're going to buy milk.", "После going to второе to не ставят."),
                ],
            ),
        ],
        compare=[
            {"left": "I'm going to the shop.", "right": "I'm going to buy milk.", "note": "Going to + место vs going to + глагол-намерение."},
            {"left": "We're going to visit Grandma.", "right": "We visit Grandma on Sundays.", "note": "План на будущее vs привычка Present Simple."},
        ],
        watch_out=[
            "I going to… — нужен **am/is/are**.",
            "They is going to help — they **are**.",
            "После going to не ставят to ещё раз: going to to buy — ошибка.",
        ],
        remember="План и очевидное будущее — **be going to + V1**. Be обязателен.",
    ),
    "adjectives-a1": lesson(
        "Прилагательное описывает качество человека или вещи и в английском **не меняется** по роду, числу и падежу: a red car, red cars. Главное на A1 — место (перед существительным или после связки) и то, что прилагательное не получает -s.",
        [
            rule(
                "Перед существительным",
                "Несколько прилагательных обычно идут в порядке: мнение → размер → возраст → цвет → материал.",
                [
                    ex("a lovely little old town", "милый маленький старый город"),
                    ex("a small black bag", "маленькая чёрная сумка"),
                    ex("They have a big house.", "У них большой дом."),
                ],
                tables=[
                    table(
                        ["Место", "Схема", "Пример"],
                        [
                            ["перед существительным", "adj + noun", "a **blue** car"],
                            ["после связки", "be / look / feel + adj", "She is **tall**."],
                        ],
                    ),
                ],
                pairs=[
                    pair("a car blue", "a blue car", "В атрибутивной позиции прилагательное перед существительным."),
                    pair("greens books", "green books", "Прилагательное не получает множественное -s."),
                ],
            ),
            rule(
                "После be / look / feel",
                "Здесь прилагательное — часть сказуемого. После look в значении «выглядеть» нужно именно прилагательное, не наречие на -ly.",
                [
                    ex("I feel tired.", "Я чувствую себя усталым."),
                    ex("She looks happy.", "Она выглядит счастливой."),
                    ex("He is a careful driver.", "Он аккуратный водитель."),
                ],
            ),
            rule(
                "Усилители very / really",
                "Very и really стоят перед прилагательным. Порядок: усилитель → прилагательное → (существительное).",
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
            "Прилагательное не получает множественное **-s**.",
            "Feel badly про самочувствие на A1 обычно заменяют на feel bad.",
        ],
        remember="Прилагательное неизменно. Место: перед словом или после be/look/feel. Усилитель — перед ним.",
    ),
}
