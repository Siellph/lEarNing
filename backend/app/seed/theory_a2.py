"""Enriched A2 grammar theory (Russian explanations, English examples).

Tone: impersonal / descriptive Russian. No direct address to the learner.
"""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

A2_THEORY = {
    "present-simple-vs-continuous": lesson(
        "На A1 времена учили по отдельности. На A2 нужно выбирать: привычка и постоянный факт — **Present Simple**; действие в развитии или временный период — **Present Continuous**.\n\nРусское «я работаю» покрывает оба смысла, поэтому опора — не дословный перевод, а вопрос: так бывает вообще или именно сейчас?",
        [
            rule(
                "Present Simple: каркас жизни",
                "Привычки, расписания, факты и постоянная работа. Это «как устроено», а не «что происходит на глазах».",
                [
                    ex("She teaches maths at a college.", "Она преподаёт математику в колледже (постоянно)."),
                    ex("The ferry leaves at 7.15.", "Паром отходит в 7.15 (расписание)."),
                    ex("On Sundays she visits her grandparents.", "По воскресеньям она навещает бабушку и дедушку."),
                ],
                tables=[
                    table(
                        ["Время", "Форма", "Типичные маркеры"],
                        [
                            ["Present Simple", "V1 / he-she-it + **-s**", "always, usually, every day, on Mondays"],
                            ["Present Continuous", "am/is/are + **-ing**", "now, at the moment, today, this week, Look!"],
                        ],
                    ),
                ],
            ),
            rule(
                "Present Continuous: сейчас и временно",
                "Действие в момент речи, временная ситуация или изменение.",
                [
                    ex("I'm packing a suitcase at the moment.", "Я сейчас собираю чемодан."),
                    ex("He's staying with his aunt this month.", "В этом месяце он живёт у тёти."),
                    ex("This week we are staying late because of a deadline.", "На этой неделе мы задерживаемся из‑за дедлайна."),
                ],
                pairs=[
                    pair("I work now.", "I'm working now.", "Если действие разворачивается на глазах — Continuous."),
                ],
            ),
            rule(
                "Глаголы состояния",
                "Know, like, love, hate, want, need, believe, belong, own, understand обычно не ставят в Continuous. Have в значении «владеть» — Simple; have dinner / have a shower — может быть Continuous.",
                [
                    ex("I understand the rule now.", "Я сейчас понимаю правило (не am understanding)."),
                    ex("We're having lunch, can I call you later?", "Мы обедаем — здесь have = есть."),
                    ex("I don't like this soup.", "Мне не нравится этот суп."),
                ],
                callouts=[
                    callout("He is knowing / I am wanting на A2 почти всегда ошибка: состояния держат в Simple.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "I live in Porto.", "right": "I'm living with friends until May.", "note": "Постоянный адрес vs временное жильё."},
            {"left": "She works nights.", "right": "She's working a day shift today.", "note": "Обычный график vs исключение сегодня."},
        ],
        watch_out=[
            "Не I work now, если действие разворачивается на глазах: **I'm working** now.",
            "Не He is knowing / I am wanting — это состояния.",
            "В вопросе Continuous нужен be, не do: **Are** you waiting?",
        ],
        remember="Привычка и факт — Simple. Сейчас и временно — Continuous. Состояния почти всегда Simple.",
    ),
    "past-continuous": lesson(
        "Past Continuous (**was/were + V-ing**) показывает процесс в конкретной точке прошлого. Часто он рисует фон, а Past Simple сообщает, что его прервало.",
        [
            rule(
                "Форма was/were + V-ing",
                "Как и в Present Continuous, нужен вспомогательный be — уже в прошедшем.",
                [
                    ex("At 9 p.m. I was still editing the slides.", "В 9 вечера я всё ещё правил слайды."),
                    ex("They weren't listening to the announcement.", "Они не слушали объявление."),
                    ex("Were you sleeping when I texted?", "Ты спал, когда я написал?"),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Форма"],
                        [
                            ["I / he / she / it", "**was** + V-ing"],
                            ["you / we / they", "**were** + V-ing"],
                        ],
                    ),
                ],
                pairs=[
                    pair("I were working.", "I was working.", "I/he/she/it — was."),
                    pair("They was waiting.", "They were waiting.", "They — were."),
                ],
            ),
            rule(
                "Прерванное действие",
                "Длительное действие — Continuous; короткое событие — Past Simple. While чаще с Continuous; when часто с прерывающим Simple.",
                [
                    ex("I was boiling pasta when the lights went out.", "Я варил пасту, когда погас свет."),
                    ex("While we were queuing, it started to rain.", "Пока мы стояли в очереди, начался дождь."),
                ],
                tables=[
                    table(
                        ["Роль", "Время", "Пример"],
                        [
                            ["фон / процесс", "Past Continuous", "I was boiling pasta…"],
                            ["точка-событие", "Past Simple", "…when the lights went out."],
                        ],
                    ),
                ],
            ),
            rule(
                "Два параллельных процесса",
                "Если оба действия длились одновременно, оба могут быть в Continuous. Законченные факты без «фона» — только Past Simple.",
                [
                    ex("Mum was cooking while Dad was laying the table.", "Мама готовила, а папа накрывал на стол."),
                    ex("She sent the file and left.", "Она отправила файл и ушла (два факта, не процесс)."),
                ],
            ),
        ],
        compare=[
            {"left": "I watched a documentary yesterday.", "right": "I was watching a documentary at 10 last night.", "note": "Факт о вечере vs процесс в конкретный час."},
        ],
        watch_out=[
            "Не I were / they was.",
            "Не ставят Continuous на короткие завершённые действия вроде «чашка разбилась».",
            "When he was arriving звучит странно, если прибытие — точка; лучше When he **arrived**.",
        ],
        remember="**Was/were + -ing** = процесс в прошлом. Точка-событие — Past Simple.",
    ),
    "present-perfect-intro": lesson(
        "Present Perfect связывает прошлое с настоящим. На A2 достаточно трёх опор: опыт без даты, результат, который виден сейчас, и период, который ещё не закрыт (today, this week, since, for).\n\nЕсли есть точная дата прошлого — обычно Past Simple.",
        [
            rule(
                "Форма have/has + V3",
                "Смысловой глагол — в третьей форме (sent, seen, finished).",
                [
                    ex("I've sent the email.", "Я отправил письмо (и это важно сейчас)."),
                    ex("Has she finished the report?", "Она закончила отчёт?"),
                    ex("We haven't met before.", "Мы раньше не встречались."),
                ],
                tables=[
                    table(
                        ["Подлежащее", "Форма"],
                        [
                            ["I / you / we / they", "**have** + V3"],
                            ["he / she / it", "**has** + V3"],
                        ],
                    ),
                ],
                pairs=[
                    pair("He have finished.", "He has finished.", "Для he/she/it — has."),
                    pair("I've seen her yesterday.", "I saw her yesterday.", "Точная дата прошлого → Past Simple."),
                ],
            ),
            rule(
                "Опыт и результат сейчас",
                "Опыт без даты: Have you ever…? I've never…. Результат, который влияет на момент речи: I've lost my keys (поэтому нельзя открыть дверь).",
                [
                    ex("Have you ever tried sushi?", "Ты когда‑нибудь пробовал суши?"),
                    ex("I've lost my keys — I can't open the door.", "Я потерял ключи — не могу открыть дверь."),
                ],
            ),
            rule(
                "Already, yet, just, ever, never",
                "Эти маркеры помогают выбрать Perfect, но не сильнее явной даты прошлого.",
                [
                    ex("I've just arrived.", "Я только что приехал."),
                    ex("Have you finished yet?", "Ты уже закончил?"),
                    ex("She's never been abroad.", "Она никогда не была за границей."),
                ],
                tables=[
                    table(
                        ["Маркер", "Типичное место", "Смысл"],
                        [
                            ["just", "утверждение", "только что"],
                            ["already", "утверждение", "уже"],
                            ["yet", "вопрос / отрицание", "уже / ещё"],
                            ["ever / never", "опыт", "когда‑либо / никогда"],
                        ],
                    ),
                ],
            ),
        ],
        compare=[
            {"left": "I've sent the email.", "right": "I sent the email yesterday.", "note": "Результат сейчас vs закрытая дата."},
        ],
        watch_out=[
            "I've seen her yesterday — ошибка; нужна Past Simple.",
            "He have finished — нужно **has**.",
            "После yet в отрицании: I haven't finished **yet**.",
        ],
        remember="**Have/has + V3**. Опыт и результат сейчас. Точная дата прошлого — не сюда.",
    ),
    "will-vs-going-to": lesson(
        "Будущее на A2 выбирают не по календарю, а по ситуации. **Will** — решение и обещание в момент речи, предложение помощи, прогноз «вообще». **Be going to** — уже принятый план или предсказание по примете, которую видно сейчас.",
        [
            rule(
                "Will / won't",
                "Will + V1 для всех лиц. Часто: спонтанное решение, обещание, предложение помощи, прогноз без явной приметы.",
                [
                    ex("It's cold in here. I'll close the window.", "Холодно. Я закрою окно (решил сейчас)."),
                    ex("I won't tell anyone.", "Никому не скажу."),
                    ex("I think it'll be fine.", "Думаю, всё будет нормально."),
                ],
                tables=[
                    table(
                        ["Сигнал", "Форма", "Пример"],
                        [
                            ["решил сейчас / обещание", "**will** + V1", "I'll help you."],
                            ["план уже есть / видна примета", "**be going to** + V1", "We're going to move."],
                        ],
                    ),
                ],
            ),
            rule(
                "Be going to",
                "Am/is/are + going to + V1. План уже есть или есть примета в настоящем.",
                [
                    ex("We're going to move in June.", "Мы переезжаем в июне (план)."),
                    ex("Look at those clouds — it's going to rain.", "Смотри на тучи — сейчас пойдёт дождь."),
                ],
                pairs=[
                    pair("She going to leave.", "She's going to leave.", "Без be конструкция не собирается."),
                    pair("I will to go.", "I will go.", "После will нет to."),
                ],
            ),
            rule(
                "Shall в британском стиле",
                "Shall I…? / Shall we…? — вежливое предложение действия. На A2 это полезный шаблон, но will остаётся основной формой будущего.",
                [
                    ex("Shall I carry that bag?", "Давай я понесу эту сумку?"),
                    ex("Shall we start?", "Начнём?"),
                ],
            ),
        ],
        compare=[
            {"left": "I'll call her now.", "right": "I'm going to call her tonight.", "note": "Решение сейчас vs уже задуманный план."},
        ],
        watch_out=[
            "Не I will to go / she wills.",
            "Без be нет going to: не She going to leave.",
            "Не смешивают will и going to в одной клетке без причины.",
        ],
        remember="Решил сейчас / обещание — **will**. Уже планировал или видна примета — **going to**.",
    ),
    "comparatives": lesson(
        "Сравнительная степень показывает разницу между двумя людьми или вещами: A is … **than** B. Короткие прилагательные обычно берут **-er**, длинные — **more**. Отдельно: good → better, bad → worse.",
        [
            rule(
                "Как образуется сравнение",
                "После сравнительной формы почти всегда нужен **than**.",
                [
                    ex("This bag is cheaper than that one.", "Эта сумка дешевле той."),
                    ex("This film is more interesting than the book.", "Фильм интереснее книги."),
                    ex("His English is better than mine.", "Его английский лучше моего."),
                ],
                tables=[
                    table(
                        ["Тип прилагательного", "Сравнительная форма", "Пример"],
                        [
                            ["короткое (1 слог, многие на -y)", "**-er**", "old → older, happy → happier"],
                            ["длинное", "**more** + adj", "interesting → more interesting"],
                            ["особые", "отдельные формы", "good → **better**, bad → **worse**"],
                        ],
                    ),
                ],
                pairs=[
                    pair("more happier", "happier", "Не смешивают more и -er."),
                    pair("more better", "better", "Better уже сравнительная форма."),
                ],
            ),
            rule(
                "As … as и less",
                "Равенство: as + adj + as. Меньшая степень: less + adj (+ than). Not as … as — мягкое «не такой … как».",
                [
                    ex("She is as tall as her brother.", "Она такого же роста, как брат."),
                    ex("This task is less difficult than the last one.", "Это задание менее сложное, чем прошлое."),
                ],
            ),
        ],
        compare=[
            {"left": "cheaper than", "right": "more expensive than", "note": "-er для коротких; more для длинных."},
        ],
        watch_out=[
            "More happier / more better — ошибки.",
            "После сравнительной обычно нужен **than**, не then.",
            "Во второй части часто нужен ориентир: than mine / than that one.",
        ],
        remember="**-er** или **more**, затем **than**. Равенство — as … as. Good → better.",
    ),
    "superlatives": lesson(
        "Превосходная степень выделяет один объект из группы: **the** … -est / **the most** …. Почти всегда нужен артикль the. Дальше уточняют место (**in**) или набор (**of**).",
        [
            rule(
                "Форма the + -est / the most",
                "Без the форма обычно выглядит неполной.",
                [
                    ex("She is the tallest in her class.", "Она самая высокая в классе."),
                    ex("This is the most expensive option.", "Это самый дорогой вариант."),
                    ex("That was the best day of the trip.", "Это был лучший день поездки."),
                ],
                tables=[
                    table(
                        ["Тип", "Превосходная", "Пример"],
                        [
                            ["короткое", "**the** + -est", "the oldest, the happiest"],
                            ["длинное", "**the most** + adj", "the most interesting"],
                            ["особые", "отдельные формы", "the **best**, the **worst**"],
                        ],
                    ),
                ],
                pairs=[
                    pair("most interestingest", "the most interesting", "Не смешивают most и -est."),
                    pair("one of the best film", "one of the best films", "После one of the — множественное существительное."),
                ],
            ),
            rule(
                "In и of",
                "In — для места и группы-контейнера. Of — для набора единиц.",
                [
                    ex("He is the youngest in the family.", "Он самый младший в семье."),
                    ex("This is the oldest of the three bridges.", "Это самый старый из трёх мостов."),
                ],
                tables=[
                    table(
                        ["Предлог", "Роль", "Пример"],
                        [
                            ["**in**", "место / группа-контейнер", "the tallest in the class"],
                            ["**of**", "набор единиц", "the oldest of the three"],
                        ],
                    ),
                ],
            ),
        ],
        compare=[
            {"left": "taller than Sam", "right": "the tallest in the room", "note": "Сравнение двоих vs выбор из группы."},
        ],
        watch_out=[
            "Most interestingest — нельзя смешивать more/most и -est.",
            "One of the best film — нужно **films**.",
            "Не опускают **the** без особой идиомы.",
        ],
        remember="**The** + -est / the most. Место — in, набор — of. Good → the best.",
    ),
    "countable-uncountable": lesson(
        "Исчисляемые существительные можно посчитать и поставить во множественное: a ticket — tickets. Неисчисляемые в общем смысле не берут **a/an** и не получают **-s**: information, advice, furniture, luggage. От типа зависит выбор much/many и артикля.",
        [
            rule(
                "Два типа существительных",
                "Тип — не «перевод», а грамматическое поведение слова.",
                [
                    ex("I bought two tickets.", "Я купил два билета."),
                    ex("I need some advice.", "Мне нужен совет."),
                    ex("There is milk in the fridge.", "В холодильнике есть молоко."),
                ],
                tables=[
                    table(
                        ["", "Исчисляемые", "Неисчисляемые"],
                        [
                            ["a/an", "да (a ticket)", "нет (не an advice)"],
                            ["множественное -s", "tickets", "обычно нет"],
                            ["many / few", "many tickets", "—"],
                            ["much / little", "—", "much information"],
                            ["пример", "chair, idea, ticket", "milk, news, advice, furniture"],
                        ],
                    ),
                ],
                pairs=[
                    pair("an advice", "some advice / a piece of advice", "Advice неисчисляемое."),
                    pair("informations", "information", "Без обычного множественного."),
                ],
            ),
            rule(
                "Слова-ловушки",
                "Information, advice, furniture, luggage, homework, weather — неисчисляемые на A2. News согласуется как единственное: The news **is** good. Hair в общем смысле часто неисчисляемое; a hair — один волос.",
                [
                    ex("The furniture is new.", "Мебель новая."),
                    ex("Her hair is short.", "У неё короткие волосы."),
                    ex("Can I have a piece of advice?", "Можно один совет?"),
                ],
            ),
        ],
        compare=[
            {"left": "a ticket / many tickets", "right": "some information / much information", "note": "Штуки vs масса/абстракция."},
        ],
        watch_out=[
            "An advice / informations — ошибки.",
            "News are — обычно The news **is**.",
            "Much tickets — нужно **many** tickets.",
        ],
        remember="Можно посчитать штуки — a/an и -s. Вещество и абстракция — без -s и часто без a/an.",
    ),
    "quantifiers-a2": lesson(
        "Квантификаторы говорят о количестве без точной цифры. Выбор зависит от типа существительного и от того, утверждение это, вопрос или отрицание.",
        [
            rule(
                "Some, any, a lot of",
                "Some — обычно утверждение (и вежливые предложения). Any — вопросы и отрицания. A lot of / lots of — и с исчисляемыми, и с неисчисляемыми.",
                [
                    ex("I have some questions.", "У меня есть несколько вопросов."),
                    ex("Have you got any milk?", "Есть молоко?"),
                    ex("We have a lot of work today.", "Сегодня у нас много работы."),
                ],
            ),
            rule(
                "Much, many, few, little",
                "Many/few — штуки. Much/little — масса. A few / a little — «есть немного»; few / little — «мало» с негативным оттенком.",
                [
                    ex("How many apples do you need?", "Сколько яблок нужно?"),
                    ex("There isn't much time.", "Времени мало."),
                    ex("I have a few friends here.", "У меня здесь есть несколько друзей."),
                ],
                tables=[
                    table(
                        ["", "Исчисляемые", "Неисчисляемые"],
                        [
                            ["много (нейтр.)", "many / a lot of", "much / a lot of"],
                            ["немного есть", "**a few**", "**a little**"],
                            ["мало (негативно)", "**few**", "**little**"],
                        ],
                    ),
                ],
                pairs=[
                    pair("much apples", "many apples", "Apples — исчисляемые."),
                    pair("many rice", "much rice / a lot of rice", "Rice — неисчисляемое."),
                ],
                callouts=[
                    callout("**Few** и **a few** — не синонимы по тону: few friends ≈ почти нет друзей; a few friends ≈ несколько друзей есть.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "a few eggs", "right": "a little milk", "note": "Штуки vs неисчисляемое."},
            {"left": "few friends", "right": "a few friends", "note": "Мало (почти нет) vs немного есть."},
        ],
        watch_out=[
            "Much apples / many rice — перепутан тип существительного.",
            "Few и a few — не синонимы по тону.",
            "Some в грубом отрицании обычно не ставят: I haven't got **any**.",
        ],
        remember="Many/few — штуки. Much/little — масса. A few / a little — «есть немного».",
    ),
    "modals-must-should-have-to": lesson(
        "Три модальных контура A2: обязанность, совет и запрет. Must и have to близки по силе обязанности, но источник разный. Should мягче. **Mustn't** и **don't have to** — почти противоположны.",
        [
            rule(
                "Must, have to, should",
                "Must часто — внутреннее правило или сильное ощущение говорящего. Have to — внешнее требование. Should — совет, не жёсткий приказ.",
                [
                    ex("You must keep this door closed.", "Эту дверь нужно держать закрытой (жёсткое правило)."),
                    ex("I have to wear a badge at work.", "На работе я обязан носить бейдж."),
                    ex("You should see a doctor.", "Стоит сходить к врачу."),
                ],
                tables=[
                    table(
                        ["Смысл", "Форма", "Пример"],
                        [
                            ["сильная обязанность / правило", "**must** + V1", "You must stop."],
                            ["внешнее требование", "**have/has to** + V1", "She has to leave."],
                            ["совет", "**should** + V1", "You should rest."],
                        ],
                    ),
                ],
            ),
            rule(
                "Mustn't vs don't have to",
                "Это одна из главных ловушек уровня: запрет и отсутствие обязанности выглядят похоже в русском, но в английском это разные схемы.",
                [
                    ex("You mustn't park here.", "Здесь нельзя парковаться."),
                    ex("You don't have to come if you're tired.", "Можно не приходить, если устал."),
                ],
                tables=[
                    table(
                        ["Форма", "Смысл"],
                        [
                            ["**mustn't**", "нельзя, запрещено"],
                            ["**don't / doesn't have to**", "обязанности нет; можно не делать"],
                        ],
                    ),
                ],
                pairs=[
                    pair("You mustn't to park here.", "You mustn't park here.", "После must/should нет to."),
                    pair("She have to leave.", "She has to leave.", "Для he/she/it — has to."),
                ],
                callouts=[
                    callout("Mustn't ≠ don't have to. Первое запрещает действие; второе снимает обязанность.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "You mustn't tell anyone.", "right": "You don't have to tell anyone.", "note": "Запрет vs отсутствие обязанности."},
        ],
        watch_out=[
            "Must to / should to — после модальных нет to (кроме have to).",
            "Не путают mustn't и don't have to.",
            "Has to для he/she/it: She **has to** leave early.",
        ],
        remember="Must/have to — обязанность. Should — совет. Mustn't — нельзя. Don't have to — можно не делать.",
    ),
    "zero-first-conditional": lesson(
        "Условные на A2 пока про два случая: общий закон (**Zero**) и реальное будущее (**First**). В части с if на этих уровнях не ставят will: там Present Simple.",
        [
            rule(
                "Zero и First рядом",
                "Обе конструкции начинаются с if + Present. Разница — в главной части.",
                [
                    ex("If you heat ice, it melts.", "Если нагреть лёд, он тает."),
                    ex("If it rains, we'll take a taxi.", "Если пойдёт дождь, возьмём такси."),
                    ex("Unless you hurry, you'll miss the bus.", "Если не поторопишься, опоздаешь на автобус."),
                ],
                tables=[
                    table(
                        ["Тип", "If-часть", "Главная часть", "Смысл"],
                        [
                            ["Zero", "Present Simple", "Present Simple", "закон / привычка"],
                            ["First", "Present Simple", "**will** + V1", "реальное будущее"],
                        ],
                    ),
                ],
                pairs=[
                    pair("If it will rain, we'll stay.", "If it rains, we'll stay.", "В if-части на A2 — Present, не will."),
                ],
                callouts=[
                    callout("Will — только в главной части First Conditional. В if-части will обычно ошибка уровня.", "key"),
                ],
            ),
            rule(
                "Unless и порядок частей",
                "Unless ≈ if … not. Часть с if/unless может стоять второй: We'll stay inside if it rains. Запятая нужна, когда if-часть первая.",
                [
                    ex("We'll stay inside if it rains.", "Останемся дома, если пойдёт дождь."),
                    ex("If she passes, she'll call us.", "Если она сдаст, она нам позвонит."),
                ],
            ),
        ],
        compare=[
            {"left": "If you heat ice, it melts.", "right": "If it rains, we'll take a taxi.", "note": "Закон/привычка vs реальное будущее."},
        ],
        watch_out=[
            "If it will rain — на A2 ошибка; в if-части Present.",
            "Не ставят will в обе части First Conditional без нужды.",
            "Unless уже содержит отрицание: не unless you don't…",
        ],
        remember="If + Present. Факт — Present в обеих частях. Реальное будущее — will только в главной.",
    ),
    "relative-who-which-that": lesson(
        "Относительные местоимения присоединяют пояснение к существительному. **Who** — люди. **Which** — вещи и животные. **That** — в определяющих придаточных для людей и вещей. **Where** — места.",
        [
            rule(
                "Who, which, that",
                "Who не ставят к вещам; which не используют для людей в стандартном A2-стиле. That часто заменяет who/which в определяющих придаточных.",
                [
                    ex("The woman who called you is my boss.", "Женщина, которая тебе звонила, — мой начальник."),
                    ex("The book which I bought is excellent.", "Книга, которую я купил, отличная."),
                    ex("The film that we saw was long.", "Фильм, который мы смотрели, был длинным."),
                ],
                tables=[
                    table(
                        ["Слово", "К чему относится"],
                        [
                            ["**who**", "люди"],
                            ["**which**", "вещи / животные"],
                            ["**that**", "люди и вещи (определяющее придаточное)"],
                            ["**where**", "места"],
                            ["**whose**", "чей"],
                        ],
                    ),
                ],
                pairs=[
                    pair("the man which helped me", "the man who helped me", "Для людей — who/that."),
                ],
            ),
            rule(
                "Пропуск дополнения",
                "Если местоимение — дополнение, его можно опустить: The film (that) we saw was long.",
                [
                    ex("The film we saw was long.", "То же без that — нормально."),
                    ex("This is the café where we met.", "Это кафе, где мы встретились."),
                    ex("The man whose car was stolen called the police.", "Мужчина, чью машину украли, вызвал полицию."),
                ],
            ),
        ],
        compare=[
            {"left": "the teacher who helped me", "right": "the map which helped me", "note": "Люди — who; вещи — which/that."},
        ],
        watch_out=[
            "The man which… — для людей лучше who/that.",
            "Не ставят лишнее what вместо that/which в этом типе придаточных.",
            "Два подлежащих подряд без относительного слова — ошибка.",
        ],
        remember="Люди — who. Вещи — which/that. Дополнение можно опустить. Места — where.",
    ),
    "used-to": lesson(
        "Used to + V1 описывает прошлую привычку или состояние, которых сейчас уже нет. Это не то же самое, что **be used to** (привыкнуть к чему‑то) и не Past Simple про одноразовый факт.",
        [
            rule(
                "Used to: форма и смысл",
                "Смысл: раньше да, сейчас иначе. В утверждении — used to; в вопросе и отрицании с did пишут **use to**.",
                [
                    ex("I used to play tennis every weekend.", "Раньше я каждое выходное играл в теннис."),
                    ex("I didn't use to like coffee.", "Раньше мне не нравился кофе."),
                    ex("Did you use to walk to school?", "Ты раньше ходил в школу пешком?"),
                ],
                tables=[
                    table(
                        ["Тип", "Форма"],
                        [
                            ["Утверждение", "**used to** + V1"],
                            ["Отрицание", "didn't **use to** + V1"],
                            ["Вопрос", "Did … **use to** + V1?"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Did you used to smoke?", "Did you use to smoke?", "После did — use to."),
                    pair("I used to living there.", "I used to live there.", "Used to + V1, не -ing."),
                ],
            ),
            rule(
                "Не путать с be used to",
                "Be used to + noun/-ing = привычен к чему‑то сейчас. Get used to — привыкать. Это другой смысл.",
                [
                    ex("I'm used to getting up early.", "Я привык рано вставать."),
                    ex("You'll get used to the noise.", "Ты привыкнешь к шуму."),
                    ex("She used to live in York.", "Раньше она жила в Йорке."),
                ],
                callouts=[
                    callout("I used to live = раньше жил. I'm used to living = сейчас это привычно. Путаница часто из‑за похожей орфографии.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "I used to smoke.", "right": "I'm used to noise.", "note": "Прошлая привычка vs привычность сейчас."},
        ],
        watch_out=[
            "I used to living — нужно I used to **live** ИЛИ I'm used to living.",
            "В вопросе с did — **use to**, не used to.",
            "Used to не ставят для одноразового прошлого факта с датой без идеи «больше не так».",
        ],
        remember="**Used to + V1** = раньше да, сейчас нет. В did-вопросе — use to.",
    ),
    "passive-present-past": lesson(
        "В пассиве важен объект и то, что с ним сделали, а не деятель. Формула: **be** нужного времени + **V3**. Present: am/is/are + V3. Past: was/were + V3. By добавляют только если деятель важен.",
        [
            rule(
                "Present и Past Passive",
                "Выбор am/is/are или was/were зависит от подлежащего-пациенса и времени.",
                [
                    ex("English is spoken here.", "Здесь говорят по-английски."),
                    ex("The office is cleaned every day.", "Офис убирают каждый день."),
                    ex("The emails were sent yesterday.", "Письма отправили вчера."),
                ],
                tables=[
                    table(
                        ["Время", "Схема", "Пример"],
                        [
                            ["Present Simple Passive", "am/is/are + **V3**", "The room is cleaned."],
                            ["Past Simple Passive", "was/were + **V3**", "The window was broken."],
                        ],
                    ),
                ],
                pairs=[
                    pair("The room does cleaned.", "The room is cleaned.", "В пассиве do/does не нужен."),
                    pair("The emails was sent.", "The emails were sent.", "Множественное подлежащее → were."),
                ],
            ),
            rule(
                "By и когда пассив уместен",
                "By + деятель — только если он важен. Если деятель неизвестен, очевиден или неважен — by не нужен.",
                [
                    ex("The mural was painted by a local artist.", "Фреску написал местный художник."),
                    ex("My bike was stolen.", "Мой велосипед украли (кто — неважно)."),
                ],
            ),
        ],
        compare=[
            {"left": "Someone stole my bike.", "right": "My bike was stolen.", "note": "Актив с someone vs пассив с объектом в фокусе."},
        ],
        watch_out=[
            "Was steal / is speak — нужна **III форма**.",
            "Не ставят do/does в пассивный Present: The room is cleaned, не does cleaned.",
            "Согласуют be с новым подлежащим: emails **were**, не was.",
        ],
        remember="**Be + V3**. Сейчас — am/is/are. Прошлое — was/were. By — только если деятель важен.",
    ),
    "adverbs-frequency-manner": lesson(
        "Наречия частоты говорят, как часто бывает действие; наречия образа действия — как оно выполняется. На A2 критичен порядок: частота обычно **до** смыслового глагола и **после** be; -ly чаще после глагола или в конце.",
        [
            rule(
                "Частота и место",
                "Always, usually, often, sometimes, rarely, never.",
                [
                    ex("She often cooks at home.", "Она часто готовит дома."),
                    ex("She is never late.", "Она никогда не опаздывает."),
                    ex("Do you often travel for work?", "Ты часто ездишь по работе?"),
                ],
                tables=[
                    table(
                        ["Тип глагола", "Место частоты", "Пример"],
                        [
                            ["смысловой глагол", "**перед** глаголом", "She **often** cooks."],
                            ["be", "**после** be", "She is **never** late."],
                            ["вопрос с do/does", "после подлежащего", "Do you **often** travel?"],
                        ],
                    ),
                ],
                pairs=[
                    pair("She often is late.", "She is often late.", "После be частота идёт сразу за ним."),
                ],
            ),
            rule(
                "Образ действия и особые формы",
                "Many manner adverbs end in -ly. Good → **well**. Hard, fast, late, early часто без -ly. Hardly — почти не; это не «тяжёло».",
                [
                    ex("He spoke quietly.", "Он говорил тихо."),
                    ex("She speaks English well.", "Она хорошо говорит по-английски."),
                    ex("I hardly sleep before exams.", "Перед экзаменами я почти не сплю."),
                ],
                tables=[
                    table(
                        ["Прилагательное / база", "Наречие", "Смысл"],
                        [
                            ["good", "**well**", "хорошо"],
                            ["hard", "hard", "усердно"],
                            ["hard", "**hardly**", "почти не"],
                            ["late", "late / lately", "поздно / в последнее время"],
                        ],
                    ),
                ],
                callouts=[
                    callout("He works **hard** ≠ He **hardly** works. Первое — усердно; второе — почти не работает.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "She is often tired.", "right": "She often feels tired.", "note": "После be vs перед смысловым глаголом."},
            {"left": "He works hard.", "right": "He hardly works.", "note": "Усердно vs почти не."},
        ],
        watch_out=[
            "She often is late — обычно She **is often** late.",
            "He speaks English good — нужно **well**.",
            "Hardly ≠ hard.",
        ],
        remember="Частота: до глагола, после be. Образ: -ly после действия. Well, hard, late — особые.",
    ),
}
