from app.seed.helpers import err, ex, fill, lesson, mc, module, rule, xf

A2 = [
    module(
        "present-simple-vs-continuous",
        "Present Simple и Present Continuous",
        "Привычка и факт против действия «прямо сейчас» и временной ситуации.",
        22,
        "Какое настоящее выбрать",
        lesson(
            "На A1 времена учили по отдельности. На A2 нужно выбирать: привычка и постоянный факт — Present Simple; действие в развитии или временный период — Present Continuous. Русское «я работаю» закрывает оба смысла, поэтому опора — не перевод, а вопрос: это вообще так или именно сейчас?",
            [
                rule(
                    "Present Simple: каркас жизни",
                    "I/you/we/they + V1; he/she/it + -s. Привычки, расписания, научные факты, постоянная работа и характер. Маркеры: always, usually, every day, on Mondays.",
                    [
                        ex("She teaches maths at a college.", "Она преподаёт математику в колледже (постоянно)."),
                        ex("The ferry leaves at 7.15.", "Паром отходит в 7.15 (расписание)."),
                    ],
                ),
                rule(
                    "Present Continuous: сейчас и временно",
                    "am/is/are + V-ing. Действие в момент речи, временная ситуация, изменение. Маркеры: now, at the moment, today, this week, Look!",
                    [
                        ex("I'm packing a suitcase at the moment.", "Я сейчас собираю чемодан."),
                        ex("He's staying with his aunt this month.", "В этом месяце он живёт у тёти."),
                    ],
                ),
                rule(
                    "Глаголы состояния",
                    "Know, like, love, hate, want, need, believe, belong, own, understand обычно не ставят в Continuous. Have в значении «владеть» — Simple; have dinner / have a shower — может быть Continuous.",
                    [
                        ex("I understand the rule now.", "Я сейчас понимаю правило (не am understanding)."),
                        ex("We're having lunch, can I call you later?", "Мы обедаем — здесь have = есть."),
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
                "В вопросе Continuous нужен be, не do: Are you waiting? не Do you waiting?",
            ],
            remember="Привычка и факт — Simple. Сейчас и временно — Continuous. Состояния почти всегда Simple.",
        ),
        [
            mc("Сейчас за окном шум: Listen! The neighbours ___ a party.", ["have", "are having", "has"], "are having", "Listen! указывает на действие в момент речи; have a party допускает Continuous."),
            fill("She usually ___ to work, but today she ___ the tram. (cycle / take)", "cycles / is taking", "Привычка — Simple, сегодня — Continuous.", ["cycles/is taking", "cycles, is taking"]),
            err("I am knowing his name.", "I know his name.", "Know — глагол состояния, Continuous не нужен."),
            xf("Сделайте Continuous: He writes an email now.", "He is writing an email now.", "be + V-ing для «сейчас».", ["He's writing an email now"]),
            fill("The museum ___ at six every day. (close)", "closes", "Расписание — Present Simple, 3-е лицо + -s."),
            mc("I ___ this soup. It's too salty.", ["am not liking", "don't like", "not like"], "don't like", "Like — состояние; отрицание через don't."),
        ],
        [
            mc("This week we ___ late because of a deadline.", ["stay", "are staying", "stays"], "are staying", "This week + временная ситуация."),
            fill("Water ___ at 100°C. (boil)", "boils", "Научный факт — Simple."),
            err("Do you waiting for the bus?", "Are you waiting for the bus?", "В Continuous вопрос начинается с am/is/are."),
            xf("Отрицание Continuous: They are using my charger.", "They aren't using my charger.", "not после be.", ["They are not using my charger", "They're not using my charger"]),
            fill("He ___ the answer, he just needs time. (know)", "knows", "Know не ставят в Continuous."),
            mc("On Sundays she ___ her grandparents. (привычка)", ["visits", "is visiting", "visit"], "visits", "Регулярное действие — Simple + -s."),
        ],
    ),
    module(
        "past-continuous",
        "Past Continuous",
        "Действие в развитии в прошлом и фон для Past Simple.",
        20,
        "Что происходило в тот момент",
        lesson(
            "Past Continuous (was/were + V-ing) показывает процесс в конкретной точке прошлого. Часто он рисует фон, а Past Simple сообщает, что его прервало. Русское «я смотрел фильм, когда…» как раз про эту пару.",
            [
                rule(
                    "Форма",
                    "I/he/she/it was + V-ing. You/we/they were + V-ing. Отрицание: wasn't / weren't. Вопрос: Was she sleeping? Were you driving?",
                    [
                        ex("At 9 p.m. I was still editing the slides.", "В 9 вечера я всё ещё правил слайды."),
                        ex("They weren't listening to the announcement.", "Они не слушали объявление."),
                    ],
                ),
                rule(
                    "Прерванное действие",
                    "Длительное действие — Continuous; короткое событие — Past Simple. While чаще с Continuous, when — с любой частью, но часто с прерывающим Simple.",
                    [
                        ex("I was boiling pasta when the lights went out.", "Я варил пасту, когда погас свет."),
                        ex("While we were queuing, it started to rain.", "Пока мы стояли в очереди, начался дождь."),
                    ],
                ),
                rule(
                    "Два параллельных процесса",
                    "Если оба действия длились одновременно, оба могут быть в Continuous. Законченное событие в прошлом без «фона» — только Past Simple.",
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
                "Не ставьте Past Continuous на короткие завершённые действия: не I was breaking the cup, если чашка просто упала.",
                "When he was arriving звучит странно, если прибытие — точка; лучше When he arrived.",
            ],
            remember="Was/were + -ing = процесс в прошлом. Точка-событие — Past Simple.",
        ),
        [
            fill("At 6.30 she ___ home. (still + drive)", "was still driving", "Конкретное время + процесс."),
            mc("I ___ a podcast when my phone died.", ["listened", "was listening", "were listening"], "was listening", "Фон в Continuous, I + was."),
            err("They was waiting outside.", "They were waiting outside.", "They сочетается с were."),
            xf("Вопрос: He was repairing the tap.", "Was he repairing the tap?", "Was выходит перед подлежащим."),
            fill("While we ___ , the kettle boiled. (talk)", "were talking", "While + Continuous для фона."),
            mc("She opened the door and ___ the parcel. (факт)", ["was taking", "took", "taken"], "took", "Короткое завершённое действие — Past Simple."),
        ],
        [
            fill("We ___ attention, so we missed the stop. (not + pay, Past Continuous)", "weren't paying", "We + were; отрицание перед V-ing.", ["were not paying"]),
            mc("___ you sleeping when I texted?", ["Was", "Were", "Did"], "Were", "You + were в Continuous."),
            err("I was break the glass when I washed up.", "I broke the glass when I was washing up.", "Разбить — точка (Past Simple); мыть посуду — фон (Continuous).", ["I broke the glass while I was washing up"]),
            xf("Отрицание: She was wearing a helmet.", "She wasn't wearing a helmet.", "wasn't + V-ing.", ["She was not wearing a helmet"]),
            fill("He ___ an email when the client called. (write)", "was writing", "Прерванный процесс."),
            mc("Yesterday I ___ the whole series. (законченный факт)", ["was watching", "watched", "were watching"], "watched", "Без точки-процесса — Past Simple."),
        ],
    ),
    module(
        "present-perfect-intro",
        "Present Perfect: первое знакомство",
        "Have/has + V3: опыт, результат сейчас, already / just / yet / ever / never.",
        24,
        "Связь прошлого с настоящим",
        lesson(
            "Present Perfect соединяет прошлое с сейчас. Русского близнеца нет: «я уже отправил» может быть и I've sent, и I sent. На A2 держите три опоры: опыт за жизнь, видимый результат и маркеры just / already / yet / ever / never. Точное прошедшее время (yesterday, in 2019) пока не ставьте в это время — это ловушка.",
            [
                rule(
                    "Форма",
                    "I/you/we/they have + V3. He/she/it has + V3. Краткие: I've, she's, they've. Отрицание: haven't / hasn't. Вопрос: Have you…? Has she…? Правильные глаголы: V3 = V-ed. Неправильные: go—gone, see—seen, write—written, eat—eaten, do—done.",
                    [
                        ex("I've booked the tickets.", "Я забронировал билеты (они уже есть)."),
                        ex("She hasn't finished the report yet.", "Она ещё не закончила отчёт."),
                    ],
                ),
                rule(
                    "Опыт и результат",
                    "Опыт: когда именно — неважно. Результат: прошлое действие важно сейчас. Ever/never типичны для опыта; just — только что.",
                    [
                        ex("Have you ever ridden a horse?", "Ты когда-нибудь ездил верхом?"),
                        ex("He's just left, so the office is empty.", "Он только что ушёл — офис пустой."),
                    ],
                ),
                rule(
                    "Already, yet, never",
                    "Already обычно в утверждении (часто перед V3). Yet — в вопросах и отрицаниях, ближе к концу. Never = ни разу за жизнь, глагол остаётся утвердительным: I have never tried.",
                    [
                        ex("We've already eaten, thanks.", "Мы уже поели, спасибо."),
                        ex("I have never tried kimchi.", "Я никогда не пробовал кимчи."),
                    ],
                ),
            ],
            compare=[
                {"left": "I've lost my pass — I can't get in.", "right": "I lost my pass last Tuesday and got a new one.", "note": "Результат сейчас vs законченная история с датой."},
            ],
            watch_out=[
                "Не I've seen her yesterday — с yesterday нужен Past Simple.",
                "Не I have went / I have ate — нужна 3-я форма: gone, eaten.",
                "He have — ошибка: he/she/it + has.",
            ],
            remember="Have/has + V3. Опыт и результат сейчас. Точная дата прошлого — не сюда.",
        ),
        [
            fill("She ___ the kitchen. (just + clean, Present Perfect)", "has just cleaned", "Just обычно между have/has и V3.", ["she's just cleaned"]),
            mc("___ you ever visited Georgia?", ["Did", "Have", "Has"], "Have", "You + have в вопросе об опыте."),
            err("I have saw that film.", "I have seen that film.", "See — saw — seen; после have нужна V3.", ["I've seen that film"]),
            xf("Отрицание с yet: They have paid the bill.", "They haven't paid the bill yet.", "haven't + V3 + yet.", ["They have not paid the bill yet"]),
            fill("He ___ sushi. (never + try, Present Perfect)", "has never tried", "Never стоит между has и V3; 3-е лицо — has.", ["he's never tried"]),
            mc("We ___ the keys, so we can go in now.", ["lost", "have lost", "are losing"], "have lost", "Результат важен сейчас — дверь можно открыть."),
        ],
        [
            fill("I ___ to the manager. (already + speak, Present Perfect)", "have already spoken", "Speak — spoke — spoken; already перед V3.", ["I've already spoken"]),
            mc("Has she ___ the email yet?", ["wrote", "written", "write"], "written", "После has — V3."),
            err("They has finished the test.", "They have finished the test.", "They + have."),
            xf("Вопрос: You have met her parents.", "Have you met her parents?", "Have перед подлежащим."),
            fill("___ he arrived yet?", "Has", "He + Has в вопросе."),
            mc("I ___ Rome in 2018. (дата)", ["have visited", "visited", "am visiting"], "visited", "Год — Past Simple, не Present Perfect."),
        ],
    ),
    module(
        "will-vs-going-to",
        "Will и be going to",
        "Спонтанное решение и обещание против плана и приметы.",
        20,
        "Два способа сказать о будущем",
        lesson(
            "Русское «я сделаю» не подсказывает выбор. Will — решение в момент речи, обещание, предложение и прогноз «по мнению». Be going to — уже принятый план или будущее, которое видно по приметам. На A2 этого контраста достаточно.",
            [
                rule(
                    "Will / won't",
                    "Will + V1 для всех лиц. Краткие: I'll, she'll, we'll. Отрицание: won't. Типично: I think / I'm sure / probably + will. Спонтанно: The phone's ringing. I'll get it.",
                    [
                        ex("It's dark. I'll turn on the lamp.", "Темно. Сейчас включу лампу (решил сейчас)."),
                        ex("I won't forget your book.", "Я не забуду твою книгу (обещание)."),
                    ],
                ),
                rule(
                    "Be going to",
                    "am/is/are + going to + V1. План уже есть до разговора. Предсказание по видимому: Look at those bags — she's going to drop them.",
                    [
                        ex("We're going to repaint the kitchen in May.", "Мы собираемся перекрасить кухню в мае (план)."),
                        ex("The sky is yellow-grey. It's going to storm.", "Небо жёлто-серое. Будет гроза (примета)."),
                    ],
                ),
                rule(
                    "Shall и вежливость",
                    "Shall I/we…? — предложение помощи или совместного действия в британском варианте. Will you…? — просьба. Для чистого плана shall не нужен.",
                    [
                        ex("Shall I save you a seat?", "Тебе место придержать?"),
                        ex("Will you send me the link?", "Пришлёшь ссылку?"),
                    ],
                ),
            ],
            compare=[
                {"left": "I'll have the mushroom soup.", "right": "I'm going to have soup — I brought a flask.", "note": "Заказ в кафе vs план, который уже был."},
            ],
            watch_out=[
                "Не I will to call и не I'm going call — после will глагол без to; после going нужен to.",
                "Не ставьте will только потому, что действие в будущем: заранее обдуманный план чаще going to.",
                "Won't = will not, не want.",
            ],
            remember="Решил сейчас / обещаю — will. Уже планировал или вижу примету — going to.",
        ),
        [
            mc("The bag is open. Those apples ___ fall out.", ["will", "are going to", "going"], "are going to", "Видимая примета — going to."),
            fill("It's stuffy in here. I ___ open a window. (спонтанно)", "I'll", "Решение в момент речи — will.", ["I will", "will"]),
            err("She will to help us tomorrow.", "She will help us tomorrow.", "После will — голый инфинитив."),
            xf("Отрицание: I will tell anyone.", "I won't tell anyone.", "won't = will not.", ["I will not tell anyone"]),
            fill("They ___ going to launch the app in June.", "are", "They + are going to."),
            mc("___ I carry that box for you?", ["Will", "Shall", "Do"], "Shall", "Shall I…? — предложение помощи."),
        ],
        [
            fill("Look at the time! We ___ miss the train. (примета)", "are going to", "Опоздание уже видно — going to.", ["'re going to"]),
            mc("I forgot sugar. I ___ buy some on the way.", ["am going to", "will", "going to"], "will", "Решение возникло только что."),
            err("He going to start at nine.", "He is going to start at nine.", "Нужен is.", ["He's going to start at nine"]),
            xf("Вопрос о плане: You are going to sell the bike.", "Are you going to sell the bike?", "Are на первое место."),
            fill("I promise I ___ be late. (отрицание)", "won't", "Обещание — will/won't.", ["will not"]),
            mc("We've already booked the cabin. We ___ there in August.", ["will stay", "are going to stay", "stay"], "are going to stay", "Бронь = заранее принятый план."),
        ],
    ),
    module(
        "comparatives",
        "Сравнительная степень",
        "Older / more careful и конструкция as … as.",
        18,
        "Как сравнить два объекта",
        lesson(
            "Сравнительная степень отвечает на вопрос «кто/что больше, лучше, удобнее». Короткие прилагательные обычно берут -er, длинные — more. После сравнения почти всегда than, не then. Равенство — as … as.",
            [
                rule(
                    "Короткие прилагательные",
                    "Один слог: cheap → cheaper, tall → taller. Согласная + гласная + согласная: big → bigger. -y после согласной: easy → easier, happy → happier.",
                    [
                        ex("This street is quieter than the main road.", "Эта улица спокойнее главной дороги."),
                        ex("The second task was easier than the first.", "Второе задание было легче первого."),
                    ],
                ),
                rule(
                    "Длинные и особые формы",
                    "Два и более слогов чаще с more: more useful, more expensive. Не ставьте more и -er вместе. Особые: good → better, bad → worse, far → further/farther.",
                    [
                        ex("Trains are more reliable than coaches on this route.", "Поезда надёжнее автобусов на этом маршруте."),
                        ex("Her Spanish is better than mine.", "Её испанский лучше моего."),
                    ],
                ),
                rule(
                    "As … as и less",
                    "Одинаково: as + adj + as. Неравенство вниз: not as … as или less + adj. После than местоимение чаще объектное в разговорной речи: than me; в аккуратной — than I am.",
                    [
                        ex("The sequel isn't as funny as the first film.", "Продолжение не такое смешное, как первый фильм."),
                        ex("This bag is less practical than a backpack.", "Эта сумка менее практична, чем рюкзак."),
                    ],
                ),
            ],
            watch_out=[
                "More better / more cheaper — двойная степень, так нельзя.",
                "Than, не then: older than me.",
                "Не more easy — нужно easier.",
            ],
            remember="-er или more, затем than. Равенство — as … as. Good → better.",
        ),
        [
            fill("My laptop is ___ than yours. (light)", "lighter", "Один слог + -er."),
            mc("This hotel is ___ than the hostel.", ["more cheap", "cheaper", "more cheaper"], "cheaper", "Cheap — короткий; more cheaper — ошибка."),
            err("She is more taller than her brother.", "She is taller than her brother.", "Нельзя more + -er."),
            xf("Сравните: The red bag is 20€. The blue bag is 35€. (expensive)", "The blue bag is more expensive than the red bag.", "Длинное прилагательное — more + than."),
            fill("Today is ___ than yesterday. (good)", "better", "Good → better."),
            mc("This puzzle is ___ the last one.", ["as hard as", "harder as", "more hard than"], "as hard as", "Равенство — as … as."),
        ],
        [
            fill("The evenings are getting ___. (dark)", "darker", "Один слог + -er."),
            mc("His explanation was ___ than the textbook.", ["clearer", "more clearer", "clear more"], "clearer", "Clear берёт -er."),
            err("This film is funnier then the book.", "This film is funnier than the book.", "Нужен than, не then."),
            xf("Равенство: My tea is hot. Your tea is hot too.", "My tea is as hot as your tea.", "as + adj + as.", ["My tea is as hot as yours"]),
            fill("Winter here is ___ than on the coast. (bad)", "worse", "Bad → worse."),
            mc("Online tickets are ___ paper ones.", ["more convenient than", "conveniencier than", "more convenient as"], "more convenient than", "Длинное прилагательное + than."),
        ],
    ),
    module(
        "superlatives",
        "Превосходная степень",
        "The oldest / the most popular и выбор in / of.",
        18,
        "Самый в группе",
        lesson(
            "Превосходная степень выделяет один объект из группы. Почти всегда нужен the. Короткие прилагательные берут -est, длинные — the most. Группу задают in (место, организация) или of (набор: of all, of the three).",
            [
                rule(
                    "Форма",
                    "cheap → the cheapest, big → the biggest, easy → the easiest. Длинные: the most comfortable. Особые: the best, the worst, the furthest/farthest.",
                    [
                        ex("This is the cheapest charger in the shop.", "Это самое дешёвое зарядное в магазине."),
                        ex("Monday was the worst day of the week.", "Понедельник был худшим днём недели."),
                    ],
                ),
                rule(
                    "In и of",
                    "In + место или коллектив: in Europe, in our class, in the building. Of + конкретный набор: of all my cousins, of the two options (хотя для двух чаще comparative).",
                    [
                        ex("She's the youngest person in the team.", "Она самый молодой человек в команде."),
                        ex("This photo is the sharpest of the three.", "Этот снимок самый резкий из трёх."),
                    ],
                ),
                rule(
                    "One of the + множественное",
                    "One of the + превосходная + существительное во множественном: one of the best cafés. Не one of the best café.",
                    [
                        ex("It's one of the oldest bridges in the city.", "Это один из старейших мостов в городе."),
                    ],
                ),
            ],
            compare=[
                {"left": "This bag is cheaper than that one.", "right": "This is the cheapest bag in the sale.", "note": "Два объекта — comparative; вся распродажа — superlative."},
            ],
            watch_out=[
                "Не the most cheapest — одна степень, не две.",
                "Не забывайте the: не She is tallest.",
                "После one of the — множественное число существительного.",
            ],
            remember="The + -est / the most. Место — in, набор — of. Good → the best.",
        ),
        [
            fill("This is ___ river in the country. (long)", "the longest", "The + -est для короткого прилагательного."),
            mc("It's ___ restaurant we've tried here.", ["the more expensive", "the most expensive", "most expensive the"], "the most expensive", "Длинное прилагательное — the most."),
            err("He is the most youngest in the family.", "He is the youngest in the family.", "Нельзя most + -est."),
            xf("Превосходная: This park is quiet. (in the district)", "This is the quietest park in the district.", "the + -est + in + место.", ["This park is the quietest in the district"]),
            fill("That was ___ film of the year. (good)", "the best", "Good → the best."),
            mc("It's one of the ___ streets in town.", ["busiest", "busyest", "most busy"], "busiest", "y → i + -est; после one of the — множественное streets уже в предложении."),
        ],
        [
            fill("Which is ___ building in your city? (tall)", "the tallest", "The + -est."),
            mc("This is the ___ of the four endings.", ["sadder", "saddest", "most sadder"], "saddest", "Из четырёх — превосходная; d удваивается."),
            err("She is nicest person in the office.", "She is the nicest person in the office.", "Нужен артикль the."),
            xf("one of / best / bakeries / the / city / in / the", "It's one of the best bakeries in the city.", "one of the + множественное.", ["one of the best bakeries in the city"]),
            fill("That joke was ___ of all. (bad)", "the worst", "Bad → the worst."),
            mc("He is the fastest runner ___ our club.", ["of", "in", "from"], "in", "Клуб как место/коллектив — in."),
        ],
    ),
    module(
        "countable-uncountable",
        "Исчисляемые и неисчисляемые",
        "A/an, множественное число и слова без -s: advice, information, furniture.",
        20,
        "Можно ли посчитать",
        lesson(
            "Исчисляемые имеют единственное и множественное число: a ticket — tickets. Неисчисляемые в общем смысле не берут a/an и не получают -s: rice, music, money. Для русских ловушка в словах, которые «звучат как много»: information, advice, furniture, homework, news, luggage — в английском они неисчисляемые.",
            [
                rule(
                    "Исчисляемые",
                    "Можно сказать a/an и числительное: an umbrella, three umbrellas. Вопрос: How many…?",
                    [
                        ex("I bought two notebooks and a pen.", "Я купил две тетради и ручку."),
                        ex("How many sockets are there?", "Сколько розеток?"),
                    ],
                ),
                rule(
                    "Неисчисляемые",
                    "Без a/an и без множественного в общем смысле. Нужна мера: a piece of advice, a bottle of water, a slice of bread. Вопрос: How much…?",
                    [
                        ex("We need more flour, not more bowls.", "Нужно больше муки, не больше мисок."),
                        ex("How much time do we have?", "Сколько у нас времени?"),
                    ],
                ),
                rule(
                    "Типичные «ложные множественные»",
                    "Advice, information, furniture, homework, news, money, luggage, progress, accommodation — без -s. Some news is… — согласование единственного. Hair в значении «волосы на голове» обычно неисчисляемое.",
                    [
                        ex("She gave me useful advice.", "Она дала мне полезный совет (не an advice)."),
                        ex("The furniture looks new.", "Мебель выглядит новой (не furnitures)."),
                    ],
                ),
            ],
            compare=[
                {"left": "a coffee (чашка в кафе)", "right": "coffee (напиток вообще)", "note": "Многие неисчисляемые становятся исчисляемыми, когда речь о порции."},
            ],
            watch_out=[
                "Не informations, advices, homeworks, furnitures, luggages.",
                "News выглядит как множественное, но: The news is good.",
                "Не a money / a bread — нужна мера или some.",
            ],
            remember="Можно посчитать штуки — a/an и -s. Вещество, абстракция, «ложные множественные» — без -s.",
        ),
        [
            mc("I need ___ about the visa.", ["an information", "some information", "informations"], "some information", "Information неисчисляемое — some, не a и не -s."),
            fill("She gave me two useful ___ . (совет как «штуки»)", "pieces of advice", "Штуки совета — pieces of advice.", ["bits of advice"]),
            err("The furnitures in this flat are old.", "The furniture in this flat is old.", "Furniture неисчисляемое, глагол в единственном."),
            xf("Сделайте исчисляемую порцию: I'd like water.", "I'd like a glass of water.", "Мера + неисчисляемое.", ["I'd like a bottle of water", "I'd like a cup of water"]),
            fill("How ___ chairs do we need?", "many", "Chairs исчисляемые — many."),
            mc("Your ___ is by the lift.", ["luggages", "luggage", "a luggages"], "luggage", "Luggage без -s."),
        ],
        [
            fill("How ___ milk is left?", "much", "Milk неисчисляемое — much."),
            mc("He has a lot of ___ to do this weekend.", ["homeworks", "homework", "a homework"], "homework", "Homework неисчисляемое."),
            err("I have a good news.", "I have some good news.", "News неисчисляемое — some, не a.", ["I have good news"]),
            xf("Множественное: This ticket is cheap.", "These tickets are cheap.", "Исчисляемое ticket → tickets, this→these, is→are."),
            fill("There isn't ___ bread.", "any", "Отрицание + неисчисляемое — any (или much).", ["much"]),
            mc("She has long dark ___.", ["hairs", "hair", "a hairs"], "hair", "Волосы на голове обычно hair без -s."),
        ],
    ),
    module(
        "quantifiers-a2",
        "Квантификаторы A2",
        "Some, any, much, many, a lot of, a few, a little, few, little.",
        22,
        "Сколько — и достаточно ли",
        lesson(
            "Квантификатор говорит о количестве без точной цифры. Выбор зависит от типа существительного и от того, утверждение это, вопрос или отрицание. Отдельная тонкость A2: a few / a little — «немного, но есть»; few / little без a — «мало, почти нет».",
            [
                rule(
                    "Some, any, a lot of",
                    "Some — утверждения и вежливые предложения/вопросы. Any — вопросы и отрицания. A lot of / lots of работает и с исчисляемыми, и с неисчисляемыми в утверждении.",
                    [
                        ex("We've got some spare plates.", "У нас есть запасные тарелки."),
                        ex("Have you got any change?", "Есть мелочь?"),
                        ex("There is a lot of traffic tonight.", "Сегодня сильные пробки."),
                    ],
                ),
                rule(
                    "Much, many, how",
                    "Many + исчисляемые во множественном. Much + неисчисляемые; в утверждениях much звучит формально, чаще a lot of. How many / how much — вопросы о числе и количестве.",
                    [
                        ex("How many stops are left?", "Сколько остановок осталось?"),
                        ex("There isn't much space in the boot.", "В багажнике мало места."),
                    ],
                ),
                rule(
                    "Few и little",
                    "A few + исчисляемые = несколько (достаточно). A little + неисчисляемые = немного (достаточно). Few / little без a подчёркивают нехватку. Too many / too much — чрезмерность.",
                    [
                        ex("I have a few minutes — we can talk.", "У меня есть несколько минут — можем поговорить."),
                        ex("Few people came, so we cancelled.", "Пришло мало людей, поэтому мы отменили."),
                    ],
                ),
            ],
            compare=[
                {"left": "a little sugar (хватит подсластить)", "right": "little sugar (почти нет, чай пресный)", "note": "Статья a меняет оценку количества."},
            ],
            watch_out=[
                "Не much people и не many money.",
                "Не some в обычном отрицании: There isn't any milk, не isn't some milk.",
                "Few ≠ a few: без a смысл ближе к «почти никто/ничего».",
            ],
            remember="Many/few — штуки. Much/little — масса. A few / a little — «есть немного».",
        ),
        [
            mc("There aren't ___ free seats.", ["some", "any", "much"], "any", "Отрицание — any."),
            fill("How ___ rice should I cook?", "much", "Rice неисчисляемое."),
            err("There are much tourists in July.", "There are many tourists in July.", "Tourists исчисляемые — many.", ["There are a lot of tourists in July"]),
            xf("Сделайте отрицание: We have some butter.", "We haven't any butter.", "haven't + any + неисчисляемое.", ["We don't have any butter", "We have no butter"]),
            fill("I take ___ sugar in tea — just half a spoon. (достаточно)", "a little", "A little = немного и хватает."),
            mc("___ students understood the joke, so the room stayed quiet.", ["A few", "Few", "A little"], "Few", "Мало, почти никто — few без a."),
        ],
        [
            fill("Would you like ___ water?", "some", "Вежливое предложение — some.", ["a little"]),
            mc("There is ___ noise from the road, but I can work.", ["a few", "a little", "few"], "a little", "Noise неисчисляемое; шум есть, но терпимо."),
            err("How much apples are in the bag?", "How many apples are in the bag?", "Apples — many."),
            xf("Слишком много (исчисл.): cars / in the car park", "There are too many cars in the car park.", "Too many + исчисляемые."),
            fill("___ people came, so we cancelled the tour. (почти никто)", "Few", "Few без a = почти никто."),
            mc("There isn't ___ time before boarding.", ["many", "much", "a few"], "much", "Time неисчисляемое — much."),
        ],
    ),
    module(
        "modals-must-should-have-to",
        "Must, should, have to",
        "Обязанность, совет и запрет; mustn't не равно don't have to.",
        22,
        "Надо, следует, не обязан",
        lesson(
            "Три модальности путают, потому что русское «должен» закрывает и внутренний долг, и правило извне, и совет. Must — сильная необходимость от говорящего или жёсткое правило. Have to — обязанность из ситуации, расписания, закона. Should — совет, не приказ. Ключевой контраст отрицаний: mustn't = нельзя; don't have to = не обязательно.",
            [
                rule(
                    "Must и have to",
                    "Must + V1 (без to). Have to / has to + V1. Вопрос и прошедшее для внешней обязанности обычно через have to: Did you have to…? I had to wait. Mustn't — запрет.",
                    [
                        ex("You must keep this door closed.", "Эту дверь нужно держать закрытой (жёсткое правило)."),
                        ex("I have to wear a badge at work.", "На работе я обязан носить бейдж (требование места)."),
                    ],
                ),
                rule(
                    "Should / shouldn't",
                    "Should + V1 — рекомендация. Мягче, чем must. Should I…? — запрос совета. Не should to.",
                    [
                        ex("You should back up the files tonight.", "Тебе стоит сделать резервную копию файлов сегодня вечером."),
                        ex("He shouldn't skip breakfast before the exam.", "Ему не стоит пропускать завтрак перед экзаменом."),
                    ],
                ),
                rule(
                    "Отрицания, которые путают",
                    "Mustn't = запрещено. Don't / doesn't have to = нет обязанности, можно не делать. Русское «не должен» часто хотят сказать don't have to, а пишут mustn't.",
                    [
                        ex("You mustn't park on the pavement.", "Нельзя парковаться на тротуаре."),
                        ex("You don't have to book — walk-ins are fine.", "Бронировать не обязательно — можно просто прийти."),
                    ],
                ),
            ],
            compare=[
                {"left": "You must not tell anyone.", "right": "You don't have to tell anyone.", "note": "Запрет vs отсутствие обязанности."},
            ],
            watch_out=[
                "Не must to / should to / don't must.",
                "He have to — ошибка: he/she/it + has to.",
                "Mustn't ≠ don't have to.",
            ],
            remember="Must/have to — обязанность. Should — совет. Mustn't — нельзя. Don't have to — можно не делать.",
        ),
        [
            mc("In this lab you ___ wear goggles. It's a safety rule.", ["should", "must", "don't have to"], "must", "Жёсткое правило безопасности — must (или have to)."),
            fill("She ___ start at 7 tomorrow. (внешняя обязанность, have to)", "has to", "He/she + has to."),
            err("You don't must come if you're busy.", "You don't have to come if you're busy.", "Отрицание обязанности — don't have to, не don't must."),
            xf("Совет: He stays up too late. (should / not)", "He shouldn't stay up too late.", "shouldn't + V1.", ["He should not stay up too late"]),
            fill("You ___ touch that switch — it's dangerous. (запрет)", "mustn't", "Запрет — mustn't.", ["must not"]),
            mc("It's a free museum. You ___ pay.", ["mustn't", "don't have to", "shouldn't to"], "don't have to", "Вход свободный — платить не обязательно."),
        ],
        [
            fill("You ___ drink more water. (совет)", "should", "Should + V1."),
            mc("Last night I ___ stay until closing.", ["must", "had to", "should to"], "had to", "Прошедшая внешняя обязанность — had to."),
            err("He have to renew his passport.", "He has to renew his passport.", "He + has to."),
            xf("Вопрос-совет: I / call / her / now?", "Should I call her now?", "Should + подлежащее + V1."),
            fill("We ___ show ID at the gate. (внешняя обязанность)", "have to", "We have to + V1."),
            mc("Guests ___ smoke in the rooms. It's forbidden.", ["don't have to", "mustn't", "should"], "mustn't", "Forbidden = mustn't."),
        ],
    ),
    module(
        "zero-first-conditional",
        "Zero и First Conditional",
        "If + Present для фактов и реальных будущих условий; will не ставят в if.",
        24,
        "Если — факт и если — реальный план",
        lesson(
            "Условные на A2 делят мир на два: всегда правда (Zero) и реальное будущее (First). В обеих конструкциях в части с if стоит Present Simple. Will живёт только в главной части First Conditional. Unless = if not.",
            [
                rule(
                    "Zero Conditional",
                    "If + Present Simple, Present Simple. Законы природы, инструкции, привычные реакции. If можно заменить на when без большой потери смысла.",
                    [
                        ex("If you heat chocolate, it melts.", "Если шоколад нагреть, он тает."),
                        ex("If the light is red, we stop.", "Если свет красный, мы останавливаемся."),
                    ],
                ),
                rule(
                    "First Conditional",
                    "If + Present Simple, will / won't + V1. Реальное или вероятное будущее. В if-части will не нужен. Возможны can, might, imperative в главной части: If you see her, call me.",
                    [
                        ex("If the shop is open, I'll buy bread.", "Если магазин будет открыт, куплю хлеб."),
                        ex("If it rains, we won't eat outside.", "Если пойдёт дождь, мы не будем есть на улице."),
                    ],
                ),
                rule(
                    "Unless и порядок частей",
                    "Unless + утверждение = if + not. Запятая нужна, когда if/unless стоит в начале. Части можно менять местами.",
                    [
                        ex("Unless you hurry, you'll miss the tram.", "Если не поторопишься, пропустишь трамвай."),
                        ex("I'll message you if the train is delayed.", "Напишу, если поезд задержат."),
                    ],
                ),
            ],
            compare=[
                {"left": "If you press this, the lamp turns on.", "right": "If you press this, the lamp will turn on.", "note": "Инструкция/факт vs конкретный будущий раз."},
            ],
            watch_out=[
                "Не If it will rain — в if на A2 нужен Present Simple.",
                "Не Unless you don't… — двойное отрицание.",
                "Will не дублируют в обеих частях.",
            ],
            remember="If + Present. Факт — Present в обеих частях. Реальное будущее — will только в главной.",
        ),
        [
            fill("If you ___ water to 100°C, it ___ . (heat / boil)", "heat / boils", "Zero: Present + Present.", ["heat/boils", "heat, boils"]),
            mc("If I ___ late, I'll text you.", ["will be", "am", "was"], "am", "В if-части First — Present, не will."),
            err("If it will snow, we stay at home.", "If it snows, we will stay at home.", "First: Present в if, will в главной.", ["If it snows, we'll stay at home"]),
            xf("First Conditional: she / miss / the bus / she / not leave / now", "If she doesn't leave now, she will miss the bus.", "If + Present, will.", ["If she does not leave now, she will miss the bus", "She will miss the bus if she doesn't leave now"]),
            fill("Unless he ___ , we'll start without him. (arrive)", "arrives", "Unless + Present; he + -s."),
            mc("If you feel dizzy, ___ down.", ["you'll sit", "sit", "you sitting"], "sit", "Инструкция — императив в главной части."),
        ],
        [
            fill("If the battery ___ low, the phone shuts down. (be)", "is", "Zero: факт об устройстве."),
            mc("We'll cancel the picnic if it ___ .", ["will rain", "rains", "rained"], "rains", "If + Present в First."),
            err("Unless you don't save the file, you'll lose it.", "Unless you save the file, you'll lose it.", "Unless уже несёт not.", ["If you don't save the file, you'll lose it"]),
            xf("Zero: ice / float / you / drop / it / in water", "If you drop ice in water, it floats.", "If + Present, Present.", ["If you drop it in water, ice floats"]),
            fill("If they offer me the shift, I ___ take it. (will)", "will", "Главная часть First — will + V1.", ["'ll"]),
            mc("___ you mix red and blue, you get purple.", ["If", "Unless", "Will"], "If", "Zero-факт — If + Present, Present."),
        ],
    ),
    module(
        "relative-who-which-that",
        "Who, which, that",
        "Определительные придаточные: люди, вещи, места; опущение that.",
        18,
        "Какой именно",
        lesson(
            "Относительные местоимения присоединяют уточнение к существительному. Who — люди. Which — вещи и животные. That — и люди, и вещи в определяющих придаточных (без паузы и без запятой). Where — места. Если местоимение — дополнение, that/who/which часто можно опустить.",
            [
                rule(
                    "Who и which",
                    "The woman who called you is my neighbour. The charger which I bought yesterday is already broken. В разговорной речи для вещей чаще that, чем which.",
                    [
                        ex("The nurse who took my blood was very calm.", "Медсестра, которая брала кровь, была очень спокойной."),
                        ex("This is the app which crashed twice.", "Это то приложение, которое дважды зависло."),
                    ],
                ),
                rule(
                    "That в определяющих придаточных",
                    "That заменяет who или which, когда придаточное нужно, чтобы понять, о ком/чём речь. Запятую перед that в этой роли не ставят.",
                    [
                        ex("The keys that I left on the counter are gone.", "Ключи, которые я оставил на стойке, пропали."),
                        ex("Anyone that arrives after 8 waits outside.", "Все, кто приходит после восьми, ждут снаружи."),
                    ],
                ),
                rule(
                    "Опущение и where",
                    "Если после who/which/that сразу идёт подлежащее (не глагол), местоимение можно убрать: the book I lent you. Where = in/at which для мест: the café where we met.",
                    [
                        ex("The jacket I tried on was too tight.", "Куртка, которую я мерил, была слишком узкой."),
                        ex("That's the platform where the express stops.", "Это платформа, где останавливается экспресс."),
                    ],
                ),
            ],
            watch_out=[
                "Не who для вещей: the film who — ошибка.",
                "Не what в этой роли: the book what I read — нужно that/which или опущение.",
                "Если после местоимения сразу глагол, его нельзя выкинуть: the man who lives… — who нужен.",
            ],
            remember="Люди — who. Вещи — which/that. Дополнение можно опустить. Места — where.",
        ),
        [
            mc("The engineer ___ fixed the lift was here at dawn.", ["which", "who", "where"], "who", "Инженер — человек."),
            fill("This is the map ___ we used yesterday.", "that", "Вещь + определяющее придаточное — that или which.", ["which"]),
            err("I don't like films who have no ending.", "I don't like films that have no ending.", "Films — вещи, не who.", ["I don't like films which have no ending"]),
            xf("Соедините: That's the hostel. We stayed there.", "That's the hostel where we stayed.", "Место — where.", ["That is the hostel where we stayed"]),
            fill("The man ___ lives upstairs plays the cello.", "who", "После пробела сразу глагол lives — who (или that) опустить нельзя.", ["that"]),
            mc("Here's the photo ___ I took from the roof.", ["what", "who", "— (можно опустить)"], "— (можно опустить)", "I took — местоимение-дополнение, его можно не ставить."),
        ],
        [
            fill("Students ___ miss the quiz take it on Friday.", "who", "Люди + сразу глагол — who/that.", ["that"]),
            mc("The tram ___ goes to the stadium is the 12.", ["who", "which", "where"], "which", "Tram — вещь."),
            err("This is the shop what sells beans in bulk.", "This is the shop that sells beans in bulk.", "Нужен that/which, не what.", ["This is the shop which sells beans in bulk"]),
            xf("Опустите местоимение: the song that she wrote", "the song she wrote", "Дополнение that можно убрать."),
            fill("Is this the street ___ the market is?", "where", "Место — where."),
            mc("The people ___ I invited are late.", ["which", "who", "where"], "who", "People — люди; who можно и опустить, но из вариантов верный who."),
        ],
    ),
    module(
        "used-to",
        "Used to",
        "Прошлые привычки и состояния, которых больше нет.",
        18,
        "Раньше так было, сейчас нет",
        lesson(
            "Used to + V1 описывает регулярное прошлое или прошлое состояние, которое закончилось. Это не «привык» в значении be used to. Вопрос и отрицание на A2: Did you use to…? I didn't use to… — без -d у use.",
            [
                rule(
                    "Утверждение",
                    "Подлежащее + used to + V1. Работает и с действиями, и с состояниями: I used to cycle; the building used to be a bakery.",
                    [
                        ex("I used to share a flat with two designers.", "Когда-то я снимал квартиру с двумя дизайнерами."),
                        ex("There used to be a tram along this street.", "По этой улице когда-то ходил трамвай."),
                    ],
                ),
                rule(
                    "Отрицание и вопрос",
                    "Did + подлежащее + use to + V1. Didn't use to + V1. Форма used to в этих конструкциях теряет -d. Never used to тоже возможно.",
                    [
                        ex("Did you use to play in that courtyard?", "Ты раньше играл в том дворе?"),
                        ex("She didn't use to drink coffee.", "Раньше она не пила кофе."),
                    ],
                ),
                rule(
                    "Не путать с похожими формами",
                    "Be used to + noun/-ing = привычен к. Get used to = привыкать. Used to + V1 не ставят для одноразового прошлого: для этого Past Simple.",
                    [
                        ex("I'm used to early trains now.", "Теперь я привык к ранним поездам (не used to)."),
                        ex("I used to hate early trains.", "Раньше я ненавидел ранние поезда — а сейчас, видимо, нет."),
                    ],
                ),
            ],
            compare=[
                {"left": "I used to live by the river.", "right": "I'm used to living by the river.", "note": "Больше не живу vs живу и мне это привычно."},
            ],
            watch_out=[
                "Не I use to live (нужно used to в утверждении).",
                "Не Did you used to — в вопросе use без -d.",
                "Не used to для вчерашнего одноразового действия.",
            ],
            remember="Used to + V1 = раньше да, сейчас нет. В did-вопросе — use to.",
        ),
        [
            fill("He ___ work night shifts. (раньше, сейчас нет)", "used to", "Утверждение — used to + V1."),
            mc("___ you use to have a dog?", ["Did", "Do", "Are"], "Did", "Вопрос — Did + use to."),
            err("I didn't used to like olives.", "I didn't use to like olives.", "После didn't — use, не used."),
            xf("Прошлое состояние: This hall is a gym now. (cinema)", "This hall used to be a cinema.", "used to be + существительное."),
            fill("We ___ use to lock the door. (отрицание привычки)", "didn't", "Didn't use to + V1.", ["did not"]),
            mc("I ___ spicy food — I grew up with it. (привычен сейчас)", ["used to", "am used to", "use to"], "am used to", "Be used to = привычен, не «раньше»."),
        ],
        [
            fill("They used ___ keep bees on the roof.", "to", "used to + V1."),
            mc("She ___ a lot, but she sold the piano.", ["used to practise", "is used to practise", "use to practise"], "used to practise", "Законченная привычка — used to + V1."),
            err("I use to take this bus every morning. (раньше, сейчас нет)", "I used to take this bus every morning.", "В утверждении нужно used to."),
            xf("Вопрос: You used to live in Tartu.", "Did you use to live in Tartu?", "Did + use to."),
            fill("There ___ to be a fountain here.", "used", "There used to be."),
            mc("Don't worry, you'll ___ the noise.", ["used to", "get used to", "use to"], "get used to", "Процесс привыкания — get used to."),
        ],
    ),
    module(
        "passive-present-past",
        "Пассив: Present и Past Simple",
        "Be + V3, когда важнее действие или объект, а не тот, кто делает.",
        22,
        "Что сделали с подлежащим",
        lesson(
            "В пассиве подлежащее — то, на что действие направлено. Форма: be в нужном времени + V3. Present: am/is/are + V3. Past: was/were + V3. Деятеля (by …) добавляют, только если он важен. Русское «дом строится» часто требует пассива, а не they build the house, если строитель неизвестен.",
            [
                rule(
                    "Present Simple Passive",
                    "The office is cleaned every night. Вопросы: Is English spoken here? Отрицание: isn't / aren't + V3.",
                    [
                        ex("Rice is grown in this valley.", "В этой долине выращивают рис."),
                        ex("These doors aren't locked during the day.", "Эти двери днём не запирают."),
                    ],
                ),
                rule(
                    "Past Simple Passive",
                    "The window was repaired yesterday. They → were: The emails were sent at noon.",
                    [
                        ex("My bag was stolen on the train.", "Мою сумку украли в поезде."),
                        ex("The results were published on Friday.", "Результаты опубликовали в пятницу."),
                    ],
                ),
                rule(
                    "By и когда пассив уместен",
                    "By + деятель, если без него смысл дырявый: The mural was painted by a local artist. Если деятель — they/someone/people, by обычно не нужен.",
                    [
                        ex("This track was written by her brother.", "Этот трек написал её брат."),
                        ex("The street is swept every morning.", "Улицу подметают каждое утро (кто — неважно)."),
                    ],
                ),
            ],
            compare=[
                {"left": "They cancelled the concert.", "right": "The concert was cancelled.", "note": "Актив называет «они»; пассив ставит концерт в центр."},
            ],
            watch_out=[
                "Нужна V3, не V1: не was steal, а was stolen.",
                "Согласуйте be: emails were sent, не was sent.",
                "Не ставьте пассив на непереходные глаголы без объекта: happen, arrive не делают *was happened.",
            ],
            remember="Be + V3. Сейчас — am/is/are. Прошлое — was/were. By — только если деятель важен.",
        ),
        [
            fill("Spanish ___ spoken in several countries. (be)", "is", "Present Passive, it/Spanish + is + V3."),
            mc("The parcels ___ delivered yesterday.", ["are", "were", "was"], "were", "Parcels множественное + прошедшее — were."),
            err("The window was break last night.", "The window was broken last night.", "Break — broke — broken."),
            xf("Пассив: They lock the gate at 10.", "The gate is locked at 10.", "Present Passive, деятель не нужен."),
            fill("This song ___ written by a teenager. (be, past)", "was", "Единственное + Past Passive."),
            mc("___ olives grown in this region?", ["Do", "Are", "Is"], "Are", "Вопрос Present Passive: Are + подлежащее + V3."),
        ],
        [
            fill("The chairs ___ moved yesterday. (be)", "were", "Множественное + Past Passive."),
            mc("Breakfast ___ served until 10.", ["is", "was being", "has"], "is", "Регулярное правило отеля — Present Passive."),
            err("The emails was sent at noon.", "The emails were sent at noon.", "Emails + were."),
            xf("Пассив прошедшего: Someone stole her bike.", "Her bike was stolen.", "Past Passive без someone.", ["Her bike was stolen by someone"]),
            fill("English ___ taught at that school. (отрицание, Present Passive)", "isn't", "Present Passive negative: isn't + V3.", ["is not"]),
            mc("The bridge ___ damaged in the storm.", ["were", "was", "is being"], "was", "Один мост + прошедшее событие."),
        ],
    ),
    module(
        "adverbs-frequency-manner",
        "Наречия частоты и образа действия",
        "Always / often перед смысловым глаголом; well, hard, late и ложные пары.",
        16,
        "Как часто и каким образом",
        lesson(
            "Наречия частоты отвечают «как часто», наречия образа действия — «как». Частота в утверждениях обычно стоит перед смысловым глаголом и после am/is/are: she always checks; she is always late. Образ действия чаще после глагола или дополнения: she explained it clearly. Ряд пар путает русских: good/well, hard/hardly, late/lately.",
            [
                rule(
                    "Частота и место",
                    "always, usually, often, sometimes, rarely, never. Перед V: I often forget names. После be: He is never rude. Sometimes может стоять в начале предложения.",
                    [
                        ex("We usually buy bread on the way home.", "Мы обычно покупаем хлеб по дороге домой."),
                        ex("She is rarely in the office on Fridays.", "По пятницам её редко бывает в офисе."),
                    ],
                ),
                rule(
                    "Образ действия",
                    "Многие наречия = прилагательное + -ly: careful → carefully, easy → easily, happy → happily. После глагола: He packed the cups carefully.",
                    [
                        ex("Please speak slowly — the line is bad.", "Говори, пожалуйста, медленно — связь плохая."),
                        ex("She found the street easily.", "Она легко нашла улицу."),
                    ],
                ),
                rule(
                    "Особые формы",
                    "Good → well (не good после глагола действия). Hard = усердно / сильно; hardly = почти не. Late = поздно; lately = в последнее время. Fast, early, daily не берут -ly в этой роли. Friendly — прилагательное, не наречие.",
                    [
                        ex("He did well in the practical test.", "Он хорошо справился с практическим тестом."),
                        ex("I could hardly hear the announcement.", "Я почти не слышал объявление."),
                    ],
                ),
            ],
            compare=[
                {"left": "She works hard.", "right": "She hardly works.", "note": "Усердно vs почти не работает."},
            ],
            watch_out=[
                "Не He speaks English good — нужно well.",
                "Не I go always there — частота перед глаголом: I always go.",
                "Hardly ≠ hard.",
            ],
            remember="Частота: до глагола, после be. Образ: -ly после действия. Well, hard, late — особые.",
        ),
        [
            mc("She ___ checks the locks before bed.", ["always", "always is", "is always checks"], "always", "Перед смысловым глаголом checks."),
            fill("He explained the rule ___. (clear)", "clearly", "Прилагательное + -ly."),
            err("You speak English very good.", "You speak English very well.", "После speak нужно наречие well."),
            xf("Поставьте often: I am late for the first class.", "I am often late for the first class.", "После be наречие частоты."),
            fill("She trained ___ all spring. (усердно)", "hard", "Hard без -ly в значении «усердно»."),
            mc("I've been tired ___.", ["late", "lately", "hardly"], "lately", "Lately = в последнее время."),
        ],
        [
            fill("They are ___ at home in the evening. (обычно)", "usually", "После are — частота."),
            mc("I could ___ see the sign in the fog.", ["hard", "hardly", "lately"], "hardly", "Hardly = почти не."),
            err("He drives dangerous when it rains.", "He drives dangerously when it rains.", "Нужно наречие -ly."),
            xf("Поставьте never: She eats meat.", "She never eats meat.", "Never перед смысловым глаголом."),
            fill("The team played ___ yesterday. (good → наречие)", "well", "Good → well."),
            mc("Please arrive ___. The briefing starts at 9 sharp.", ["lately", "early", "hardly"], "early", "Early — наречие без -ly."),
        ],
    ),
]
