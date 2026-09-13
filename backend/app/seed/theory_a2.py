"""Enriched A2 grammar theory (Russian explanations, English examples)."""

from app.seed.helpers import ex, lesson, rule

A2_THEORY = {
    "present-simple-vs-continuous": lesson(
        "На A1 времена учили по отдельности. На A2 нужно выбирать: привычка и постоянный факт — Present Simple; действие в развитии или временный период — Present Continuous. Русское «я работаю» покрывает оба смысла, поэтому опора — не дословный перевод, а вопрос: так бывает вообще или именно сейчас?",
        [
            rule(
                "Present Simple: каркас жизни",
                "I/you/we/they + V1; he/she/it + -s. Используйте для привычек, расписаний, фактов и постоянной работы. Маркеры: always, usually, every day, on Mondays. Это «как устроено», а не «что происходит на глазах».",
                [
                    ex("She teaches maths at a college.", "Она преподаёт математику в колледже (постоянно)."),
                    ex("The ferry leaves at 7.15.", "Паром отходит в 7.15 (расписание)."),
                    ex("On Sundays she visits her grandparents.", "По воскресеньям она навещает бабушку и дедушку."),
                ],
            ),
            rule(
                "Present Continuous: сейчас и временно",
                "Am/is/are + V-ing. Действие в момент речи, временная ситуация или изменение. Маркеры: now, at the moment, today, this week, Look! Listen!",
                [
                    ex("I'm packing a suitcase at the moment.", "Я сейчас собираю чемодан."),
                    ex("He's staying with his aunt this month.", "В этом месяце он живёт у тёти."),
                    ex("This week we are staying late because of a deadline.", "На этой неделе мы задерживаемся из‑за дедлайна."),
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
            ),
        ],
        compare=[
            {"left": "I live in Porto.", "right": "I'm living with friends until May.", "note": "Постоянный адрес vs временное жильё."},
            {"left": "She works nights.", "right": "She's working a day shift today.", "note": "Обычный график vs исключение сегодня."},
        ],
        watch_out=[
            "Не I work now, если действие разворачивается на глазах: I'm working now.",
            "Не He is knowing / I am wanting — это состояния.",
            "В вопросе Continuous нужен be, не do: Are you waiting?",
        ],
        remember="Привычка и факт — Simple. Сейчас и временно — Continuous. Состояния почти всегда Simple.",
    ),
    "past-continuous": lesson(
        "Past Continuous (was/were + V-ing) показывает процесс в конкретной точке прошлого. Часто он рисует фон, а Past Simple сообщает, что его прервало. Русское «я смотрел фильм, когда…» как раз про эту пару времён.",
        [
            rule(
                "Форма was/were + V-ing",
                "I/he/she/it was + V-ing. You/we/they were + V-ing. Отрицание: wasn't / weren't. Вопрос: Was she sleeping? Were you driving? Как и в Present Continuous, нужен вспомогательный be.",
                [
                    ex("At 9 p.m. I was still editing the slides.", "В 9 вечера я всё ещё правил слайды."),
                    ex("They weren't listening to the announcement.", "Они не слушали объявление."),
                    ex("Were you sleeping when I texted?", "Ты спал, когда я написал?"),
                ],
            ),
            rule(
                "Прерванное действие",
                "Длительное действие — Continuous; короткое событие — Past Simple. While чаще с Continuous; when часто с прерывающим Simple. Картина: фон шёл, потом случилась точка.",
                [
                    ex("I was boiling pasta when the lights went out.", "Я варил пасту, когда погас свет."),
                    ex("While we were queuing, it started to rain.", "Пока мы стояли в очереди, начался дождь."),
                ],
            ),
            rule(
                "Два параллельных процесса",
                "Если оба действия длились одновременно, оба могут быть в Continuous. Законченные факты без «фона» — только Past Simple: She sent the file and left.",
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
            "Не ставьте Continuous на короткие завершённые действия вроде «чашка разбилась».",
            "When he was arriving звучит странно, если прибытие — точка; лучше When he arrived.",
        ],
        remember="Was/were + -ing = процесс в прошлом. Точка-событие — Past Simple.",
    ),
    "present-perfect-intro": lesson(
        "Present Perfect связывает прошлое с настоящим. На A2 достаточно трёх опор: опыт без даты, результат, который виден сейчас, и период, который ещё не закрыт (today, this week, since, for). Если есть точная дата прошлого — обычно Past Simple.",
        [
            rule(
                "Форма have/has + V3",
                "I/you/we/they have + V3. He/she/it has + V3. Краткие: I've, she's. Отрицание: haven't / hasn't. Вопрос: Have you…? Has she…? Смысловой глагол — в третьей форме (sent, seen, finished).",
                [
                    ex("I've sent the email.", "Я отправил письмо (и это важно сейчас)."),
                    ex("Has she finished the report?", "Она закончила отчёт?"),
                    ex("We haven't met before.", "Мы раньше не встречались."),
                ],
            ),
            rule(
                "Опыт и результат сейчас",
                "Опыт без даты: Have you ever…? I've never… Результат, который влияет на момент речи: I've lost my keys (поэтому не могу открыть дверь). Не называйте yesterday/last year вместе с Perfect.",
                [
                    ex("Have you ever tried sushi?", "Ты когда‑нибудь пробовал суши?"),
                    ex("I've lost my keys — I can't open the door.", "Я потерял ключи — не могу открыть дверь."),
                ],
            ),
            rule(
                "Already, yet, just, ever, never",
                "Already — уже (часто утверждение). Yet — уже/ещё в вопросах и отрицаниях. Just — только что. Ever/never — про опыт. Эти маркеры помогают выбрать Perfect, но не сильнее явной даты прошлого.",
                [
                    ex("I've just arrived.", "Я только что приехал."),
                    ex("Have you finished yet?", "Ты уже закончил?"),
                    ex("She's never been abroad.", "Она никогда не была за границей."),
                ],
            ),
        ],
        compare=[
            {"left": "I've sent the email.", "right": "I sent the email yesterday.", "note": "Результат сейчас vs закрытая дата."},
        ],
        watch_out=[
            "I've seen her yesterday — ошибка; нужна Past Simple.",
            "He have finished — нужно has.",
            "После yet в отрицании: I haven't finished yet.",
        ],
        remember="Have/has + V3. Опыт и результат сейчас. Точная дата прошлого — не сюда.",
    ),
    "will-vs-going-to": lesson(
        "Будущее на A2 выбирают не по календарю, а по ситуации. Will — решение и обещание в момент речи, предложение помощи, прогноз «вообще». Be going to — уже принятый план или предсказание по примете, которую видно сейчас.",
        [
            rule(
                "Will / won't",
                "Will + V1 для всех лиц. I'll help you. She won't agree. Часто: спонтанное решение, обещание, предложение (I'll open the window), прогноз без явной приметы.",
                [
                    ex("It's cold in here. I'll close the window.", "Холодно. Я закрою окно (решил сейчас)."),
                    ex("I won't tell anyone.", "Никому не скажу."),
                    ex("I think it'll be fine.", "Думаю, всё будет нормально."),
                ],
            ),
            rule(
                "Be going to",
                "Am/is/are + going to + V1. План уже есть: We're going to move in June. Или примета: Look at those clouds — it's going to rain.",
                [
                    ex("We're going to move in June.", "Мы переезжаем в июне (план)."),
                    ex("Look at those clouds — it's going to rain.", "Смотри на тучи — сейчас пойдёт дождь."),
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
            "Не смешивайте will и going to в одной клетке без причины.",
        ],
        remember="Решил сейчас / обещаю — will. Уже планировал или вижу примету — going to.",
    ),
    "comparatives": lesson(
        "Сравнительная степень показывает разницу между двумя людьми или вещами: A is … than B. Короткие прилагательные обычно берут -er, длинные — more. Отдельно запомните good → better, bad → worse.",
        [
            rule(
                "Короткие прилагательные",
                "Односложные и многие двусложные на -y: older, taller, happier (y→i). После сравнительной формы почти всегда than. Удвоение согласной: big → bigger.",
                [
                    ex("This bag is cheaper than that one.", "Эта сумка дешевле той."),
                    ex("She is happier now.", "Сейчас она счастливее."),
                    ex("My flat is bigger than yours.", "Моя квартира больше твоей."),
                ],
            ),
            rule(
                "Длинные прилагательные и особые формы",
                "Interesting → more interesting; careful → more careful. Good → better, bad → worse, far → farther/further. Нельзя more better.",
                [
                    ex("This film is more interesting than the book.", "Фильм интереснее книги."),
                    ex("His English is better than mine.", "Его английский лучше моего."),
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
            "После сравнительной обычно нужен than, не then.",
            "Не забывайте артикль/местоимение во второй части: than mine / than that one.",
        ],
        remember="-er или more, затем than. Равенство — as … as. Good → better.",
    ),
    "superlatives": lesson(
        "Превосходная степень выделяет один объект из группы: the … -est / the most …. Почти всегда нужен the. Дальше уточняют место (in) или набор (of).",
        [
            rule(
                "Форма the + -est / the most",
                "Короткие: the oldest, the happiest. Длинные: the most interesting. Особые: the best, the worst, the farthest/furthest. Без the форма обычно выглядит неполной.",
                [
                    ex("She is the tallest in her class.", "Она самая высокая в классе."),
                    ex("This is the most expensive option.", "Это самый дорогой вариант."),
                    ex("That was the best day of the trip.", "Это был лучший день поездки."),
                ],
            ),
            rule(
                "In и of",
                "In — для места и группы-контейнера: in the world, in my team. Of — для набора единиц: of all my friends, of the three options.",
                [
                    ex("He is the youngest in the family.", "Он самый младший в семье."),
                    ex("This is the oldest of the three bridges.", "Это самый старый из трёх мостов."),
                ],
            ),
            rule(
                "One of the + превосходная",
                "One of the + прилагательное в превосходной + существительное во множественном: one of the best films. Существительное после one of the почти всегда во множественном числе.",
                [
                    ex("It is one of the best films I've seen.", "Это один из лучших фильмов, которые я видел."),
                ],
            ),
        ],
        compare=[
            {"left": "taller than Sam", "right": "the tallest in the room", "note": "Сравнение двоих vs выбор из группы."},
        ],
        watch_out=[
            "Most interestingest — нельзя смешивать more/most и -est.",
            "One of the best film — нужно films.",
            "Не опускайте the без особой идиомы.",
        ],
        remember="The + -est / the most. Место — in, набор — of. Good → the best.",
    ),
    "countable-uncountable": lesson(
        "Исчисляемые существительные можно посчитать и поставить во множественное: a ticket — tickets. Неисчисляемые в общем смысле не берут a/an и не получают -s: information, advice, furniture, luggage. От типа зависит выбор much/many и артикля.",
        [
            rule(
                "Исчисляемые",
                "Есть единственное и множественное: a chair / chairs, an idea / ideas. С ними работают a/an, many, few, these/those, there are.",
                [
                    ex("I bought two tickets.", "Я купил два билета."),
                    ex("There are three chairs here.", "Здесь три стула."),
                ],
            ),
            rule(
                "Неисчисляемые",
                "Без a/an и без обычного множественного: milk, rice, music, money, news, advice. Согласование часто единственное: The news is good. To count them, use a piece of / a bottle of / some.",
                [
                    ex("I need some advice.", "Мне нужен совет."),
                    ex("There is milk in the fridge.", "В холодильнике есть молоко."),
                    ex("Can I have a piece of advice?", "Можно один совет?"),
                ],
            ),
            rule(
                "Слова-ловушки",
                "Information, advice, furniture, luggage, homework, weather — неисчисляемые на A2. Hair в общем смысле часто неисчисляемое; a hair — один волос.",
                [
                    ex("The furniture is new.", "Мебель новая."),
                    ex("Her hair is short.", "У неё короткие волосы."),
                ],
            ),
        ],
        compare=[
            {"left": "a ticket / many tickets", "right": "some information / much information", "note": "Штуки vs масса/абстракция."},
        ],
        watch_out=[
            "An advice / informations — ошибки.",
            "News are — обычно The news is.",
            "Much tickets — нужно many tickets.",
        ],
        remember="Можно посчитать штуки — a/an и -s. Вещество и абстракция — без -s и часто без a/an.",
    ),
    "quantifiers-a2": lesson(
        "Квантификаторы говорят о количестве без точной цифры. Выбор зависит от типа существительного и от того, утверждение это, вопрос или отрицание.",
        [
            rule(
                "Some, any, a lot of",
                "Some — обычно утверждение (и вежливые предложения). Any — вопросы и отрицания. A lot of / lots of — и с исчисляемыми, и с неисчисляемыми в утверждении.",
                [
                    ex("I have some questions.", "У меня есть несколько вопросов."),
                    ex("Have you got any milk?", "Есть молоко?"),
                    ex("We have a lot of work today.", "Сегодня у нас много работы."),
                ],
            ),
            rule(
                "Much, many, how",
                "Many + исчисляемые; much + неисчисляемые. How many / how much — вопросы о количестве. В утверждениях much часто заменяют на a lot of.",
                [
                    ex("How many apples do you need?", "Сколько яблок нужно?"),
                    ex("There isn't much time.", "Времени мало."),
                ],
            ),
            rule(
                "Few / little и a few / a little",
                "Few / little — мало (с негативным оттенком). A few / a little — немного, но достаточно. Few/a few — штуки; little/a little — масса.",
                [
                    ex("I have a few friends here.", "У меня здесь есть несколько друзей."),
                    ex("There is little hope left.", "Надежды почти не осталось."),
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
            "Some в грубом отрицании обычно не ставят: I haven't got any.",
        ],
        remember="Many/few — штуки. Much/little — масса. A few / a little — «есть немного».",
    ),
    "modals-must-should-have-to": lesson(
        "Три модальных контура A2: обязанность, совет и запрет. Must и have to близки по силе обязанности, но источник разный. Should мягче. Mustn't и don't have to — почти противоположны.",
        [
            rule(
                "Must и have to",
                "Must часто — внутреннее правило или сильное ощущение говорящего. Have to — внешнее требование (работа, закон, расписание). Форма: must + V1; have/has to + V1.",
                [
                    ex("You must keep this door closed.", "Эту дверь нужно держать закрытой (жёсткое правило)."),
                    ex("I have to wear a badge at work.", "На работе я обязан носить бейдж."),
                ],
            ),
            rule(
                "Should / shouldn't",
                "Совет и рекомендация, не жёсткий приказ: You should see a doctor. He shouldn't skip breakfast.",
                [
                    ex("You should see a doctor.", "Тебе стоит сходить к врачу."),
                    ex("He shouldn't skip breakfast before the exam.", "Ему не стоит пропускать завтрак перед экзаменом."),
                ],
            ),
            rule(
                "Mustn't vs don't have to",
                "Mustn't = нельзя, запрещено. Don't have to = можно не делать, обязанности нет. Это одна из главных ловушек уровня.",
                [
                    ex("You mustn't park here.", "Здесь нельзя парковаться."),
                    ex("You don't have to come if you're tired.", "Можешь не приходить, если устал."),
                ],
            ),
        ],
        compare=[
            {"left": "You mustn't tell anyone.", "right": "You don't have to tell anyone.", "note": "Запрет vs отсутствие обязанности."},
        ],
        watch_out=[
            "Must to / should to — после модальных нет to (кроме have to).",
            "Не путайте mustn't и don't have to.",
            "Has to для he/she/it: She has to leave early.",
        ],
        remember="Must/have to — обязанность. Should — совет. Mustn't — нельзя. Don't have to — можно не делать.",
    ),
    "zero-first-conditional": lesson(
        "Условные на A2 пока про два случая: общий закон (Zero) и реальное будущее (First). В части с if на этих уровнях не ставят will: там Present Simple.",
        [
            rule(
                "Zero Conditional",
                "If + Present Simple, Present Simple. Факты, привычки, инструкции: If you heat ice, it melts. Обе части — «как устроено».",
                [
                    ex("If you heat ice, it melts.", "Если нагреть лёд, он тает."),
                    ex("If I don't sleep, I get headaches.", "Если я не сплю, у меня болит голова."),
                ],
            ),
            rule(
                "First Conditional",
                "If + Present Simple, will + V1. Реальное будущее условие и следствие: If it rains, we'll take a taxi. Will — только в главной части.",
                [
                    ex("If it rains, we'll take a taxi.", "Если пойдёт дождь, возьмём такси."),
                    ex("If she passes, she'll call us.", "Если она сдаст, она нам позвонит."),
                ],
            ),
            rule(
                "Unless и порядок частей",
                "Unless ≈ if … not. Часть с if/unless может стоять второй: We'll stay inside if it rains. Запятая нужна, когда if-часть первая.",
                [
                    ex("Unless you hurry, you'll miss the bus.", "Если не поторопишься, опоздаешь на автобус."),
                    ex("We'll stay inside if it rains.", "Останемся дома, если пойдёт дождь."),
                ],
            ),
        ],
        compare=[
            {"left": "If you heat ice, it melts.", "right": "If it rains, we'll take a taxi.", "note": "Закон/привычка vs реальное будущее."},
        ],
        watch_out=[
            "If it will rain — на A2 ошибка; в if-части Present.",
            "Не ставьте will в обе части First Conditional без нужды.",
            "Unless уже содержит отрицание: не unless you don't…",
        ],
        remember="If + Present. Факт — Present в обеих частях. Реальное будущее — will только в главной.",
    ),
    "relative-who-which-that": lesson(
        "Относительные местоимения присоединяют пояснение к существительному. Who — люди. Which — вещи и животные. That — в определяющих придаточных для людей и вещей. Where — места.",
        [
            rule(
                "Who и which",
                "The woman who called you… The book which I bought… Who не ставят к вещам; which не используют для людей в стандартном A2-стиле.",
                [
                    ex("The woman who called you is my boss.", "Женщина, которая тебе звонила, — мой начальник."),
                    ex("The book which I bought is excellent.", "Книга, которую я купил, отличная."),
                ],
            ),
            rule(
                "That и пропуск дополнения",
                "В определяющих придаточных that часто заменяет who/which. Если местоимение — дополнение, его можно опустить: The film (that) we saw was long.",
                [
                    ex("The film that we saw was long.", "Фильм, который мы смотрели, был длинным."),
                    ex("The film we saw was long.", "То же без that — нормально."),
                ],
            ),
            rule(
                "Where и чьё",
                "Where = in/at which для места: the café where we met. Whose — чей: the man whose car was stolen.",
                [
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
            "Не ставьте лишнее what вместо that/which в этом типе придаточных.",
            "Два подлежащих подряд без относительного слова — ошибка.",
        ],
        remember="Люди — who. Вещи — which/that. Дополнение можно опустить. Места — where.",
    ),
    "used-to": lesson(
        "Used to + V1 описывает прошлую привычку или состояние, которых сейчас уже нет. Это не то же самое, что be used to (привыкнуть к чему‑то) и не Past Simple про одноразовый факт.",
        [
            rule(
                "Утверждение",
                "Used to + V1 для всех лиц: I used to play tennis. She used to live in York. Смысл: раньше да, сейчас иначе.",
                [
                    ex("I used to play tennis every weekend.", "Раньше я каждое выходное играл в теннис."),
                    ex("She used to live in York.", "Раньше она жила в Йорке."),
                ],
            ),
            rule(
                "Отрицание и вопрос",
                "Didn't use to + V1. Did you use to…? В этих формах пишут use, не used. Утверждение — used to.",
                [
                    ex("I didn't use to like coffee.", "Раньше мне не нравился кофе."),
                    ex("Did you use to walk to school?", "Ты раньше ходил в школу пешком?"),
                ],
            ),
            rule(
                "Не путать с be used to",
                "Be used to + noun/-ing = привычен к чему‑то сейчас: I'm used to getting up early. Get used to — привыкать. Это другой смысл.",
                [
                    ex("I'm used to getting up early.", "Я привык рано вставать."),
                    ex("You'll get used to the noise.", "Ты привыкнешь к шуму."),
                ],
            ),
        ],
        compare=[
            {"left": "I used to smoke.", "right": "I'm used to noise.", "note": "Прошлая привычка vs привычность сейчас."},
        ],
        watch_out=[
            "I used to living — нужно I used to live ИЛИ I'm used to living.",
            "В вопросе с did — use to, не used to.",
            "Used to не ставят для одноразового прошлого факта с датой без идеи «больше не так».",
        ],
        remember="Used to + V1 = раньше да, сейчас нет. В did-вопросе — use to.",
    ),
    "passive-present-past": lesson(
        "В пассиве важен объект и то, что с ним сделали, а не деятель. Формула: be нужного времени + V3. Present: am/is/are + V3. Past: was/were + V3. By добавляют только если деятель важен.",
        [
            rule(
                "Present Simple Passive",
                "English is spoken here. The office is cleaned every day. Выбор am/is/are зависит от подлежащего-пациенса.",
                [
                    ex("English is spoken here.", "Здесь говорят по-английски."),
                    ex("The office is cleaned every day.", "Офис убирают каждый день."),
                ],
            ),
            rule(
                "Past Simple Passive",
                "The window was broken. The emails were sent yesterday. Was/were + V3. Это законченное прошлое в пассивной рамке.",
                [
                    ex("The window was broken.", "Окно было разбито."),
                    ex("The emails were sent yesterday.", "Письма отправили вчера."),
                ],
            ),
            rule(
                "By и когда пассив уместен",
                "By + деятель — только если он важен: The mural was painted by a local artist. Если деятель неизвестен, очевиден или неважен — by не нужен.",
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
            "Was steal / is speak — нужна III форма.",
            "Не ставьте do/does в пассивный Present: The room is cleaned, не does cleaned.",
            "Согласуйте be с новым подлежащим: emails were, не was.",
        ],
        remember="Be + V3. Сейчас — am/is/are. Прошлое — was/were. By — только если деятель важен.",
    ),
    "adverbs-frequency-manner": lesson(
        "Наречия частоты говорят, как часто бывает действие; наречия образа действия — как оно выполняется. На A2 критичен порядок: частота обычно до смыслового глагола и после be; -ly чаще после глагола или в конце.",
        [
            rule(
                "Частота и место",
                "Always, usually, often, sometimes, rarely, never. Перед смысловым глаголом: She often cooks. После be: She is never late. В вопросе частота идёт после подлежащего: Do you often travel?",
                [
                    ex("She often cooks at home.", "Она часто готовит дома."),
                    ex("She is never late.", "Она никогда не опаздывает."),
                    ex("Do you often travel for work?", "Ты часто ездишь по работе?"),
                ],
            ),
            rule(
                "Образ действия",
                "Many manner adverbs end in -ly: carefully, quickly, quietly. Обычно после глагола или дополнения: He spoke quietly. She opened the door carefully.",
                [
                    ex("He spoke quietly.", "Он говорил тихо."),
                    ex("She opened the door carefully.", "Она осторожно открыла дверь."),
                ],
            ),
            rule(
                "Особые формы",
                "Good → well (наречие). Hard, fast, late, early часто без -ly. Hardly — почти не; это не «тяжёло». Late (поздно) ≠ lately (в последнее время).",
                [
                    ex("She speaks English well.", "Она хорошо говорит по-английски."),
                    ex("He works hard.", "Он усердно работает."),
                    ex("I hardly sleep before exams.", "Перед экзаменами я почти не сплю."),
                ],
            ),
        ],
        compare=[
            {"left": "She is often tired.", "right": "She often feels tired.", "note": "После be vs перед смысловым глаголом."},
            {"left": "He works hard.", "right": "He hardly works.", "note": "Усердно vs почти не."},
        ],
        watch_out=[
            "She often is late — обычно She is often late.",
            "He speaks English good — нужно well.",
            "Hardly ≠ hard.",
        ],
        remember="Частота: до глагола, после be. Образ: -ly после действия. Well, hard, late — особые.",
    ),
}
