"""Enriched C1 grammar theory (Russian explanations, English examples).

Tone: impersonal / descriptive Russian. No direct address to the learner.
"""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

C1_THEORY = {
    "inversion-full": lesson(
        "На C1 инверсия — не только never / not only. Сюда входят **so / such**, **little** («совсем не»), условные **should / were / had** без if, **not until / not since** и категорические запреты.\n\nЧасть схем сохраняет вспомогательный перед подлежащим (частичная инверсия); часть ставит смысловой глагол перед подлежащим при обстоятельстве места (полная инверсия). Это сильный стилистический жест: одного приёма на абзац обычно достаточно.",
        [
            rule(
                "So / such и little",
                "So + adjective + be + subject: So dense was the fog… Such + be + NP (such как предикатив): Such was the backlog… Little did we know — «и не подозревали».",
                [
                    ex("So brittle was the paper that we stopped using clips.", "Бумага была такой хрупкой, что перестали пользоваться скрепками."),
                    ex("Little did the crew suspect the log had two missing hours.", "Команда и не подозревала, что в журнале не хватает двух часов."),
                    ex("Such was the heat that the wax slumped.", "Жара была такой, что воск осел."),
                ],
                tables=[
                    table(
                        ["Схема", "Порядок", "Пример якоря"],
                        [
                            ["so + adj", "so + adj + be + subject", "So dense was the fog…"],
                            ["such (предикатив)", "such + be + subject", "Such was the backlog…"],
                            ["little", "little + aux + subject", "Little did we know…"],
                            ["условие без if", "Should/Were/Had + subject", "Had we known…"],
                            ["not until / since", "инверсия в главной", "Not until… did we…"],
                            ["место + движение", "AdvP + V + subject", "Down the quay came…"],
                        ],
                    ),
                ],
            ),
            rule(
                "Условная инверсия: should, were, had",
                "Should you need… = If you need… Were the tide higher… = If the tide were higher… Had we known… = If we had known… Отрицание: Had we not left… Were it not for… Should здесь не «следует» — это гипотетическое if.",
                [
                    ex("Should the generator fail, switch to the battery bank.", "Если генератор откажет, переключение на батареи."),
                    ex("Were it not for the sandbar, the channel would be obvious.", "Если бы не песчаная коса, фарватер был бы очевиден."),
                    ex("Had we labelled the crates, the mix-up would have been obvious.", "Если бы клети подписали, путаница была бы очевидна."),
                ],
                pairs=[
                    pair("Not until did the fog lift we saw the marker.", "Not until the fog lifted did we see the marker.", "Сначала until-клауза, затем инверсия в главной."),
                    pair("Should you will need help, text the rota.", "Should you need help, text the rota.", "После should — bare infinitive, не will."),
                ],
            ),
            rule(
                "Not until и директивная инверсия",
                "Not until the credits ended did anyone speak. Вспомогательный инвертируется в главной части, не внутри until. Under no circumstances / on no account — строгий запрет. Полная инверсия места: Down the quay came the pilot boat.",
                [
                    ex("Not until the varnish cured did we hang the sign.", "Только после того как лак схватился, повесили вывеску."),
                    ex("Along the parapet stood three unused floodlights.", "Вдоль парапета стояли три неиспользованных прожектора."),
                    ex("On no account should the originals be photocopied.", "Ни в коем случае оригиналы не следует копировать."),
                ],
                callouts=[
                    callout("Were she to leave предпочтительнее Was she to leave в аккуратной гипотезе.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "If she had checked the tide, she would have waited.", "right": "Had she checked the tide, she would have waited.", "note": "Смысл тот же; инверсия плотнее и формальнее."},
            {"left": "The pilot boat came down the quay.", "right": "Down the quay came the pilot boat.", "note": "Справа сначала место, потом появление."},
        ],
        watch_out=[
            "Инверсия внутри until-клаузы — ошибка.",
            "После should в условии — bare infinitive.",
        ],
        remember="Отрицание в начале тянет вспомогательный вперёд. Should/were/had без if — сжатое условие. Место + came/stood — полная инверсия.",
    ),
    "fronting-emphasis": lesson(
        "**Fronting** — вынос элемента из канонической позиции в начало, чтобы задать топик или контраст. Английский терпит это хуже, чем русский, поэтому фронтирование маркировано: звучит как сознательный жест.\n\nДополнение, предикатив, обстоятельство и as for-группа готовят слушателя к комментарию. Иногда вызывается инверсия, иногда порядок подлежащее–глагол сохраняется.",
        [
            rule(
                "Дополнение и предикатив влево",
                "This clause I will not sign. Brilliant the talk was not. Вынос почти всегда контрастен: не то, а вот это. В речи удар падает на фронтированный кусок.",
                [
                    ex("The footnotes I can live with; the missing corpus I cannot.", "Со сносками смириться можно, с отсутствующим корпусом — нет."),
                    ex("Happy with the mix she was not.", "Довольна сведением она не была."),
                    ex("The delay I can accept.", "Задержку принять можно."),
                ],
                tables=[
                    table(
                        ["Что вынесено", "Инверсия?", "Пример"],
                        [
                            ["дополнение", "обычно нет", "This clause I will not sign."],
                            ["предикатив", "обычно нет", "Happy she was not."],
                            ["место + be/come/stand", "часто да", "In the drawer lay…"],
                            ["away/out + NP", "да (не с местоимением)", "Away ran the intern."],
                            ["as for / as to", "рамка, не инверсия", "As for the budget…"],
                        ],
                    ),
                ],
            ),
            rule(
                "Обстоятельства и инверсия",
                "In the top drawer lay the unsent postcard. Если глагол — be или непереходный глагол движения/положения, подлежащее часто уходит вправо. С местоимением инверсия обычно блокируется: Away he ran, не Away ran he.",
                [
                    ex("On the blotting paper sat a ring of rust.", "На промокашке лежало ржавое кольцо."),
                    ex("Out of the fog loomed the north beacon.", "Из тумана выступил северный бакен."),
                    ex("Behind the curtain were three crates.", "За занавеской стояли три клети."),
                ],
                pairs=[
                    pair("Away ran they when the siren started.", "Away they ran when the siren started.", "Местоимение не инвертируется после away."),
                ],
            ),
            rule(
                "As for / as to",
                "As for the budget, we are still waiting. As to whether they will renew, nobody will say. Сначала назвали тему, потом дали оценку.",
                [
                    ex("As for the raw files, they never left the lab machine.", "Что касается сырых файлов, они не покинули лабораторный компьютер."),
                    ex("As to why the beam sagged, the inquiry is still open.", "Что до того, почему провисла балка, расследование ещё открыто."),
                ],
                callouts=[
                    callout("Приём работает только при контрасте или смене кадра. Фронтировать всё подряд — шум, не эмфаза.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "I will not sign this clause.", "right": "This clause I will not sign.", "note": "Справа контраст с другими пунктами."},
            {"left": "The postcard lay in the top drawer.", "right": "In the top drawer lay the postcard.", "note": "Справа сначала сцена, потом объект."},
        ],
        watch_out=[
            "Away ran she — неестественно; с местоимением: Away she ran.",
            "Не фронтировать без мотива контраста.",
        ],
        remember="Влево уходит топик или контраст. Место + be/come/stand часто инвертирует подлежащее. As for открывает рамку.",
    ),
    "subjunctive-mandative": lesson(
        "Мандативный **subjunctive** выражает требование, рекомендацию или необходимость: после insist, demand, recommend и после it is essential / vital that смысловой глагол стоит в **базовой форме** для всех лиц: that she leave, that the samples be sealed.\n\nБританский регистр часто вставляет **should**: that she should leave. **Were-subjunctive** обслуживает гипотезы: if he were, I wish I were.",
        [
            rule(
                "Глаголы требования и рекомендаций",
                "They insisted that the clause be struck. Отрицание: that she not sign (без don't). В американском академическом стиле голая база частотнее; в британском — should + база.",
                [
                    ex("The board demanded that the minutes be circulated the same day.", "Совет потребовал, чтобы протокол разослали в тот же день."),
                    ex("I suggest that she not present the unverified figures.", "Предлагается, чтобы она не представляла непроверенные цифры."),
                    ex("They recommended that the film be recut.", "Рекомендовали перемонтировать фильм."),
                ],
                tables=[
                    table(
                        ["Контекст", "Форма в that-клаузе", "Пример"],
                        [
                            ["требование (AmE)", "базовая форма", "that she leave"],
                            ["требование (BrE)", "should + база", "that she should leave"],
                            ["отрицание", "not + база", "that she not sign"],
                            ["гипотеза", "were", "If I were…"],
                        ],
                    ),
                ],
            ),
            rule(
                "It is + adjective + that",
                "It is essential / imperative / crucial / desirable that + subjunctive. It is important that тоже может брать subjunctive, но indicative (that he leaves) звучит скорее как констатация, а не предписание.",
                [
                    ex("It is vital that the backup remain offline.", "Крайне важно, чтобы резервная копия оставалась офлайн."),
                    ex("It is desirable that every witness be heard in private first.", "Желательно, чтобы каждого свидетеля сначала выслушали наедине."),
                ],
                pairs=[
                    pair("The chair insisted that the vote is postponed.", "The chair insisted that the vote be postponed.", "Требование, не констатация."),
                    pair("It is vital that she remains offline.", "It is vital that she remain offline.", "Remain без -s в предписании."),
                ],
            ),
            rule(
                "Were-subjunctive и формулы",
                "If I were you, Were she to resign…, as it were. Формулы: Be that as it may, Suffice it to say, Far be it from me — застыли и не спрягаются.",
                [
                    ex("Were the licence to lapse, the archive would close to visitors.", "Если бы лицензия истекла, архив закрыли бы для посетителей."),
                    ex("Be that as it may, the tide will not wait.", "Как бы то ни было, прилив ждать не будет."),
                ],
                callouts=[
                    callout("She insisted that he was wrong — факт (indicative). She insisted that he be present — требование (subjunctive). Один глагол — два смысла.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "She insisted that he was wrong.", "right": "She insisted that he be present.", "note": "Факт vs требование."},
            {"left": "It is essential that she is there.", "right": "It is essential that she be there.", "note": "Справа предписание."},
        ],
        watch_out=[
            "That she leaves после demand в формальном предписании — сбой нормы C1.",
            "That she doesn't sign → that she not sign / should not sign.",
        ],
        remember="Предписание: that + база (или should + база) для всех лиц. Were — гипотеза. Не путать с констатацией факта.",
    ),
    "impersonal-passive": lesson(
        "Репортажный пассив отдаляет источник: важно содержание, а не кто сказал. Две главные схемы: безличная **It is said that…** и личная **Subject + is said + to-infinitive**.\n\nЕсли после that есть there, возможен **There is said to be…**. Перфектный инфинитив относит репортируемое в прошлое.",
        [
            rule(
                "It + passive + that",
                "It is widely assumed that the ferry will skip Tuesday. Подлежащее it — синтаксическая заглушка, не «вещь».",
                [
                    ex("It is rumoured that the foundry will close in March.", "Ходят слухи, что литейный цех закроют в марте."),
                    ex("It was estimated that the backlog would last six weeks.", "По оценкам, отставание продлится шесть недель."),
                    ex("It is said that the tide tables were misprinted.", "Говорят, таблицы приливов напечатали с ошибкой."),
                ],
                tables=[
                    table(
                        ["Схема", "Форма", "Когда"],
                        [
                            ["безличная", "It is said that + clause", "удобно сохранить полную клаузу"],
                            ["личная", "NP is said to + inf", "тема — человек/объект"],
                            ["there", "There is said to be…", "существование"],
                            ["прошлое репортажа", "to have (+ been) + V3", "уже случилось"],
                        ],
                    ),
                ],
            ),
            rule(
                "Личный пассив + инфинитив",
                "The foundry is rumoured to be closing. She is thought to have declined the prize. Простой инфинитив — одновременность; to have + V3 — предшествование.",
                [
                    ex("The skipper is said to distrust automatic pilots in fog.", "Говорят, шкипер не доверяет автопилоту в тумане."),
                    ex("Two crates are reported to have gone missing at the hub.", "Сообщают, что на узле пропали две клети."),
                ],
                pairs=[
                    pair("They are rumoured that they sold the quay.", "They are rumoured to have sold the quay.", "После личного пассива — to-infinitive, не that."),
                    pair("He is said he declined the knighthood.", "He is said to have declined the knighthood.", "To have + V3."),
                ],
            ),
            rule(
                "There-схема",
                "There is believed to be a second ledger. There are said to have been witnesses. Избегать двойного that: She is said that she…",
                [
                    ex("There is thought to be a sandbar just east of the marker.", "Считается, что сразу к востоку от знака есть коса."),
                    ex("There are said to have been three unlogged landings.", "Говорят, было три незафиксированные посадки."),
                ],
                callouts=[
                    callout("People say X → X is said to… убирает people и ставит X темой. Выбор схемы — про информационную структуру, не только про «пассивность».", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "People say the editor has resigned.", "right": "The editor is said to have resigned.", "note": "Личный пассив убирает people."},
            {"left": "It is believed that there is a leak.", "right": "There is believed to be a leak.", "note": "Вторая схема короче и типичнее для сводок."},
        ],
        watch_out=[
            "He is said that he left — ошибка.",
            "Прошлое репортируемого — to have + V3.",
        ],
        remember="Либо it + that-клауза, либо подлежащее + to-infinitive. There is said to be… для существования.",
    ),
    "hedging-modality": lesson(
        "Хедж — языковой зазор между утверждением и полной ответственностью за него. На C1 это не «вода», а **этика точности**: seem / appear, tend to, may well, it could be argued.\n\nСлишком много хеджей размывает тезис; слишком мало — выдаёт догадку за факт.",
        [
            rule(
                "Seem / appear / tend",
                "She seems to have missed the briefing. There appears to be a second leak. Tend to — склонность, не единичный случай. Raising: It seems that she missed → She seems to have missed.",
                [
                    ex("The mix appears to have been bounced too hot.", "Похоже, сведение выгрузили со слишком горячим уровнем."),
                    ex("Early drafts tend to over-explain the method.", "Ранние черновики обычно слишком подробно объясняют метод."),
                    ex("They appear to have skipped the dry run.", "Похоже, прогон пропустили."),
                ],
                tables=[
                    table(
                        ["Сила", "Средство", "Оттенок"],
                        [
                            ["мягкий вывод", "seem / appear + to", "интерпретация"],
                            ["склонность", "tend to", "не единичный случай"],
                            ["уверенный хедж", "may well", "вполне правдоподобно"],
                            ["осторожнее", "might conceivably / could arguably", "слабая гипотеза"],
                            ["рамка", "it could be argued that…", "дистанция аргумента"],
                        ],
                    ),
                ],
            ),
            rule(
                "Шкала may / might / could",
                "May well = вполне возможно и правдоподобно. Might conceivably / could arguably — ещё осторожнее. Should в хедже — «по ожиданиям модели», не приказ.",
                [
                    ex("The delay may well reflect a customs backlog rather than a shortage.", "Задержка вполне может отражать затор на таможне."),
                    ex("The anomaly could arguably be an artefact of the sensor housing.", "Аномалию, пожалуй, можно счесть артефактом корпуса датчика."),
                ],
                pairs=[
                    pair("She seems that she distrusts the autopilot.", "She seems to distrust the autopilot.", "Seem + to-infinitive или It seems that…"),
                    pair("The data prove maybe the washer failed.", "The data suggest the washer may have failed.", "Prove слишком силён при неуверенности."),
                ],
            ),
            rule(
                "Безличные рамки аргумента",
                "It could be argued that…, One possible reading is…, The figures would appear to suggest… Would здесь — дистанцирование, не будущее. Данные лучше ставить субъектом, чем I think.",
                [
                    ex("It might be objected that the sample is coastal-only.", "Могут возразить, что выборка исключительно прибрежная."),
                    ex("The logs would appear to contradict the verbal briefing.", "Журналы, судя по всему, противоречат устному брифингу."),
                ],
                callouts=[
                    callout("I think maybe it could possibly perhaps — стопка хеджей уничтожает тезис. Один слой дистанции обычно достаточен.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "The beam failed because of the washer.", "right": "The beam appears to have failed because of the washer.", "note": "Справа вывод помечен как интерпретация."},
            {"left": "This may be the cause.", "right": "This may well be the cause.", "note": "May well повышает правдоподобие, оставаясь хеджем."},
        ],
        watch_out=[
            "Seem that сразу после лица — ошибка.",
            "Стопка хеджей вместо одного точного.",
        ],
        remember="Сначала сила данных, потом сила модального. Seem/appear + to. May well — уверенный хедж.",
    ),
    "nominalization": lesson(
        "**Номинализация** переводит процесс или качество в существительное: decide → decision, refuse → refusal. Академический английский любит такие имена: уже известное действие упаковывается в топик.\n\nЦена — тяжесть и размытые роли (кто сделал?). Хороший C1-текст чередует живой глагол и имя.",
        [
            rule(
                "От глагола и прилагательного к имени",
                "Суффиксы: -tion/-sion, -ment, -al, -ance/-ence, -ity, -ness. The committee decided X → The committee's decision to X. Сохранять валентность: decision to / that; refusal of.",
                [
                    ex("Their withdrawal from the tender surprised no one.", "Их отзыв заявки никого не удивил."),
                    ex("The instability of the emulsion ruined the last batch.", "Нестабильность эмульсии испортила последнюю партию."),
                    ex("their refusal to sign the clause", "их отказ подписать пункт"),
                ],
                tables=[
                    table(
                        ["Источник", "Имя", "Типичный слот"],
                        [
                            ["decide", "decision", "to / that"],
                            ["refuse", "refusal", "to / of"],
                            ["withdraw", "withdrawal", "from"],
                            ["insist", "insistence", "on"],
                            ["unstable", "instability", "of"],
                            ["fail", "failure", "to"],
                        ],
                    ),
                ],
            ),
            rule(
                "Of-фразы и скрытый агенс",
                "The destruction of the samples (кем?) можно раскрыть: the technicians' destruction… / …by the technicians. Если агенс важен для ответственности, не прятать его. Цепочки of of of — сигнал переписать глаголами.",
                [
                    ex("The postponement of the launch by the harbour master angered the skippers.", "Отсрочка выхода гаванским капитаном разозлила шкиперов."),
                    ex("Her insistence on a paper trail delayed the payment.", "Настойчивость относительно бумажного следа задержала платёж."),
                ],
                pairs=[
                    pair("The inspecting of the hull by the surveyor was done.", "The surveyor inspected the hull.", "Пустую номинализацию разжимают в глагол."),
                    pair("Informations about the leak were scarce.", "Information about the leak was scarce.", "Information неисчисляемое."),
                ],
            ),
            rule(
                "Когда лучше оставить глагол",
                "Инструкции и живой абзац выигрывают от finite verb. Номинализация уместна, когда процесс уже введён и становится темой следующего предложения.",
                [
                    ex("We measured the sag twice. This measurement later became Exhibit C.", "Дважды измерили провис. Это измерение позже стало приложением C."),
                    ex("The surveyor inspected the hull.", "Вместо the undertaking of an inspection of the hull by the surveyor."),
                ],
                callouts=[
                    callout("Имя упаковывает процесс в топик. Если нет нового смыслового узла — вернуть глагол.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "They decided to freeze the branch.", "right": "Their decision to freeze the branch…", "note": "Справа решение может стать подлежащим следующего хода."},
            {"left": "Because the emulsion was unstable, the batch failed.", "right": "Emulsion instability caused the batch to fail.", "note": "Имя короче, но теряется оттенок because."},
        ],
        watch_out=[
            "The doing of the making of — пустая номинализация.",
            "Артикли и число: a decision, two refusals; information без a.",
        ],
        remember="Имя упаковывает процесс в топик. Вернуть агенса, если важна ответственность. Чередовать с живыми глаголами.",
    ),
    "ellipsis-substitution": lesson(
        "Связный английский постоянно что-то опускает (**ellipsis**) или заменяет (**substitution**: so / neither, do so, one). Это грамматика данного: полный повтор звучит тяжело.\n\nЕсли восстановление двоится — эллипсис запрещён.",
        [
            rule(
                "So / neither / nor",
                "So do I, Neither was the deputy. Порядок: so / neither + вспомогательный + подлежащее. Too / either — без инверсии: I do too.",
                [
                    ex("The skipper distrusts the autopilot. — So does the pilot.", "Шкипер не доверяет автопилоту. — И лоцман тоже."),
                    ex("I haven't logged the dive. — Neither have I.", "Погружение не занесено в журнал. — И у меня тоже."),
                ],
                tables=[
                    table(
                        ["Реплика", "Схема", "Не путать с"],
                        [
                            ["я тоже (+)", "So + aux + subject", "So I do (эмфаза «и правда»)"],
                            ["я тоже (−)", "Neither + aux + subject", "Neither… don't"],
                            ["всё действие", "do so", "do it so"],
                            ["исчисляемое", "one / ones", "голый the green"],
                        ],
                    ),
                ],
                pairs=[
                    pair("So I do — в значении «я тоже».", "So do I.", "Для «тоже» нужна инверсия."),
                ],
            ),
            rule(
                "Do so и one / ones",
                "Do so заменяет всё сказуемое: Those who wish to object may do so in writing. One / ones — исчисляемое существительное. So после believe / expect / say замещает that-клаузу: I expect so.",
                [
                    ex("If you need to override the lock, do so before dusk.", "Если нужно обойти замок, сделать это до сумерек."),
                    ex("Pass me the cracked jar, not the sealed ones.", "Передать треснувшую банку, не запечатанные."),
                ],
            ),
            rule(
                "Сравнительный эллипсис",
                "She edits faster than he does. She likes the intern more than the editor — двусмысленно. Тогда оставить глагол: …more than the editor does.",
                [
                    ex("The afternoon tide ran higher than the morning tide did.", "Дневной прилив был выше, чем утренний."),
                    ex("A: Will they renew? B: I should think so.", "— Продлят? — Думаю, да."),
                ],
                callouts=[
                    callout("Do so плохо заменяет be и have в значении обладания — там нужен другой вспомогательный.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "I need a spare impeller. — I need a spare impeller too.", "right": "I need a spare impeller. — So do I.", "note": "Справа стандартное согласие без полного повтора."},
            {"left": "She likes the intern more than the editor.", "right": "She likes the intern more than the editor does.", "note": "Справа ясно: сравнение субъектов."},
        ],
        watch_out=[
            "So I do ≠ So do I.",
            "Если смысл двоится — вернуть глагол.",
        ],
        remember="So / neither + aux + subject. Do so = всё действие. One — исчисляемый повтор.",
    ),
    "advanced-conditionals": lesson(
        "C1 расширяет условные союзным аппаратом и инверсией. **Provided (that) / as long as / on condition that** задают ограничение-разрешение. **Unless** — единственное препятствие, не универсальный if not.\n\n**But for** + noun и **were it not for** вводят единственный фактор. **Even if** ≠ **even though**.",
        [
            rule(
                "Provided, as long as, unless",
                "You may board provided your pass is dated today. As long as подчёркивает длящееся условие. Unless = if not, но плохо стыкуется с would в вежливом предложении.",
                [
                    ex("We will release the cut provided that legal signs off by noon.", "Монтаж выйдет при условии, что юристы завизируют до полудня."),
                    ex("The drone can fly as long as the wind stays below twelve knots.", "Дрон может лететь, пока ветер ниже двенадцати узлов."),
                    ex("Unless you hold a dated pass, you cannot board.", "Без датированного пропуска на борт нельзя."),
                ],
                tables=[
                    table(
                        ["Связка", "Смысл", "Ограничение"],
                        [
                            ["provided / providing", "разрешение под условием", "часто формально"],
                            ["as long as", "пока условие держится", "длящийся контроль"],
                            ["unless", "if not / единственный блокер", "не вежливое unless you wouldn't"],
                            ["but for + NP", "если бы не X", "только именная группа"],
                            ["even if", "гипотетическая уступка", "≠ even though"],
                            ["even though", "уступка-факт", "уже верно"],
                        ],
                    ),
                ],
            ),
            rule(
                "But for и инверсия",
                "But for the sandbar, we would have gone aground. Had it not been for her note… — формальные двойники. Should / were / had без if — см. также inversion-full.",
                [
                    ex("But for a jammed pulley, the sail would have come down cleanly.", "Если бы не заклинивший блок, парус лег бы чисто."),
                    ex("Had it not been for the spare gasket, the pump would have thrown oil.", "Если бы не запасная прокладка, насос выбросил бы масло."),
                ],
                pairs=[
                    pair("Even though the fog lifts tomorrow, we will not cross.", "Even if the fog lifts tomorrow, we will not cross.", "Гипотеза о завтра — even if."),
                    pair("But for we had a spare gasket, the pump failed.", "But for a spare gasket, the pump would have failed.", "But for + NP, не клауза."),
                ],
            ),
            rule(
                "Even if, even though, given that",
                "Even if the fog lifts, we will not cross — условие может быть ложным. Even though the fog has lifted — факт. Given that вводит данность как основание.",
                [
                    ex("Even if the client waives the fee, the clause stays.", "Даже если клиент откажется от сбора, пункт останется."),
                    ex("Given that the tide turns at 16:10, we should be off the wall by 15:40.", "Учитывая смену прилива в 16:10, сойти со стенки к 15:40."),
                ],
                callouts=[
                    callout("Unless you wouldn't mind — калька. Для вежливости: If you wouldn't mind.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "If you don't have a pass, you can't board.", "right": "Unless you have a pass, you can't board.", "note": "Здесь unless уместен: нет пропуска — единственный блокер."},
            {"left": "Even if it rains, the market stays open.", "right": "Even though it is raining, the market is open.", "note": "If — гипотеза; though — уже идёт дождь."},
        ],
        watch_out=[
            "But for + клауза невозможно.",
            "Even if ≠ even though.",
        ],
        remember="Provided / as long as = разрешение под условием. But for + имя = единственный фактор. Even if ≠ even though.",
    ),
    "complex-noun-phrases": lesson(
        "Академическое подлежащее на C1 редко бывает голым существительным. Его собирают из детерминатива, **премодификаторов** и **постмодификаторов**.\n\nГлавный навык — видеть **голову** группы и не согласовывать глагол с ближайшим существительным справа. Второй — не строить цепочку, которую нельзя разобрать с одного раза.",
        [
            rule(
                "Премодификация и классификаторы",
                "Ближе к голове всё конкретнее: those three damaged harbour-wall floodlights. Классификатор обычно в единственном: a tide table. Дефисы помогают: a well-argued objection.",
                [
                    ex("The two remaining salt-stained canvas covers were useless.", "Два оставшихся просоленных парусиновых чехла были бесполезны."),
                    ex("A last-minute legal objection froze the release.", "Возражение юристов в последнюю минуту заморозило выпуск."),
                ],
                tables=[
                    table(
                        ["Зона", "Что входит", "Риск"],
                        [
                            ["детерминатив", "the / those / a", "пропуск при повторном введении"],
                            ["премодификаторы", "adj, V-ing/V3, классификатор", "порядок и дефисы"],
                            ["голова", "главное существительное", "к ней согласование"],
                            ["постмодификаторы", "of, PP, relative, to-inf", "перегруз хвостами"],
                        ],
                    ),
                ],
            ),
            rule(
                "Постмодификация",
                "The decision of the harbour master to delay the sailing… Голова — decision. Причастие справа: the samples stored in aisle C. Инфинитив: the need to relabel every jar.",
                [
                    ex("The refusal of the foundry to honour the last invoice delayed the parts.", "Отказ литейки оплатить последний счёт задержал детали."),
                    ex("Anyone hoping to board after dusk must radio the wall.", "Любой, кто надеется сесть на борт после сумерек, должен вызвать стенку по рации."),
                ],
                pairs=[
                    pair("The set of wet plates were stacked too soon.", "The set of wet plates was stacked too soon.", "Голова set — единственное число."),
                    pair("A documents archive sat in the loft.", "A document archive sat in the loft.", "Классификатор без -s."),
                ],
            ),
            rule(
                "Согласование и читаемость",
                "The quality of the recordings is… — глагол к quality. Если постмодификаторов больше трёх — разбить на два предложения.",
                [
                    ex("The accuracy of the tide tables issued in March is now in doubt.", "Точность мартовских таблиц приливов теперь под вопросом."),
                    ex("The harbour master delayed the evening freight ferry. The sailing had already been announced.", "Два коротких предложения яснее одной перегруженной группы."),
                ],
                callouts=[
                    callout("Proximity error: согласование с ближайшим существительным справа — типичный сбой C1 на письме.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "the damaged floodlights on the harbour wall", "right": "the harbour-wall floodlights that were damaged", "note": "Разный порядок уточнений — разный фокус."},
            {"left": "The results of the tests was leaked.", "right": "The results of the tests were leaked.", "note": "Голова results — множественное; was — proximity error."},
        ],
        watch_out=[
            "The set of plates were… — нужно was, если голова set.",
            "Тяжесть больше трёх хвостов — делить.",
        ],
        remember="Найти голову — к ней глагол. Премодификаторы уточняют класс; постмодификаторы добавляют отношения.",
    ),
    "reporting-verb-patterns": lesson(
        "Глаголы передачи речи на C1 различаются не только смыслом, но и **обязательным дополнением**. Accuse somebody of -ing, warn somebody against -ing, threaten to, insist on -ing / that, suggest -ing / that (но не suggest somebody to).\n\nОшибка почти всегда в предлоге или в лишнем to. Глагол лучше учить пакетом с моделью.",
        [
            rule(
                "Предлог + -ing",
                "Accuse of, suspect of, criticise for, apologise for, congratulate on, insist on, warn against, prevent somebody from. Герундий называет действие как факт-событие.",
                [
                    ex("They accused the intern of leaking the stills.", "Интерна обвинили в сливе кадров."),
                    ex("She apologised for having frozen the wrong branch.", "Извинилась за то, что заморозила не ту ветку."),
                    ex("She congratulated the intern on spotting the mismatch.", "Поздравила интерна с тем, что заметил несовпадение."),
                ],
                tables=[
                    table(
                        ["Глагол", "Модель", "Нельзя"],
                        [
                            ["accuse", "sb of -ing", "accuse to"],
                            ["congratulate", "sb on -ing", "congratulate for — реже"],
                            ["insist", "on -ing / that", "insist to do"],
                            ["threaten / refuse", "to + V1", "threaten -ing"],
                            ["suggest / recommend", "-ing / that", "suggest sb to"],
                            ["explain", "sth to sb", "explain sb sth"],
                            ["warn", "sb to / against -ing", "—"],
                            ["blame", "sb for / sth on sb", "—"],
                        ],
                    ),
                ],
            ),
            rule(
                "To-infinitive и that-клауза",
                "Threaten, refuse, promise, offer, claim + to. Remind / warn somebody to. Insist / suggest / recommend / demand + that (+ subjunctive / should). Suggest -ing возможно без адресата.",
                [
                    ex("The contractor threatened to halt the pour.", "Подрядчик пригрозил остановить заливку."),
                    ex("He reminded us to log the dive before changing tanks.", "Напомнил занести погружение в журнал до смены баллонов."),
                    ex("She suggested postponing the release.", "Предложила отложить выпуск."),
                ],
                pairs=[
                    pair("He suggested us to radio the wall.", "He suggested that we radio the wall.", "Не suggest somebody to."),
                    pair("Legal recommended him to freeze the branch.", "Legal recommended that he freeze the branch.", "Recommend + that / -ing."),
                ],
            ),
            rule(
                "Типичные ловушки",
                "Explain somebody the problem → explain the problem to somebody. Tell somebody that; say that / say to somebody. Blame somebody for; blame something on somebody.",
                [
                    ex("She explained the sag to the surveyor.", "Объяснила провис сюрвейеру."),
                    ex("They blamed the failure on the washer.", "Возложили вину за поломку на шайбу."),
                ],
                callouts=[
                    callout("Suggest/recommend без somebody to. Insist on doing / insist that — не insist to do.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "She suggested that we postpone.", "right": "She suggested postponing.", "note": "Оба верны; нет адресата-объекта перед to."},
            {"left": "He warned us not to cross.", "right": "He warned us against crossing.", "note": "To и against -ing близки; against чаще о линии поведения."},
        ],
        watch_out=[
            "Suggest her to wait — сбой стандарта C1.",
            "Insist to do — ошибка.",
        ],
        remember="Учить пакет: глагол + предлог + форма. Suggest/recommend без somebody to. Explain something to somebody.",
    ),
}
