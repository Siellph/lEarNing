from app.seed.helpers import err, ex, fill, lesson, mc, module, rule, xf

B1 = [
    module(
        "present-perfect-vs-past-simple",
        "Present Perfect и Past Simple",
        "Незавершённый период и результат сейчас против законченной истории с датой.",
        24,
        "Уже произошло — но какая точка опоры",
        lesson(
            "Оба времени смотрят в прошлое, но точка опоры разная. Present Perfect связывает прошлое с настоящим: опыт, результат, ещё не закрытый период (today, this week, since, for). Past Simple относит событие к закрытому прошлому: yesterday, last March, in 2016, when I was a child. Для русского «я жил / я живу здесь уже…» выберите время по смыслу: этап закончился — Past Simple; ситуация всё ещё длится — Present Perfect.",
            [
                rule(
                    "Present Perfect: период ещё открыт",
                    "Have/has + V3. For + длительность, since + точка старта. Already / yet / just / ever / never. Вопрос How long have you…? если ситуация не закончилась.",
                    [
                        ex("I've worked night shifts since April.", "Я работаю в ночную смену с апреля (и сейчас тоже)."),
                        ex("Have you finished the invoice yet?", "Ты уже доделал счёт?"),
                    ],
                ),
                rule(
                    "Past Simple: точка закрыта",
                    "V2 / V-ed. Маркеры: ago, last, in + год, when + прошлое. How long did you…? если период закончился.",
                    [
                        ex("I worked night shifts in 2022.", "Я работал в ночную в 2022-м (уже нет)."),
                        ex("She sent the invoice an hour ago.", "Она отправила счёт час назад."),
                    ],
                ),
                rule(
                    "Один факт — два взгляда",
                    "Gone vs been: He's gone to Riga (ещё там или в пути). He's been to Riga (был и вернулся). Past Simple + точная дата побеждает даже слово already в голове говорящего.",
                    [
                        ex("I've been to Lisbon twice.", "Я бывал в Лиссабоне дважды (опыт, даты не важны)."),
                        ex("I went to Lisbon in May.", "Я ездил в Лиссабон в мае (закрытая поездка)."),
                    ],
                ),
            ],
            compare=[
                {"left": "I've lived here for six years.", "right": "I lived there for six years.", "note": "Всё ещё здесь vs тот этап закончился."},
            ],
            watch_out=[
                "Не I've seen her yesterday / I've started the course last week.",
                "Не I live here since 2020 — нужен Present Perfect: I've lived.",
                "For + период (for three days), since + момент (since Monday), не наоборот.",
            ],
            remember="Есть дата-закрытие — Past Simple. Период ещё открыт или важен результат — Present Perfect.",
        ),
        [
            mc("I ___ this series last winter.", ["have watched", "watched", "am watching"], "watched", "Last winter закрывает период — Past Simple."),
            fill("She ___ in Oslo since 2019. (live)", "has lived", "Since + незакрытый период — Present Perfect, she + has.", ["she's lived"]),
            err("I have sent the parcel yesterday.", "I sent the parcel yesterday.", "Yesterday требует Past Simple."),
            xf("Задайте вопрос о незакрытой длительности: you / work / here", "How long have you worked here?", "How long + Present Perfect.", ["How long have you been working here"]),
            fill("They ___ the shop two years ago. (open)", "opened", "Ago — Past Simple."),
            mc("He isn't at his desk. He ___ to lunch.", ["has been", "has gone", "went already"], "has gone", "Has gone = ушёл и ещё не вернулся."),
        ],
        [
            fill("Вставьте нужную форму (lose): I ___ my keys — I can't open the door. (lose)", "have lost", "Результат сейчас — Present Perfect.", ["I've lost"]),
            mc("Выберите вспомогательный глагол: ___ you see the eclipse in 2024?", ["Have", "Did", "Has"], "Did", "2024 как закрытая дата — Past Simple, Did + V1."),
            err("We live in this street for five years.", "We have lived in this street for five years.", "For + всё ещё длящаяся ситуация — Present Perfect.", ["We've lived in this street for five years"]),
            xf("Перепишите в Past Simple и добавьте в предложение маркер «last Tuesday»: She has already called the clinic.", "She called the clinic last Tuesday.", "Точная дата вытесняет Present Perfect. В ответе обязательно нужен маркер «last Tuesday»: She called the clinic last Tuesday."),
            fill("Вставьте верную пару форм: How long ___ you ___ this phone? (have, всё ещё ваш)", "have / had", "How long + Present Perfect of have.", ["have had"]),
            mc("Выберите время глагола: I ___ to the new gallery; I came back an hour ago.", ["have gone", "have been", "had gone"], "have been", "Been = съездил и вернулся."),
        ],
    ),
    module(
        "present-perfect-continuous",
        "Present Perfect Continuous",
        "Have been + V-ing: длительность, недавняя активность и видимый след.",
        22,
        "Сколько уже длится процесс",
        lesson(
            "Present Perfect Continuous (have/has been + V-ing) подчёркивает саму деятельность и её длительность до сейчас. Present Perfect Simple чаще ставит акцент на результат или количество. Русское «я уже два часа читаю» почти всегда Continuous. Глаголы состояния (know, own, like) в Continuous не ставят — для них Simple: I've known her since school.",
            [
                rule(
                    "Форма",
                    "I/you/we/they have been + V-ing. He/she/it has been + V-ing. Отрицание: haven't/hasn't been. Вопрос: Have you been waiting long?",
                    [
                        ex("I've been editing this chapter all morning.", "Я всё утро правлю эту главу."),
                        ex("Has she been practising the solo?", "Она репетировала соло?"),
                    ],
                ),
                rule(
                    "Зачем Continuous",
                    "How long + процесс. Recently / lately. Видимый след: You're out of breath — have you been running? Раздражение на повторяющееся: He's been leaving wet towels on the floor.",
                    [
                        ex("We've been looking for a plumber since Monday.", "Мы ищем сантехника с понедельника."),
                        ex("Your hands are blue. Have you been painting?", "Руки синие. Ты что, красил?"),
                    ],
                ),
                rule(
                    "Когда лучше Simple",
                    "Законченный результат и число: I've written three emails. Состояния: I've had this bike for a year. Live/work/study допускают оба, если ситуация стабильна: I've lived / I've been living here for a year.",
                    [
                        ex("I've read five articles today.", "Я прочитал пять статей (количество — Simple)."),
                        ex("I've been reading all afternoon, but I haven't finished one.", "Я всё после обеда читаю, а ни одной не закончил."),
                    ],
                ),
            ],
            compare=[
                {"left": "She's written the report.", "right": "She's been writing the report.", "note": "Отчёт готов vs процесс ещё идёт или только что шёл."},
            ],
            watch_out=[
                "Не I am living here for two years — для «уже … как» нужен Perfect, не Present Continuous.",
                "Не I've been knowing him — know только Simple.",
                "Been, не being: have been waiting, не have being waiting.",
            ],
            remember="Have been + -ing = процесс до сейчас. Число и готовый результат — Perfect Simple.",
        ),
        [
            fill("They ___ for a taxi for twenty minutes. (wait)", "have been waiting", "How-long процесс — Perfect Continuous.", ["they've been waiting"]),
            mc("I ___ three loaves this morning.", ["have been baking", "have baked", "am baking"], "have baked", "Число готовых буханок — Perfect Simple."),
            err("She has being studying since six.", "She has been studying since six.", "Нужно been, не being.", ["She's been studying since six"]),
            xf("Вопрос о длительности: he / repair / the lock", "How long has he been repairing the lock?", "Has he been + V-ing."),
            fill("You look dusty. ___ you ___ the attic? (clear)", "Have / been clearing", "Видимый след — Perfect Continuous.", ["Have you been clearing"]),
            mc("I ___ her since we were at college.", ["have been knowing", "have known", "know"], "have known", "Know — состояние, только Simple."),
        ],
        [
            fill("Вставьте нужную форму (work): He ___ overtime all week. (work)", "has been working", "All week + процесс, he + has.", ["he's been working"]),
            mc("Выберите форму Present Perfect Continuous: Sorry about the mess. I ___ the shelves.", ["have painted", "have been painting", "painted yesterday"], "have been painting", "След деятельности важнее законченного результата."),
            err("I am learning German for two years.", "I have been learning German for two years.", "For + длительность до сейчас — Perfect Continuous.", ["I've been learning German for two years"]),
            xf("Отрицание: We have been using your mug.", "We haven't been using your mug.", "haven't been + V-ing.", ["We have not been using your mug"]),
            fill("Вставьте верную пару форм: How many pages ___ you ___ today? (write)", "have / written", "How many + результат — Perfect Simple.", ["have written"]),
            mc("Выберите форму Present Perfect Continuous: It ___ since noon, and the pitch is flooded.", ["has rained", "has been raining", "rains"], "has been raining", "Длящийся процесс с видимым следствием."),
        ],
    ),
    module(
        "past-perfect",
        "Past Perfect",
        "Had + V3: более раннее из двух прошедших.",
        22,
        "Что случилось ещё раньше",
        lesson(
            "Past Perfect нужен не «потому что прошлое», а потому что в прошлом уже есть точка, а другое действие было до неё. Форма одна для всех лиц: had + V3. Без второй прошлой точки обычно хватает Past Simple. Типичные якоря: already, by the time, after, before, because.",
            [
                rule(
                    "Форма и место на линии",
                    "I/you/he/we/they had + V3. Отрицание: hadn't. Вопрос: Had she left? Краткая: I'd, we'd.",
                    [
                        ex("The platform was empty: the train had already gone.", "Платформа была пуста: поезд уже ушёл."),
                        ex("Had you booked a table before you arrived?", "Вы забронировали столик до того, как пришли?"),
                    ],
                ),
                rule(
                    "By the time, after, before",
                    "By the time + Past Simple часто тянет Past Perfect в другой части. After + Past Perfect / before + Past Simple — частый каркас, но если порядок и так ясен, носители могут оставить два Past Simple.",
                    [
                        ex("By the time we sat down, the talk had started.", "К тому моменту, как мы сели, доклад уже начался."),
                        ex("She went home after she had locked the lab.", "Она ушла домой, после того как закрыла лабораторию."),
                    ],
                ),
                rule(
                    "Причина и «уже» в прошлом",
                    "Past Perfect объясняет прошлое другим, ещё более ранним фактом. Never / just / already хорошо живут между had и V3.",
                    [
                        ex("I wasn't hungry because I had eaten on the train.", "Я не хотел есть: я уже поел в поезде."),
                        ex("We had never seen that street in daylight.", "Мы никогда не видели эту улицу при дневном свете."),
                    ],
                ),
            ],
            compare=[
                {"left": "When I arrived, he left.", "right": "When I arrived, he had left.", "note": "Ушёл в момент прихода vs уже ушёл до него."},
            ],
            watch_out=[
                "Не ставьте Past Perfect на единственное прошлое: I had gone to the shop yesterday — если это просто факт дня.",
                "После had нужна V3: had went — ошибка.",
                "Had как «имел» (Past Simple of have) ≠ Past Perfect: I had a key vs I had lost a key.",
            ],
            remember="Две точки в прошлом — более ранняя = had + V3.",
        ),
        [
            fill("The cake was gone because the kids ___ it. (eat)", "had eaten", "Причина раньше главного прошлого — Past Perfect."),
            mc("When I switched on the lamp, someone ___ the window.", ["already closed", "had already closed", "has already closed"], "had already closed", "Окно закрыли до того момента."),
            err("She had went out when we arrived.", "She had gone out when we arrived.", "Go — went — gone."),
            xf("Более раннее действие: We missed the start. The film started first.", "The film had started before we arrived.", "Had + V3 до второй точки.", ["The film had already started"]),
            fill("By the time the plumber came, we ___ the tap. (already + fix)", "had already fixed", "By the time + более ранний результат."),
            mc("I ___ a spare charger in my bag, so I was fine. (владение в прошлом)", ["had had", "had", "have had"], "had", "Одно прошлое «имел» — Past Simple, не Past Perfect."),
        ],
        [
            fill("Вставьте нужную форму (forget): He couldn't get in because he ___ his pass. (forget)", "had forgotten", "Forget — forgot — forgotten."),
            mc("Выберите форму Past Perfect: The kettle clicked: the water ___ already.", ["boiled", "had boiled", "has boiled"], "had boiled", "Кипение завершилось до щелчка — Past Perfect."),
            err("When I had arrived, she cooked dinner. (она начала после моего прихода)", "When I arrived, she cooked dinner.", "Один ряд последовательных фактов — два Past Simple, Perfect не нужен.", ["When I arrived, she started cooking dinner"]),
            xf("Отрицание: They had met before.", "They hadn't met before.", "hadn't + V3.", ["They had not met before"]),
            fill("Вставьте вспомогательный глагол: ___ you packed before the taxi came?", "Had", "Вопрос Past Perfect — Had + подлежащее."),
            mc("Выберите форму Past Perfect: The streets were wet. It ___ earlier.", ["rained", "had rained", "has rained"], "had rained", "Дождь раньше наблюдаемого прошлого."),
        ],
    ),
    module(
        "future-continuous",
        "Future Continuous",
        "Will be + V-ing: процесс в будущей точке и вежливый вопрос о планах.",
        18,
        "Что будет происходить в тот час",
        lesson(
            "Future Continuous показывает действие как процесс в конкретный будущий момент, а не как решение или пункт плана. Форма: will be + V-ing для всех лиц. Его любят для вежливых вопросов о чужих планах: Will you be using this desk? — меньше давления, чем Will you use…?",
            [
                rule(
                    "Форма",
                    "Will be + V-ing. Отрицание: won't be + V-ing. Вопрос: Will she be working? Краткие: I'll be, they'll be.",
                    [
                        ex("This time tomorrow I'll be sitting on a night train.", "Завтра в это время я буду сидеть в ночном поезде."),
                        ex("Don't call at 8 — she'll be putting the kids to bed.", "Не звони в восемь: она будет укладывать детей."),
                    ],
                ),
                rule(
                    "Процесс, не пункт списка",
                    "Will / going to называют факт или намерение. Continuous рисует фон будущего: пока одно длится, может случиться другое.",
                    [
                        ex("I'll send the file at six.", "Отправлю файл в шесть (пункт)."),
                        ex("I'll be sending files all afternoon, so I may be slow to reply.", "Буду весь день рассылать файлы — отвечу не сразу."),
                    ],
                ),
                rule(
                    "Вежливые планы",
                    "Will you be + V-ing…? спрашивает о уже вероятном ходе вещей, не просит одолжения напрямую. Still часто сопровождает Continuous: Will you still be living here in June?",
                    [
                        ex("Will you be passing the post office?", "Ты будешь проходить мимо почты?"),
                        ex("We won't be staying late — the last bus is at 10.", "Мы не будем засиживаться: последний автобус в 10."),
                    ],
                ),
            ],
            compare=[
                {"left": "I'll talk to her tomorrow.", "right": "I'll be talking to her tomorrow at 11.", "note": "Обещание/факт vs процесс в час."},
            ],
            watch_out=[
                "Не will be to talk и не will being talk.",
                "Состояния (know, want, belong) в Future Continuous почти не ставят.",
                "Не путайте с going to: I'm going to be late — это примета/ожидание, не Continuous как аспект.",
            ],
            remember="Will be + -ing = процесс в будущей точке или мягкий вопрос о плане.",
        ),
        [
            fill("At 10 tonight we ___ through the tunnel. (drive)", "will be driving", "Конкретный будущий час + процесс.", ["we'll be driving"]),
            mc("___ you be using the meeting room at 3?", ["Do", "Will", "Are"], "Will", "Will you be + V-ing."),
            err("I will being work at noon.", "I will be working at noon.", "Will be + V-ing.", ["I'll be working at noon"]),
            xf("Отрицание: She will be waiting downstairs.", "She won't be waiting downstairs.", "won't be + V-ing.", ["She will not be waiting downstairs"]),
            fill("Don't visit at 7. He ___ the baby. (bath)", "will be bathing", "Фон будущего — не беспокоить.", ["he'll be bathing"]),
            mc("I ___ the document tonight, I promise.", ["will be sending", "will send", "am send"], "will send", "Обещание-пункт — will + V1, не Continuous."),
        ],
        [
            fill("Вставьте модальный глагол (will/would): This time next week she ___ in Lisbon. (land, процесс поездки: fly)", "will be flying", "This time next week — классический маркер.", ["she'll be flying"]),
            mc("Выберите форму Future Continuous: Will you ___ late again on Friday?", ["be working", "working", "to work"], "be working", "Will you be + V-ing."),
            err("They will be stay at a hostel.", "They will be staying at a hostel.", "Нужен V-ing.", ["They'll be staying at a hostel"]),
            xf("Вежливый вопрос: you / pass / the bakery", "Will you be passing the bakery?", "Will you be + V-ing."),
            fill("Вставьте модальный глагол (will/would): We ___ emails all morning, so replies may be slow. (answer)", "will be answering", "Длительный будущий процесс.", ["we'll be answering"]),
            mc("Выберите модальный глагол (will/would): I ___ you at the kiosk at 5. (договорённость-факт)", ["will be meeting", "will meet", "meet will"], "will meet", "Простая договорённость — will + V1."),
        ],
    ),
    module(
        "second-conditional",
        "Second Conditional",
        "If + Past Simple, would + V: нереальная или маловероятная ситуация сейчас/в будущем.",
        22,
        "Если бы сейчас было иначе",
        lesson(
            "Second Conditional говорит о воображаемом настоящем или маловероятном будущем. Русское «если бы» здесь без «тогда в прошлом». Формула: If + Past Simple, would/wouldn't + V1. В if не ставят would. Для be в формальном и учебном варианте — were для всех лиц: If I were you.",
            [
                rule(
                    "Форма",
                    "If I had time, I would walk. Краткие: I'd, she'd, they wouldn't. Вместо would возможны could / might в главной части.",
                    [
                        ex("If I lived closer, I'd cycle to the studio.", "Если бы я жил ближе, ездил бы в студию на велосипеде."),
                        ex("If she knew the code, she could let us in.", "Если бы она знала код, смогла бы нас впустить."),
                    ],
                ),
                rule(
                    "Were и If I were you",
                    "If I/he/she/it were — стандарт совета и формальной грамматики. If I was встречается в речи, но в тесте обычно ждут were, особенно в If I were you.",
                    [
                        ex("If I were you, I'd decline the extra shift.", "На твоём месте я бы отказался от дополнительной смены."),
                        ex("If it were cheaper, we would book tonight.", "Если бы это было дешевле, забронировали бы сегодня."),
                    ],
                ),
                rule(
                    "Не путать с First",
                    "First — реальное будущее (If + Present, will). Second — гипотеза (If + Past, would). Past в if не означает прошлый факт, это «дистанция» от реальности.",
                    [
                        ex("If they offer me the job, I'll take it.", "Если предложат — возьму (реально)."),
                        ex("If they offered me the job, I would take it.", "Если бы предложили — взял бы (пока не похоже)."),
                    ],
                ),
            ],
            compare=[
                {"left": "If I have money, I'll buy a lamp.", "right": "If I had money, I would buy a lamp.", "note": "Деньги возможны vs денег нет / почти нет."},
            ],
            watch_out=[
                "Не If I would have / If she would know — в if нужен Past Simple, не would.",
                "Не will в главной части Second: не I will buy, а I would buy.",
                "If I were you — устойчивый совет, не If I would be you.",
            ],
            remember="If + Past, would + V. Это не прошлое, а нереальный сейчас. Were в If I were you.",
        ),
        [
            fill("If he ___ the roster, he would swap with you. (see)", "saw", "If + Past Simple."),
            mc("If I ___ you, I wouldn't sign today.", ["was", "were", "would be"], "were", "Учебная норма — If I were you."),
            err("If she would live nearer, she would walk.", "If she lived nearer, she would walk.", "В if — Past Simple, не would."),
            xf("Составьте Second Conditional из двух фактов: I don't have a balcony. I don't grow tomatoes.", "If I had a balcony, I would grow tomatoes.", "If + Past, would + V1.", ["If I had a balcony, I'd grow tomatoes"]),
            fill("We ___ stay longer if the last metro were later. (would)", "would", "Главная часть — would + V1.", ["'d"]),
            mc("If it ___ this weekend, we'd cancel the hike. (маловероятно / гипотеза)", ["rains", "rained", "will rain"], "rained", "Second — Past в if."),
        ],
        [
            fill("Вставьте вспомогательный глагол: If they ___ fewer clients, they could leave at six. (have)", "had", "If + Past; have → had."),
            mc("Выберите модальный глагол (will/would): I ___ join you if I didn't have a rehearsal.", ["will", "would", "would to"], "would", "Would + V1."),
            err("If I were you, I will ignore that email.", "If I were you, I would ignore that email.", "После If I were you — would, не will.", ["If I were you, I'd ignore that email"]),
            xf("С could: The printer is broken. We can't copy this.", "If the printer worked, we could copy this.", "Could в главной части.", ["If the printer weren't broken, we could copy this", "If the printer wasn't broken, we could copy this"]),
            fill("Вставьте нужную форму (not live): If I ___ nearer, I'd walk. (not live)", "didn't live", "If + Past negative.", ["did not live"]),
            mc("Выберите нужную форму (факт всегда): If you heated the chocolate, it ___ . (факт всегда)", ["would melt", "melts", "melted"], "melts", "Всегда правда — Zero, не Second."),
        ],
    ),
    module(
        "third-conditional",
        "Third Conditional",
        "If + Past Perfect, would have + V3: сожаление о закрытом прошлом.",
        24,
        "Если бы тогда вышло иначе",
        lesson(
            "Third Conditional смотрит на прошлое, которое уже не переиграть. If + had + V3, would have + V3. Русское «если бы тогда» = эта схема, не Second. В речи звучит I'd have, she'd have, we wouldn't have. Could have / might have смягчают результат.",
            [
                rule(
                    "Форма",
                    "If I had left earlier, I would have caught the train. Отрицание: If I hadn't left / I wouldn't have caught. Вопрос: Would you have agreed if they had asked?",
                    [
                        ex("If we had booked sooner, we would have got a window seat.", "Если бы забронировали раньше, взяли бы место у окна."),
                        ex("She wouldn't have missed the call if she had heard the phone.", "Она бы не пропустила звонок, если бы услышала телефон."),
                    ],
                ),
                rule(
                    "Сожаление и вина",
                    "Часто рядом I wish / if only, но сам Third уже несёт «жаль, что так вышло». Не ставьте would have в if-часть в стандартном тесте.",
                    [
                        ex("If I had checked the expiry date, I wouldn't have bought that yoghurt.", "Если бы я посмотрел срок, не купил бы этот йогурт."),
                    ],
                ),
                rule(
                    "Could have / might have",
                    "If + Past Perfect, could have + V3 — была бы возможность. Might have — менее уверенный результат. Это всё ещё прошлое нереальное.",
                    [
                        ex("If you had told me, I could have picked you up.", "Если бы сказал, я мог бы заехать."),
                        ex("If she had applied, she might have got an interview.", "Если бы подала заявку, могла бы пройти на собеседование."),
                    ],
                ),
            ],
            compare=[
                {"left": "If I had money, I would take a taxi. (сейчас)", "right": "If I had had money, I would have taken a taxi. (тогда)", "note": "Second про сейчас, Third про вчера."},
            ],
            watch_out=[
                "Не If I would have known — в if нужно If I had known.",
                "Не would + V3 без have: I would caught — ошибка; I would have caught.",
                "Had, не have, в if: If she has left — это уже не Third.",
            ],
            remember="If + had + V3, would have + V3. Только о прошлом, которое не изменить.",
        ),
        [
            fill("If you ___ me, I would have waited. (text)", "had texted", "If + Past Perfect."),
            mc("They ___ the flight if the tram had been on time.", ["would catch", "would have caught", "had caught"], "would have caught", "Главная часть Third — would have + V3."),
            err("If I would have seen the sign, I would have stopped.", "If I had seen the sign, I would have stopped.", "В if — had + V3, не would have."),
            xf("Составьте Third Conditional из двух фактов: I didn't save the draft. I lost the chapter.", "If I had saved the draft, I wouldn't have lost the chapter.", "If + had + V3, wouldn't have + V3.", ["If I had saved the draft, I would not have lost the chapter"]),
            fill("She ___ have come if you had invited her. (would)", "would", "Would have + V3; have уже в предложении."),
            mc("If he hadn't spilt the tea, the keyboard ___ .", ["wouldn't break", "wouldn't have broken", "didn't break"], "wouldn't have broken", "Отрицательный результат в прошлом."),
        ],
        [
            fill("Вставьте нужную форму (finish): We would have hired her if she ___ the trial task. (finish)", "had finished", "If + had + V3."),
            mc("Выберите модальный глагол: If they had left a key, we ___ in.", ["could have got", "could get", "can have got"], "could have got", "Could have + V3 — упущенная возможность."),
            err("I would have wrote sooner.", "I would have written sooner.", "Write — wrote — written."),
            xf("Сожаление: He didn't take a map. He got lost.", "If he had taken a map, he wouldn't have got lost.", "Third с отрицательным результатом.", ["If he had taken a map, he would not have got lost"]),
            fill("Вставьте нужную форму (not be): If I ___ hungry, I would have ordered dessert. (not be)", "hadn't been", "If + hadn't + V3 (been).", ["had not been"]),
            mc("Выберите вспомогательный глагол: If I ___ more time tomorrow, I would help. (гипотеза о будущем)", ["had had", "had", "would have"], "had", "Завтра + нереально сейчас — Second, не Third."),
        ],
    ),
    module(
        "modals-possibility",
        "Модальные глаголы возможности и вывода",
        "Must, might, may, could, can't: насколько мы уверены в догадке.",
        22,
        "Должно быть, может быть, не может быть",
        lesson(
            "Здесь must — не обязанность, а сильный вывод. Шкала уверенности в настоящем: must (почти уверен) → should (ожидаю) → may/might/could (возможно) → can't (логически исключено). Для прошлого вывода к модальному добавляют have + V3: must have left, can't have seen. Русское «должно быть» часто пишут как must to — to не нужно.",
            [
                rule(
                    "Вывод о сейчас",
                    "Must + V1: единственное разумное объяснение. Might / may / could + V1: варианты. Can't + V1: это не сходится с фактами. Couldn't в этом значении тоже встречается, но can't чаще в учебниках.",
                    [
                        ex("The lights are on. Someone must be upstairs.", "Свет горит. Кто-то, должно быть, наверху."),
                        ex("He isn't answering. He might be on the metro.", "Он не отвечает. Может, он в метро."),
                        ex("That can't be the baker — he retired.", "Это не может быть пекарь: он на пенсии."),
                    ],
                ),
                rule(
                    "Вывод о прошлом",
                    "Must have + V3 / might have + V3 / can't have + V3. Не must had и не can't has.",
                    [
                        ex("The pavement is dry. It can't have rained.", "Тротуар сухой. Не могло пройти дождя."),
                        ex("She isn't here. She must have gone home.", "Её нет. Она, должно быть, ушла домой."),
                    ],
                ),
                rule(
                    "Не смешивать с обязанностью",
                    "Must / have to как долг вы уже знаете. В догадке отрицание сильного must — это can't, не mustn't. Mustn't остаётся запретом.",
                    [
                        ex("He must be tired after that shift. (вывод)", "Он, должно быть, устал после смены."),
                        ex("He mustn't skip the briefing. (запрет)", "Ему нельзя пропускать планёрку."),
                    ],
                ),
            ],
            compare=[
                {"left": "She must be in. Her bike is here.", "right": "She can't be in. The flat is dark.", "note": "Сильный да vs сильный нет."},
            ],
            watch_out=[
                "Не must to be / might to go.",
                "Отрицание вывода «это невозможно» — can't, не mustn't.",
                "Прошлое: must have gone, не must had gone.",
            ],
            remember="Must = почти уверен. Might/may/could = возможно. Can't = исключено. Прошлое — modal + have + V3.",
        ),
        [
            mc("The bakery is dark and the shutters are down. It ___ be open.", ["mustn't", "can't", "shouldn't to"], "can't", "Логически исключено — can't."),
            fill("You cooked all afternoon. You ___ be exhausted. (сильный вывод)", "must", "Must + V1 без to."),
            err("He must to be the new intern.", "He must be the new intern.", "После must нет to."),
            xf("Прошлый вывод: Her cup is still warm. (she / leave / just)", "She must have just left.", "Must have + V3.", ["She must have left just now"]),
            fill("I'm not sure. The delay ___ be a signal failure. (возможно)", "might", "Might/may/could; канонический ответ — might.", ["may", "could"]),
            mc("I saw him on the platform. He ___ gone home already.", ["can't have", "mustn't have", "can't has"], "can't have", "Противоречит факту — can't have + V3."),
        ],
        [
            fill("Вставьте модальный глагол must: That painting ___ have cost a fortune. (сильный вывод о прошлом)", "must", "Must have + V3; have уже в предложении."),
            mc("Выберите модальный глагол can: She ___ be in Prague — she posted a story from the office five minutes ago.", ["must", "can't", "might not to"], "can't", "Факт ломает гипотезу."),
            err("They must had forgotten the key.", "They must have forgotten the key.", "Must have + V3, не must had."),
            xf("Мягкая догадка: perhaps + he / wait / outside", "He might be waiting outside.", "Might + be + V-ing для процесса сейчас.", ["He may be waiting outside", "He could be waiting outside"]),
            fill("Вставьте модальный глагол must: We ___ have taken the wrong exit — nothing looks familiar. (вывод о прошлом)", "must", "Must have + V3.", ["might"]),
            mc("Выберите модальный глагол must: You ___ tell anyone — it's confidential. (запрет, не вывод)", ["can't have", "mustn't", "might not be"], "mustn't", "Confidential = запрет, mustn't."),
        ],
    ),
    module(
        "reported-statements",
        "Косвенная речь: утверждения",
        "Say/tell, сдвиг времён, местоимения и маркеры времени.",
        24,
        "Что именно он сказал",
        lesson(
            "В косвенной речи мы передаём чужое утверждение своими словами. После прошедшего reporting-глагола (said, told) времена обычно сдвигаются на шаг в прошлое. Tell требует адресата: she told me. Say — нет: she said (that). That можно опустить.",
            [
                rule(
                    "Say и tell",
                    "Tell + человек + (that) + клауза. Say (+ that) + клауза. Не she said me и не she told that без объекта, если имеете в виду «сказала мне».",
                    [
                        ex("He said (that) the printer was jammed.", "Он сказал, что принтер зажёлся."),
                        ex("He told me (that) the printer was jammed.", "Он сказал мне, что принтер зажёлся."),
                    ],
                ),
                rule(
                    "Сдвиг времён",
                    "Present Simple → Past Simple. Present Continuous → Past Continuous. Present Perfect / Past Simple → Past Perfect. Will → would. Can → could. Must / have to часто → had to. Если факт всё ещё верен, сдвиг иногда не делают, но в упражнении его ждут.",
                    [
                        ex("'I need a receipt.' → She said she needed a receipt.", "«Мне нужен чек» → Она сказала, что ей нужен чек."),
                        ex("'I've booked it.' → He said he had booked it.", "«Я забронировал» → Он сказал, что забронировал."),
                    ],
                ),
                rule(
                    "Местоимения и время-место",
                    "I/you пересчитываются от новой точки зрения. Today → that day, tomorrow → the next day / the following day, yesterday → the day before, now → then, here → there, this → that, ago → before.",
                    [
                        ex("'I'll call tomorrow.' → She said she would call the next day.", "«Позвоню завтра» → Сказала, что позвонит на следующий день."),
                        ex("'We live here.' → They said they lived there.", "«Мы здесь живём» → Сказали, что живут там."),
                    ],
                ),
            ],
            watch_out=[
                "Не she said me the news — нужно told me или said to me.",
                "Кавычки снимают, порядок слов остаётся повествовательным.",
                "Won't → wouldn't, не would not to.",
            ],
            remember="Told + кому. Времена шагают назад. Tomorrow → the next day.",
        ),
        [
            fill("She ___ me the shop closed at eight. (tell, past)", "told", "Tell + адресат."),
            mc("'I am tired.' → Выберите форму в косвенной речи: He said he ___ tired.", ["is", "was", "had been"], "was", "Present Simple → Past Simple."),
            err("Anna said me she was ready.", "Anna told me she was ready.", "Said me нельзя; нужно told me.", ["Anna said to me she was ready"]),
            xf("Косвенно: 'I will send the link tomorrow.' (she / say)", "She said she would send the link the next day.", "Will → would, tomorrow → the next day.", ["She said that she would send the link the next day", "She said she would send the link the following day"]),
            fill("'We have lost the key.' → They said they ___ the key.", "had lost", "Present Perfect → Past Perfect."),
            mc("'I can start on Monday.' → She said she ___ start on Monday.", ["can", "could", "would can"], "could", "Can → could."),
        ],
        [
            fill("Вставьте пропущенное слово: 'I bought this yesterday.' → He said he had bought that ___.", "the day before", "Yesterday → the day before.", ["the previous day"]),
            mc("Выберите пропущенное слово: She ___ that the lift was broken.", ["told", "said", "told to"], "said", "Said that без обязательного адресата."),
            err("He told that he was late.", "He said that he was late.", "Told без адресата нельзя.", ["He told me that he was late"]),
            xf("Передайте косвенной речью от She said: 'I don't like fennel.'", "She said she didn't like fennel.", "Don't → didn't.", ["She said that she didn't like fennel", "She said she did not like fennel"]),
            fill("Вставьте пропущенное слово: 'We're meeting here.' → They said they were meeting ___.", "there", "Here → there."),
            mc("Выберите конструкцию have to: 'I must leave at 5.' → He said he ___ leave at 5.", ["must to", "had to", "have to"], "had to", "Must обязанности часто → had to."),
        ],
    ),
    module(
        "reported-questions",
        "Косвенные вопросы",
        "If/whether и вопросительные слова; порядок как в утверждении, без do/does/did.",
        22,
        "Он спросил, а не «спросил ли» калькой",
        lesson(
            "Косвенный вопрос — это уже не вопрос по форме: знак вопроса часто пропадает, вспомогательный do уходит, подлежащее стоит перед глаголом. Yes/no передаём через if или whether. Специальные — через what/where/when/why/how/who. Reporting-глагол обычно asked (иногда wanted to know).",
            [
                rule(
                    "Yes / no",
                    "He asked if/whether + повествовательный порядок. Сдвиг времён как в утверждениях, если asked в прошлом.",
                    [
                        ex("'Are you free?' → She asked if I was free.", "«Ты свободен?» → Спросила, свободен ли я."),
                        ex("'Have you paid?' → He asked whether we had paid.", "«Вы заплатили?» → Спросил, заплатили ли мы."),
                    ],
                ),
                rule(
                    "Wh- вопросы",
                    "Ask + вопрос-слово + подлежащее + глагол. Не ask where do you live, а ask where I lived.",
                    [
                        ex("'Where do you park?' → She asked where I parked.", "«Где паркуешься?» → Спросила, где я паркуюсь."),
                        ex("'Why has he left?' → They asked why he had left.", "«Почему он ушёл?» → Спросили, почему он ушёл."),
                    ],
                ),
                rule(
                    "To-infinitive после вопроса",
                    "После what/how/where + to часто остаётся инфинитив: She asked how to reset the router. Для вежливых просьб asked me to + V.",
                    [
                        ex("He asked how to get to the depot.", "Он спросил, как проехать до депо."),
                        ex("She asked me to wait by the lift.", "Она попросила меня подождать у лифта."),
                    ],
                ),
            ],
            compare=[
                {"left": "Where do you live?", "right": "She asked where I lived.", "note": "Инверсия и do исчезают."},
            ],
            watch_out=[
                "Не He asked me where do I live.",
                "Не if will I — сдвиг: if I would.",
                "Whether и if почти взаимозаменимы; whether or not звучит официальнее.",
            ],
            remember="Asked + if/whether или wh-слово + прямой порядок. Без do и без вопросительного знака.",
        ),
        [
            fill("'Are they open?' → She asked ___ they were open.", "if", "Yes/no — if или whether.", ["whether"]),
            mc("'What time does the ferry leave?' → He asked what time the ferry ___.", ["does leave", "left", "did leave"], "left", "Does уходит, Present → Past."),
            err("She asked me where do I work.", "She asked me where I worked.", "Повествовательный порядок, сдвиг времени."),
            xf("Передайте косвенным вопросом от He asked me: 'Can you swim?'", "He asked me if I could swim.", "Can → could, if + прямой порядок.", ["He asked me whether I could swim"]),
            fill("'When will you arrive?' → They asked when I ___ arrive.", "would", "Will → would."),
            mc("I asked her ___ she wanted tea or coffee.", ["if", "whether", "what"], "whether", "Выбор or — типичный whether."),
        ],
        [
            fill(
                "Косвенный вопрос: вставьте сдвиг (Present Perfect → Past Perfect): "
                "'Have you seen my pass?' → He asked if I ___ his pass.",
                "had seen",
                "Present Perfect → Past Perfect.",
            ),
            mc(
                "Косвенный вопрос: выберите сдвиг (Past Simple → Past Perfect): "
                "'Who took the parcel?' → She asked who ___ the parcel.",
                ["did take", "had taken", "has taken"],
                "had taken",
                "Past Simple часто → Past Perfect в репортаже.",
            ),
            err("He asked what did I mean.", "He asked what I meant.", "Без did, порядок S + V."),
            xf("Передайте косвенным вопросом от She asked: 'Why are you laughing?'", "She asked why I was laughing.", "Present Continuous → Past Continuous.", ["She asked why I was laughing."]),
            fill("Вставьте предлог: The tourist asked how ___ get to the station. (инфинитив)", "to", "How to + V1."),
            mc("Выберите предлог: They asked me ___ wait outside.", ["if", "to", "that"], "to", "Ask someone to + V — просьба."),
        ],
    ),
    module(
        "passive-all-simple",
        "Пассив во всех простых временах",
        "Be в нужном времени + V3: Present, Past, Perfect, Future и модальный пассив.",
        22,
        "Подлежащее — то, что получают",
        lesson(
            "На A2 пассив был в Present и Past Simple. На B1 добавляются Present Perfect Passive (has/have been + V3), Future (will be + V3) и модальный (must/can/should be + V3). Во всех случаях меняется только be (и возможные have/will/modal), смысловой глагол остаётся V3.",
            [
                rule(
                    "Карта форм",
                    "Present: is/are + V3. Past: was/were + V3. Present Perfect: has/have been + V3. Future: will be + V3. Модальный: modal + be + V3.",
                    [
                        ex("The invoices have been sent.", "Счета уже отправлены."),
                        ex("The hall will be repainted in May.", "Зал перекрасят в мае."),
                        ex("Phones must be switched off in here.", "Здесь телефоны должны быть выключены."),
                    ],
                ),
                rule(
                    "Вопрос и отрицание",
                    "Вспомогательный элемент выходит вперёд: Has the parcel been scanned? Will the results be published? Отрицание цепляется к первому вспомогательному: hasn't been, won't be, shouldn't be.",
                    [
                        ex("Has the leak been fixed yet?", "Течь уже устранили?"),
                        ex("The names won't be announced today.", "Имена сегодня не объявят."),
                    ],
                ),
                rule(
                    "Зачем пассив на B1",
                    "Процесс, новость, правило, неизвестный деятель. By добавляйте, когда без него теряется смысл. Get + V3 (got stolen) разговорнее; в формальном письме держите be.",
                    [
                        ex("A new cycle lane is being discussed. (уже Continuous, для ориентира)", "Обсуждают новую велополосу."),
                        ex("My wallet got stolen — more informal than was stolen.", "Кошелёк украли — разговорный get-пассив."),
                    ],
                ),
            ],
            compare=[
                {"left": "They have repaired the lift.", "right": "The lift has been repaired.", "note": "Один смысл; пассив прячет they."},
            ],
            watch_out=[
                "Been, не being, в Perfect Passive: has been sent, не has being sent.",
                "После modal — be, не been: must be signed, не must been signed.",
                "Will be done, не will done.",
            ],
            remember="Время несёт be (и have/will/modal). Смысловой глагол всегда V3.",
        ),
        [
            fill("The keys ___ already been returned. (have)", "have", "Present Perfect Passive: have been + V3."),
            mc("The results ___ published tomorrow.", ["are", "will be", "have been"], "will be", "Завтра — will be + V3."),
            err("The window has being repaired.", "The window has been repaired.", "Perfect Passive — been, не being."),
            xf("Пассив: They must lock the fire door.", "The fire door must be locked.", "Modal + be + V3."),
            fill("___ the documents been signed yet?", "Have", "Have + подлежащее + been + V3."),
            mc("This form ___ in ink.", ["must be completed", "must completed", "must been completed"], "must be completed", "Must + be + V3."),
        ],
        [
            fill("Вставьте форму to be: Two windows ___ broken in the storm. (be, past)", "were", "Past Simple Passive, множественное."),
            mc("Выберите форму Present Perfect: A decision ___ yet.", ["hasn't been made", "hasn't made", "wasn't been made"], "hasn't been made", "Present Perfect Passive negative."),
            err("The email will sent today.", "The email will be sent today.", "Will be + V3."),
            xf("Пассив Perfect: Someone has eaten the leftovers.", "The leftovers have been eaten.", "Have been + V3."),
            fill("Вставьте форму to be: Applications should ___ submitted by Friday.", "be", "Modal + be + V3."),
            mc("Выберите форму пассива: English ___ in this office.", ["speaks", "is spoken", "has spoken"], "is spoken", "Present Simple Passive."),
        ],
    ),
    module(
        "defining-nondefining",
        "Определяющие и неопределяющие придаточные",
        "Запятые, запрет that в non-defining, who/which для дополнительной информации.",
        20,
        "Нужно ли это, чтобы понять «кто именно»",
        lesson(
            "Defining-придаточное сужает класс: без него неясно, о ком речь. Non-defining добавляет комментарий о уже известном человеке или вещи и выделяется запятыми. That живёт только в defining. В non-defining who/which опустить нельзя.",
            [
                rule(
                    "Defining — без запятых",
                    "The colleague who sits by the window has your stapler. That возможно: the charger that I borrowed. Дополнение можно опустить: the charger I borrowed.",
                    [
                        ex("Passengers who boarded at Tartu should stay in carriage B.", "Пассажиры, которые сели в Тарту, остаются в вагоне B."),
                        ex("The shop that sells yeast closes at 6.", "Магазин, который продаёт дрожжи, закрывается в 6."),
                    ],
                ),
                rule(
                    "Non-defining — с запятыми",
                    "Перед и после придаточного запятые (если оно в середине). Только who / which / whose / where, не that. Смысл: это просто добавка.",
                    [
                        ex("My neighbour, who repairs bikes, offered to help.", "Мой сосед, который чинит велосипеды, предложил помочь. (сосед уже известен)"),
                        ex("The Narva gate, which was restored last year, is lit at night.", "Нарвские ворота, которые реставрировали в прошлом году, ночью подсвечены."),
                    ],
                ),
                rule(
                    "Тест «можно ли выкинуть»",
                    "Если без придаточного предложение всё ещё называет того же человека/объект однозначно — non-defining и запятые. Если без него непонятно какой — defining, без запятых.",
                    [
                        ex("My father, who hates fennel, cooked the stew. (отец один)", "Мой отец, который терпеть не может фенхель, сварил рагу."),
                        ex("The man who hates fennel cooked the stew. (какой именно мужчина)", "Мужчина, который ненавидит фенхель, сварил рагу."),
                    ],
                ),
            ],
            compare=[
                {"left": "The staff who arrived late stayed after hours.", "right": "The staff, who arrived late, stayed after hours.", "note": "Только опоздавшие vs все сотрудники (и они, кстати, опоздали)."},
            ],
            watch_out=[
                "Не that после запятой: My bike, that I bought… — нужно which.",
                "Не опускайте who/which в non-defining.",
                "Не ставьте запятую в defining: The man, who called you, is here — если мужчин много, запятые врут.",
            ],
            remember="Сужает смысл — без запятых, that можно. Комментарий — запятые, только who/which.",
        ),
        [
            mc("My sister, ___ lives in Ghent, is visiting.", ["that", "who", "what"], "who", "Non-defining, запятые — who, не that."),
            fill("The keys ___ I left on the piano have vanished. (defining, вещь)", "that", "Defining — that/which или опущение.", ["which", "—"]),
            err("Prague, that I visit every spring, is cheaper in February.", "Prague, which I visit every spring, is cheaper in February.", "После запятой which, не that."),
            xf("Добавьте non-defining: The river is frozen. The river runs past our block.", "The river, which runs past our block, is frozen.", "Запятые + which."),
            fill("People ___ skip breakfast get a headache here. (defining)", "who", "Класс людей — defining who/that.", ["that"]),
            mc("This is the adapter I borrowed. The relative pronoun is…", ["обязателен", "можно опустить", "только which"], "можно опустить", "Дополнение в defining можно не ставить."),
        ],
        [
            fill("Вставьте вопросительное / относительное слово: Our landlord, ___ is away in June, left us a spare key.", "who", "Известное лицо + запятые — who."),
            mc("Выберите вопросительное / относительное слово: The tram ___ goes to the harbour is packed at 8.", [", which", "which", ", that"], "which", "Defining без запятых; which/that оба возможны, из вариантов — which без запятой."),
            err("The woman, who sold me this ticket is a volunteer. (женщина из очереди, без неё непонятно какая)", "The woman who sold me this ticket is a volunteer.", "Defining — без запятой."),
            xf("Объедините в defining relative clause с where: That's the café. We found the cat there.", "That's the café where we found the cat.", "Where в defining.", ["That is the café where we found the cat"]),
            fill("Вставьте форму to be: The annex, which ___ rebuilt in 2019, now holds the archive. (be, past passive)", "was", "Non-defining + Past Passive."),
            mc("Выберите вопросительное / относительное слово: You cannot use ___ in a non-defining clause.", ["which", "who", "that"], "that", "That в non-defining не ставят."),
        ],
    ),
    module(
        "gerund-vs-infinitive",
        "Герундий и инфинитив",
        "Enjoy -ing, decide to, и пары stop / remember / try с разным смыслом.",
        24,
        "После глагола: -ing или to?",
        lesson(
            "После одних глаголов английский хочет -ing (герундий), после других — to + V1. Список нужно копить, но каркас B1 уже устойчив. Отдельный слой — глаголы, которые берут оба варианта с разным смыслом: stop, remember, forget, try, regret. Русский инфинитив («люблю читать») не подсказывает форму.",
            [
                rule(
                    "Обычно герундий",
                    "Enjoy, mind, avoid, finish, keep, suggest, consider, miss, practise, risk, give up, look forward to + -ing. После предлога тоже -ing: I'm good at baking.",
                    [
                        ex("Would you mind closing the vent?", "Не закроешь форточку?"),
                        ex("She suggested taking the earlier coach.", "Она предложила сесть на более ранний автобус."),
                    ],
                ),
                rule(
                    "Обычно инфинитив",
                    "Decide, hope, want, need, plan, promise, refuse, afford, learn, offer, fail, agree + to + V1. После прилагательных часто to: it's hard to hear.",
                    [
                        ex("We decided to split the bill.", "Мы решили разделить счёт."),
                        ex("He promised to send the measurements.", "Он пообещал прислать размеры."),
                    ],
                ),
                rule(
                    "Два смысла",
                    "Stop doing — перестать делать. Stop to do — остановиться, чтобы сделать. Remember doing — помню, как делал. Remember to do — не забыть сделать. Try doing — попробовать способ. Try to do — пытаться (есть трудность).",
                    [
                        ex("I stopped drinking coffee. / I stopped to drink water.", "Бросил кофе. / Остановился, чтобы выпить воды."),
                        ex("I remember locking the door. / Remember to lock the door.", "Помню, как запирал. / Не забудь запереть."),
                    ],
                ),
            ],
            compare=[
                {"left": "I tried to open it — the lock was frozen.", "right": "I tried opening it with oil — that worked.", "note": "Попытка с усилием vs эксперимент со способом."},
            ],
            watch_out=[
                "Look forward to + -ing: to здесь предлог, не инфинитив. Не I look forward to see you.",
                "Suggest going, не suggest to go (в этом значении).",
                "После would like / would love — to, не -ing: I'd like to sit.",
            ],
            remember="Предлог и enjoy/avoid/suggest — -ing. Decide/want/promise — to. Stop/remember/try меняют смысл.",
        ),
        [
            fill("I enjoy ___ bread on Sundays. (bake)", "baking", "Enjoy + -ing."),
            mc("They decided ___ the lease.", ["renewing", "to renew", "renew"], "to renew", "Decide + to."),
            err("I look forward to meet your team.", "I look forward to meeting your team.", "To — предлог, дальше -ing."),
            xf("Перестаньте делать: Please stop / slam / the door", "Please stop slamming the door.", "Stop + -ing = прекратить действие."),
            fill("Remember ___ the spare key to Lena. (не забыть)", "to leave", "Remember to = не забыть сделать.", ["to give"]),
            mc("He suggested ___ a later train.", ["to take", "taking", "take"], "taking", "Suggest + -ing."),
        ],
        [
            fill("Вставьте нужную форму (not call): She promised ___ after 10. (not call)", "not to call", "Promise + not to + V1."),
            mc("Выберите пропущенное слово: I stopped ___ a sandwich and then continued walking.", ["eating", "to eat", "eat"], "to eat", "Остановился, чтобы поесть."),
            err("Would you mind to wait here?", "Would you mind waiting here?", "Mind + -ing."),
            xf("Попытка-способ: The jar was stuck. (try / tap / the lid)", "I tried tapping the lid.", "Try + -ing = способ.", ["Try tapping the lid."]),
            fill("Вставьте нужную форму (check): It's important ___ the date. (check)", "to check", "Прилагательное + to."),
            mc("Выберите пропущенное слово: I remember ___ her at the harbour in 2019.", ["to meet", "meeting", "meet"], "meeting", "Помню сам факт встречи — remember + -ing."),
        ],
    ),
    module(
        "wish-past-simple",
        "Wish + Past Simple",
        "Сожаление о настоящем: I wish I had / I wish I could; if only.",
        18,
        "Жаль, что сейчас не так",
        lesson(
            "I wish + Past Simple рисует другое настоящее. Глагол в прошедшем — это снова «дистанция», как во Second Conditional, а не рассказ о вчера. I wish I could — неумение сейчас. If only усиливает то же значение. Wish + would используют, когда чужое повторяющееся поведение раздражает; к своим привычкам would обычно не ставят.",
            [
                rule(
                    "Другое настоящее",
                    "I wish + Past Simple: I wish we lived nearer the depot. Для be чаще I wish I were (учебная норма), в речи встречается was.",
                    [
                        ex("I wish I knew her extension number.", "Жаль, что я не знаю её добавочный."),
                        ex("I wish it were Friday already.", "Хоть бы уже была пятница."),
                    ],
                ),
                rule(
                    "Could и if only",
                    "I wish I could + V1 — нет способности или возможности сейчас. If only + Past Simple = более эмоциональный wish.",
                    [
                        ex("I wish I could stay for the encore.", "Жаль, что не могу остаться на бис."),
                        ex("If only this tram had USB sockets.", "Вот бы в этом трамвае были USB-разъёмы. (had = Past для настоящего желания)"),
                    ],
                ),
                rule(
                    "Wish + would — не про себя",
                    "I wish you would… = сделай иначе / перестань. I wish it would stop raining. Не I wish I would study more — для своего поведения лучше I wish I studied или I wish I could.",
                    [
                        ex("I wish you wouldn't leave crumbs on the map.", "Хоть бы ты не оставлял крошки на карте."),
                        ex("I wish the neighbours would turn the bass down.", "Хоть бы соседи убавили бас."),
                    ],
                ),
            ],
            compare=[
                {"left": "I wish I had a balcony. (сейчас нет)", "right": "I wish I had had a balcony then. (это уже wish + Past Perfect, уровень выше)", "note": "Past Simple после wish = настоящее. Past Perfect = прошлое."},
            ],
            watch_out=[
                "Не I wish I have / I wish I know — нужен Past.",
                "Не I wish I would be taller — рост не «поведение»; I wish I were taller.",
                "Wish + would не для собственной дисциплины.",
            ],
            remember="Wish + Past Simple = жаль, что сейчас не так. Could — нет возможности. Would — чужое поведение.",
        ),
        [
            fill("I wish I ___ the code to the loft. (know)", "knew", "Wish + Past Simple."),
            mc("I wish I ___ taller.", ["am", "were", "would be"], "were", "Учебная норма — were."),
            err("I wish I have more free evenings.", "I wish I had more free evenings.", "После wish — Past."),
            xf("Сожаление о настоящем: I can't drive.", "I wish I could drive.", "Wish + could + V1."),
            fill("If only it ___ so noisy here. (not be)", "weren't", "If only + Past; be → were.", ["wasn't", "were not", "was not"]),
            mc("I wish you ___ slam the gate at midnight.", ["wouldn't", "didn't to", "won't"], "wouldn't", "Чужое раздражающее действие — wish + would."),
        ],
        [
            fill("Вставьте нужную форму (live): She wishes she ___ nearer the river. (live)", "lived", "Wish + Past Simple, 3-е лицо wishes."),
            mc("Выберите модальный глагол: I wish I ___ stay, but the last bus is at 10.", ["can", "could", "would can"], "could", "Нет возможности сейчас."),
            err("I wish I would wake up earlier. (про свою привычку)", "I wish I woke up earlier.", "Для своего поведения — Past Simple, не would.", ["I wish I could wake up earlier"]),
            xf("If only + настоящее желание: the shop / be / open", "If only the shop were open.", "If only + Past.", ["If only the shop was open"]),
            fill("Вставьте нужную форму (not have): I wish we ___ to rush. (not have)", "didn't have", "Wish + Past negative.", ["did not have"]),
            mc("Выберите нужную форму (это уже прошлое — маркер уровня): I wish I ___ that email yesterday. (это уже прошлое — маркер уровня)", ["didn't send", "hadn't sent", "wouldn't send"], "hadn't sent", "Закрытое вчера — wish + Past Perfect, не Past Simple."),
        ],
    ),
    module(
        "question-tags",
        "Разделительные вопросы",
        "Хвостик противоположной полярности: aren't I, shall we, will you.",
        18,
        "Правда же?",
        lesson(
            "Question tag цепляется к утверждению и просит подтверждения. Если фраза плюс — хвост минус, и наоборот. Вспомогательный глагол в хвосте тот же, что несёт время: do/does/did, be, have, will, can, should. Местоимение в хвосте, не имя. Тон: падение — почти уверен; подъём — настоящий вопрос.",
            [
                rule(
                    "Базовая полярность",
                    "You're on the early shift, aren't you? She left, didn't she? They haven't called, have they? Отрицательное слово (never, hardly, nobody) делает предложение «минусом»: Nobody called, did they?",
                    [
                        ex("The tram stops here, doesn't it?", "Трамвай здесь останавливается, да?"),
                        ex("He never eats fennel, does he?", "Он никогда не ест фенхель, правда?"),
                    ],
                ),
                rule(
                    "Особые хвосты",
                    "I'm → aren't I. Let's → shall we. There is/are → isn't there / aren't there. Don't… (императив) → will you? После have как смыслового «иметь» в британском варианте часто have/haven't; в американском — do/don't.",
                    [
                        ex("I'm next, aren't I?", "Я следующий, да?"),
                        ex("Let's take the riverside path, shall we?", "Давай пойдём вдоль реки, хорошо?"),
                        ex("Don't forget the tokens, will you?", "Не забудь жетоны, ладно?"),
                    ],
                ),
                rule(
                    "Have, used to, there",
                    "She's left (has) → hasn't she? She has a loft (владение, BrE) → hasn't she? You used to cycle here → didn't you?",
                    [
                        ex("There were spare chairs, weren't there?", "Были же запасные стулья?"),
                        ex("You used to work nights, didn't you?", "Ты ведь раньше работал по ночам?"),
                    ],
                ),
            ],
            watch_out=[
                "Не повтор имени: Marta is late, isn't Marta? — нужно isn't she?",
                "I'm …, aren't I? не amn't I в стандартном английском.",
                "Never / hardly уже отрицание — хвост положительный.",
            ],
            remember="Плюс → минус-хвост. I'm → aren't I. Let's → shall we. Местоимение, не имя.",
        ),
        [
            fill("You're taking the night train, ___ you?", "aren't", "Положительное be → отрицательный хвост."),
            mc("She sent the file, ___ she?", ["hasn't", "didn't", "doesn't"], "didn't", "Past Simple — did."),
            err("I'm late, am I not? (разговорный стандартный хвост)", "I'm late, aren't I?", "Стандарт — aren't I.", ["I am late, aren't I?"]),
            xf("Добавьте хвост: Let's skip dessert.", "Let's skip dessert, shall we?", "Let's → shall we.", ["Let us skip dessert, shall we?"]),
            fill("He never locks the shed, ___ he?", "does", "Never = отрицание → положительный хвост does."),
            mc("Don't lean on that glass, ___ you?", ["do", "will", "won't"], "will", "Отрицательный императив → will you?"),
        ],
        [
            fill("Вставьте вспомогательный глагол: They haven't billed us, ___ they?", "have", "Отрицание have → положительный хвост."),
            mc("Выберите пропущенное слово: There is a spare key, ___ ?", ["isn't it", "isn't there", "aren't there"], "isn't there", "There is → isn't there."),
            err("Marta can swim, can't Marta?", "Marta can swim, can't she?", "В хвосте местоимение."),
            xf("Хвост: You used to live above the bakery.", "You used to live above the bakery, didn't you?", "Used to → did."),
            fill("Вставьте модальный глагол should: We should leave a tip, ___ we?", "shouldn't", "Should → shouldn't."),
            mc("Выберите вспомогательный глагол: Nobody called back, ___ they?", ["did", "didn't", "do"], "did", "Nobody — отрицательное слово, хвост положительный; they для nobody."),
        ],
    ),
]
