"""Enriched B1 grammar theory (Russian explanations, English examples).

Tone: impersonal / descriptive Russian. Tables / pairs for densest rule blobs.
"""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

B1_THEORY = {
    "present-perfect-vs-past-simple": lesson(
        "Оба времени смотрят в прошлое, но точка опоры разная. **Present Perfect** связывает прошлое с настоящим: опыт, результат, ещё не закрытый период. **Past Simple** относит событие к закрытому прошлому.\n\nДля русского «я жил / я живу здесь уже…» выбор зависит от смысла: этап закончился — Past Simple; ситуация всё ещё длится — Present Perfect.",
        [
            rule(
                "Два взгляда на прошлое",
                "Важен не календарь сам по себе, а связь с «сейчас» vs закрытая точка на шкале времени.",
                [
                    ex("I've worked night shifts since April.", "Я работаю в ночную смену с апреля (и сейчас тоже)."),
                    ex("I worked night shifts in 2022.", "Я работал в ночную в 2022-м (уже нет)."),
                    ex("I've lived here for six years.", "Я живу здесь уже шесть лет."),
                ],
                tables=[
                    table(
                        ["Сигнал", "Время", "Пример"],
                        [
                            ["результат / опыт / since-for (ещё длится)", "**Present Perfect**", "I've lost my keys."],
                            ["ago / last / in + год / when + прошлое", "**Past Simple**", "I lost them yesterday."],
                            ["today / this week (период ещё открыт)", "часто Perfect", "Have you seen her today?"],
                            ["yesterday / last week (период закрыт)", "Past Simple", "Did you see her yesterday?"],
                        ],
                    ),
                ],
                pairs=[
                    pair("I've seen her yesterday.", "I saw her yesterday.", "Закрывающая дата не сочетается с Perfect."),
                    pair("I live here since 2020.", "I've lived here since 2020.", "Since с незакрытой ситуацией → Perfect."),
                ],
            ),
            rule(
                "For / since и gone / been",
                "For + длительность, since + точка старта. Gone vs been: He's gone to Riga (ещё там или в пути). He's been to Riga (был и вернулся).",
                [
                    ex("I've been to Lisbon twice.", "Я бывал в Лиссабоне дважды (опыт, даты не важны)."),
                    ex("I went to Lisbon in May.", "Я ездил в Лиссабон в мае (закрытая поездка)."),
                    ex("He isn't at his desk. He has gone to lunch.", "Его нет на месте: он ушёл на обед."),
                ],
                callouts=[
                    callout("Короткий тест: есть дата-закрытие или when-прошедшее? → Past Simple. Важен результат сейчас, опыт или since/for с незакрытой ситуацией? → Present Perfect.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "I've lived here for six years.", "right": "I lived there for six years.", "note": "Всё ещё здесь vs тот этап закончился."},
            {"left": "Have you seen her today?", "right": "Did you see her yesterday?", "note": "Today ещё может быть открыт; yesterday уже закрыт."},
        ],
        watch_out=[
            "Не I've seen her yesterday / I've started the course last week.",
            "Не I live here since 2020 — нужен Present Perfect: **I've lived**.",
            "For + период (for three days), since + момент (since Monday), не наоборот.",
        ],
        remember="Есть дата-закрытие — Past Simple. Период ещё открыт или важен результат — Present Perfect.",
    ),
    "present-perfect-continuous": lesson(
        "Present Perfect Continuous (**have/has been + V-ing**) подчёркивает саму деятельность и её длительность до сейчас. Present Perfect Simple чаще ставит акцент на результат или количество. Глаголы состояния (know, own, like) в Continuous не ставят.",
        [
            rule(
                "Форма и акцент",
                "Continuous — «занимался / всё ещё в процессе». Simple — «сделал / сколько раз / какой результат».",
                [
                    ex("I've been editing this chapter all morning.", "Я всё утро правлю эту главу."),
                    ex("I've read five chapters.", "Я прочитал пять глав."),
                    ex("I've known her since school.", "Я знаю её со школы."),
                ],
                tables=[
                    table(
                        ["Акцент", "Форма", "Пример"],
                        [
                            ["процесс / длительность", "have/has **been** + V-ing", "I've been waiting for 40 minutes."],
                            ["результат / число", "have/has + **V3**", "I've read five chapters."],
                            ["состояние", "только Simple", "I've known her since school."],
                        ],
                    ),
                ],
                pairs=[
                    pair("I've been knowing her.", "I've known her.", "Состояния не ставят в Continuous."),
                ],
            ),
            rule(
                "След недавней активности",
                "Часто виден след: I'm tired because I've been running. How long have you been…? — если процесс связан с сейчас.",
                [
                    ex("I've been waiting for forty minutes.", "Я жду уже сорок минут."),
                    ex("She's been crying — her eyes are red.", "Она плакала: глаза красные."),
                    ex("Has she been practising the solo?", "Она репетировала соло?"),
                ],
            ),
        ],
        compare=[
            {"left": "I've painted the wall.", "right": "I've been painting the wall.", "note": "Готово vs ещё в процессе / недавно этим занимался."},
        ],
        watch_out=[
            "Не I've been knowing / been wanting.",
            "Не путают с Past Continuous: was painting — только прошлое без связи с сейчас.",
            "For/since остаются, но меняется акцент Simple/Continuous.",
        ],
        remember="Have/has been + V-ing — длительность и процесс до сейчас. Результат и число — чаще Simple.",
    ),
    "past-perfect": lesson(
        "Past Perfect нужен не «потому что прошлое», а потому что в прошлом уже есть точка, а другое действие было **раньше** неё. Форма одна для всех лиц: **had + V3**. Без второй прошлой точки обычно хватает Past Simple.",
        [
            rule(
                "Раньше другой прошлой точки",
                "Сначала более раннее — Past Perfect, затем более позднее — Past Simple.",
                [
                    ex("She had already left when I arrived.", "Когда я приехал, она уже ушла."),
                    ex("By the time we got there, the film had started.", "К нашему приходу фильм уже начался."),
                    ex("I didn't call because I had lost my phone.", "Я не позвонил, потому что потерял телефон."),
                ],
                tables=[
                    table(
                        ["Порядок событий", "Время"],
                        [
                            ["более раннее действие", "**had** + V3"],
                            ["более поздняя точка в прошлом", "Past Simple"],
                        ],
                    ),
                ],
                pairs=[
                    pair("When I arrived, she left. (если уже ушла)", "When I arrived, she had left.", "Had показывает «уже до приезда»."),
                ],
                callouts=[
                    callout("Если события идут просто по порядку и смысл ясен (I opened the door and went in), Past Perfect часто не нужен.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "When I arrived, she left.", "right": "When I arrived, she had left.", "note": "Ушла после приезда vs уже ушла к моменту приезда."},
        ],
        watch_out=[
            "Не ставят Past Perfect во все подряд прошлые предложения.",
            "Has left — это Present Perfect; для «до прошлого» нужен **had**.",
            "After he had had breakfast звучит тяжело; иногда достаточно After he had breakfast.",
        ],
        remember="**Had + V3** = раньше другой прошлой точки. Без второй точки чаще хватает Past Simple.",
    ),
    "future-continuous": lesson(
        "Future Continuous (**will be + V-ing**) показывает действие как процесс в будущей точке или вежливый вопрос о планах. Это не «просто будущее», а будущее-в-процессе: At 8 I'll be driving.",
        [
            rule(
                "Процесс в будущей точке",
                "Для всех лиц одинаково: will be + V-ing. Часто с at this time tomorrow, at 8, when you arrive.",
                [
                    ex("At 8 I'll be driving home.", "В 8 я буду ехать домой."),
                    ex("This time tomorrow we'll be flying.", "Завтра в это время мы будем в полёте."),
                    ex("Will you be using the meeting room at noon?", "Комната для переговоров в полдень нужна?"),
                ],
                tables=[
                    table(
                        ["Смысл", "Форма", "Пример"],
                        [
                            ["точка-обещание / решение", "will + V1", "I'll call you at 8."],
                            ["процесс в этот час", "will be + **V-ing**", "I'll be driving at 8."],
                        ],
                    ),
                ],
                pairs=[
                    pair("I will be go home.", "I will be going home.", "Нужна форма V-ing."),
                ],
            ),
        ],
        compare=[
            {"left": "I'll call you at 8.", "right": "I'll be driving at 8.", "note": "Точка-обещание vs процесс в этот час."},
        ],
        watch_out=[
            "Will be go — нужна форма **V-ing**.",
            "Не путают с Future Perfect (will have + V3).",
            "Will you be…? — не то же самое, что Are you going to…?, хотя темы пересекаются.",
        ],
        remember="**Will be + V-ing** — процесс в будущей точке или мягкий вопрос о занятости.",
    ),
    "second-conditional": lesson(
        "Second Conditional описывает нереальное или маловероятное настоящее/будущее. В if-части — Past Simple (по форме), в главной — **would + V1**. Это не рассказ о прошлом.",
        [
            rule(
                "Структура и смысл",
                "Условие сейчас неверно или маловероятно. Форма прошедшая, смысл — сейчас/будущее.",
                [
                    ex("If I had more time, I would travel more.", "Если бы у меня было больше времени, я бы больше путешествовал."),
                    ex("If I were you, I'd talk to her.", "На твоём месте я бы с ней поговорил."),
                    ex("If she lived nearer, we'd meet more often.", "Если бы она жила ближе, мы бы чаще встречались."),
                ],
                tables=[
                    table(
                        ["Тип", "If-часть", "Главная", "Смысл"],
                        [
                            ["First", "Present", "will + V1", "реальное будущее"],
                            ["**Second**", "Past Simple", "**would** + V1", "нереальное сейчас/будущее"],
                            ["Third", "Past Perfect", "would have + V3", "нереальное прошлое"],
                        ],
                    ),
                ],
                pairs=[
                    pair("If I would have more time…", "If I had more time…", "В if-части Second Conditional would обычно не ставят."),
                ],
                callouts=[
                    callout("Were часто предпочитают для всех лиц в учебном стиле: If I **were** you.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "If it rains, we'll stay in.", "right": "If it rained, we would stay in.", "note": "Реальное будущее vs гипотеза."},
        ],
        watch_out=[
            "If I would have… — не стандартный Second Conditional.",
            "If I was you встречается, но If I were you безопаснее в учебном стиле.",
            "Не путают с Third Conditional (had + V3 / would have + V3).",
        ],
        remember="If + Past, would + V1. Форма прошедшая, смысл — нереальное сейчас/будущее.",
    ),
    "third-conditional": lesson(
        "Third Conditional говорит о нереальном прошлом: условие уже не изменить. **If + Past Perfect**, **would have + V3**. Часто это сожаление или анализ ошибки.",
        [
            rule(
                "Нереальное прошлое",
                "Обе части про прошлое, которого не было. Could have / might have — варианты силы.",
                [
                    ex("If I had left earlier, I would have caught the train.", "Если бы я вышел раньше, успел бы на поезд."),
                    ex("If she had studied, she might have passed.", "Если бы она занималась, могла бы сдать."),
                    ex("I'd have helped if I'd seen your message.", "Помог бы, если бы увидел сообщение."),
                ],
                tables=[
                    table(
                        ["Часть", "Форма"],
                        [
                            ["If-часть", "**had** + V3"],
                            ["Главная часть", "**would have** + V3"],
                        ],
                    ),
                ],
                pairs=[
                    pair("If I would have known…", "If I had known…", "В if-части — had + V3, не would have."),
                    pair("If I had time, I would have helped.", "If I had had time, I would have helped.", "Для прошлого в if нужна Past Perfect."),
                ],
            ),
        ],
        compare=[
            {"left": "If I had time, I would help.", "right": "If I had had time, I would have helped.", "note": "Нереальное сейчас vs нереальное прошлое."},
        ],
        watch_out=[
            "If I would have known — распространённая ошибка; нужно If I **had** known.",
            "Would have в if-части в стандартном Third не ставят.",
            "Не сокращают так, чтобы пропал have: I'd helped ≠ I'd have helped.",
        ],
        remember="If + had + V3, would have + V3. Нереальное прошлое и часто сожаление.",
    ),
    "modals-possibility": lesson(
        "Модальные возможности B1 различают силу гипотезы: **must** (почти уверен), **may/might/could** (возможно), **can't** (почти исключено). Речь не о разрешении can, а о выводе из фактов.",
        [
            rule(
                "Шкала уверенности",
                "Must / can't — сильный логический вывод. May / might / could — возможность без уверенности.",
                [
                    ex("He's not answering. He must be busy.", "Он не отвечает. Должно быть, он занят."),
                    ex("That can't be her car — it's the wrong colour.", "Это не может быть её машина: цвет не тот."),
                    ex("She may be at lunch.", "Возможно, она на обеде."),
                ],
                tables=[
                    table(
                        ["Сила", "Модальный", "Смысл"],
                        [
                            ["очень вероятно", "**must**", "логически почти наверняка"],
                            ["возможно", "**may / might / could**", "есть шанс"],
                            ["почти исключено", "**can't**", "логически почти невозможно"],
                        ],
                    ),
                    table(
                        ["Время вывода", "Схема", "Пример"],
                        [
                            ["сейчас / процесс", "modal + be + V-ing", "She must be waiting."],
                            ["прошлое", "modal + **have** + V3", "He might have forgotten."],
                        ],
                    ),
                ],
                callouts=[
                    callout("Для логического отрицания обычно берут **can't**, не mustn't (mustn't на A2 — про запрет).", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "She must be at work.", "right": "She has to be at work at 9.", "note": "Вывод vs обязанность по правилам."},
        ],
        watch_out=[
            "Mustn't для логического отрицания обычно не подходит; берут **can't**.",
            "Can в утверждении редко значит «может быть, что… сейчас» (She can be at lunch); для эпистемической гипотезы берут may/might/could.",
            "Must have + V3 — про прошлый вывод, не Present Perfect «просто так».",
        ],
        remember="Must/can't — сильный вывод. May/might/could — возможность. Для прошлого: modal + have + V3.",
    ),
    "reported-statements": lesson(
        "В косвенной речи утверждений сдвигаются местоимения, время (**backshift**) и маркеры времени/места. Say и tell различаются по наличию объекта: tell somebody, say something (to somebody).",
        [
            rule(
                "Backshift и say / tell",
                "Если факт всё ещё истинен, сдвиг иногда не делают, но на B1 отрабатывают стандартный сдвиг.",
                [
                    ex("«I'm tired.» → She said she was tired.", "«Я устала.» → Она сказала, что устала."),
                    ex("«I've finished.» → He said he had finished.", "«Я закончил.» → Он сказал, что закончил."),
                    ex("She told me she was leaving.", "Она сказала мне, что уходит."),
                ],
                tables=[
                    table(
                        ["Прямая речь", "Косвенная (типичный сдвиг)"],
                        [
                            ["Present Simple", "Past Simple"],
                            ["Present Continuous", "Past Continuous"],
                            ["Present Perfect / Past Simple", "Past Perfect"],
                            ["will", "would"],
                            ["can", "could"],
                            ["today / tomorrow / yesterday", "that day / the next day / the day before"],
                            ["here / this", "there / that"],
                        ],
                    ),
                ],
                pairs=[
                    pair("She said me she was ill.", "She told me she was ill.", "Tell + адресат; said me — ошибка."),
                ],
            ),
        ],
        compare=[
            {"left": "She said she was ill.", "right": "She told me she was ill.", "note": "Say без обязательного объекта; tell — с адресатом."},
        ],
        watch_out=[
            "She said me… — ошибка; нужно **told me** или said to me.",
            "Не забывают сдвигать will → would.",
            "Кавычки в косвенной речи не ставят.",
        ],
        remember="Сдвигают время и маркеры. Tell + человек. Say + содержание.",
    ),
    "reported-questions": lesson(
        "Косвенные вопросы теряют инверсию прямого вопроса: порядок как в утверждении. **If/whether** — для общих вопросов; Wh-слово сохраняется для специальных.",
        [
            rule(
                "Порядок утверждения",
                "После ask нет вопросительного знака и нет инверсии do/does/did.",
                [
                    ex("«Where do you live?» → He asked where I lived.", "Спросил, где я живу."),
                    ex("«Are you ready?» → She asked if I was ready.", "Спросила, готов ли я."),
                    ex("I wondered why they were late.", "Интересовало, почему они опаздывают."),
                ],
                tables=[
                    table(
                        ["Тип", "Схема"],
                        [
                            ["Wh-вопрос", "ask + wh + подлежащее + глагол"],
                            ["Yes/No", "ask + **if/whether** + подлежащее + глагол"],
                        ],
                    ),
                ],
                pairs=[
                    pair("He asked where did I live.", "He asked where I lived.", "Лишний did и инверсия."),
                ],
            ),
        ],
        compare=[
            {"left": "Where do you work?", "right": "She asked where I worked.", "note": "Прямой вопрос с инверсией vs косвенный без инверсии."},
        ],
        watch_out=[
            "He asked where did I live — лишний did и инверсия.",
            "Не оставляют ? в конце косвенного вопроса.",
            "If/whether нужны для yes/no, не для wh.",
        ],
        remember="Косвенный вопрос = Wh/if + порядок утверждения. Времена обычно сдвигаются.",
    ),
    "passive-all-simple": lesson(
        "На B1 пассив расширяется на Perfect и модальные. Фокус по-прежнему на пациенсе и результате, а не на деятеле.",
        [
            rule(
                "Линейка пассивов",
                "Везде **be** нужного времени + **V3**. By добавляют только если источник действия значим.",
                [
                    ex("The report has been sent.", "Отчёт уже отправили."),
                    ex("The hall will be painted next week.", "Зал покрасят на следующей неделе."),
                    ex("It must be finished today.", "Это должно быть закончено сегодня."),
                ],
                tables=[
                    table(
                        ["Время / тип", "Схема", "Пример"],
                        [
                            ["Present", "am/is/are + V3", "is cleaned"],
                            ["Past", "was/were + V3", "was cleaned"],
                            ["Perfect", "has/have **been** + V3", "has been cleaned"],
                            ["Future", "will be + V3", "will be cleaned"],
                            ["Modal", "modal + be + V3", "must be finished"],
                        ],
                    ),
                ],
                pairs=[
                    pair("The report has been send.", "The report has been sent.", "Нужна III форма."),
                    pair("It must be finish.", "It must be finished.", "Modal + be + V3."),
                ],
            ),
        ],
        compare=[
            {"left": "Someone has sent the report.", "right": "The report has been sent.", "note": "Актив с someone vs пассив с результатом."},
        ],
        watch_out=[
            "Has been send — нужна V3: **sent**.",
            "Must be finish — must be **finished**.",
            "Не теряют been в Perfect Passive.",
        ],
        remember="Be нужного времени + V3. Perfect: has/have been + V3. Modal: modal + be + V3.",
    ),
    "defining-nondefining": lesson(
        "Defining relative clauses уточняют, о ком/чём речь, и без них смысл ломается. Non-defining дают дополнительную информацию и выделяются запятыми; **that** в них обычно не используют.\n\nЗапятая — не украшение: она меняет, сколько объектов подразумевается в классе.",
        [
            rule(
                "Defining vs non-defining",
                "Defining — без запятых: придаточное нужно, чтобы понять «какой именно». Non-defining — добавка к уже ясному объекту, в запятых.",
                [
                    ex("The students who arrived late missed the test.", "Студенты, которые опоздали, пропустили тест (не все, а опоздавшие)."),
                    ex("My sister, who lives in Oslo, is visiting.", "Сестра (она и так известна) живёт в Осло — это ремарка."),
                    ex("The book I read was excellent.", "Книга, которую прочитали, была отличной (дополнение можно опустить: that/which)."),
                ],
                tables=[
                    table(
                        ["", "Defining", "Non-defining"],
                        [
                            ["Запятые", "нет", "да"],
                            ["Роль", "нужно, чтобы понять «какой именно»", "добавка к уже ясному объекту"],
                            ["that", "можно", "обычно нет"],
                            ["пропуск дополнения", "можно", "нельзя"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Paris, that we visited in March, was cold.", "Paris, which we visited in March, was cold.", "Non-defining не берёт that."),
                    pair("My brother, who lives abroad called.", "My brother, who lives abroad, called.", "Non-defining требует пару запятых."),
                ],
                callouts=[
                    callout("My brother who lives abroad… подразумевает нескольких братьев. My brother, who lives abroad,… — один брат, abroad — ремарка.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "My brother who lives abroad called.", "right": "My brother, who lives abroad, called.", "note": "Один из братьев vs единственный брат + добавка."},
        ],
        watch_out=[
            "That в non-defining с запятыми — плохой учебный стиль.",
            "Не ставят запятые в defining, если без придаточного объект неясен.",
            "Which для людей в defining лучше заменить на who.",
        ],
        remember="Defining уточняет без запятых. Non-defining — добавка в запятых, без that.",
    ),
    "gerund-vs-infinitive": lesson(
        "После одних глаголов нужен **-ing**, после других — **to-infinitive**, а у части глаголов смена формы меняет смысл. На B1 полезнее выучить частые списки и пары-ловушки, чем искать одно «правило на всё».",
        [
            rule(
                "Списки и пары со сменой смысла",
                "После предлога тоже -ing: interested in learning. Look forward to + -ing (здесь to — предлог).",
                [
                    ex("I enjoy cooking at weekends.", "Мне нравится готовить по выходным."),
                    ex("We decided to leave early.", "Мы решили уйти пораньше."),
                    ex("I stopped smoking last year.", "Я бросил курить в прошлом году."),
                    ex("I stopped to buy water.", "Я остановился, чтобы купить воду."),
                ],
                tables=[
                    table(
                        ["После глагола", "Форма", "Частые глаголы"],
                        [
                            ["часто -ing", "**V-ing**", "enjoy, avoid, finish, suggest, keep, mind"],
                            ["часто to-inf", "**to** + V1", "want, decide, hope, plan, promise, refuse, learn"],
                        ],
                    ),
                    table(
                        ["Пара", "+ -ing", "+ to-inf"],
                        [
                            ["stop", "перестать делать", "остановиться, чтобы сделать"],
                            ["remember", "помнить, как делал", "не забыть сделать"],
                            ["try", "попробовать способ", "пытаться (есть трудность)"],
                        ],
                    ),
                ],
                pairs=[
                    pair("She suggested to go.", "She suggested going.", "Suggest обычно + -ing."),
                ],
            ),
        ],
        compare=[
            {"left": "I remembered locking the door.", "right": "I remembered to lock the door.", "note": "Помню, как закрывал vs не забыл закрыть."},
        ],
        watch_out=[
            "Suggest to go — обычно suggest **going**.",
            "После предлога to как предлога (look forward to) нужен -ing: look forward to **seeing**.",
            "Не путают to (частица инфинитива) и to (предлог).",
        ],
        remember="Списки + пары stop/remember/try. После предлога — -ing.",
    ),
    "wish-past-simple": lesson(
        "I wish / if only + Past Simple выражает желание изменить настоящее или будущее. Форма прошедшая, смысл — сейчас. Для сожаления о прошлом позже появляется wish + Past Perfect.",
        [
            rule(
                "Wish: настоящее vs поведение",
                "I hope + Present/will — реальная надежда. I wish + Past — контрфакт.",
                [
                    ex("I wish I knew the answer.", "Жаль, что я не знаю ответа."),
                    ex("I wish you would listen.", "Хоть бы ты слушал."),
                    ex("I hope you pass the exam.", "Надеюсь, ты сдашь экзамен."),
                ],
                tables=[
                    table(
                        ["Конструкция", "Смысл", "Пример"],
                        [
                            ["wish + Past Simple", "нереальное сейчас", "I wish I knew."],
                            ["wish + would", "чужое поведение / раздражение", "I wish you would stop."],
                            ["hope + Present/will", "реальная надежда", "I hope you pass."],
                        ],
                    ),
                ],
                pairs=[
                    pair("I wish I know.", "I wish I knew.", "Нужна прошедшая форма."),
                    pair("I wish I would be rich.", "I wish I were rich.", "Для состояния — Past, не would."),
                ],
            ),
        ],
        compare=[
            {"left": "I hope she calls.", "right": "I wish she called more often.", "note": "Реальная надежда vs желание изменить привычку."},
        ],
        watch_out=[
            "I wish I know — нужна прошедшая форма **knew**.",
            "I wish I would be rich — для состояния: I wish I **were** rich.",
            "Wish + Past Perfect оставляют для прошлого сожаления.",
        ],
        remember="Wish + Past Simple — про нереальное сейчас. Wish + would — про чужое поведение.",
    ),
    "question-tags": lesson(
        "Question tags — короткий хвост-вопрос в конце фразы: It's cold, isn't it? Обычно утверждение → отрицательный tag, и наоборот.\n\nTag не вводит новую грамматику времени: он **зеркалит** вспомогательный глагол (или подставляет do) и меняет полярность.",
        [
            rule(
                "Полярность и особые случаи",
                "Вспомогательный глагол в tag повторяет время/модальность основной части. Если aux нет — подставляют do/does/did.",
                [
                    ex("You're ready, aren't you?", "Готов, правда?"),
                    ex("You like jazz, don't you?", "Любишь джаз, да?"),
                    ex("I'm early, aren't I?", "Я рано, правда?"),
                    ex("Let's go, shall we?", "Пойдём, а?"),
                ],
                tables=[
                    table(
                        ["Основа", "Tag"],
                        [
                            ["утверждение с be/modal/aux", "отрицательный tag"],
                            ["отрицание", "положительный tag"],
                            ["нет aux → do/does/did", "You like it, **don't** you?"],
                            ["I am …", "**aren't I?**"],
                            ["Let's …", "**shall we?**"],
                            ["There is …", "**isn't there?**"],
                            ["Everyone / somebody …", "aux + **they?** (Everyone is ready, **aren't they?**)"],
                        ],
                    ),
                ],
                pairs=[
                    pair("You like jazz, like you?", "You like jazz, don't you?", "В tag не повторяют смысловой глагол — нужен do."),
                    pair("I'm early, amn't I?", "I'm early, aren't I?", "Устойчивое исключение: aren't I."),
                    pair("Everyone is here, isn't he?", "Everyone is here, aren't they?", "Everyone → they в tag; вспомогательный зеркалит время основы."),
                ],
                callouts=[
                    callout("Утверждение → отрицательный tag; отрицание → положительный. Это учебный default; интонация потом отличает «проверку» от «согласие».", "tip"),
                    callout("Everyone / somebody в tag берут **they**, но aux совпадает с основой: Everyone came, **didn't they?** / Everyone is ready, **aren't they?**", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "You can drive, can't you?", "right": "You can't drive, can you?", "note": "Полярность tag зеркалит основу."},
        ],
        watch_out=[
            "Учебный default для You are ready — **aren't you?**",
            "I am → aren't I — исключение.",
            "Не повторяют смысловой глагол в tag: like you? неверно.",
            "Everyone is here, isn't he? — нужен **aren't they?**",
        ],
        remember="Утверждение → отрицательный tag. Отрицание → положительный. Повторяют aux/be/modal.",
    ),
}
