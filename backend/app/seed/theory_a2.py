"""Enriched A2 grammar theory (Russian explanations, English examples).

Tone: impersonal / descriptive Russian. No direct address to the learner.
"""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

A2_THEORY = {
    "present-simple-vs-continuous": lesson(
        "На уровне A2 Present Simple и Present Continuous рассматриваются как два способа по-разному представить ситуацию во времени. **Present Simple** описывает действие как обычный, повторяющийся, постоянный или закономерный факт, тогда как **Present Continuous** представляет его как процесс, временную ситуацию или развивающееся изменение.\n\nРусская форма «я работаю» может соответствовать обоим временам: **I work** обычно означает «я работаю вообще, постоянно», а **I am working** — «я работаю сейчас или в ограниченный период». Поэтому выбор определяется контекстом: ситуация является характеристикой обычной жизни или рассматривается как временно происходящий процесс.",
        [
            rule(
                "Present Simple: каркас жизни",
                "Present Simple употребляется для регулярных действий, привычек, постоянных состояний, общеизвестных фактов и расписаний. Действие не обязано происходить в момент речи: оно представляется как часть обычного порядка вещей. Маркеры **always, usually, often, sometimes, never, every day** помогают распознать это значение, но сами по себе не являются обязательными.",
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
                "Present Continuous употребляется для действия в момент речи, временной ситуации, ограниченного периода и процессов изменения. Основная форма — **am/is/are + V-ing**. Значение временности может быть понятно из контекста и без слов now или at the moment.",
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
                "Глаголы состояния (**stative verbs**) обычно описывают не действие как процесс, а состояние, отношение, знание, восприятие или обладание: **know, understand, believe, want, need, like, love, hate, belong, own, prefer**. В нейтральной норме они употребляются в Simple. Однако некоторые глаголы меняют значение: **have** в значении «владеть» обычно остаётся в Simple, а в сочетаниях *have lunch / have a shower* возможен Continuous. Аналогично *I think…* выражает мнение, а *I am thinking about…* — процесс размышления.",
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
        "Past Continuous (**was/were + V-ing**) представляет действие как процесс, находившийся в развитии в определённый момент прошлого. В отличие от Past Simple, сообщающего о событии как о факте, эта форма позволяет показать действие «в процессе». Частая модель — фон в Past Continuous и отдельное событие в Past Simple, но это не абсолютное правило: важнее способ представления ситуации, а не физическая продолжительность действия.",
        [
            rule(
                "Форма was/were + V-ing",
                "Как и в Present Continuous, конструкция обязательно содержит вспомогательный **be**, но в форме прошедшего времени: **was/were + V-ing**. Отрицание образуется с **not**, а вопрос — перестановкой was/were перед подлежащим; do/did здесь не используются.",
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
                "Часто одно действие рассматривается как развивающийся фон, а другое — как отдельное событие. Тогда процесс обычно выражается Past Continuous, а событие — Past Simple. Однако формулу «Continuous = долго, Simple = коротко» нельзя считать абсолютной: выбор зависит от того, как говорящий представляет ситуацию. **While** естественно сочетается с процессом, а **when** может вводить как отдельное событие, так и временной контекст.",
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
        "Present Perfect связывает прошлое событие с настоящим. В центре внимания находится не точная дата, а актуальный результат, жизненный опыт или связь с продолжающимся периодом. На A2 особенно важны опыт без конкретного времени, результат, значимый сейчас, и ситуации, связанные с ещё не завершившимся периодом.\n\nЕсли указывается конкретное завершённое время прошлого — **yesterday, last year, in 2024, two days ago** и т. п. — обычно используется Past Simple. Однако **today, this week, this year** требуют анализа контекста: если период ещё продолжается и связь с настоящим важна, возможен Present Perfect.",
        [
            rule(
                "Форма have/has + V3",
                "После **have/has** используется третья форма смыслового глагола (**V3**, Past Participle). У правильных глаголов она обычно совпадает с формой на **-ed**, а неправильные формы необходимо запоминать: *go → went → gone, see → saw → seen*.",
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
                "Эти слова часто сопровождают Present Perfect, но не заменяют анализа контекста. **Just** и **already** обычно стоят перед V3, **yet** — преимущественно в конце вопросительного или отрицательного предложения, а **ever/never** используются при разговоре о жизненном опыте.",
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
        "Будущее в английском языке выражается несколькими конструкциями. Выбор зависит от того, как представлено событие: как спонтанное решение, заранее существующий план, личное намерение, договорённость или вывод по наблюдаемым признакам. **Will** типично выражает решение в момент речи, обещание, предложение помощи и прогноз-мнение; **be going to** — ранее сформированное намерение или предсказание, имеющее основания в настоящем.",
        [
            rule(
                "Will / won't",
                "После **will** используется начальная форма глагола без **to**; форма will не меняется по лицам и числам. Помимо будущего значения, она может выражать готовность, обещание, предложение помощи или предположение. Отрицательная форма — **will not / won't**.",
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
                "Конструкция **am/is/are + going to + V1** требует формы **be**, поэтому именно она участвует в образовании вопроса и отрицания. Конструкция особенно естественна, когда намерение существовало до момента речи или настоящее содержит очевидные признаки будущего результата.",
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
                callouts=[
                    callout("На A2 рядом с will / going to часто стоит ещё один контур будущего: Present Continuous для **уже договорённого** плана (I'm meeting Sam at 6). Это не «сейчас», а запись в календаре.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "I'll call her now.", "right": "I'm going to call her tonight.", "note": "Решение сейчас vs уже задуманный план."},
            {"left": "I'm meeting the dentist on Friday.", "right": "I'll meet you there if you want.", "note": "Договорённость в календаре vs предложение/решение в момент речи."},
        ],
        watch_out=[
            "Не I will to go / she wills.",
            "Без be нет going to: не She going to leave.",
            "Не смешивают will и going to в одной клетке без причины.",
            "I'm meeting… может быть будущим договорённым планом, не только «прямо сейчас».",
        ],
        remember="Решил сейчас / обещание — **will**. Уже планировал или видна примета — **going to**. Договорённость в календаре — часто Present Continuous.",
    ),
    "comparatives": lesson(
        "Сравнительная степень используется для сопоставления качеств двух объектов, лиц или ситуаций. Типичная модель — **A + comparative + than + B**, хотя объект сравнения может не называться, если он понятен из контекста. Односложные прилагательные обычно получают **-er**, многие двусложные на **-y** — **-ier**, более длинные часто образуют форму с **more**. Есть неправильные формы: **good/well → better, bad/badly → worse, far → farther/further**.",
        [
            rule(
                "Как образуется сравнение",
                "**Than** вводит второй элемент сравнения, когда он выражен явно. Однако сравнительная форма может употребляться и самостоятельно: *This option is cheaper*. Поэтому than не является обязательным, если объект сравнения уже понятен из ситуации.",
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
                "**As + adjective + as** выражает равную степень качества. **Not as/so + adjective + as** показывает неравенство. **Less + adjective + than** обозначает меньшую степень качества; выбор между этой конструкцией и формой на -er зависит от конкретного прилагательного и естественности выражения.",
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
        "Превосходная степень выделяет один объект как обладающий качеством в наибольшей степени среди определённой группы. Основные модели — **the + adjective-est** и **the most + adjective**. После формы часто уточняется область сравнения: **in** для места или группы и **of** для ограниченного набора.",
        [
            rule(
                "Форма the + -est / the most",
                "В обычной конструкции превосходная степень употребляется с **the**, поскольку выделяется один объект внутри группы. Однако после притяжательных определителей возможны формы без the: *my best friend, his oldest son*, а также существуют устойчивые выражения.",
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
        "Исчисляемые и неисчисляемые существительные различаются прежде всего по грамматическому поведению. Исчисляемые обозначают отдельные единицы и сочетаются с **a/an**, числительными и формой множественного числа. Неисчисляемые обычно рассматриваются как вещество, абстрактное понятие, информация или совокупность и в общем значении не употребляются с **a/an** и обычным -s. Для отдельной единицы используются слова меры: **a piece of advice, a piece of information, a bottle of water**.",
        [
            rule(
                "Два типа существительных",
                "Грамматический тип определяется поведением слова именно в английском языке, а не его переводом. Поэтому русскому исчисляемому слову может соответствовать английское неисчисляемое существительное, например **advice**.",
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
                            ["much / little", "—", "not much information (часто вопрос/отриц.)"],
                            ["a lot of", "a lot of tickets", "a lot of information"],
                            ["пример", "chair, idea, ticket", "milk, news, advice, furniture"],
                        ],
                    ),
                ],
                pairs=[
                    pair("an advice", "some advice / a piece of advice", "Advice неисчисляемое."),
                    pair("informations", "information", "Без обычного множественного."),
                ],
                callouts=[
                    callout("Much с неисчисляемыми естественнее в вопросах и отрицаниях; в обычном утверждении «много» чаще говорят **a lot of** information.", "tip"),
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
            {"left": "a ticket / many tickets", "right": "some information / a lot of information", "note": "Штуки vs масса/абстракция; в утверждении про «много» чаще a lot of, не much."},
        ],
        watch_out=[
            "An advice / informations — ошибки.",
            "News are — обычно The news **is**.",
            "Much tickets — нужно **many** tickets.",
        ],
        remember="Можно посчитать штуки — a/an и -s. Вещество и абстракция — без -s и часто без a/an.",
    ),
    "quantifiers-a2": lesson(
        "Квантификаторы выражают неопределённое количество. Их выбор зависит прежде всего от того, является существительное исчисляемым или неисчисляемым, а также от типа предложения и смыслового оттенка. Упрощённые схемы «some только в утверждении» и «any только в вопросе и отрицании» имеют важные исключения.",
        [
            rule(
                "Some, any, a lot of",
                "В нейтральных утверждениях обычно используется **some**, а **any** типично для вопросов и отрицаний. Однако **some** естественно в предложениях и просьбах, где ожидается положительный ответ: *Would you like some tea?* **Any** может использоваться в утверждении в значении «любой». **A lot of/lots of** сочетаются и с исчисляемыми, и с неисчисляемыми существительными.",
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
                            ["много (утверждение, обычный стиль)", "**a lot of**", "**a lot of**"],
                            ["много (вопрос / отрицание)", "**many**", "**much**"],
                            ["немного есть", "**a few**", "**a little**"],
                            ["мало (негативно)", "**few**", "**little**"],
                        ],
                    ),
                ],
                pairs=[
                    pair("much apples", "many apples / a lot of apples", "Apples — исчисляемые; much с ними не ставят."),
                    pair("many rice", "much rice / a lot of rice", "Rice — неисчисляемое."),
                    pair("I have much time today.", "I have a lot of time today.", "Much в обычном утверждении звучит тяжело/формально."),
                ],
                callouts=[
                    callout("**Few** и **a few** — не синонимы по тону: few friends ≈ почти нет друзей; a few friends ≈ несколько друзей есть.", "key"),
                    callout("Much/many естественны в вопросах и отрицаниях. В обычном утверждении чаще **a lot of**; much в утверждении — скорее формальный регистр (Much has been written…).", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "a few eggs", "right": "a little milk", "note": "Штуки vs неисчисляемое."},
            {"left": "few friends", "right": "a few friends", "note": "Мало (почти нет) vs немного есть."},
            {"left": "How much time have we got?", "right": "We haven't got much time.", "note": "Much уместен в вопросе и отрицании."},
        ],
        watch_out=[
            "Much apples / many rice — перепутан тип существительного.",
            "I have much money — в обычной речи лучше **a lot of** money.",
            "Few и a few — не синонимы по тону.",
            "Some в грубом отрицании обычно не ставят: I haven't got **any**.",
        ],
        remember="Many/much — штуки/масса, чаще в вопросе и отрицании. Утверждение «много» — обычно a lot of. A few / a little — «есть немного».",
    ),
    "modals-must-should-have-to": lesson(
        "На уровне A2 важно различать обязанность, необходимость, совет и запрет. **Must** и **have to** часто переводятся одинаково, но типично различаются источником необходимости: must связано с правилом или позицией говорящего, have to — с внешними обстоятельствами или требованиями. Это различие является тенденцией, а не абсолютно жёстким правилом. **Should** выражает рекомендацию. **Mustn't** означает запрет, а **don't have to** — отсутствие обязанности.",
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
        "Условные конструкции связывают условие и результат. **Zero Conditional** описывает общие закономерности, инструкции и повторяющиеся последствия. **First Conditional** относится к реальному или вероятному будущему. В стандартной модели после **if** используется Present Simple, хотя смысл относится к будущему; **will** обычно находится в главной части.",
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
                "**Unless** обычно близко по смыслу к **if … not**, но не всегда заменяется механически без проверки значения. Условная часть может стоять до или после главной; если она стоит первой, обычно используется запятая.",
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
        "Относительные слова вводят придаточные определения и связывают дополнительную информацию с существительным, к которому относится пояснение. **Who** относится к людям, **which** — к предметам и животным, **that** может заменять who/which в определяющих придаточных, **where** указывает на место, а **whose** выражает принадлежность. В добавочных придаточных, выделяемых запятыми, **that** не употребляется.",
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
                "Пропуск возможен, если относительное слово является дополнением придаточного. Если оно выполняет функцию подлежащего, пропуск невозможен: *The man who lives next door*.",
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
        "**Used to + V1** описывает регулярную привычку или состояние, характерные для прошлого и противопоставляемые настоящему. Конструкция подходит и для повторяющихся действий, и для состояний. Она отличается от **be used to + noun/-ing**, которое выражает привычность сейчас, и **get used to + noun/-ing**, которое обозначает процесс привыкания.",
        [
            rule(
                "Used to: форма и смысл",
                "Конструкция обычно выражает контраст между прошлым и настоящим. В утверждении используется **used to**, а после **did/didn't** — **use to**, поскольку показатель прошедшего времени уже выражен вспомогательным глаголом. В современной практике встречается вариант *didn't used to*, но для учебной нормы предпочтительно **didn't use to**.",
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
        "В страдательном залоге (**Passive Voice**) в центре сообщения находится объект действия, а деятель может быть неизвестен, очевиден или неважен. Формула — **be** в нужном времени + **V3**. При преобразовании активной конструкции объект становится подлежащим, поэтому форма be согласуется уже с новым подлежащим. **By + деятель** добавляется только при смысловой необходимости.",
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
        "Наречия частоты показывают регулярность действия, а наречия образа действия характеризуют способ его выполнения. Наречия частоты обычно стоят перед смысловым глаголом, но после **be**. Многие наречия образуются с **-ly**, однако это не универсальное правило: некоторые слова имеют одинаковую форму прилагательного и наречия, а добавление -ly иногда меняет значение.",
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
                "Многие наречия образуются с помощью **-ly**: *careful → carefully*. Однако **good → well**, а слова **hard, fast, late, early** часто используются без -ly. Формы с -ly могут иметь самостоятельное значение: **hardly** = «почти не», **lately** = «в последнее время», поэтому их нельзя механически считать обычными наречиями от исходного прилагательного.",
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
