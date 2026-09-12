from app.seed.helpers import err, ex, fill, lesson, mc, module, rule, xf

B2 = [
    module(
        "mixed-conditionals",
        "Смешанные условные предложения",
        "Как соединить прошлое условие с настоящим результатом и наоборот.",
        24,
        "Два времени — одна конструкция",
        lesson(
            "Классические второй и третий типы условных держат причину и следствие в одном временном плане. Смешанные условные разводят эти планы: прошлое решение продолжает влиять на настоящее, или устойчивая черта характера объясняет вчерашнюю ошибку. Это не «ещё один тип ради списка», а точный выбор двух якорей: когда случилось условие и когда проявляется следствие.",
            [
                rule(
                    "Прошлое условие → нынешний результат",
                    "If + Past Perfect, would / could / might + инфинитив. Условие уже не изменить; следствие описывает текущую ситуацию, роль, привычку или состояние.",
                    [
                        ex("If I had accepted that transfer, I would live in Osaka now.", "Если бы я тогда принял перевод, я бы сейчас жил в Осаке."),
                        ex("If she hadn't sprained her ankle, she could be playing in the final tonight.", "Если бы она не подвернула лодыжку, сегодня вечером она могла бы играть в финале."),
                    ],
                ),
                rule(
                    "Настоящее/устойчивое условие → прошлый результат",
                    "If + Past Simple (или were), would have / could have / might have + V3. Черта характера, привычка или текущий факт объясняют уже свершившееся.",
                    [
                        ex("If he were more diplomatic, he wouldn't have emailed the whole board.", "Если бы он был дипломатичнее, он бы не разослал письмо всему совету."),
                        ex("If I didn't hate heights, I would have taken the glass lift.", "Если бы я не боялся высоты, я бы поехал на стеклянном лифте."),
                    ],
                ),
                rule(
                    "Как выбрать смесь, а не «чистый» тип",
                    "Спросите: условие уже в прошлом или это всё ещё правда о человеке/мире? Результат — сейчас или тогда? Маркеры now, today, still, these days тянут следствие в настоящее; yesterday, last year, that evening — в прошлое.",
                    [
                        ex("If you had packed the adapter, we wouldn't be hunting for a charger now.", "Если бы ты положил адаптер, мы бы сейчас не искали зарядку."),
                        ex("If she spoke Arabic, she would have taken the Cairo posting last spring.", "Если бы она говорила по-арабски, она бы взяла каирскую командировку прошлой весной."),
                    ],
                ),
            ],
            compare=[
                {"left": "If I had studied law, I would have become a solicitor.", "right": "If I had studied law, I would be a solicitor now.", "note": "Слева весь сценарий в прошлом; справа прошлое решение держит нынешнюю профессию."},
            ],
            watch_out=[
                "Не ставьте would в if-части: If I would have known — ошибка.",
                "Were остаётся естественным в гипотезах о настоящем: If I were richer, not If I was richer в аккуратной письменной речи.",
            ],
            remember="Смешивайте времена только если условие и результат живут в разных эпохах. Сначала якорь условия, затем якорь следствия.",
        ),
        [
            mc("If she ___ the grant, she would be leading the lab now.", ["won", "had won", "would win"], "had won", "Прошлое условие при нынешнем результате требует Past Perfect."),
            fill("If I were tidier, I ___ lost the keys yesterday. (not / would)", "wouldn't have", "Устойчивая черта → прошлый результат: wouldn't have + V3.", ["would not have"]),
            xf("Смешайте: прошлый отказ от курса → сейчас нет сертификата. If I / take / the course → I / have / a certificate now.", "If I had taken the course, I would have a certificate now.", "Past Perfect в условии, would + инфинитив в результате."),
            err("If he would have slept more, he wouldn't be exhausted today.", "If he had slept more, he wouldn't be exhausted today.", "В if-части нужен Past Perfect, не would have."),
            fill("If they ___ so stubborn, they would have signed the deal last week. (not / be)", "weren't", "Текущая черта — Past Simple.", ["were not"]),
            mc("Какая пара времён для «тогда не уехал → сейчас всё ещё здесь»?", ["If + Past Simple, would have + V3", "If + Past Perfect, would + infinitive", "If + Present Simple, will + infinitive"], "If + Past Perfect, would + infinitive", "Прошлое условие, нынешний результат."),
        ],
        [
            mc("If I ___ allergic to cats, I would have kept the kitten.", ["hadn't been", "weren't", "wouldn't be"], "weren't", "Аллергия — устойчивое настоящее условие."),
            fill("If we had booked earlier, we ___ on the waiting list now. (not / be)", "wouldn't be", "Прошлое условие, нынешнее состояние.", ["would not be"]),
            xf("Смешайте: он не бережлив (сейчас) → вчера истратил всю премию.", "If he were more frugal, he wouldn't have spent the whole bonus yesterday.", "Were + wouldn't have + V3."),
            err("If she studied medicine, she would have been a surgeon now.", "If she had studied medicine, she would be a surgeon now.", "Учёба в прошлом, профессия сейчас."),
            fill("If you ___ me the brief, I wouldn't be improvising on stage. (send / past)", "had sent", "Пропущенный бриф — прошлое условие."),
            mc("If I didn't trust her, I ___ her the draft last night.", ["wouldn't send", "wouldn't have sent", "hadn't sent"], "wouldn't have sent", "Текущее доверие объясняет уже совершённое действие."),
        ],
    ),
    module(
        "wish-if-only",
        "Wish и if only",
        "Сожаление о настоящем и прошлом, раздражение и сильное желание изменить факт.",
        22,
        "Когда реальность не нравится",
        lesson(
            "Wish и if only не описывают будущее обещание, а оценивают реальность как неудовлетворительную. Грамматическое «сдвиг назад» показывает нереальность: настоящее рисуется Past Simple, прошлое — Past Perfect, чужое поведение, которое нас раздражает, — would. If only звучит эмоциональнее, чем I wish.",
            [
                rule(
                    "Настоящее и устойчивые факты: wish + Past Simple / could",
                    "Жалеем о том, что верно сейчас. I wish I knew, I wish I could swim, I wish it weren't raining. Were предпочтителен в формальной речи.",
                    [
                        ex("I wish I had a spare charger in this bag.", "Жаль, что у меня в сумке нет запасной зарядки."),
                        ex("If only this office weren't so noisy after lunch.", "Если бы только этот офис не был таким шумным после обеда."),
                    ],
                ),
                rule(
                    "Прошлое: wish + Past Perfect",
                    "Сожаление о уже случившемся или не случившемся. Это близкий родственник третьего условного, но без явного if-сценария.",
                    [
                        ex("She wishes she had saved the earlier draft.", "Она жалеет, что не сохранила более ранний черновик."),
                        ex("If only we had checked the tide timetable.", "Если бы только мы сверили расписание приливов."),
                    ],
                ),
                rule(
                    "Раздражение и отказ меняться: wish + would",
                    "Would указывает на чужое повторяющееся поведение или на ситуацию, которую собеседник theoretically может изменить. Не говорят I wish I would — собственную волю так не кодируют.",
                    [
                        ex("I wish you wouldn't leave mugs on the scanner.", "Хотел бы я, чтобы ты не оставлял кружки на сканере."),
                        ex("If only the neighbours would stop drilling at dawn.", "Если бы только соседи перестали сверлить на рассвете."),
                    ],
                ),
            ],
            compare=[
                {"left": "I wish I lived nearer the station.", "right": "I wish I had lived nearer the station last year.", "note": "Слева нынешний адрес; справа адрес в прошлом, который уже не вернуть."},
                {"left": "I wish it would stop raining.", "right": "I wish it weren't raining.", "note": "Would — нетерпеливое ожидание перемены; Past Simple — оценка текущего факта."},
            ],
            watch_out=[
                "I wish I would be taller — ошибка; о себе в настоящем: I wish I were taller.",
                "Wish + would не подходит, если субъект не может «решить» измениться: погода иногда допустима как жалоба, рост — нет.",
            ],
            remember="Сдвиг назад маркирует нереальность. Про себя в настоящем — Past Simple; о прошлом — Past Perfect; о чужом упрямстве — would.",
        ),
        [
            mc("I wish I ___ the name of that café.", ["know", "knew", "had known"], "knew", "Незнание актуально сейчас — Past Simple."),
            fill("If only they ___ the attachment before sending. (check)", "had checked", "Сожаление о прошлом действии."),
            xf("Выразите раздражение: The printer keeps jamming.", "I wish the printer wouldn't keep jamming.", "Wish + would о повторяющейся помехе.", ["I wish the printer would stop jamming"]),
            err("I wish I would have more free evenings.", "I wish I had more free evenings.", "О своём расписании нужен Past Simple, не would."),
            fill("She wishes she ___ interrupt the keynote. (not / would)", "wouldn't", "Чужое поведение.", ["would not"]),
            mc("If only we ___ a table earlier.", ["book", "booked", "had booked"], "had booked", "Упущенный шанс в прошлом."),
        ],
        [
            fill("I wish this corridor ___ so dark. (not / be)", "weren't", "Нынешний факт.", ["were not", "wasn't", "was not"]),
            mc("He wishes he ___ louder during the pitch.", ["speaks", "spoke", "had spoken"], "had spoken", "Питч уже закончился."),
            xf("Сильнее, чем I wish: I wish I had asked for feedback.", "If only I had asked for feedback.", "If only усиливает то же Past Perfect."),
            err("I wish you will stop humming.", "I wish you would stop humming.", "Раздражение кодируется would, не will."),
            fill("They wish they ___ the later train. (catch)", "had caught", "Пропущенный поезд — Past Perfect."),
            mc("I wish I ___ ski, then I'd join you this weekend.", ["can", "could", "had been able"], "could", "Нынешнее умение: wish + could."),
        ],
    ),
    module(
        "modals-deduction",
        "Модальные глаголы: вывод о настоящем",
        "Must, can't, should, might, could, may — степень уверенности, а не обязанность.",
        21,
        "Насколько мы уверены прямо сейчас",
        lesson(
            "На уровне B2 модальные часто описывают не правила, а логический вывод. Говорящий оценивает вероятность текущего факта: от почти доказанного must до осторожного might / could / may и категорического can't. Should здесь — «ожидаемо по норме», а не совет.",
            [
                rule(
                    "Высокая уверенность: must и can't",
                    "Must = единственное разумное объяснение. Can't (иногда couldn't в британском) = вывод исключает возможность. Don't use mustn’t for deduction: mustn't — запрет.",
                    [
                        ex("Her coat is still on the hook; she must be in the building.", "Её пальто всё ещё на крючке: она, должно быть, в здании."),
                        ex("That rumour can't be true — the minutes contradict it.", "Этот слух не может быть правдой: протоколу он противоречит."),
                    ],
                ),
                rule(
                    "Средняя и низкая вероятность: should, may, might, could",
                    "Should — ожидаемый ход вещей. May / might / could — открытые гипотезы; might чуть осторожнее may, could подчёркивает одну из опций, а не «умение».",
                    [
                        ex("The package should be at reception by now.", "Посылка к этому моменту уже должна быть на ресепшене."),
                        ex("He might be stuck in the underpass — the signal dies there.", "Он, возможно, застрял в подземном переходе — там пропадает связь."),
                    ],
                ),
                rule(
                    "Отрицание и вопрос о гипотезе",
                    "May not / might not = возможно, нет. Couldn't в выводе часто ближе к can't. Вопрос о возможности: Could this be the wrong file? Couldn't she be travelling?",
                    [
                        ex("The figures may not be final; finance is still reconciling.", "Цифры могут быть ещё не финальными: финансы всё ещё сверяют."),
                        ex("Could that hum be the projector fan?", "Этот гул может быть вентилятором проектора?"),
                    ],
                ),
            ],
            compare=[
                {"left": "She must be the new editor.", "right": "She must be at the meeting — it's compulsory.", "note": "Слева логический вывод; справа обязанность. Контекст решает, не форма."},
                {"left": "He can't be serious.", "right": "He mustn't be late.", "note": "Can't — невозможный вывод; mustn't — запрет."},
            ],
            watch_out=[
                "Mustn't не заменяет can't в значении «не может быть, что…».",
                "Can в утверждении почти не выражает слабую вероятность: не He can be at home в смысле «может быть дома» — нужно may/might/could.",
            ],
            remember="Must / can't — почти доказано. Should — по ожиданиям. May / might / could — гипотеза. Смотрите на запрет versus вывод.",
        ),
        [
            mc("The lights are on. They ___ be working late.", ["can't", "must", "mustn't"], "must", "Включенный свет — сильный довод в пользу вывода."),
            fill("This translation ___ be hers — she doesn't know Finnish. (can't)", "can't", "Факт исключает авторство."),
            xf("Ослабьте уверенность: She is in the archive.", "She might be in the archive.", "Might кодирует гипотезу.", ["She may be in the archive", "She could be in the archive"]),
            err("He mustn't be the author; the style is completely different.", "He can't be the author; the style is completely different.", "Для невозможного вывода нужен can't."),
            fill("The train ___ be delayed — there's engineering work. (should / expectation)", "should", "Ожидаемый ход событий."),
            mc("Choose the most tentative option.", ["She must be joking.", "She may be joking.", "She can't be joking."], "She may be joking.", "May оставляет возможность открытой."),
        ],
        [
            fill("You've been on your feet all day; you ___ be exhausted. (must)", "must", "Логичный вывод о состоянии."),
            mc("It ___ be the original file; the metadata looks generated.", ["must", "can't", "mustn't"], "can't", "Метаданные опровергают подлинность."),
            xf("Сделайте осторожный вывод: The café is closed.", "The café might be closed.", "Might / may / could допустимы; канонический ответ — might.", ["The café may be closed", "The café could be closed"]),
            err("She can be at the dentist, I'm not sure.", "She could be at the dentist, I'm not sure.", "Для гипотезы в утверждении нужен could/might/may, не can."),
            fill("They ___ not have the latest patch yet. (may)", "may", "Возможно, патча нет."),
            mc("The kettle has boiled, so the water ___ be ready.", ["should", "can't", "mustn't"], "should", "По нормальному ходу вещей вода готова."),
        ],
    ),
    module(
        "past-modals",
        "Модальные о прошлом",
        "Must have, can't have, should have, needn't have и отличие от didn't need to.",
        25,
        "Вывод, упрёк и лишняя работа вчера",
        lesson(
            "Чтобы говорить о прошлом выводе или оценке, модальный соединяется с перфектным инфинитивом: modal + have + V3. Так кодируются почти доказанный факт (must have), невозможность (can't have), упущенная норма (should have) и действие, которое оказалось ненужным (needn't have). Отдельно стоит didn't need to: необходимости не было, и часто действие так и не совершили.",
            [
                rule(
                    "Вывод о прошлом: must / can't / might have",
                    "Must have + V3 — единственное правдоподобное объяснение вчерашнего. Can't / couldn't have — такое прошлое несовместимо с фактами. Might / may / could have — одна из версий.",
                    [
                        ex("The streets are dry; it can't have rained overnight.", "Улицы сухие: ночью не могло пройти дождя."),
                        ex("He might have left his pass in the taxi.", "Он, возможно, оставил пропуск в такси."),
                    ],
                ),
                rule(
                    "Оценка прошлого: should have, ought to have, could have",
                    "Should have — ожидаемое, но не сделанное, или упрёк. Could have — неиспользованная возможность, иногда укор. Эти формы смотрят назад, а не планируют.",
                    [
                        ex("You should have labelled the samples before the audit.", "Тебе следовало подписать образцы до аудита."),
                        ex("We could have taken the river path and avoided the roadworks.", "Мы могли пойти вдоль реки и обойти ремонт."),
                    ],
                ),
                rule(
                    "Needn't have и didn't need to",
                    "Needn't have + V3: действие совершили, потом выяснилось, что зря. Didn't need to: обязанности не было; часто (но не всегда) действие не делали. Контекст должен это показать.",
                    [
                        ex("You needn't have printed fifty copies; the room has a screen.", "Зря ты печатал пятьдесят копий: в зале есть экран."),
                        ex("We didn't need to print anything — they had already circulated the slides.", "Нам не нужно было ничего печатать: слайды уже разослали."),
                    ],
                ),
            ],
            compare=[
                {"left": "She must have missed the announcement.", "right": "She should have heard the announcement.", "note": "Must have — вывод о факте; should have — норма, которую она, видимо, нарушила."},
                {"left": "I needn't have packed a coat.", "right": "I didn't need to pack a coat, so I left it.", "note": "Needn't have подразумевает, что пальто всё-таки положили."},
            ],
            watch_out=[
                "Must + V3 без have не даёт прошлого вывода: She must left — невозможно.",
                "Didn't need to не автоматически значит «сделали зря»; для «зря сделали» надёжнее needn't have.",
            ],
            remember="Modal + have + V3 смотрит в прошлое. Сначала решите: вывод, упрёк или лишняя работа — затем выберите модальный.",
        ),
        [
            mc("The gate is locked, so they ___ left already.", ["must have", "must", "should"], "must have", "Прошлый вывод требует have + V3."),
            fill("He ___ have seen the email; he never ignores legal notices. (can't)", "can't", "Поведение исключает версию «видел»."),
            xf("Упрёк: You didn't save a backup.", "You should have saved a backup.", "Should have + V3."),
            err("She must forgot the code.", "She must have forgotten the code.", "Нужен перфектный инфинитив have forgotten."),
            fill("You ___ have bought water; the hotel provides it. (need)", "needn't", "Действие совершено зря."),
            mc("We ___ book a taxi — a colleague offered a lift, so we walked to her car.", ["needn't have", "didn't need to", "mustn't have"], "didn't need to", "Необходимости не было, такси не заказывали."),
        ],
        [
            fill("They ___ have taken the coastal road; they arrived salt-stained. (must)", "must", "Следы соли — сильный довод."),
            mc("I baked three cakes, but only six people came. I ___ baked so many.", ["didn't need to", "needn't have", "mustn't have"], "needn't have", "Выпечка уже сделана и оказалась лишней."),
            xf("Невозможность: She didn't write this — the tone is wrong.", "She can't have written this.", "Can't have + V3."),
            err("You should have to warn me yesterday.", "You should have warned me yesterday.", "Should have + V3, без to."),
            fill("We ___ have caught the earlier ferry, but we lingered over coffee. (could)", "could", "Неиспользованная возможность."),
            mc("The lab was empty at eight, so the team ___ finished early.", ["must have", "must", "should"], "must have", "Пустая лаборатория объясняет ранний уход."),
        ],
    ),
    module(
        "passive-perfect-infinitive",
        "Пассив и перфектный инфинитив",
        "To be done, to have done, to have been done и конструкции He is said to…",
        23,
        "Когда действие уже совершено, а форма — инфинитив",
        lesson(
            "Инфинитив тоже различает залог и «уже / ещё нет». To do — актив, процесс впереди относительно точки отсчёта. To be done — пассив. To have done / to have been done сдвигают действие в более ранний момент. Эти формы особенно частотны после be said / thought / believed / reported и после прилагательных вроде lucky, sorry, likely.",
            [
                rule(
                    "Простой и перфектный инфинитив",
                    "She hopes to finish (ещё нет). She hopes to have finished by Friday (к пятнице процесс уже будет позади). Перфектный инфинитив относит событие раньше контрольной точки.",
                    [
                        ex("I was sorry to have missed your opening remarks.", "Мне было жаль, что я пропустил ваши вступительные слова."),
                        ex("They expect to have cleared the backlog by Monday.", "Они рассчитывают к понедельнику уже закрыть отставание."),
                    ],
                ),
                rule(
                    "Пассивный инфинитив",
                    "To be + V3: задача ещё в будущем относительно точки. To have been + V3: пассив уже состоялся раньше. После want, need, deserve, wait часто именно пассив, если подлежащее — объект действия.",
                    [
                        ex("The mural needs to be restored before winter.", "Фреску нужно отреставрировать до зимы."),
                        ex("The files appear to have been copied overnight.", "Похоже, файлы скопировали за ночь."),
                    ],
                ),
                rule(
                    "Личный пассив с инфинитивом",
                    "It is said that she resigned → She is said to have resigned. Если действие одновременное: She is said to live in Ghent. Перфектный инфинитив обязателен, когда репортируемое уже в прошлом.",
                    [
                        ex("He is rumoured to have declined the knighthood.", "Ходят слухи, что он отказался от рыцарского звания."),
                        ex("The start-up is believed to be seeking a second round.", "Считается, что стартап ищет второй раунд."),
                    ],
                ),
            ],
            compare=[
                {"left": "She is said to work in Lisbon.", "right": "She is said to have worked in Lisbon.", "note": "Работает сейчас / работала раньше — решает перфектный инфинитив."},
                {"left": "The essay has to be rewritten.", "right": "The essay seems to have been rewritten already.", "note": "Слева необходимость впереди; справа вывод о уже сделанном."},
            ],
            watch_out=[
                "После is said не ставьте that сразу к человеку: She is said that… — ошибка.",
                "Не путайте have to be done (необходимость) и to have been done (перфектный пассивный инфинитив).",
            ],
            remember="Точка отсчёта — глагол слева. Если событие раньше неё, берите have. Если подлежащее терпит действие — пассивный инфинитив.",
        ),
        [
            mc("The minister is said ___ the inquiry last week.", ["to resign", "to have resigned", "to be resigned"], "to have resigned", "Отставка уже в прошлом относительно is said."),
            fill("These samples need ___ frozen within an hour. (be)", "to be", "Пассивный инфинитив: need to be + V3."),
            xf("Сверните: It is believed that they have left the city.", "They are believed to have left the city.", "Личный пассив + перфектный инфинитив."),
            err("She was lucky to be surviving the storm.", "She was lucky to have survived the storm.", "Выживание уже позади — перфектный инфинитив."),
            fill("The contract appears ___ been signed twice. (have)", "to have", "to have been signed."),
            mc("I'm glad ___ invited before the list closed.", ["to be", "to have been", "being"], "to have been", "Приглашение предшествует Glad."),
        ],
        [
            fill("He is thought ___ negotiating with two publishers. (be)", "to be", "Одновременный процесс — простой инфинитив."),
            mc("The windows ought ___ before the storm.", ["to have boarded", "to be boarded", "board"], "to be boarded", "Ещё не сделано, объект — окна."),
            xf("Сверните: People say she won a fellowship.", "She is said to have won a fellowship.", "Is said + to have + V3."),
            err("The letter seems to be stolen yesterday.", "The letter seems to have been stolen yesterday.", "Yesterday требует перфектного пассива."),
            fill("We were sorry ___ caused a delay. (have)", "to have", "Sorry + перфектный инфинитив."),
            mc("The data is reported ___ independently verified.", ["to have been", "to have", "being"], "to have been", "Пассив уже совершён."),
        ],
    ),
    module(
        "causative-have-get",
        "Каузатив have / get",
        "Have something done, get something done, have someone do и нежелательный опыт.",
        22,
        "Кто действует, а кто организует",
        lesson(
            "Каузатив нужен, когда подлежащее не выполняет работу руками, а устраивает её. Have something done звучит нейтрально-планирующе; get something done — энергичнее и разговорнее, иногда с оттенком «удалось добиться». Have someone do (брит.) и get someone to do включают исполнителя-человека. Отдельный смысл — неприятность: I had my bag stolen.",
            [
                rule(
                    "Have / get + объект + V3",
                    "Подлежащее организует услугу. Время несёт have/get: I'm having the lock changed; we got the roof patched last May. Артикль и определение при объекте обычны: have the brakes checked.",
                    [
                        ex("We're having the cellar damp-proofed this month.", "В этом месяце нам гидроизолируют подвал."),
                        ex("She finally got the subtitle file aligned with the picture.", "Она наконец добилась, чтобы субтитры совпали с картинкой."),
                    ],
                ),
                rule(
                    "Исполнитель-человек",
                    "Have + person + bare infinitive: I'll have the intern compile the citations. Get + person + to-infinitive: Can you get Mara to proof the French? Get чуть более «уговорить / добиться».",
                    [
                        ex("I'll have security escort you to the side door.", "Я попрошу охрану проводить вас к боковой двери."),
                        ex("We got the curator to open the archive for an hour.", "Мы добились, чтобы куратор открыл архив на час."),
                    ],
                ),
                rule(
                    "Нежелательный опыт и make",
                    "Have + объект + V3 может значить «со мной это случилось»: He had his visa revoked. Make + person + bare infinitive — принуждение, не услуга: The editor made us cut the anecdote.",
                    [
                        ex("They had their heating cut off during the works.", "Им отключили отопление на время работ."),
                        ex("The storm made the ferry cancel the evening crossing.", "Шторм заставил паром отменить вечерний рейс."),
                    ],
                ),
            ],
            compare=[
                {"left": "I painted the kitchen.", "right": "I had the kitchen painted.", "note": "Сам кистью / нанял мастеров."},
                {"left": "I'll have Sam check the links.", "right": "I'll get Sam to check the links.", "note": "Одинаковый смысл; get требует to."},
            ],
            watch_out=[
                "I have done my hair cut — ошибка; нужно I have my hair cut или I had my hair cut.",
                "Get someone do без to — ошибка; to обязательно.",
            ],
            remember="Объект + V3 = работу сделали с вещью. Человек + инфинитив = человек действует. Have нейтральнее, get настойчивее.",
        ),
        [
            mc("I ___ my passport renewed before the trip.", ["had", "have made", "got to"], "had", "Have + объект + V3."),
            fill("Can you get the technician ___ the sensor? (recalibrate)", "to recalibrate", "Get + person + to-infinitive."),
            xf("Перепишите: A tailor shortened my coat.", "I had my coat shortened.", "Каузатив have + объект + V3.", ["I got my coat shortened"]),
            err("We got the plumber fix the leak.", "We got the plumber to fix the leak.", "После get person нужен to."),
            fill("They ___ their windows smashed in the hailstorm. (have / past)", "had", "Нежелательный опыт: had + объект + V3."),
            mc("I'll ___ the intern photocopy the signatures.", ["get", "have", "make to"], "have", "Have + person + bare infinitive."),
        ],
        [
            fill("She is ___ her portrait painted by a local artist. (have)", "having", "Процесс: is having + объект + V3."),
            mc("We ___ the neighbours to move their skip.", ["had", "got", "made"], "got", "Get + person + to."),
            xf("Принуждение: The coach insisted we rerun the scene. → The coach ___ us rerun the scene.", "The coach made us rerun the scene.", "Make + person + bare infinitive."),
            err("I have cutting my keys yesterday.", "I had my keys cut yesterday.", "Have + объект + V3 в нужном времени."),
            fill("Did you get the essay ___ before midnight? (proofread)", "proofread", "Get + объект + V3."),
            mc("He ___ his application rejected on a technicality.", ["had", "made", "did"], "had", "Нежелательный опыт: had + объект + V3.")
        ],
    ),
    module(
        "participle-clauses",
        "Причастные обороты",
        "Doing, done, having done и опасность «висячего» причастия.",
        26,
        "Сжать придаточное до причастия",
        lesson(
            "Причастный оборот упаковывает время, причину, условие или сопутствующее действие без полного придаточного. Present participle (V-ing) обычно одновременно или причинно связано с главным глаголом. Past participle (V3) даёт пассив. Perfect participle (having + V3) подчёркивает предшествование. Подлежащее оборота должно совпадать с подлежащим главного предложения — иначе получается dangling participle.",
            [
                rule(
                    "V-ing: одновременность, причина, фон",
                    "Walking along the quay, we compared notes. Feeling unprepared, she asked for a delay. Обороты часто стоят в начале и отделяются запятой.",
                    [
                        ex("Sorting the slides, he noticed two versions of the same chart.", "Разбирая слайды, он заметил две версии одного графика."),
                        ex("Not wanting to interrupt, we waited in the corridor.", "Не желая перебивать, мы подождали в коридоре."),
                    ],
                ),
                rule(
                    "V3 и being + V3: пассив",
                    "Built in 1891, the viaduct still carries freight. Being delayed at security, we missed the slot. Having been + V3 — пассив уже до главного действия.",
                    [
                        ex("Printed on cheap stock, the map tore at the folds.", "Напечатанная на дешёвой бумаге, карта порвалась на сгибах."),
                        ex("Having been warned twice, the crew sealed the hatch.", "Будучи дважды предупреждённой, команда задраила люк."),
                    ],
                ),
                rule(
                    "Having + V3 и согласование подлежащих",
                    "Having + V3 ясно говорит «сначала это, потом главное». Если деятели разные, причастие нельзя оставлять без своего подлежащего: If the weather permits…, а не Permitting, we will sail, если permitting относится к погоде.",
                    [
                        ex("Having filed the return, we shut the laptop and walked out.", "Подав декларацию, мы закрыли ноутбук и вышли."),
                        ex("The weather permitting, the drone will map the ridge at dawn.", "Если погода позволит, дрон на рассвете снимет хребет."),
                    ],
                ),
            ],
            compare=[
                {"left": "After she had checked the bolts, she started the engine.", "right": "Having checked the bolts, she started the engine.", "note": "Тот же порядок событий, короче и формальнее."},
                {"left": "Walking into the hall, I dropped my badge.", "right": "Walking into the hall, my badge fell.", "note": "Справа висячее причастие: ходит как будто бейдж."},
            ],
            watch_out=[
                "Подлежащее причастия = подлежащее главной части, если нет абсолютной конструкции (The weather permitting).",
                "Being tired he left без запятой в начале часто читается тяжело; в письменной речи запятая помогает.",
            ],
            remember="V-ing — фон или причина. V3 — пассив. Having + V3 — «сначала». Проверьте, кто реально действует.",
        ),
        [
            mc("___ the appendix, she spotted a duplicated footnote.", ["Read", "Reading", "Having been read"], "Reading", "Одновременный фон — V-ing."),
            fill("___ lost the brief, we asked for a reprint. (have)", "Having", "Having + V3: сначала потеря, потом просьба."),
            xf("Сожмите: Because he was delayed at customs, he missed the panel.", "Delayed at customs, he missed the panel.", "Пассивное причастие в начале.", ["Being delayed at customs, he missed the panel"]),
            err("Walking down the lane, the church came into view.", "Walking down the lane, we saw the church come into view.", "Иначе получается, что идёт церковь.", ["As we walked down the lane, the church came into view"]),
            fill("___ in haste, the notice omitted the venue. (write)", "Written", "Пассив: notice написали."),
            mc("___ the samples, they left the lab.", ["Having labelled", "Labelling having", "Labelled having"], "Having labelled", "Сначала маркировка, потом уход."),
        ],
        [
            fill("___ wanting a scene, she answered in a whisper. (not)", "Not", "Отрицание перед V-ing."),
            mc("___ repaired twice, the hinge still sagged.", ["Having been", "Having", "Being have"], "Having been", "Пассив предшествует главному глаголу."),
            xf("Сожмите: When I opened the crate, I found rust.", "Opening the crate, I found rust.", "V-ing оборота."),
            err("Having ate, we stacked the trays.", "Having eaten, we stacked the trays.", "Having + V3: eaten."),
            fill("The fog ___, the ferry stayed in harbour. (lift / not; absolute)", "not lifting", "Абсолютная конструкция: свой субъект the fog."),
            mc("___ by lightning, the oak split along the trunk.", ["Striking", "Struck", "Having striking"], "Struck", "Дерево претерпело удар — V3."),
        ],
    ),
    module(
        "inversion-intro",
        "Инверсия: первые конструкции",
        "Never, not only, hardly, only then — когда отрицание выталкивает вспомогательный глагол вперёд.",
        23,
        "Отрицание в начале меняет порядок",
        lesson(
            "Ограничительные и отрицательные наречия в начале предложения вызывают инверсию: вспомогательный глагол встаёт перед подлежащим, как в вопросе, но это утверждение. На B2 достаточно освоить частотный набор: never, rarely, seldom, not only… but also, hardly / scarcely / barely… when, no sooner… than, only then / only after. Полный список и условная инверсия ждут уровня C1.",
            [
                rule(
                    "Never, rarely, seldom, under no circumstances",
                    "Never have I… Rarely does the tide… Если нет вспомогательного, подставляется do/does/did. Смысл усиливается: факт подаётся как исключительный.",
                    [
                        ex("Never had the archive felt so empty after a launch night.", "Никогда архив не казался таким пустым после ночи открытия."),
                        ex("Seldom do we release a build without a dry run.", "Редко мы выпускаем сборку без прогона."),
                    ],
                ),
                rule(
                    "Not only… but also и only + обстоятельство",
                    "Not only did she redesign the form, she also rewrote the guidance. Only then / only after + clause требуют инверсии в главной части: Only after the audit did we notice the gap.",
                    [
                        ex("Not only was the path flooded, but the bridge had shifted.", "Мало того что тропа была затоплена — ещё и мост сдвинулся."),
                        ex("Only then did the sensors start logging again.", "Только тогда датчики снова начали писать лог."),
                    ],
                ),
                rule(
                    "Hardly / scarcely / no sooner",
                    "Hardly had we sat down when the fire alarm sounded. No sooner had the credits rolled than the debate started. When и than не путают: hardly… when, no sooner… than.",
                    [
                        ex("Scarcely had the ink dried when legal asked for a revision.", "Едва чернила высохли, как юристы попросили правку."),
                        ex("No sooner had she muted the call than someone knocked.", "Не успела она выключить звук, как кто-то постучал."),
                    ],
                ),
            ],
            compare=[
                {"left": "I have never seen the vault so tidy.", "right": "Never have I seen the vault so tidy.", "note": "Тот же факт; справа эмфаза и формальный тон."},
                {"left": "Hardly had we begun when the lights failed.", "right": "No sooner had we begun than the lights failed.", "note": "Пара when / than закреплена за конкретным наречием."},
            ],
            watch_out=[
                "Инверсия только если отрицательное слово стоит в начале всей клаузы, не в середине.",
                "No sooner… when — типичная ошибка; нужно than.",
            ],
            remember="Отрицание впереди → вспомогательный + подлежащее + остальное. Hardly… when. No sooner… than.",
        ),
        [
            mc("Never ___ I heard the choir from that stairwell.", ["I have", "have", "did I have"], "have", "Never + have + подлежащее."),
            fill("Not only ___ the roof leak, the cellar flooded. (do / past)", "did", "Did + подлежащее + глагол."),
            xf("Инверсия: I have seldom tasted better bread.", "Seldom have I tasted better bread.", "Seldom + have + I."),
            err("No sooner had we arrived when the guide left.", "No sooner had we arrived than the guide left.", "No sooner сочетается с than."),
            fill("Only after sunset ___ the bats appear. (do)", "did", "Only after + обстоятельство → инверсия в главной."),
            mc("Hardly had the meeting started ___ the projector died.", ["than", "when", "that"], "when", "Hardly… when."),
        ],
        [
            fill("Rarely ___ the river freeze this far south. (do)", "does", "Does + подлежащее the river."),
            mc("Only then ___ we understand the missing page.", ["we did", "did", "have we did"], "did", "Only then + did + we."),
            xf("Инверсия: She not only cut the scene, she recast the lead.", "Not only did she cut the scene, she recast the lead.", "Not only + did + she."),
            err("Never I have agreed to such a clause.", "Never have I agreed to such a clause.", "Have встаёт перед I."),
            fill("Scarcely had he sat down ___ his phone buzzed. (when)", "when", "Scarcely… when."),
            mc("Under no circumstances ___ the originals leave the building.", ["the originals must", "must", "must not"], "must", "On/under no circumstances + must + подлежащее. Отрицание уже в under no circumstances.")
        ],
    ),
    module(
        "cleft-sentences",
        "Расщеплённые предложения",
        "It-cleft, wh-cleft и all-cleft: как вытащить фокус из нейтральной фразы.",
        21,
        "Разделить предложение, чтобы подсветить кусок",
        lesson(
            "Cleft (от to cleave — расщепить) перестраивает простое предложение так, чтобы одна единица стала ремой — новой или контрастной информацией. It-cleft: It was the intern who spotted the mismatch. Wh-cleft (псевдоклефт): What we need is a quieter room. All-cleft сужает до единственного желаемого: All I asked for was a receipt. На B2 это инструмент устной эмфазы и аккуратного письменного контраста.",
            [
                rule(
                    "It-cleft: It is / was + фокус + that / who",
                    "Фокус — существительное, предложная группа, иногда обстоятельство. Who для людей в относительно разговорном регистре; that универсален. Время it-согласуется с исходным событием: It was last May that…",
                    [
                        ex("It was the footnotes that delayed the proofs.", "Именно сноски задержали вёрстку."),
                        ex("It is on Thursdays that the ferry skips this pier.", "Именно по четвергам паром не заходит к этому причалу."),
                    ],
                ),
                rule(
                    "Wh-cleft: What / Why / Where + клауза + be + фокус",
                    "What they ignored was the humidity. What I want is for you to wait. После what часто стоит номинализованное действие. Согласование be: What we need is… (фокус в единственном числе).",
                    [
                        ex("What irritated her was the casual tone of the refusal.", "Что её раздражало — это небрежный тон отказа."),
                        ex("Why the beam failed was a missing washer, not the steel grade.", "Почему балка не выдержала — отсутствующая шайба, а не марка стали."),
                    ],
                ),
                rule(
                    "All-cleft и it + because",
                    "All I want is ten quiet minutes. All they did was forward the complaint. It-cleft с because подчёркивает причину: It was because the tide turned that we aborted.",
                    [
                        ex("All we requested was access to the raw tables.", "Всё, что мы просили, — доступ к сырым таблицам."),
                        ex("It was because the ink ran that the stamp was rejected.", "Именно из-за поплывших чернил штамп не приняли."),
                    ],
                ),
            ],
            compare=[
                {"left": "Mara found the error.", "right": "It was Mara who found the error.", "note": "Справа контраст: не Павел, а Мара."},
                {"left": "We need patience.", "right": "What we need is patience.", "note": "Wh-cleft готовит слушателя к существительному-фокусу."},
            ],
            watch_out=[
                "What we need are — часто спорят; стандарт учебной нормы: What we need is + даже если дальше список, фокус мыслится как идея.",
                "Не копируйте два фокуса сразу: It was yesterday that it was Mara who… перегружает схему.",
            ],
            remember="It-cleft ставит фокус после it is/was. Wh-cleft начинает с what и кладёт фокус после be. All сужает до единственного требования.",
        ),
        [
            mc("___ the tide chart that saved the crossing.", ["It is", "It was", "What was"], "It was", "Прошлое событие — it was."),
            fill("What the board rejected ___ the timeline, not the budget. (be)", "was", "Wh-cleft: what-клауза + was + фокус."),
            xf("It-cleft, фокус — место: We signed the papers in the kitchen.", "It was in the kitchen that we signed the papers.", "It was + обстоятельство + that."),
            err("It was the intern which noticed the mismatch.", "It was the intern who noticed the mismatch.", "Для человека естественнее who.", ["It was the intern that noticed the mismatch"]),
            fill("All I asked for ___ a dated stamp. (be)", "was", "All-cleft + was."),
            mc("___ delayed us was the unscheduled inspection.", ["It", "What", "All that it"], "What", "Wh-cleft открывается What."),
        ],
        [
            fill("It ___ because the cable frayed that the lights flickered. (be / past)", "was", "It-cleft причины."),
            mc("All they did ___ forward the complaint.", ["was", "were", "have"], "was", "All they did was + bare infinitive."),
            xf("Wh-cleft: The humidity damaged the prints.", "What damaged the prints was the humidity.", "What + глагол + be + фокус."),
            err("It is last Monday that we froze the branch.", "It was last Monday that we froze the branch.", "Прошлое требует was."),
            fill("It was Lena ___ rewrote the abstract.", "who", "Фокус-человек.", ["that"]),
            mc("What we lack ___ a second pair of eyes.", ["are", "is", "be"], "is", "Учебная норма: is + идея/вещь."),
        ],
    ),
    module(
        "narrative-tenses",
        "Повествовательные времена",
        "Past Simple, Continuous, Perfect, Perfect Continuous и привычки used to / would.",
        27,
        "Слои прошлого в рассказе",
        lesson(
            "Хороший рассказ на английском держит несколько слоёв: скелет событий (Past Simple), фон и незаконченный процесс (Past Continuous), «ещё раньше» (Past Perfect), длительность до точки (Past Perfect Continuous). Used to рисует прекратившуюся привычку или состояние; would — только повторяющиеся действия в прошлом, не состояния вроде live / know.",
            [
                rule(
                    "Скелет и фон: Simple vs Continuous",
                    "Simple двигает сюжет: She opened the hatch. Continuous держит декорации или прерванный процесс: Rain was hammering the roof when the radio crackled. Два Continuous — параллельный фон.",
                    [
                        ex("I was lining up the shot when a cyclist cut across the frame.", "Я выстраивал кадр, когда велосипедист пересёк кадр."),
                        ex("While the choir was rehearsing, the electrician tested the spots.", "Пока хор репетировал, электрик проверял софиты."),
                    ],
                ),
                rule(
                    "Предпрошедшее: Perfect и Perfect Continuous",
                    "Past Perfect ставит событие левее основной линии: By the time we docked, the market had closed. Past Perfect Continuous подчёркивает длительность: She had been editing for six hours when the file corrupted.",
                    [
                        ex("He realised he had packed the wrong lens.", "Он понял, что упаковал не тот объектив."),
                        ex("They had been arguing about the caption since breakfast.", "Они спорили о подписи с самого завтрака."),
                    ],
                ),
                rule(
                    "Used to и would",
                    "Used to + инфинитив — привычка или состояние, которого больше нет: She used to live above the bakery. Would + инфинитив — повторяющиеся сцены в уже заданном прошлом: Every August we would hire a dinghy. Would не ставят с be, have (владение), know в значении состояния.",
                    [
                        ex("I used to keep the negatives in a biscuit tin.", "Раньше я хранил негативы в банке из-под печенья."),
                        ex("After dinner he would walk the harbour wall and count the masts.", "После ужина он имел обыкновение идти по стенке гавани и считать мачты."),
                    ],
                ),
            ],
            compare=[
                {"left": "When I arrived, she left.", "right": "When I arrived, she had left.", "note": "Слева последовательность спорная; справа она уже ушла к моменту прихода."},
                {"left": "He used to own a barge.", "right": "He would own a barge.", "note": "Would с владением звучит неверно; для состояния — used to."},
            ],
            watch_out=[
                "Не ставьте Past Perfect на каждое прошлое действие — только на «раньше основной точки».",
                "Would не заменяет used to в I would be a teacher when I was ten.",
            ],
            remember="Simple двигает сюжет, Continuous рисует фон, Perfect отодвигает в ещё более раннее. Used to — привычка и состояние; would — только повтор действий.",
        ),
        [
            mc("I ___ the proofs when the client rang.", ["checked", "was checking", "had been check"], "was checking", "Прерванный процесс — Past Continuous."),
            fill("By dusk the tide ___ covered the steps. (have)", "had", "К моменту dusk действие уже завершено."),
            xf("Длительность до поломки: She edited from noon; at six the file died.", "She had been editing since noon when the file died at six.", "Past Perfect Continuous + when + Past Simple."),
            err("Every summer we used to would rent the same cabin.", "Every summer we would rent the same cabin.", "Один маркер привычки, не два.", ["Every summer we used to rent the same cabin"]),
            fill("He ___ to distrust automatic backups. (used)", "used", "Used to + инфинитив."),
            mc("When we opened the crate, the fruit ___ already.", ["ripened", "had ripened", "was ripen"], "had ripened", "Созревание раньше открытия."),
        ],
        [
            fill("While I ___ labels, she sealed the jars. (write)", "was writing", "Параллельный фон."),
            mc("She ___ the keys and walked out — сюжетный шаг.", ["was finding", "found", "had been found"], "found", "Скелет рассказа — Past Simple."),
            xf("Состояние в прошлом, которого нет: He lived by the canal then.", "He used to live by the canal.", "Used to + live."),
            err("I would know the harbour master quite well in those days.", "I used to know the harbour master quite well in those days.", "Know как состояние — used to, не would."),
            fill("They ___ waiting forty minutes when the shuttle arrived. (be)", "had been", "Past Perfect Continuous."),
            mc("The lights failed while we ___ the final chorus.", ["rehearsed", "were rehearsing", "had rehearsed"], "were rehearsing", "Фон в момент сбоя."),
        ],
    ),
    module(
        "unreal-past",
        "Нереальное прошедшее",
        "It's time, I'd rather, suppose / what if, as if / as though — форма прошлого без прошлого смысла.",
        20,
        "Прошедшее, которое не про время",
        lesson(
            "Ряд конструкций берёт Past Simple или Past Perfect не потому что событие было вчера, а потому что оно гипотетично, желательно или контрфактично. Это тот же «сдвиг для нереальности», что в wish и втором/третьем условном. It's time + Past подталкивает к действию. I'd rather + Past описывает предпочтение относительно другого человека. As if / as though выбирают Simple или Perfect в зависимости от того, насколько ситуация ложна относительно точки речи.",
            [
                rule(
                    "It's time / it's high time + Past Simple",
                    "Пора уже сделать то, что запаздывает. It's time we left, It's high time the board appointed a chair. To-infinitive тоже возможен (It's time to leave), но без упрёка «давно пора».",
                    [
                        ex("It's time we archived the beta branch.", "Пора уже заархивировать бета-ветку."),
                        ex("It's high time the captions matched the picture.", "Давно пора, чтобы титры совпадали с картинкой."),
                    ],
                ),
                rule(
                    "I'd rather / I'd sooner и suppose / what if",
                    "I'd rather you didn't record this. О себе чаще I'd rather + bare infinitive: I'd rather walk. Suppose / supposing / what if + Past — гипотеза: Suppose we missed the last tram?",
                    [
                        ex("I'd rather the reviewers saw the uncut interview.", "Я бы предпочёл, чтобы рецензенты увидели немонтированное интервью."),
                        ex("Suppose the tide turned an hour earlier — where would we beach?", "Предположим, прилив сменился на час раньше — где бы мы выбросились на берег?"),
                    ],
                ),
                rule(
                    "As if / as though",
                    "Как если бы. Если сравнение явно ложно сейчас: He talks as if he owned the quay (а не владеет). Если ложная предпосылка в прошлом: She looked as if she had seen the uncut footage. Were естественен: as if I were…",
                    [
                        ex("He issued orders as though he were still skipper.", "Он отдавал приказания, словно всё ещё был шкипером."),
                        ex("The lobby smelled as if someone had spilled turpentine.", "В вестибюле пахло так, будто кто-то разлил скипидар."),
                    ],
                ),
            ],
            compare=[
                {"left": "It's time to go.", "right": "It's time we went.", "note": "Инфинитив нейтрален; Past добавляет «хватит тянуть»."},
                {"left": "I'd rather stay.", "right": "I'd rather you stayed.", "note": "Своё действие — инфинитив; чужое — Past."},
            ],
            watch_out=[
                "It's time we go — разговорный сбой; в аккуратной речи It's time we went.",
                "I'd rather you to stay — ошибка; либо I'd rather you stayed, либо I'd rather stay.",
            ],
            remember="Past здесь — сигнал нереальности или мягкого давления, а не календарь. Смотрите, чьё действие и насколько оно ложно.",
        ),
        [
            mc("It's high time the committee ___ a date.", ["sets", "set", "had set"], "set", "It's high time + Past Simple."),
            fill("I'd rather you ___ the draft to the whole list. (not / send)", "didn't send", "Чужое действие после I'd rather — Past."),
            xf("Пора уже: We should update the signage.", "It's time we updated the signage.", "It's time + Past."),
            err("Suppose we miss the last boat yesterday — what then?", "Suppose we had missed the last boat yesterday — what then?", "Вчерашняя контрфактуальность — Past Perfect."),
            fill("She stared as if she ___ a ghost. (see)", "had seen", "Ложное прошлое впечатление — Past Perfect."),
            mc("I'd rather ___ the coastal path.", ["to take", "take", "took"], "take", "Своё предпочтение — bare infinitive."),
        ],
        [
            fill("It's time you ___ the permissions. (check)", "checked", "It's time + Past Simple."),
            mc("He spends as if he ___ unlimited credit.", ["has", "had", "would have"], "had", "Заведомо ложное настоящее — Past."),
            xf("Предпочтение о другом: Don't publish the stills.", "I'd rather you didn't publish the stills.", "I'd rather + Past negative."),
            err("It's time we to renegotiate the lease.", "It's time we renegotiated the lease.", "Past, не to-infinitive после we."),
            fill("What if the server ___ overnight? (fail / unreal past)", "failed", "Гипотеза: what if + Past."),
            mc("They behaved as though nothing ___.", ["happens", "had happened", "has happen"], "had happened", "Предшествующее «как будто не случилось» — Past Perfect."),
        ],
    ),
    module(
        "relative-advanced",
        "Относительные предложения: уровень B2",
        "Defining и non-defining, предлог + which, whose, сокращённые обороты.",
        24,
        "Какой объект, и нужна ли запятая",
        lesson(
            "Относительное придаточное либо сужает класс (defining: без запятых, that допустим), либо добавляет комментарий к уже известному (non-defining: запятые, that нельзя). На B2 к who / which / that добавляются whose, where / when / why, конструкции предлог + which / whom и сокращения до причастия. Whom жив в формальном регистре после предлога.",
            [
                rule(
                    "Defining vs non-defining",
                    "The intern who spotted the error got a mention — без придаточного неясно, какой интерн. Mara, who spotted the error, got a mention — Mara и так идентифицирована, who лишь комментирует. В non-defining that не используют.",
                    [
                        ex("The crate that leaked had been stacked on its side.", "Протекла та клеть, которую поставили на бок."),
                        ex("The old ferry, which still uses a paper log, left at six.", "Старый паром, который всё ещё ведёт бумажный журнал, отошёл в шесть."),
                    ],
                ),
                rule(
                    "Whose, where, предлог + which / whom",
                    "Whose относится и к людям, и к вещам: a building whose roof… Where = in/at which для мест. Формально: the desk at which she writes, the editor with whom I spoke. Разговорно предлог часто уходит в конец: the desk she writes at.",
                    [
                        ex("I need a binder whose rings actually close.", "Мне нужна папка, кольца которой реально смыкаются."),
                        ex("The quay on which we landed had no rail.", "У причала, к которому мы пристали, не было перил."),
                    ],
                ),
                rule(
                    "Сокращённые относительные",
                    "Defining-пассив и continuous часто теряют who/which is: the samples stored in aisle C; people waiting by the lift. Of which / of whom присоединяет количество: three of which failed.",
                    [
                        ex("The stills pinned above the desk are from the first cut.", "Кадры, приколотые над столом, — из первой сборки."),
                        ex("She listed six objections, two of which were new.", "Она перечислила шесть возражений, два из которых были новыми."),
                    ],
                ),
            ],
            compare=[
                {"left": "My brother who lives in Cork is a fiddle player.", "right": "My brother, who lives in Cork, is a fiddle player.", "note": "Слева подразумевается, что братьев несколько; справа брат один, Cork — ремарка."},
                {"left": "the shelf I put the tins on", "right": "the shelf on which I put the tins", "note": "Одинаковый смысл; справа формальнее."},
            ],
            watch_out=[
                "Запятая + that в non-defining — ошибка.",
                "Which после предлога не заменяется that: the room in that we met — невозможно.",
            ],
            remember="Нет запятых — придаточное опознаёт объект; that можно. Есть запятые — комментарий; that нельзя. Предлог + which/whom в формальном стиле.",
        ),
        [
            mc("The only ferry ___ stops here leaves at dawn.", ["that", "what", ", that"], "that", "Defining, без запятой."),
            fill("This is the editor with ___ I argued about the title. (whom)", "whom", "Предлог + whom."),
            xf("Сократите: the boxes that were stacked near the door", "the boxes stacked near the door", "Пассив без which were."),
            err("Paris, that we visited in March, was cold.", "Paris, which we visited in March, was cold.", "Non-defining не берёт that."),
            fill("A camera ___ battery dies in the cold is useless here. (whose)", "whose", "Whose + существительное."),
            mc("She offered four dates, none ___ suited the choir.", ["that", "of which", "which of"], "of which", "None of which."),
        ],
        [
            fill("The loft ___ we store the negatives is dry. (where)", "where", "Where = in which."),
            mc("Dr Chen, ___ paper you cited, is speaking on Friday.", ["that", "whose", "who's"], "whose", "Whose paper."),
            xf("Формально: the stool she perched on → the stool ___ she perched.", "the stool on which she perched", "Предлог + which."),
            err("The intern, that spotted the mismatch, was praised.", "The intern, who spotted the mismatch, was praised.", "После запятой who/which, не that."),
            fill("Anyone ___ waiting by lift B should take the stairs. (be / reduced)", "waiting", "Сокращение who is waiting."),
            mc("The harbour ___ we sheltered was unmarked on the tourist map.", ["in that", "in which", "which in"], "in which", "Предлог + which."),
        ],
    ),
]
