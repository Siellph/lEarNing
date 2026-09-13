"""Enriched B1 grammar theory (Russian explanations, English examples)."""

from app.seed.helpers import ex, lesson, rule

B1_THEORY = {
    "present-perfect-vs-past-simple": lesson(
        "Оба времени смотрят в прошлое, но точка опоры разная. Present Perfect связывает прошлое с настоящим: опыт, результат, ещё не закрытый период (today, this week, since, for). Past Simple относит событие к закрытому прошлому: yesterday, last March, in 2016, when I was a child. Для русского «я жил / я живу здесь уже…» выберите время по смыслу: этап закончился — Past Simple; ситуация всё ещё длится — Present Perfect.",
        [
            rule(
                "Present Perfect: период ещё открыт",
                "Have/has + V3. For + длительность, since + точка старта. Already / yet / just / ever / never. Вопрос How long have you…? — если ситуация не закончилась. Важен не календарь сам по себе, а связь с «сейчас».",
                [
                    ex("I've worked night shifts since April.", "Я работаю в ночную смену с апреля (и сейчас тоже)."),
                    ex("Have you finished the invoice yet?", "Ты уже доделал счёт?"),
                    ex("I've lived here for six years.", "Я живу здесь уже шесть лет."),
                ],
            ),
            rule(
                "Past Simple: период закрыт",
                "V2 / V-ed. Маркеры: ago, last, in + год, when + прошлое. How long did you…? — если период уже закончился. Точная дата прошлого обычно сильнее желания сказать «уже».",
                [
                    ex("I worked night shifts in 2022.", "Я работал в ночную в 2022-м (уже нет)."),
                    ex("She sent the invoice an hour ago.", "Она отправила счёт час назад."),
                    ex("I lived there for six years.", "Я жил там шесть лет (тот этап закончился)."),
                ],
            ),
            rule(
                "Один факт — два взгляда",
                "Gone vs been: He's gone to Riga (ещё там или в пути). He's been to Riga (был и вернулся). Опыт без даты — Perfect; та же поездка с датой — Past Simple.",
                [
                    ex("I've been to Lisbon twice.", "Я бывал в Лиссабоне дважды (опыт, даты не важны)."),
                    ex("I went to Lisbon in May.", "Я ездил в Лиссабон в мае (закрытая поездка)."),
                    ex("He isn't at his desk. He has gone to lunch.", "Его нет на месте: он ушёл на обед."),
                ],
            ),
            rule(
                "Как выбрать за 5 секунд",
                "Есть закрывающая дата или when-прошедшее? → Past Simple. Важен результат сейчас, опыт или since/for с незакрытой ситуацией? → Present Perfect. Не смешивайте yesterday с have/has + V3.",
                [
                    ex("I have lost my keys — I can't open the door.", "Результат важен сейчас."),
                    ex("I lost my keys yesterday, but I found them.", "Закрытая история с датой."),
                ],
            ),
        ],
        compare=[
            {"left": "I've lived here for six years.", "right": "I lived there for six years.", "note": "Всё ещё здесь vs тот этап закончился."},
            {"left": "Have you seen her today?", "right": "Did you see her yesterday?", "note": "Today ещё может быть открыт; yesterday уже закрыт."},
        ],
        watch_out=[
            "Не I've seen her yesterday / I've started the course last week.",
            "Не I live here since 2020 — нужен Present Perfect: I've lived.",
            "For + период (for three days), since + момент (since Monday), не наоборот.",
        ],
        remember="Есть дата-закрытие — Past Simple. Период ещё открыт или важен результат — Present Perfect.",
    ),
    "present-perfect-continuous": lesson(
        "Present Perfect Continuous (have/has been + V-ing) подчёркивает саму деятельность и её длительность до сейчас. Present Perfect Simple чаще ставит акцент на результат или количество. Русское «я уже два часа читаю» почти всегда Continuous. Глаголы состояния (know, own, like) в Continuous не ставят — для них Simple: I've known her since school.",
        [
            rule(
                "Форма",
                "I/you/we/they have been + V-ing. He/she/it has been + V-ing. Отрицание: haven't/hasn't been. Вопрос: Have you been waiting long?",
                [
                    ex("I've been editing this chapter all morning.", "Я всё утро правлю эту главу."),
                    ex("Has she been practising the solo?", "Она репетировала соло?"),
                    ex("We haven't been sleeping well.", "Мы плохо спим в последнее время."),
                ],
            ),
            rule(
                "Длительность и недавняя активность",
                "How long have you been…? for/since + процесс. Часто виден след: I'm tired because I've been running. Акцент на «занимался», не только на «сделал».",
                [
                    ex("I've been waiting for forty minutes.", "Я жду уже сорок минут."),
                    ex("She's been crying — her eyes are red.", "Она плакала: глаза красные."),
                ],
            ),
            rule(
                "Continuous vs Simple",
                "I've read five chapters — количество/результат. I've been reading all evening — процесс. Состояния: I've known, I've had this phone (не been knowing).",
                [
                    ex("I've read five chapters.", "Я прочитал пять глав."),
                    ex("I've been reading all evening.", "Я всё вечер читал."),
                    ex("I've known her since school.", "Я знаю её со школы."),
                ],
            ),
        ],
        compare=[
            {"left": "I've painted the wall.", "right": "I've been painting the wall.", "note": "Готово vs ещё в процессе / недавно этим занимался."},
        ],
        watch_out=[
            "Не I've been knowing / been wanting.",
            "Не путайте с Past Continuous: was painting — только прошлое без связи с сейчас.",
            "For/since остаются, но меняется акцент Simple/Continuous.",
        ],
        remember="Have/has been + V-ing — длительность и процесс до сейчас. Результат и число — чаще Simple.",
    ),
    "past-perfect": lesson(
        "Past Perfect нужен не «потому что прошлое», а потому что в прошлом уже есть точка, а другое действие было раньше неё. Форма одна для всех лиц: had + V3. Без второй прошлой точки обычно хватает Past Simple. Типичные маркеры: already, by the time, after, before, because.",
        [
            rule(
                "Форма had + V3",
                "Had не меняется по лицам: I/she/they had left. Отрицание hadn't. Вопрос: Had you…? Это «прошлое до прошлого».",
                [
                    ex("She had already left when I arrived.", "Когда я приехал, она уже ушла."),
                    ex("Had they booked the seats before Friday?", "Они забронировали места до пятницы?"),
                ],
            ),
            rule(
                "Порядок событий",
                "Сначала более раннее — Past Perfect, затем более позднее — Past Simple. By the time X happened, Y had already…. After/before помогают, но время всё равно должно быть логичным.",
                [
                    ex("By the time we got there, the film had started.", "К нашему приходу фильм уже начался."),
                    ex("I didn't call because I had lost my phone.", "Я не позвонил, потому что потерял телефон."),
                ],
            ),
            rule(
                "Когда Past Perfect не нужен",
                "Если события идут просто по порядку с then/after и смысл ясен, часто достаточно двух Past Simple. Past Perfect особенно полезен, когда порядок иначе легко перепутать.",
                [
                    ex("I opened the door and went in.", "Открыл дверь и вошёл — порядок ясен."),
                    ex("I realised I had opened the wrong door.", "Понял, что раньше открыл не ту дверь."),
                ],
            ),
        ],
        compare=[
            {"left": "When I arrived, she left.", "right": "When I arrived, she had left.", "note": "Ушла после приезда vs уже ушла к моменту приезда."},
        ],
        watch_out=[
            "Не ставьте Past Perfect во все подряд прошлые предложения.",
            "Has left — это Present Perfect; для «до прошлого» нужен had.",
            "After he had had breakfast звучит тяжело; иногда достаточно After he had breakfast.",
        ],
        remember="Had + V3 = раньше другой прошлой точки. Без второй точки чаще хватает Past Simple.",
    ),
    "future-continuous": lesson(
        "Future Continuous (will be + V-ing) показывает действие как процесс в будущей точке или вежливый вопрос о планах. Это не «просто будущее», а будущее-в-процессе: At 8 I'll be driving.",
        [
            rule(
                "Форма will be + V-ing",
                "Для всех лиц одинаково: I/she/they will be working. Отрицание won't be. Вопрос: Will you be using the room?",
                [
                    ex("At 8 I'll be driving home.", "В 8 я буду ехать домой."),
                    ex("Will you be using the meeting room at noon?", "Комната для переговоров в полдень тебе нужна?"),
                ],
            ),
            rule(
                "Процесс в будущей точке",
                "Часто с at this time tomorrow, at 8, when you arrive. Говорящий представляет действие длящимся, а не как точку-результат.",
                [
                    ex("This time tomorrow we'll be flying.", "Завтра в это время мы будем в полёте."),
                    ex("Don't call at 6 — I'll be having dinner.", "Не звони в 6: я буду ужинать."),
                ],
            ),
            rule(
                "Вежливые планы",
                "Will you be …? звучит мягче, чем прямой вопрос о намерении. Для уже решённых личных планов параллельно живут going to и Present Continuous.",
                [
                    ex("Will you be staying long?", "Вы надолго?"),
                    ex("I'll be working from home next week.", "На следующей неделе я буду работать из дома."),
                ],
            ),
        ],
        compare=[
            {"left": "I'll call you at 8.", "right": "I'll be driving at 8.", "note": "Точка-обещание vs процесс в этот час."},
        ],
        watch_out=[
            "Will be go — нужна форма V-ing.",
            "Не путайте с Future Perfect (will have + V3).",
            "Will you be…? — не то же самое, что Are you going to…?, хотя темы пересекаются.",
        ],
        remember="Will be + V-ing — процесс в будущей точке или мягкий вопрос о занятости.",
    ),
    "second-conditional": lesson(
        "Second Conditional описывает нереальное или маловероятное настоящее/будущее: If I had more time, I would travel. В if-части — Past Simple (по форме), в главной — would + V1. Это не рассказ о прошлом.",
        [
            rule(
                "Структура",
                "If + Past Simple, would + V1. Were часто предпочитают для all persons в формальном стиле: If I were you. Would можно заменить на could/might по смыслу.",
                [
                    ex("If I had more time, I would travel more.", "Если бы у меня было больше времени, я бы больше путешествовал."),
                    ex("If I were you, I'd talk to her.", "На твоём месте я бы с ней поговорил."),
                ],
            ),
            rule(
                "Смысл нереальности",
                "Условие сейчас неверно или маловероятно. Русское «если бы» часто ведёт сюда. Не ставьте would в if-часть в стандартном Second Conditional.",
                [
                    ex("If she lived nearer, we'd meet more often.", "Если бы она жила ближе, мы бы чаще встречались."),
                    ex("If it snowed in July, I'd be shocked.", "Если бы в июле выпал снег, я бы удивился."),
                ],
            ),
            rule(
                "Вежливые гипотезы",
                "Would you mind… / If you could… звучат мягче прямой просьбы. Could в главной части — возможность, не только would.",
                [
                    ex("If you could send the file today, that would help.", "Если сможешь отправить файл сегодня, это поможет."),
                    ex("I would buy it if it were cheaper.", "Я бы купил, если бы было дешевле."),
                ],
            ),
        ],
        compare=[
            {"left": "If it rains, we'll stay in.", "right": "If it rained, we would stay in.", "note": "Реальное будущее vs гипотеза."},
        ],
        watch_out=[
            "If I would have… — не стандартный Second Conditional.",
            "If I was you встречается, но If I were you безопаснее в учебном стиле.",
            "Не путайте с Third Conditional (had + V3 / would have + V3).",
        ],
        remember="If + Past, would + V1. Форма прошедшая, смысл — нереальное сейчас/будущее.",
    ),
    "third-conditional": lesson(
        "Third Conditional говорит о нереальном прошлом: условие уже не изменить. If + Past Perfect, would have + V3. Часто это сожаление или анализ ошибки.",
        [
            rule(
                "Структура",
                "If + had + V3, would have + V3. Could have / might have — варианты силы. Обе части про прошлое, которого не было.",
                [
                    ex("If I had left earlier, I would have caught the train.", "Если бы я вышел раньше, успел бы на поезд."),
                    ex("If she had studied, she might have passed.", "Если бы она занималась, могла бы сдать."),
                ],
            ),
            rule(
                "Сожаление и критика",
                "Типичный смысл: жаль, что так вышло. I wouldn't have said that if I had known. Не смешивайте с Second без причины (это уже mixed).",
                [
                    ex("I wouldn't have said that if I had known.", "Я бы этого не сказал, если бы знал."),
                    ex("If we had booked sooner, we would have found seats.", "Если бы забронировали раньше, нашли бы места."),
                ],
            ),
            rule(
                "Сокращения и порядок",
                "I'd have / she'd have часто звучат в речи. If-часть может быть второй: We would have called if we had seen the message.",
                [
                    ex("I'd have helped if I'd seen your message.", "Помог бы, если бы увидел сообщение."),
                    ex("We would have called if we had seen the message.", "Позвонили бы, если бы увидели сообщение."),
                ],
            ),
        ],
        compare=[
            {"left": "If I had time, I would help.", "right": "If I had had time, I would have helped.", "note": "Нереальное сейчас vs нереальное прошлое."},
        ],
        watch_out=[
            "If I would have known — распространённая ошибка; нужно If I had known.",
            "Would have в if-части в стандартном Third не ставят.",
            "Не сокращайте так, чтобы пропал have: I'd helped ≠ I'd have helped.",
        ],
        remember="If + had + V3, would have + V3. Нереальное прошлое и часто сожаление.",
    ),
    "modals-possibility": lesson(
        "Модальные возможности B1 различают силу гипотезы: must (почти уверен), may/might/could (возможно), can't (почти исключено). Речь не о разрешении can, а о выводе из фактов.",
        [
            rule(
                "Must / can't для вывода",
                "Must = логически почти наверняка. Can't = логически почти невозможно. Это про сейчас/общее заключение, не про обязанность must из A2.",
                [
                    ex("He's not answering. He must be busy.", "Он не отвечает. Должно быть, он занят."),
                    ex("That can't be her car — it's the wrong colour.", "Это не может быть её машина: цвет не тот."),
                ],
            ),
            rule(
                "May / might / could",
                "Возможность без уверенности. Might часто чуть слабее may. Could = возможно (не путать с прошлым умением could).",
                [
                    ex("She may be at lunch.", "Возможно, она на обеде."),
                    ex("It might rain later.", "Позже может пойти дождь."),
                    ex("The keys could be in your coat.", "Ключи могут быть в пальто."),
                ],
            ),
            rule(
                "Continuous и perfect после модальных",
                "Must be waiting / might be working — процесс. Must have left / might have forgotten — вывод о прошлом (модальный + have + V3).",
                [
                    ex("She must be waiting outside.", "Она, должно быть, ждёт снаружи."),
                    ex("He might have forgotten the meeting.", "Он мог забыть о встрече."),
                ],
            ),
        ],
        compare=[
            {"left": "She must be at work.", "right": "She has to be at work at 9.", "note": "Вывод vs обязанность по правилам."},
        ],
        watch_out=[
            "Mustn't для логического отрицания обычно не подходит; берите can't.",
            "Can be в смысле «возможно» слабее учебного may/might.",
            "Must have + V3 — про прошлый вывод, не Present Perfect «просто так».",
        ],
        remember="Must/can't — сильный вывод. May/might/could — возможность. Для прошлого: modal + have + V3.",
    ),
    "reported-statements": lesson(
        "В косвенной речи утверждений сдвигаются местоимения, время (backshift) и маркеры времени/места. Say и tell различаются по наличию объекта: tell somebody, say something (to somebody).",
        [
            rule(
                "Backshift",
                "Present → Past, Present Perfect/Past → Past Perfect, will → would, can → could. Если факт всё ещё истинен, сдвиг иногда не делают, но на B1 отрабатывайте стандартный сдвиг.",
                [
                    ex("«I'm tired.» → She said she was tired.", "«Я устала.» → Она сказала, что устала."),
                    ex("«I've finished.» → He said he had finished.", "«Я закончил.» → Он сказал, что закончил."),
                ],
            ),
            rule(
                "Say vs tell",
                "Tell + person: She told me the news. Say без обязательного лица: She said the news was bad. / She said to me… Tell the truth / tell a story — устойчивые сочетания.",
                [
                    ex("She told me she was leaving.", "Она сказала мне, что уходит."),
                    ex("He said he needed more time.", "Он сказал, что ему нужно больше времени."),
                ],
            ),
            rule(
                "Маркеры времени и места",
                "Today → that day, tomorrow → the next day, yesterday → the day before, here → there, this → that. Не копируйте прямую речь дословно без сдвига.",
                [
                    ex("«I'll call tomorrow.» → She said she would call the next day.", "«Позвоню завтра.» → Сказала, что позвонит на следующий день."),
                ],
            ),
        ],
        compare=[
            {"left": "She said she was ill.", "right": "She told me she was ill.", "note": "Say без обязательного объекта; tell — с адресатом."},
        ],
        watch_out=[
            "She said me… — ошибка; нужно told me или said to me.",
            "Не забывайте сдвигать will → would.",
            "Кавычки в косвенной речи не ставят.",
        ],
        remember="Сдвигайте время и маркеры. Tell + человек. Say + содержание.",
    ),
    "reported-questions": lesson(
        "Косвенные вопросы теряют инверсию прямого вопроса: порядок как в утверждении. If/whether — для общих вопросов; Wh-слово сохраняется для специальных. Сдвиг времён тот же, что в утверждениях.",
        [
            rule(
                "Wh-вопросы",
                "Ask + wh + clause: He asked where she lived. Не He asked where did she live. Вспомогательный do/does/did обычно исчезает.",
                [
                    ex("«Where do you live?» → He asked where I lived.", "Спросил, где я живу."),
                    ex("«What has she bought?» → They asked what she had bought.", "Спросили, что она купила."),
                ],
            ),
            rule(
                "Yes/No через if/whether",
                "He asked if I was ready. Whether звучит чуть формальнее и удобнее при or not.",
                [
                    ex("«Are you ready?» → She asked if I was ready.", "Спросила, готов ли я."),
                    ex("He asked whether we needed help or not.", "Спросил, нужна ли нам помощь."),
                ],
            ),
            rule(
                "Ask / wonder / want to know",
                "Глаголы ввода: ask, wonder, want to know. После них нет вопросительного знака и нет инверсии.",
                [
                    ex("I wondered why they were late.", "Я думал, почему они опаздывают."),
                    ex("She wanted to know how to get to the depot.", "Она хотела узнать, как проехать до депо."),
                ],
            ),
        ],
        compare=[
            {"left": "Where do you work?", "right": "She asked where I worked.", "note": "Прямой вопрос с инверсией vs косвенный без инверсии."},
        ],
        watch_out=[
            "He asked where did I live — лишний did и инверсия.",
            "Не оставляйте ? в конце косвенного вопроса.",
            "If/whether нужны для yes/no, не для wh.",
        ],
        remember="Косвенный вопрос = Wh/if + порядок утверждения. Времена обычно сдвигаются.",
    ),
    "passive-all-simple": lesson(
        "На B1 пассив расширяется на Perfect и модальные: has been + V3, will be + V3, must be + V3. Фокус по-прежнему на пациенсе и результате, а не на деятеле.",
        [
            rule(
                "Линейка простых пассивов",
                "Present: is cleaned. Past: was cleaned. Perfect: has been cleaned. Future: will be cleaned. Везде be нужного времени + V3.",
                [
                    ex("The report has been sent.", "Отчёт уже отправили."),
                    ex("The hall will be painted next week.", "Зал покрасят на следующей неделе."),
                ],
            ),
            rule(
                "Модальный пассив",
                "Modal + be + V3: It must be finished today. The form can be downloaded. Отрицание: can't be / mustn't be — по смыслу.",
                [
                    ex("It must be finished today.", "Это должно быть закончено сегодня."),
                    ex("Tickets can be bought online.", "Билеты можно купить онлайн."),
                ],
            ),
            rule(
                "Когда выбирать пассив",
                "Деятель неизвестен, неважен или очевиден; важен объект/процесс. By добавляйте только если источник действия значим.",
                [
                    ex("My phone was stolen on the train.", "Телефон украли в поезде."),
                    ex("The song was written by a teenager.", "Песню написал подросток."),
                ],
            ),
        ],
        compare=[
            {"left": "Someone has sent the report.", "right": "The report has been sent.", "note": "Актив с someone vs пассив с результатом."},
        ],
        watch_out=[
            "Has been send — нужна V3: sent.",
            "Must be finish — must be finished.",
            "Не теряйте been в Perfect Passive.",
        ],
        remember="Be нужного времени + V3. Perfect: has/have been + V3. Modal: modal + be + V3.",
    ),
    "defining-nondefining": lesson(
        "Defining relative clauses уточняют, о ком/чём речь, и без них смысл ломается. Non-defining дают дополнительную информацию и выделяются запятыми; that в них обычно не используют.",
        [
            rule(
                "Defining — без запятых",
                "The students who arrived late missed the test. Which/that/who возможны (в пределах стиля). Без придаточного непонятно, какие именно students.",
                [
                    ex("The students who arrived late missed the test.", "Студенты, которые опоздали, пропустили тест."),
                    ex("I need the file that you sent yesterday.", "Мне нужен файл, который ты вчера прислал."),
                ],
            ),
            rule(
                "Non-defining — с запятыми",
                "My sister, who lives in Oslo, is visiting. Это добавка; сестра и так идентифицирована. That здесь обычно не ставят.",
                [
                    ex("My sister, who lives in Oslo, is visiting.", "Моя сестра, которая живёт в Осло, приезжает."),
                    ex("Bergen, which is on the coast, gets a lot of rain.", "Берген, что на побережье, часто дождливый."),
                ],
            ),
            rule(
                "Пропуск местоимения",
                "В defining, если относительное слово — дополнение, его можно опустить: the book (that) I read. В non-defining пропуск недоступен.",
                [
                    ex("The book I read was excellent.", "Книга, которую я прочитал, была отличной."),
                    ex("This novel, which I read in June, was excellent.", "Этот роман, который я читал в июне, был отличным."),
                ],
            ),
        ],
        compare=[
            {"left": "My brother who lives abroad called.", "right": "My brother, who lives abroad, called.", "note": "Один из братьев vs единственный брат + добавка."},
        ],
        watch_out=[
            "That в non-defining с запятыми — плохой учебный стиль.",
            "Не ставьте запятые в defining, если без придаточного объект неясен.",
            "Which для людей в defining лучше заменить на who.",
        ],
        remember="Defining уточняет без запятых. Non-defining — добавка в запятых, без that.",
    ),
    "gerund-vs-infinitive": lesson(
        "После одних глаголов нужен -ing, после других — to-infinitive, а у части глаголов смена формы меняет смысл. На B1 полезнее выучить частые списки и пары-ловушки, чем искать одно «правило на всё».",
        [
            rule(
                "Глагол + -ing",
                "Enjoy, avoid, finish, suggest, keep, mind, consider + -ing. После предлога тоже -ing: interested in learning, good at swimming.",
                [
                    ex("I enjoy cooking at weekends.", "Мне нравится готовить по выходным."),
                    ex("She suggested taking a break.", "Она предложила сделать перерыв."),
                ],
            ),
            rule(
                "Глагол + to-infinitive",
                "Want, decide, hope, plan, promise, refuse, afford, learn + to + V1. Цель: I went to the shop to buy milk.",
                [
                    ex("We decided to leave early.", "Мы решили уйти пораньше."),
                    ex("He hopes to find a new flat.", "Он надеется найти новую квартиру."),
                ],
            ),
            rule(
                "Пары со сменой смысла",
                "Stop doing — перестать делать. Stop to do — остановиться, чтобы сделать. Remember doing — помню, как делал. Remember to do — не забыть сделать. Try doing — попробовать способ. Try to do — пытаться (есть трудность).",
                [
                    ex("I stopped smoking last year.", "Я бросил курить в прошлом году."),
                    ex("I stopped to buy water.", "Я остановился, чтобы купить воду."),
                    ex("Remember to lock the door.", "Не забудь закрыть дверь."),
                ],
            ),
        ],
        compare=[
            {"left": "I remembered locking the door.", "right": "I remembered to lock the door.", "note": "Помню, как закрывал vs не забыл закрыть."},
        ],
        watch_out=[
            "Suggest to go — обычно suggest going.",
            "После предлога to как предлога (look forward to) нужен -ing: look forward to seeing.",
            "Не путайте to (частица инфинитива) и to (предлог).",
        ],
        remember="Списки + пары stop/remember/try. После предлога — -ing.",
    ),
    "wish-past-simple": lesson(
        "I wish / if only + Past Simple выражает желание изменить настоящее или будущее. Форма прошедшая, смысл — сейчас. Для сожаления о прошлом позже появится wish + Past Perfect.",
        [
            rule(
                "Wish + Past Simple",
                "I wish I knew. She wishes she had a car. Were часто для всех лиц: I wish I were taller. If only звучит эмоциональнее.",
                [
                    ex("I wish I knew the answer.", "Жаль, что я не знаю ответа."),
                    ex("If only it weren't so noisy.", "Если бы только не было так шумно."),
                ],
            ),
            rule(
                "Wish + would",
                "I wish you would stop interrupting — раздражение или желание, чтобы кто‑то изменил поведение. Не для собственных привычек: не I wish I would…",
                [
                    ex("I wish you would listen.", "Хоть бы ты слушал."),
                    ex("I wish it would stop raining.", "Хоть бы дождь закончился."),
                ],
            ),
            rule(
                "Не путать с надеждой",
                "I hope + Present/will — реальная надежда. I wish + Past — контрфакт. I hope you pass ≠ I wish you passed.",
                [
                    ex("I hope you pass the exam.", "Надеюсь, ты сдашь экзамен."),
                    ex("I wish I had more free time.", "Жаль, что у меня мало свободного времени."),
                ],
            ),
        ],
        compare=[
            {"left": "I hope she calls.", "right": "I wish she called more often.", "note": "Реальная надежда vs желание изменить привычку."},
        ],
        watch_out=[
            "I wish I know — нужна прошедшая форма knew.",
            "I wish I would be rich — для состояния берите Past: I wish I were rich.",
            "Wish + Past Perfect оставьте для прошлого сожаления.",
        ],
        remember="Wish + Past Simple — про нереальное сейчас. Wish + would — про чужое поведение.",
    ),
    "question-tags": lesson(
        "Question tags — короткий хвост-вопрос в конце фразы: It's cold, isn't it? Они проверяют ожидание согласия или смягчают тон. Обычно + утверждение → отрицательный tag, и наоборот.",
        [
            rule(
                "Базовый полярность",
                "You are ready, aren't you? She isn't late, is she? Вспомогательный глагол в tag повторяет время/модальность основной части.",
                [
                    ex("You're ready, aren't you?", "Ты готов, правда?"),
                    ex("She isn't late, is she?", "Она же не опаздывает?"),
                ],
            ),
            rule(
                "Do/does/did и особые случаи",
                "Если в основе нет aux/be/modal, берут do/does/did: You like jazz, don't you? I am → aren't I? Let's → shall we? Don't… → will you?",
                [
                    ex("You like jazz, don't you?", "Ты любишь джаз, да?"),
                    ex("I'm early, aren't I?", "Я рано, правда?"),
                    ex("Let's go, shall we?", "Пойдём, а?"),
                ],
            ),
            rule(
                "Тон и смысл",
                "Нисходящий тон — ожидание согласия. Восходящий — более настоящий вопрос. There is → isn't there? Someone / everyone → they в tag.",
                [
                    ex("There's a problem, isn't there?", "Проблема есть, правда?"),
                    ex("Everyone agreed, didn't they?", "Все согласились, да?"),
                ],
            ),
        ],
        compare=[
            {"left": "You can drive, can't you?", "right": "You can't drive, can you?", "note": "Полярность tag зеркалит основу."},
        ],
        watch_out=[
            "You are ready, are you? как обычный confirming tag без особого тона звучит иначе; учебный default — aren't you?",
            "I am, aren't I — исключение.",
            "Не повторяйте смысловой глагол в tag: like you? неверно.",
        ],
        remember="Утверждение → отрицательный tag. Отрицание → положительный. Повторяйте aux/be/modal.",
    ),
}
