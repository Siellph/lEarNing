"""Enriched B2 grammar theory (Russian explanations, English examples).

Tone: impersonal / descriptive Russian. No direct address to the learner.
Examples keep {en, ru}. Body may use **…** for emphasis; rules may include
tables / callouts / wrong–right pairs for LessonView.
"""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

B2_THEORY = {
    "mixed-conditionals": lesson(
        "Классические второй и третий типы условных предложений обычно помещают условие и его следствие в один временной план. **Смешанные условные предложения (mixed conditionals)** необходимы тогда, когда эти два компонента относятся к разным моментам времени. Поэтому смешанный conditional следует понимать не как отдельный «четвёртый тип», а как комбинацию грамматических моделей, выбранных в соответствии с временной перспективой каждого компонента.\n\nГлавный принцип — сначала определить, **когда относится условие**, а затем отдельно определить, **когда проявляется следствие**. Прошлое нереальное условие может объяснять нынешнее состояние: If I had taken the job, I would live abroad now. И наоборот, нынешняя характеристика человека может объяснять конкретный результат в прошлом: If he were more careful, he would have noticed the error. В условной части сохраняется форма, соответствующая нереальному условию, а в главной части — форма, соответствующая времени следствия.\n\nВажно отличать временную форму от временного значения. Past Perfect в if-части не означает, что всё предложение обязательно рассказывает о прошлом; он может обозначать условие в прошлом, тогда как результат относится к настоящему. Аналогично Past Simple после if может обозначать не прошедшее время, а нереальную характеристику настоящего. В письменной речи полезно проверять каждую часть отдельно: когда существует условие и когда проявляется его результат.",
        [
            rule(
                "Прошлое условие → нынешний результат",
                "If + **Past Perfect**, would / could / might + **инфинитив**. Условие уже не изменить; следствие описывает текущую роль, привычку или состояние. Маркеры now, today, still, these days тянут правую часть в настоящее.",
                [
                    ex("If I had accepted that transfer, I would live in Osaka now.", "Если бы тогда принял перевод, сейчас жил бы в Осаке."),
                    ex("If she hadn't sprained her ankle, she could be playing in the final tonight.", "Если бы не подвернула лодыжку, сегодня вечером могла бы играть в финале."),
                    ex("If you had packed the adapter, we wouldn't be hunting for a charger now.", "Если бы адаптер положили заранее, сейчас не искали бы зарядку."),
                ],
                tables=[
                    table(
                        ["План", "If-часть", "Главная часть"],
                        [
                            ["прошлое → сейчас", "had + V3", "would / could / might + V1"],
                            ["черта сейчас → прошлое", "Past Simple / were", "would have + V3"],
                        ],
                    ),
                ],
            ),
            rule(
                "Устойчивое условие → прошлый результат",
                "If + **Past Simple** (или were), would have / could have / might have + **V3**. Черта характера, привычка или текущий факт объясняют уже случившееся.",
                [
                    ex("If he were more diplomatic, he wouldn't have emailed the whole board.", "Если бы был дипломатичнее, не разослал бы письмо всему совету."),
                    ex("If I didn't hate heights, I would have taken the glass lift.", "Если бы не боялся высоты, поехал бы на стеклянном лифте."),
                    ex("If she spoke Arabic, she would have taken the Cairo posting last spring.", "Если бы говорила по-арабски, взяла бы каирскую командировку прошлой весной."),
                ],
                pairs=[
                    pair("If I would have known, I would help now.", "If I had known, I would help now.", "В if-части would не ставят — нужен Past Perfect."),
                    pair("If she studied medicine, she would have been a surgeon now.", "If she had studied medicine, she would be a surgeon now.", "Учёба в прошлом, профессия сейчас."),
                ],
            ),
            rule(
                "Когда смесь уместна",
                "Вопрос не «какой тип красивее», а два отдельных: условие уже в прошлом или всё ещё правда? Результат — сейчас или тогда? Если оба конца в одной эпохе, достаточно «чистого» второго или третьего типа.",
                [
                    ex("If I had studied law, I would have become a solicitor.", "Весь сценарий в прошлом — третий тип, не смесь."),
                    ex("If I had studied law, I would be a solicitor now.", "Прошлое решение держит нынешнюю профессию — смесь."),
                ],
                callouts=[
                    callout("Were предпочтителен в гипотезах о настоящем: If I were richer… В аккуратной письменной речи was здесь выглядит слабее.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "If I had studied law, I would have become a solicitor.", "right": "If I had studied law, I would be a solicitor now.", "note": "Слева весь сценарий в прошлом; справа прошлое решение держит нынешнюю роль."},
        ],
        watch_out=[
            "Would в if-части: If I would have known — ошибка.",
            "Смесь только при разных временных планах условия и следствия.",
            "Маркер now / yesterday помогает выбрать правую часть.",
        ],
        remember="Сначала время условия, затем время следствия. Разные эпохи — смесь; одна эпоха — «чистый» тип.",
    ),
    "wish-if-only": lesson(
        "**Wish** и **if only** используются для оценки действительности как неудовлетворительной, желательной или отличной от предполагаемой. Важнейший принцип — грамматический сдвиг назад: форма прошедшего времени здесь часто выражает не прошлое, а **нереальность или дистанцию от факта**. Для настоящего положения дел употребляется Past Simple, для сожаления о прошлом — Past Perfect, а **would** обычно связано с желанием изменить поведение или ход ситуации.\n\nI wish и if only в основном следуют одной и той же грамматической системе. Разница прежде всего стилистическая: **if only** обычно эмоциональнее и сильнее подчёркивает сожаление или желание. В гипотезах с be форма **were** традиционно предпочтительна в формальной и учебной речи: I wish I were more patient.\n\nВажно различать wish и hope. Hope относится к реальной или вполне возможной ситуации: I hope she comes. Wish предполагает, что действительность не соответствует желаемой. Поэтому выбор конструкции определяется не самим фактом будущего времени, а отношением говорящего к реальности ситуации.",
        [
            rule(
                "Настоящее: wish + Past Simple / could",
                "Жалоба на то, что верно сейчас. I wish I knew, I wish I could swim, I wish it weren't raining. Were предпочтителен в формальной речи.",
                [
                    ex("I wish I had a spare charger in this bag.", "Жаль, что в сумке нет запасной зарядки."),
                    ex("If only this office weren't so noisy after lunch.", "Если бы только офис не был таким шумным после обеда."),
                    ex("I wish I could ski, then I'd join you this weekend.", "Жаль, что не умею кататься на лыжах."),
                ],
                tables=[
                    table(
                        ["О чём сожаление", "Форма после wish", "Пример"],
                        [
                            ["факт / состояние сейчас", "Past Simple / were", "I wish I knew"],
                            ["умение сейчас", "could + V1", "I wish I could swim"],
                            ["уже случилось", "Past Perfect", "I wish I had asked"],
                            ["чужое упрямство", "would + V1", "I wish you wouldn't…"],
                        ],
                    ),
                ],
            ),
            rule(
                "Прошлое: wish + Past Perfect",
                "Сожаление о уже случившемся или не случившемся — близкий родственник третьего условного, но без явного if-сценария.",
                [
                    ex("She wishes she had saved the earlier draft.", "Жалеет, что не сохранила более ранний черновик."),
                    ex("If only we had checked the tide timetable.", "Если бы только сверили расписание приливов."),
                    ex("He wishes he had spoken louder during the pitch.", "Жалеет, что говорил недостаточно громко на питче."),
                ],
            ),
            rule(
                "Раздражение: wish + would",
                "Would указывает на чужое повторяющееся поведение или ситуацию, которую другой агент теоретически может изменить. О собственной воле так не говорят: не I wish I would…",
                [
                    ex("I wish you wouldn't leave mugs on the scanner.", "Хотелось бы, чтобы кружки не оставляли на сканере."),
                    ex("If only the neighbours would stop drilling at dawn.", "Если бы только соседи перестали сверлить на рассвете."),
                    ex("I wish it would stop raining.", "Хотелось бы, чтобы дождь прекратился (нетерпеливое ожидание перемены)."),
                ],
                pairs=[
                    pair("I wish I would be taller.", "I wish I were taller.", "О себе в настоящем — Past Simple / were, не would."),
                    pair("I wish you will stop humming.", "I wish you would stop humming.", "Раздражение кодируется would, не will."),
                ],
                callouts=[
                    callout("Wish + would плохо стыкуется с тем, что субъект не может «решить» изменить: рост, возраст. Для погоды форма иногда допустима как жалоба.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "I wish I lived nearer the station.", "right": "I wish I had lived nearer the station last year.", "note": "Нынешний адрес vs адрес в прошлом, который уже не вернуть."},
            {"left": "I wish it would stop raining.", "right": "I wish it weren't raining.", "note": "Would — ожидание перемены; Past Simple — оценка текущего факта."},
        ],
        watch_out=[
            "I wish I would… о себе в настоящем — ошибка.",
            "Прошлый упущенный шанс — Past Perfect, не Past Simple.",
            "If only усиливает тот же сдвиг, а не меняет времена.",
        ],
        remember="Сдвиг назад = нереальность. Про себя сейчас — Past Simple; о прошлом — Past Perfect; о чужом упрямстве — would.",
    ),
    "modals-deduction": lesson(
        "На уровне B2 модальные глаголы активно используются не только для разрешения, способности или обязанности, но и для **эпистемического вывода**, то есть оценки того, насколько вероятно, что некоторое положение дел является истинным. **Must** выражает сильный вывод на основании имеющихся фактов; **can't / couldn't** — вывод о невозможности; **may, might, could** оставляют несколько возможных объяснений. **Should** в таком употреблении означает ожидаемое развитие событий, а не совет.\n\nЭти значения нельзя свести к механической шкале процентов. Разница между may, might и could зависит от контекста, регистра и того, что именно хочет подчеркнуть говорящий. Модальный глагол всегда следует рассматривать вместе с ситуацией: She must be at home может быть логическим выводом, но She must be at home by six — обязанностью или требованием.\n\nДля вывода о процессе используется modal + be + V-ing, а для вывода о завершённом прошлом событии — modal + have + V3. Отрицание **mustn't** обычно не является отрицанием логического must: mustn't выражает запрет, тогда как невозможный вывод передаётся через can't.",
        [
            rule(
                "Высокая уверенность: must и can't",
                "Must = единственное разумное объяснение. Can't (иногда couldn't) = вывод исключает возможность. **Mustn't** для вывода не подходит — это запрет.",
                [
                    ex("Her coat is still on the hook; she must be in the building.", "Пальто на крючке: она, должно быть, в здании."),
                    ex("That rumour can't be true — the minutes contradict it.", "Слух не может быть правдой: протоколу противоречит."),
                    ex("You've been on your feet all day; you must be exhausted.", "Весь день на ногах — наверняка измотан."),
                ],
                tables=[
                    table(
                        ["Уверенность", "Модальный", "Смысл"],
                        [
                            ["почти доказано", "**must**", "единственное объяснение"],
                            ["исключено", "**can't** / couldn't", "факты противоречат"],
                            ["по ожиданиям", "**should**", "нормальный ход вещей"],
                            ["гипотеза", "**may / might / could**", "одна из версий"],
                        ],
                    ),
                ],
                pairs=[
                    pair("He mustn't be the author; the style is different.", "He can't be the author; the style is different.", "Для невозможного вывода — can't, не mustn't."),
                    pair("She can be at the dentist, I'm not sure.", "She could be at the dentist, I'm not sure.", "Can в утверждении почти не даёт слабую вероятность."),
                ],
            ),
            rule(
                "Средняя и низкая вероятность",
                "Should — ожидаемый ход вещей. May / might / could — открытые гипотезы; might чуть осторожнее may, could подчёркивает одну из опций, а не «умение».",
                [
                    ex("The package should be at reception by now.", "Посылка к этому моменту уже должна быть на ресепшене."),
                    ex("He might be stuck in the underpass — the signal dies there.", "Возможно, застрял в подземном переходе — там пропадает связь."),
                    ex("The café might be closed.", "Кафе, возможно, закрыто."),
                ],
            ),
            rule(
                "Отрицание и вопрос о гипотезе",
                "May not / might not = возможно, нет. Couldn't в выводе часто ближе к can't. Вопрос: Could this be the wrong file?",
                [
                    ex("The figures may not be final; finance is still reconciling.", "Цифры могут быть ещё не финальными."),
                    ex("Could that hum be the projector fan?", "Этот гул может быть вентилятором проектора?"),
                ],
                callouts=[
                    callout("Одна и та же форма must be может значить вывод или обязанность: She must be the new editor vs She must be at the meeting. Решает контекст.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "She must be the new editor.", "right": "She must be at the meeting — it's compulsory.", "note": "Слева логический вывод; справа обязанность."},
            {"left": "He can't be serious.", "right": "He mustn't be late.", "note": "Can't — невозможный вывод; mustn't — запрет."},
        ],
        watch_out=[
            "Mustn't ≠ «не может быть, что…».",
            "Can в утверждении почти не выражает «может быть».",
            "Should в выводе — ожидание, не приказ.",
        ],
        remember="Must / can't — почти доказано. Should — по ожиданиям. May / might / could — гипотеза.",
    ),
    "past-modals": lesson(
        "Конструкция **modal + have + V3** переносит модальную оценку в прошлое. Здесь have является частью перфектного инфинитива: оно показывает, что оцениваемое действие относится к более раннему моменту. Must have + V3 выражает сильный вывод о прошлом, can't/couldn't have + V3 — невозможность, may/might/could have + V3 — возможную версию.\n\nОтдельную группу составляют **should have / ought to have + V3**, которые оценивают прошлое с точки зрения нормы, ожидания или правильного поведения. **Could have + V3** часто указывает на существовавшую, но не использованную возможность. Поэтому модальные формы прошлого могут выражать разные отношения к одному событию: вывод, сожаление, упрёк, возможность или отсутствие необходимости.\n\nОсобого внимания требует противопоставление **needn't have + V3** и **didn't need to + V1**. В первом случае действие было совершено, но позднее выяснилось, что оно не требовалось. Во втором сообщается об отсутствии необходимости; сама конструкция не утверждает, что действие действительно произошло.",
        [
            rule(
                "Вывод о прошлом: must / can't / might have",
                "Must have + V3 — единственное правдоподобное объяснение. Can't / couldn't have — прошлое несовместимо с фактами. Might / may / could have — одна из версий.",
                [
                    ex("The streets are dry; it can't have rained overnight.", "Улицы сухие: ночью не могло быть дождя."),
                    ex("He might have left his pass in the taxi.", "Возможно, оставил пропуск в такси."),
                    ex("They must have taken the coastal road; they arrived salt-stained.", "Наверняка ехали по береговой — прибыли в соли."),
                ],
                tables=[
                    table(
                        ["Смысл", "Форма", "Пример"],
                        [
                            ["почти доказано", "must have + V3", "must have left"],
                            ["исключено", "can't have + V3", "can't have seen"],
                            ["упрёк / норма", "should have + V3", "should have warned"],
                            ["сделали зря", "needn't have + V3", "needn't have printed"],
                            ["нужды не было", "didn't need to + V1", "didn't need to book"],
                        ],
                    ),
                ],
            ),
            rule(
                "Оценка: should have, could have",
                "Should have — ожидаемое, но не сделанное, или упрёк. Could have — неиспользованная возможность. Эти формы смотрят назад, а не планируют.",
                [
                    ex("You should have labelled the samples before the audit.", "Образцы следовало подписать до аудита."),
                    ex("We could have taken the river path and avoided the roadworks.", "Можно было пойти вдоль реки и обойти ремонт."),
                ],
                pairs=[
                    pair("She must forgot the code.", "She must have forgotten the code.", "Нужен перфектный инфинитив have + V3."),
                    pair("You should have to warn me yesterday.", "You should have warned me yesterday.", "Should have + V3, без to."),
                ],
            ),
            rule(
                "Needn't have vs didn't need to",
                "Needn't have + V3: действие **совершили**, потом выяснилось, что зря. Didn't need to: обязанности не было; часто действие не делали. Контекст должен это показать.",
                [
                    ex("You needn't have printed fifty copies; the room has a screen.", "Зря печатали пятьдесят копий: в зале есть экран."),
                    ex("We didn't need to print anything — they had already circulated the slides.", "Печатать не нужно было: слайды уже разослали."),
                ],
                callouts=[
                    callout("Didn't need to не автоматически значит «сделали зря». Для «зря сделали» надёжнее needn't have.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "She must have missed the announcement.", "right": "She should have heard the announcement.", "note": "Must have — вывод о факте; should have — нарушенная норма."},
            {"left": "I needn't have packed a coat.", "right": "I didn't need to pack a coat, so I left it.", "note": "Needn't have подразумевает, что пальто всё-таки положили."},
        ],
        watch_out=[
            "Must + V3 без have не даёт прошлого вывода.",
            "Needn't have vs didn't need to — разный факт о том, сделали ли действие.",
        ],
        remember="Modal + have + V3 смотрит в прошлое. Сначала: вывод, упрёк или лишняя работа — затем модальный.",
    ),
    "passive-perfect-infinitive": lesson(
        "Инфинитивная конструкция способна выражать не только залог, но и относительное время. **To do** и **to be done** являются простыми инфинитивами и обычно обозначают действие, одновременное с точкой отсчёта или последующее по отношению к ней; to be done имеет пассивное значение. **To have done** и **to have been done** — перфектные инфинитивы, показывающие, что действие произошло раньше точки отсчёта.\n\nОсобенно часто перфектный инфинитив встречается после глаголов сообщения, предположения и оценки: He is believed to have left. Такая конструкция позволяет компактно передать временную дистанцию. Важно не путать **to have been done** с **to have to be done**: первая конструкция означает уже совершённое действие в пассиве, вторая содержит значение необходимости.\n\nВремя инфинитива является относительным, поэтому его следует сопоставлять с глаголом или другой точкой отсчёта в главном предложении, а не с моментом речи автоматически.",
        [
            rule(
                "Простой и перфектный инфинитив",
                "She hopes to finish — ещё нет. She hopes to have finished by Friday — к пятнице процесс уже позади. Перфектный инфинитив относит событие раньше точки слева.",
                [
                    ex("I was sorry to have missed your opening remarks.", "Жаль, что пропустил вступительные слова."),
                    ex("They expect to have cleared the backlog by Monday.", "Рассчитывают к понедельнику уже закрыть отставание."),
                    ex("She was lucky to have survived the storm.", "Повезло, что пережила шторм."),
                ],
                tables=[
                    table(
                        ["Отношение к точке", "Актив", "Пассив"],
                        [
                            ["одновременно / впереди", "to do", "to be done"],
                            ["раньше точки", "to have done", "to have been done"],
                        ],
                    ),
                ],
            ),
            rule(
                "Пассивный инфинитив",
                "To be + V3: задача ещё в будущем относительно точки. To have been + V3: пассив уже состоялся. После want, need, deserve, wait часто пассив, если подлежащее — объект действия.",
                [
                    ex("The mural needs to be restored before winter.", "Фреску нужно отреставрировать до зимы."),
                    ex("The files appear to have been copied overnight.", "Похоже, файлы скопировали за ночь."),
                    ex("The letter seems to have been stolen yesterday.", "Письмо, похоже, украли вчера."),
                ],
            ),
            rule(
                "Личный пассив с инфинитивом",
                "It is said that she resigned → She is said to have resigned. Одновременность: She is said to live in Ghent. Перфектный инфинитив обязателен, когда репортируемое уже в прошлом.",
                [
                    ex("He is rumoured to have declined the knighthood.", "Ходят слухи, что отказался от рыцарского звания."),
                    ex("The start-up is believed to be seeking a second round.", "Считается, что стартап ищет второй раунд."),
                ],
                pairs=[
                    pair("She is said that she resigned.", "She is said to have resigned.", "После is said — to-infinitive, не that сразу к человеку."),
                    pair("The letter seems to be stolen yesterday.", "The letter seems to have been stolen yesterday.", "Yesterday требует перфектного пассива."),
                ],
                callouts=[
                    callout("Не путать have to be done (необходимость) и to have been done (перфектный пассивный инфинитив).", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "She is said to work in Lisbon.", "right": "She is said to have worked in Lisbon.", "note": "Работает сейчас / работала раньше — решает перфектный инфинитив."},
            {"left": "The essay has to be rewritten.", "right": "The essay seems to have been rewritten already.", "note": "Необходимость впереди vs вывод о уже сделанном."},
        ],
        watch_out=[
            "She is said that… — ошибка.",
            "Точка отсчёта — глагол слева: если событие раньше неё, нужен have.",
        ],
        remember="Раньше точки — have. Подлежащее терпит действие — пассивный инфинитив. Is said + to…",
    ),
    "causative-have-get": lesson(
        "Конструкция **have/get + object + V3** называется каузативной: субъект не обязательно выполняет действие сам, а организует, заказывает или обеспечивает его выполнение другим лицом. I had my car repaired обычно означает, что ремонт был организован субъектом. Время выражается формой have/get, а V3 обозначает действие над объектом.\n\nHave и get близки по значению, однако get чаще имеет более разговорный и динамичный оттенок и может подчёркивать достижение результата. Каузативная модель способна описывать и неприятное, непреднамеренное событие: He had his wallet stolen. Здесь субъект не является инициатором кражи; конструкция сообщает, что с ним произошло событие, затронувшее его имущество.\n\nОтдельно существуют модели **have + person + bare infinitive** и **get + person + to-infinitive**, где назван человек, непосредственно выполняющий действие. После have используется инфинитив без to, после get — to-infinitive. **Make + person + bare infinitive** выражает принуждение и поэтому не является обычным каузативом услуги.",
        [
            rule(
                "Have / get + объект + V3",
                "Подлежащее организует услугу. Время несёт have/get: I'm having the lock changed; we got the roof patched. Артикль при объекте обычен: have the brakes checked.",
                [
                    ex("We're having the cellar damp-proofed this month.", "В этом месяце гидроизолируют подвал."),
                    ex("She finally got the subtitle file aligned with the picture.", "Наконец добилась совпадения субтитров с картинкой."),
                    ex("I had my coat shortened.", "Укоротили пальто (у портного)."),
                ],
                tables=[
                    table(
                        ["Схема", "Форма", "Оттенок"],
                        [
                            ["услуга с вещью", "have / get + NP + V3", "get настойчивее"],
                            ["человек-исполнитель", "have + person + V1", "нейтрально"],
                            ["человек-исполнитель", "get + person + to V1", "уговорить / добиться"],
                            ["нежелательный опыт", "have + NP + V3", "«со мной случилось»"],
                            ["принуждение", "make + person + V1", "не услуга"],
                        ],
                    ),
                ],
            ),
            rule(
                "Исполнитель-человек",
                "Have + person + bare infinitive: I'll have the intern compile the citations. Get + person + to-infinitive: get Mara to proof the French. Get чуть более «добиться».",
                [
                    ex("I'll have security escort you to the side door.", "Охрану попросят проводить к боковой двери."),
                    ex("We got the curator to open the archive for an hour.", "Добились, чтобы куратор открыл архив на час."),
                ],
                pairs=[
                    pair("We got the plumber fix the leak.", "We got the plumber to fix the leak.", "После get + person обязателен to."),
                    pair("I have done my hair cut.", "I had my hair cut.", "Have + объект + V3, не have done + noun + V3."),
                ],
            ),
            rule(
                "Нежелательный опыт и make",
                "Have + объект + V3 может значить «со мной это случилось»: He had his visa revoked. Make + person + bare infinitive — принуждение, не услуга.",
                [
                    ex("They had their heating cut off during the works.", "Им отключили отопление на время работ."),
                    ex("The storm made the ferry cancel the evening crossing.", "Шторм заставил паром отменить вечерний рейс."),
                ],
                callouts=[
                    callout("I painted the kitchen = сам кистью. I had the kitchen painted = наняли мастеров. Контраст деятеля — главный смысл каузатива.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "I painted the kitchen.", "right": "I had the kitchen painted.", "note": "Сам / организовал услугу."},
            {"left": "I'll have Sam check the links.", "right": "I'll get Sam to check the links.", "note": "Одинаковый смысл; get требует to."},
        ],
        watch_out=[
            "Get someone do без to — ошибка.",
            "Have my hair cut, не have done my hair cut.",
        ],
        remember="Объект + V3 = работу сделали с вещью. Человек + инфинитив = человек действует. Have нейтральнее, get настойчивее.",
    ),
    "participle-clauses": lesson(
        "Причастные конструкции позволяют компактно присоединять обстоятельство времени, причины, условия, уступки или сопутствующего действия без отдельного придаточного предложения. **V-ing** обычно представляет действие как одновременное с основным либо как его фон, причину или сопутствующее обстоятельство. **V3** чаще всего имеет пассивное значение или описывает состояние, возникшее в результате действия.\n\nФорма **having + V3** подчёркивает предшествование: Having checked the figures, she signed the report. Пассивное **having been + V3** показывает, что субъект сначала подвергся действию, а затем произошло основное действие. Однако значение причастного оборота определяется контекстом, поэтому V-ing не следует автоматически переводить одним союзом «когда».\n\nГлавное синтаксическое ограничение — скрытое подлежащее причастного оборота обычно должно совпадать с подлежащим главной части. Если Walking into the hall, my badge fell, грамматически получается, будто «бейдж вошёл в зал». Такие **dangling participles** особенно заметны в формальной письменной речи. Если субъекты разные, требуется полноценное придаточное или самостоятельная absolute construction.",
        [
            rule(
                "V-ing: одновременность, причина, фон",
                "Walking along the quay, we compared notes. Feeling unprepared, she asked for a delay. Обороты часто в начале и отделяются запятой.",
                [
                    ex("Sorting the slides, he noticed two versions of the same chart.", "Разбирая слайды, заметил две версии одного графика."),
                    ex("Not wanting to interrupt, we waited in the corridor.", "Не желая перебивать, подождали в коридоре."),
                    ex("Opening the crate, I found rust.", "Открыв клеть, обнаружил ржавчину."),
                ],
                tables=[
                    table(
                        ["Форма", "Типичный смысл", "Пример"],
                        [
                            ["V-ing", "фон / причина / одновременно", "Reading the appendix, she…"],
                            ["V3", "пассив / состояние объекта", "Written in haste, the notice…"],
                            ["having + V3", "сначала X, потом главное", "Having labelled…, they left"],
                            ["having been + V3", "пассив до главного", "Having been warned…"],
                        ],
                    ),
                ],
            ),
            rule(
                "V3 и having been + V3",
                "Built in 1891, the viaduct still carries freight. Having been + V3 — пассив уже до главного действия.",
                [
                    ex("Printed on cheap stock, the map tore at the folds.", "Напечатанная на дешёвой бумаге, карта порвалась на сгибах."),
                    ex("Having been warned twice, the crew sealed the hatch.", "Будучи дважды предупреждённой, команда задраила люк."),
                    ex("Struck by lightning, the oak split along the trunk.", "Поражённый молнией, дуб треснул вдоль ствола."),
                ],
            ),
            rule(
                "Having + V3 и согласование подлежащих",
                "Having + V3 ясно говорит «сначала это». Если деятели разные, нужна абсолютная конструкция со своим подлежащим: The weather permitting…",
                [
                    ex("Having filed the return, we shut the laptop and walked out.", "Подав декларацию, закрыли ноутбук и вышли."),
                    ex("The weather permitting, the drone will map the ridge at dawn.", "Если погода позволит, дрон на рассвете снимет хребет."),
                ],
                pairs=[
                    pair("Walking into the hall, my badge fell.", "Walking into the hall, I dropped my badge.", "Иначе получается, что «ходит» бейдж."),
                    pair("Having ate, we stacked the trays.", "Having eaten, we stacked the trays.", "Having + V3: eaten."),
                ],
                callouts=[
                    callout("Висячее причастие — одна из самых заметных ошибок B2 в письменной речи. Перед запятой проверить: кто реально действует?", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "After she had checked the bolts, she started the engine.", "right": "Having checked the bolts, she started the engine.", "note": "Тот же порядок событий, короче и формальнее."},
            {"left": "Walking into the hall, I dropped my badge.", "right": "Walking into the hall, my badge fell.", "note": "Справа dangling participle."},
        ],
        watch_out=[
            "Подлежащее причастия = подлежащее главной части (кроме absolute).",
            "Having + V3, не having + V2.",
        ],
        remember="V-ing — фон или причина. V3 — пассив. Having + V3 — «сначала». Проверить, кто действует.",
    ),
    "inversion-intro": lesson(
        "Начальная позиция отрицательного или ограничительного выражения может вызывать **инверсию** — вспомогательный или модальный глагол помещается перед подлежащим. В результате предложение получает эмфатический, часто более формальный оттенок, хотя по коммуникативному типу остаётся утверждением, а не вопросом.\n\nЕсли вспомогательный глагол уже есть, инверсия использует его: Never **have I seen**… Если вспомогательного глагола нет, появляется do-support: Rarely **does she visit**… Конструкция применяется не только с never, rarely и seldom, но и с ограничительными сочетаниями only then, only after, only when, а также в устойчивых парных моделях **hardly/scarcely/barely … when** и **no sooner … than**.\n\nИнверсия зависит от позиции выражения. Если ограничительное слово находится в начале и относится к предложению в целом, инверсия обычно обязательна. При обычной позиции слова порядок сохраняется: I have never seen it. После Only after… инверсия обычно появляется в главной части, а не внутри самого придаточного.",
        [
            rule(
                "Never, rarely, seldom, under no circumstances",
                "Never have I… Rarely does the tide… Если нет вспомогательного, подставляется do/does/did. Смысл усиливается: факт подаётся как исключительный.",
                [
                    ex("Never had the archive felt so empty after a launch night.", "Никогда архив не казался таким пустым после ночи открытия."),
                    ex("Seldom do we release a build without a dry run.", "Редко выпускаем сборку без прогона."),
                    ex("Under no circumstances must the originals leave the building.", "Ни при каких обстоятельствах оригиналы не должны покидать здание."),
                ],
                tables=[
                    table(
                        ["Начало", "Инверсия", "Пара"],
                        [
                            ["Never / Rarely / Seldom", "aux + subject + …", "—"],
                            ["Not only…", "aux + subject…", "… but also"],
                            ["Hardly / Scarcely / Barely", "had + subject…", "… when"],
                            ["No sooner", "had + subject…", "… than"],
                            ["Only then / Only after…", "aux в главной части", "—"],
                        ],
                    ),
                ],
            ),
            rule(
                "Not only… и only + обстоятельство",
                "Not only did she redesign the form, she also rewrote the guidance. Only then / only after + clause требуют инверсии в **главной** части.",
                [
                    ex("Not only was the path flooded, but the bridge had shifted.", "Мало того что тропа была затоплена — ещё и мост сдвинулся."),
                    ex("Only then did the sensors start logging again.", "Только тогда датчики снова начали писать лог."),
                    ex("Only after sunset did the bats appear.", "Только после заката появились летучие мыши."),
                ],
            ),
            rule(
                "Hardly / scarcely / no sooner",
                "Hardly had we sat down when the fire alarm sounded. No sooner had the credits rolled than the debate started. When и than не путают.",
                [
                    ex("Scarcely had the ink dried when legal asked for a revision.", "Едва чернила высохли, как юристы попросили правку."),
                    ex("No sooner had she muted the call than someone knocked.", "Не успела выключить звук, как кто-то постучал."),
                ],
                pairs=[
                    pair("No sooner had we arrived when the guide left.", "No sooner had we arrived than the guide left.", "No sooner сочетается с than."),
                    pair("Never I have agreed to such a clause.", "Never have I agreed to such a clause.", "Have встаёт перед подлежащим."),
                ],
                callouts=[
                    callout("Инверсия только если отрицательное слово стоит в начале всей клаузы, не в середине.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "I have never seen the vault so tidy.", "right": "Never have I seen the vault so tidy.", "note": "Тот же факт; справа эмфаза и формальный тон."},
            {"left": "Hardly had we begun when the lights failed.", "right": "No sooner had we begun than the lights failed.", "note": "Пара when / than закреплена за наречием."},
        ],
        watch_out=[
            "No sooner… when — типичная ошибка; нужно than.",
            "Hardly… than — ошибка; нужно when.",
        ],
        remember="Отрицание впереди → вспомогательный + подлежащее. Hardly… when. No sooner… than.",
    ),
    "cleft-sentences": lesson(
        "**Cleft sentences** — расщеплённые конструкции, предназначенные прежде всего для изменения информационной структуры предложения. Они позволяют вынести один компонент в позицию фокуса, чтобы подчеркнуть его как новую, контрастную или исправляющую информацию. В **it-cleft** используется модель It is/was + focus + that/who…, а в **wh-cleft** — конструкция What/Why/Where… + be + focus.\n\nCleft-конструкция не меняет сам факт, а меняет способ его подачи. Сравнение Mara found the error и It was Mara who found the error показывает, что во втором случае главным становится вопрос «кто именно». It-cleft может выделять лицо, предмет, место, время, причину и другие компоненты.\n\nВ wh-cleft первая часть обычно представляет действие или ситуацию как единое понятие: What we need is more time. В **all-cleft** дополнительно подчёркивается ограниченность требования: All I wanted was an explanation. При выборе is/was необходимо учитывать время исходного сообщения. В формальном английском cleft-конструкции особенно полезны для контраста, уточнения и последовательного представления сложной информации.",
        [
            rule(
                "It-cleft: It is / was + фокус + that / who",
                "Фокус — существительное, предложная группа, иногда обстоятельство. Who для людей; that универсален. Время it согласуется с исходным событием: It was last May that…",
                [
                    ex("It was the footnotes that delayed the proofs.", "Именно сноски задержали вёрстку."),
                    ex("It is on Thursdays that the ferry skips this pier.", "Именно по четвергам паром не заходит к этому причалу."),
                    ex("It was in the kitchen that we signed the papers.", "Именно на кухне подписали бумаги."),
                ],
                tables=[
                    table(
                        ["Тип", "Схема", "Задача"],
                        [
                            ["It-cleft", "It is/was + фокус + that/who…", "контраст: не X, а Y"],
                            ["Wh-cleft", "What/Why… + be + фокус", "подготовить определение"],
                            ["All-cleft", "All + clause + be + фокус", "сузить до единственного"],
                        ],
                    ),
                ],
            ),
            rule(
                "Wh-cleft и all-cleft",
                "What they ignored was the humidity. После what часто номинализованное действие. All I want is ten quiet minutes. It-cleft с because подчёркивает причину.",
                [
                    ex("What irritated her was the casual tone of the refusal.", "Что раздражало — небрежный тон отказа."),
                    ex("All we requested was access to the raw tables.", "Всё, что просили, — доступ к сырым таблицам."),
                    ex("It was because the ink ran that the stamp was rejected.", "Именно из-за поплывших чернил штамп не приняли."),
                ],
                pairs=[
                    pair("It is last Monday that we froze the branch.", "It was last Monday that we froze the branch.", "Прошлое требует was."),
                    pair("It was the intern which noticed the mismatch.", "It was the intern who noticed the mismatch.", "Для человека естественнее who (или that)."),
                ],
                callouts=[
                    callout("Учебная норма: What we need **is**… — даже если дальше список, фокус мыслится как одна идея.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "Mara found the error.", "right": "It was Mara who found the error.", "note": "Справа контраст: не кто-то другой, а Мара."},
            {"left": "We need patience.", "right": "What we need is patience.", "note": "Wh-cleft готовит слушателя к существительному-фокусу."},
        ],
        watch_out=[
            "Два фокуса сразу перегружают схему.",
            "Прошлое событие — it was, не it is.",
        ],
        remember="It-cleft — фокус после it is/was. Wh-cleft — what… + be + фокус. All сужает требование.",
    ),
    "narrative-tenses": lesson(
        "Нарративные времена образуют систему временных слоёв. **Past Simple** обычно составляет событийный каркас и продвигает рассказ вперёд. **Past Continuous** создаёт фон, описывает процесс в определённый момент или действие, которое было прервано. **Past Perfect** помещает событие до уже установленной точки прошлого, а **Past Perfect Continuous** подчёркивает длительность или продолжающийся процесс до этой точки.\n\nВыбор времени зависит не только от реальной последовательности событий, но и от точки зрения рассказчика. Past Perfect не следует ставить перед каждым событием, которое произошло раньше в реальном мире: он нужен тогда, когда необходимо явно показать предшествование или устранить неоднозначность. Когда последовательность очевидна, Past Simple часто является естественным вариантом.\n\n**Used to** описывает прежнюю привычку или состояние, которого больше нет или которое противопоставляется настоящему. **Would** обычно используется для повторяющихся действий в уже установленном прошлом контексте, но не для обычных статических состояний вроде know, own, believe или live. Поэтому used to шире по значению, чем would в описании привычек.",
        [
            rule(
                "Скелет и фон: Simple vs Continuous",
                "Simple двигает сюжет: She opened the hatch. Continuous держит декорации или прерванный процесс: Rain was hammering the roof when the radio crackled.",
                [
                    ex("I was lining up the shot when a cyclist cut across the frame.", "Выстраивал кадр, когда велосипедист пересёк кадр."),
                    ex("While the choir was rehearsing, the electrician tested the spots.", "Пока хор репетировал, электрик проверял софиты."),
                    ex("She found the keys and walked out.", "Нашла ключи и вышла — сюжетные шаги."),
                ],
                tables=[
                    table(
                        ["Слой", "Время", "Роль в рассказе"],
                        [
                            ["скелет", "Past Simple", "что произошло дальше"],
                            ["фон", "Past Continuous", "процесс / декорации"],
                            ["ещё раньше", "Past Perfect", "до точки рассказа"],
                            ["длительность до точки", "Past Perfect Continuous", "how long until…"],
                            ["бывшая привычка", "used to + V1", "действие или состояние"],
                            ["повтор в нарративе", "would + V1", "только действия"],
                        ],
                    ),
                ],
            ),
            rule(
                "Предпрошедшее",
                "Past Perfect ставит событие левее основной линии. Past Perfect Continuous подчёркивает длительность. Perfect не нужен на каждое прошлое действие — только на «раньше основной точки».",
                [
                    ex("He realised he had packed the wrong lens.", "Понял, что упаковал не тот объектив."),
                    ex("They had been arguing about the caption since breakfast.", "Спорили о подписи с самого завтрака."),
                    ex("By dusk the tide had covered the steps.", "К сумеркам прилив уже закрыл ступени."),
                ],
            ),
            rule(
                "Used to и would",
                "Used to + инфинитив — привычка или состояние, которого больше нет. Would + инфинитив — повторяющиеся сцены. Would не ставят с be, own, know в значении состояния.",
                [
                    ex("I used to keep the negatives in a biscuit tin.", "Раньше хранил негативы в банке из-под печенья."),
                    ex("After dinner he would walk the harbour wall and count the masts.", "После ужина имел обыкновение идти по стенке гавани."),
                ],
                pairs=[
                    pair("I would know the harbour master quite well.", "I used to know the harbour master quite well.", "Know как состояние — used to, не would."),
                    pair("Every summer we used to would rent the same cabin.", "Every summer we would rent the same cabin.", "Один маркер привычки, не два."),
                ],
                callouts=[
                    callout("When I arrived, she left — последовательность спорная. When I arrived, she had left — к моменту прихода её уже не было.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "When I arrived, she left.", "right": "When I arrived, she had left.", "note": "Справа она уже ушла к моменту прихода."},
            {"left": "He used to own a barge.", "right": "He would own a barge.", "note": "Would с владением звучит неверно."},
        ],
        watch_out=[
            "Не Past Perfect на каждое прошлое действие.",
            "Would не заменяет used to в состояниях.",
        ],
        remember="Simple двигает сюжет, Continuous — фон, Perfect — ещё раньше. Used to — привычка и состояние; would — только повтор действий.",
    ),
    "unreal-past": lesson(
        "Некоторые конструкции используют формы Past Simple и Past Perfect не для обычного календарного прошлого, а для выражения **нереальности, гипотезы, предпочтения или дистанции от действительности**. Это тот же общий принцип, который проявляется в Second Conditional и wish: форма «прошлого» может сигнализировать не время, а контрфактическое или смягчённое отношение говорящего.\n\nВ **It's time + Past Simple** прошедшая форма указывает на действие, которое уже назрело и должно было произойти. В **I'd rather + Past Simple** она выражает предпочтение относительно действия другого человека. Если субъект выполняет действие сам, используется bare infinitive: I'd rather stay.\n\nПосле **as if / as though** Past Simple обычно представляет ситуацию как нереальную или маловероятную в настоящем, а Past Perfect — как предполагаемую более раннюю ситуацию. При этом as if/as though не всегда означают ложность: иногда говорящий просто сравнивает внешний вид или поведение с гипотетической картиной. Поэтому степень нереальности определяется контекстом.",
        [
            rule(
                "It's time / it's high time + Past Simple",
                "Пора уже сделать то, что запаздывает. To-infinitive тоже возможен (It's time to leave), но без упрёка «давно пора».",
                [
                    ex("It's time we archived the beta branch.", "Пора уже заархивировать бета-ветку."),
                    ex("It's high time the captions matched the picture.", "Давно пора, чтобы титры совпадали с картинкой."),
                    ex("It's time you checked the permissions.", "Пора уже проверить права доступа."),
                ],
                tables=[
                    table(
                        ["Конструкция", "Форма", "Смысл"],
                        [
                            ["It's (high) time + clause", "Past Simple", "давно пора"],
                            ["It's time + to-infinitive", "to + V1", "нейтрально «пора»"],
                            ["I'd rather + своё действие", "bare infinitive", "своё предпочтение"],
                            ["I'd rather + чужое", "Past Simple", "предпочтение о другом"],
                            ["as if / as though (ложно сейчас)", "Past Simple / were", "как будто"],
                            ["as if (ложная предпосылка раньше)", "Past Perfect", "как будто уже…"],
                        ],
                    ),
                ],
            ),
            rule(
                "I'd rather и suppose / what if",
                "I'd rather you didn't record this. О себе чаще I'd rather + bare infinitive: I'd rather walk. Suppose / what if + Past — гипотеза.",
                [
                    ex("I'd rather the reviewers saw the uncut interview.", "Предпочтительнее, чтобы рецензенты увидели немонтированное интервью."),
                    ex("Suppose the tide turned an hour earlier — where would we beach?", "Предположим, прилив сменился на час раньше — где бы выбросились на берег?"),
                    ex("I'd rather take the coastal path.", "Предпочтительнее пойти береговой тропой."),
                ],
                pairs=[
                    pair("It's time we go.", "It's time we went.", "В аккуратной речи — Past Simple."),
                    pair("I'd rather you to stay.", "I'd rather you stayed.", "Чужое действие — Past, не to-infinitive."),
                ],
            ),
            rule(
                "As if / as though",
                "Если сравнение явно ложно сейчас: He talks as if he owned the quay. Если ложная предпосылка в прошлом: She looked as if she had seen the uncut footage. Were естественен: as if I were…",
                [
                    ex("He issued orders as though he were still skipper.", "Отдавал приказания, словно всё ещё был шкипером."),
                    ex("The lobby smelled as if someone had spilled turpentine.", "В вестибюле пахло так, будто разлили скипидар."),
                ],
                callouts=[
                    callout("Past здесь — сигнал нереальности или мягкого давления, а не календарь.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "It's time to go.", "right": "It's time we went.", "note": "Инфинитив нейтрален; Past добавляет «хватит тянуть»."},
            {"left": "I'd rather stay.", "right": "I'd rather you stayed.", "note": "Своё действие — инфинитив; чужое — Past."},
        ],
        watch_out=[
            "It's time we go — разговорный сбой в аккуратной речи.",
            "I'd rather you to stay — ошибка.",
        ],
        remember="Past = нереальность или мягкое давление. Чьё действие и насколько оно ложно — два главных вопроса.",
    ),
    "relative-advanced": lesson(
        "Относительные придаточные связывают существительное с дополнительной информацией и позволяют уточнять объект без отдельного предложения. Принципиально различаются **defining** и **non-defining relative clauses**. Defining-clause ограничивает множество возможных объектов и поэтому не выделяется запятыми. Non-defining-clause добавляет комментарий к уже идентифицированному объекту и выделяется запятыми.\n\nВыбор относительного слова зависит от его роли и от того, к чему оно относится. **Who** обычно употребляется для людей, **which** — для вещей и животных, **that** допустим прежде всего в defining-clause. **Whose** обозначает принадлежность и может относиться также к неодушевлённым предметам. Where и when могут соответствовать сочетаниям с предлогом, а формальный стиль допускает конструкции **preposition + which/whom**.\n\nВ defining-clause относительное местоимение можно опустить, если оно является дополнением: the file (that) I sent. Если оно является подлежащим, опускать его нельзя: the file that caused the problem. Сокращённые относительные конструкции с V-ing и V3 особенно характерны для письменной речи и требуют правильного определения смыслового субъекта.",
        [
            rule(
                "Defining vs non-defining",
                "The intern who spotted the error — без придаточного неясно, какой интерн. Mara, who spotted the error, — Mara уже идентифицирована. В non-defining that не используют.",
                [
                    ex("The crate that leaked had been stacked on its side.", "Протекла та клеть, которую поставили на бок."),
                    ex("The old ferry, which still uses a paper log, left at six.", "Старый паром, который всё ещё ведёт бумажный журнал, отошёл в шесть."),
                    ex("Paris, which we visited in March, was cold.", "Париж, который посетили в марте, был холодным."),
                ],
                tables=[
                    table(
                        ["Тип", "Запятые", "that", "Роль"],
                        [
                            ["defining", "нет", "можно", "опознать объект"],
                            ["non-defining", "да", "нельзя", "комментарий"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Paris, that we visited in March, was cold.", "Paris, which we visited in March, was cold.", "Non-defining не берёт that."),
                    pair("the room in that we met", "the room in which we met", "После предлога — which/whom, не that."),
                ],
            ),
            rule(
                "Whose, where, предлог + which / whom",
                "Whose относится и к людям, и к вещам. Where = in/at which для мест. Формально: the desk at which she writes. Разговорно предлог часто уходит в конец.",
                [
                    ex("I need a binder whose rings actually close.", "Нужна папка, кольца которой реально смыкаются."),
                    ex("The quay on which we landed had no rail.", "У причала, к которому пристали, не было перил."),
                    ex("This is the editor with whom I argued about the title.", "Это редактор, с которым спорили о заголовке."),
                ],
            ),
            rule(
                "Сокращённые относительные",
                "Defining-пассив и continuous часто теряют who/which is: the samples stored in aisle C; people waiting by the lift. Of which / of whom присоединяет количество: three of which failed.",
                [
                    ex("The stills pinned above the desk are from the first cut.", "Кадры, приколотые над столом, — из первой сборки."),
                    ex("She listed six objections, two of which were new.", "Перечислила шесть возражений, два из которых были новыми."),
                ],
                callouts=[
                    callout("Запятая решает смысл: My brother who lives in Cork… подразумевает нескольких братьев; My brother, who lives in Cork,… — один брат, Cork — ремарка.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "My brother who lives in Cork is a fiddle player.", "right": "My brother, who lives in Cork, is a fiddle player.", "note": "Слева братьев несколько; справа брат один."},
            {"left": "the shelf I put the tins on", "right": "the shelf on which I put the tins", "note": "Одинаковый смысл; справа формальнее."},
        ],
        watch_out=[
            "Запятая + that в non-defining — ошибка.",
            "Which после предлога не заменяется that.",
        ],
        remember="Нет запятых — опознание; that можно. Есть запятые — комментарий; that нельзя. Предлог + which/whom в формальном стиле.",
    ),
}
