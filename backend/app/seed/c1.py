from app.seed.helpers import err, ex, fill, lesson, mc, module, rule, xf

C1 = [
    module(
        "inversion-full",
        "Полная инверсия",
        "So/such, little, should/were/had в условии, not until и запреты в начале фразы.",
        26,
        "Когда порядок слов сам несёт эмфазу",
        lesson(
            "На C1 инверсия — не только never / not only. Сюда входят so / such, little в значении «совсем не», условные should / were / had без if, not until / not since в разнесённых конструкциях и категорические запреты. Часть схем сохраняет вспомогательный глагол перед подлежащим (частичная инверсия); часть ставит смысловой глагол перед подлежащим, когда впереди обстоятельство места и глагол непереходный (полная инверсия в узком смысле). Это сильный стилистический жест: одного приёма на абзац обычно достаточно.",
            [
                rule(
                    "So / such и little",
                    "So + adjective + be + subject: So dense was the fog that the pier vanished. Such + noun phrase + be: Such was the backlog that Friday slipped. Little did we know / Little does she realise — «и не подозревали».",
                    [
                        ex("So brittle was the paper that we stopped using clips.", "Бумага была такой хрупкой, что мы перестали пользоваться скрепками."),
                        ex("Little did the crew suspect the log had two missing hours.", "Команда и не подозревала, что в журнале не хватает двух часов."),
                    ],
                ),
                rule(
                    "Условная инверсия: should, were, had",
                    "Should you need a spare key… = If you need… Were the tide higher… = If the tide were higher… Had we known… = If we had known… Отрицание: Had we not left… Were it not for… Should не равняется «следует» — это гипотетическое if.",
                    [
                        ex("Should the generator fail, switch to the battery bank.", "Если генератор откажет, переключитесь на батареи."),
                        ex("Were it not for the sandbar, the channel would be obvious.", "Если бы не песчаная коса, фарватер был бы очевиден."),
                    ],
                ),
                rule(
                    "Not until / not since и директивная инверсия",
                    "Not until the credits ended did anyone speak. Вспомогательный глагол инвертируется в главной части, не внутри until-клаузы. Under no circumstances / on no account / in no way — строгий запрет: On no account should the originals be photocopied. Полная инверсия места: Down the quay came the pilot boat.",
                    [
                        ex("Not until the varnish cured did we hang the sign.", "Только после того как лак схватился, мы повесили вывеску."),
                        ex("Along the parapet stood three unused floodlights.", "Вдоль парапета стояли три неиспользованных прожектора."),
                    ],
                ),
            ],
            compare=[
                {"left": "If she had checked the tide, she would have waited.", "right": "Had she checked the tide, she would have waited.", "note": "Смысл тот же; инверсия плотнее и формальнее."},
                {"left": "The pilot boat came down the quay.", "right": "Down the quay came the pilot boat.", "note": "Справа сцена ставится как кинокадр: сначала место, потом появление."},
            ],
            watch_out=[
                "Not until + инверсия внутри until: Not until did we finish — ошибка; инверсия после всей until-группы.",
                "Were she to leave ≠ Was she to leave в аккуратной гипотезе; держите were.",
            ],
            remember="Отрицание или ограничение в начале тянет вспомогательный глагол вперёд. Should/were/had без if — сжатое условие. Место + came/stood — полная инверсия.",
        ),
        [
            mc("___ the delay that several ferries stacked outside the bar.", ["So great was", "So was great", "Such great was"], "So great was", "So + adj + was + subject."),
            fill("___ you misplace the fob, call the night desk. (should)", "Should", "Should + подлежащее = if."),
            xf("Инверсия: If we had labelled the crates, the mix-up would have been obvious.", "Had we labelled the crates, the mix-up would have been obvious.", "Had + subject + V3."),
            err("Not until did the fog lift we saw the marker.", "Not until the fog lifted did we see the marker.", "Сначала until-клауза, затем did + we."),
            fill("Little ___ they realise the mic was still live. (do / past)", "did", "Little did + subject."),
            mc("On no account ___ the wet plates be stacked.", ["the plates should", "should", "should not"], "should", "On no account + should + подлежащее. Второе отрицание не нужно."),
        ],
        [
            fill("Вставьте форму to be: ___ it not for the spare impeller, we would have drifted. (be)", "Were", "Were it not for."),
            mc("Выберите форму to be: Such ___ the heat that the wax slumped.", ["was", "were", "did"], "was", "Such was + noun."),
            xf("Полная инверсия места: The curator came round the corner.", "Round the corner came the curator.", "Обстоятельство + came + подлежащее."),
            err("Should you will need help, text the rota.", "Should you need help, text the rota.", "После should — bare infinitive, не will."),
            fill("Вставьте вспомогательный глагол: Not since the 1978 storm ___ the harbour wall been rebuilt. (have)", "has", "Not since + инверсия: has + subject."),
            mc("Выберите пропущенное слово: Had the samples ___ frozen, the assay would have failed.", ["not been", "been not", "not be"], "not been", "Had + subject + not been."),
        ],
    ),
    module(
        "fronting-emphasis",
        "Фронтирование и эмфаза",
        "Вынос дополнения, комплемента и обстоятельства влево; as for и контрастный топик.",
        22,
        "Сначала то, что важно услышать",
        lesson(
            "Fronting — вынос элемента из канонической позиции в начало, чтобы задать топик или контраст. Английский терпит это хуже, чем русский, поэтому фронтирование маркировано: звучит как сознательный жест. Дополнение, предикатив, обстоятельство и as for-группа готовят слушателя к комментарию. Иногда фронтирование вызывает инверсию (особенно с обстоятельством места и be / come / stand), иногда порядок подлежащее–глагол сохраняется.",
            [
                rule(
                    "Дополнение и предикатив влево",
                    "This clause I will not sign. Brilliant the talk was not. Такой вынос почти всегда контрастен: не то, а вот это. В речи удар падает на фронтированный кусок.",
                    [
                        ex("The footnotes I can live with; the missing corpus I cannot.", "Со сносками я смирюсь, с отсутствующим корпусом — нет."),
                        ex("Happy with the mix she was not.", "Довольна сведением она не была."),
                    ],
                ),
                rule(
                    "Обстоятельства и инверсия",
                    "In the top drawer lay the unsent postcard. Away ran the intern. Если глагол — be или непереходный глагол движения/положения, подлежащее часто уходит вправо. С местоимением инверсия обычно блокируется: Away he ran, не Away ran he.",
                    [
                        ex("On the blotting paper sat a ring of rust.", "На промокашке лежало ржавое кольцо."),
                        ex("Out of the fog loomed the north beacon.", "Из тумана выступил северный бакен."),
                    ],
                ),
                rule(
                    "As for / as to и топикальные рамки",
                    "As for the budget, we are still waiting. As to whether they will renew, nobody will say. Это рамка: сначала назвали тему, потом дали оценку. В академическом регистре также In the case of…, Regarding… — но as for разговорнее и резче.",
                    [
                        ex("As for the raw files, they never left the lab machine.", "Что касается сырых файлов, они так и не покинули лабораторный компьютер."),
                        ex("As to why the beam sagged, the inquiry is still open.", "Что до того, почему провисла балка, расследование ещё открыто."),
                    ],
                ),
            ],
            compare=[
                {"left": "I will not sign this clause.", "right": "This clause I will not sign.", "note": "Справа контраст с другими пунктами, которые, возможно, приемлемы."},
                {"left": "The postcard lay in the top drawer.", "right": "In the top drawer lay the postcard.", "note": "Справа сначала сцена, потом объект — типичный повествовательный кадр."},
            ],
            watch_out=[
                "Не фронтируйте всё подряд: приём работает, только если есть контраст или смена кадра.",
                "Away ran she — неестественно; с местоимением: Away she ran.",
            ],
            remember="Влево уходит топик или контраст. Место + be/come/stand часто инвертирует подлежащее. As for открывает рамку комментария.",
        ),
        [
            mc("___ the annex I have no objection.", ["As for", "For as", "As"], "As for", "As for + топик."),
            fill("___ of the tunnel poured the runoff. (out)", "Out", "Fronted adverb + inversion."),
            xf("Фронтируйте дополнение: I can accept the delay.", "The delay I can accept.", "Объект в начало."),
            err("Away ran they when the siren started.", "Away they ran when the siren started.", "Местоимение не инвертируется после away."),
            fill("Strange the decision ___, but it stood. (be / past)", "was", "Предикатив спереди, was остаётся."),
            mc("On the bench ___ the unused oars.", ["the crew left", "lay", "did lay"], "lay", "Обстоятельство места + lay + подлежащее."),
        ],
        [
            fill("Вставьте нужную форму (as): ___ to whether the lease renews, legal is silent. (as)", "As", "As to whether."),
            xf("Фронтируйте дополнение: I refuse to cut this paragraph.", "This paragraph I refuse to cut.", "Дополнение уходит влево без do и без it."),
            xf("Кадр: Three crates were behind the curtain.", "Behind the curtain were three crates.", "Место + were + подлежащее."),
            err("As for if they agree, we wait.", "As to whether they agree, we wait.", "После as to естественнее whether, не if в этой рамке.", ["As for whether they agree, we wait"]),
            fill("Вставьте форму to be: Tired she ___, she still recut the trailer. (be / past)", "was", "Предикатив Tired спереди."),
            mc("Выберите пропущенное слово: Into the inlet ___ the pilot skiff.", ["did slide", "slid", "slide"], "slid", "Полная инверсия движения: into… slid + NP."),
        ],
    ),
    module(
        "subjunctive-mandative",
        "Мандативный сослагательный",
        "Recommend / insist / it is essential that + (should) + базовая форма; were-subjunctive.",
        24,
        "That-клауза без согласования на -s",
        lesson(
            "Мандативный subjunctive выражает требование, рекомендацию или необходимость: после глаголов insist, demand, recommend, propose, request и после it is essential / vital / desirable that смысловой глагол стоит в базовой форме для всех лиц: that she leave, that the samples be sealed. Британский регистр часто вставляет should: that she should leave. Were-subjunctive обслуживает гипотезы: if he were, I wish I were. Это не «прошлое», а маркированная ирреальность.",
            [
                rule(
                    "Глаголы требования и рекомендаций",
                    "They insisted that the clause be struck. We recommend that he withdraw. Отрицание: that she not sign (без don't). В американском академическом стиле голая база частотнее; в британском — should + база.",
                    [
                        ex("The board demanded that the minutes be circulated the same day.", "Совет потребовал, чтобы протокол разослали в тот же день."),
                        ex("I suggest that she not present the unverified figures.", "Я предлагаю, чтобы она не представляла непроверенные цифры."),
                    ],
                ),
                rule(
                    "It is + adjective + that",
                    "It is essential / imperative / crucial / desirable that + subjunctive. It is important that тоже может брать subjunctive, но indicative (that he leaves) встречается и звучит как констатация, а не предписание.",
                    [
                        ex("It is vital that the backup remain offline.", "Крайне важно, чтобы резервная копия оставалась офлайн."),
                        ex("It is desirable that every witness be heard in private first.", "Желательно, чтобы каждого свидетеля сначала выслушали наедине."),
                    ],
                ),
                rule(
                    "Were-subjunctive и устойчивые формулы",
                    "If I were you, Were she to resign…, as it were. Формулы: Be that as it may, Suffice it to say, God save…, Far be it from me. Они застыли и не спрягаются.",
                    [
                        ex("Were the licence to lapse, the archive would close to visitors.", "Если бы лицензия истекла, архив закрыли бы для посетителей."),
                        ex("Be that as it may, the tide will not wait.", "Как бы то ни было, прилив ждать не будет."),
                    ],
                ),
            ],
            compare=[
                {"left": "She insisted that he was wrong.", "right": "She insisted that he be present.", "note": "Слева факт (indicative); справа требование (subjunctive)."},
                {"left": "It is essential that she is there. (факт/разг.)", "right": "It is essential that she be there.", "note": "Справа предписание; слева скорее констатация важности факта."},
            ],
            watch_out=[
                "That she leaves после demand в формальном предписании выглядит как сбой нормы C1.",
                "That she doesn't sign в мандативной клаузе заменяйте на that she not sign или that she should not sign.",
            ],
            remember="Предписание: that + базовая форма (или should + база) для всех лиц. Were — гипотеза. Не путайте с простой констатацией факта.",
        ),
        [
            mc("They recommended that the film ___ recut.", ["is", "be", "was"], "be", "Мандативный subjunctive: be для всех лиц."),
            fill("It is essential that he ___ the unredacted file. (see)", "see", "Базовая форма, не sees."),
            xf("Вставьте should (брит.): They demanded that she rewrite the abstract.", "They demanded that she should rewrite the abstract.", "Should + bare infinitive."),
            err("The chair insisted that the vote is postponed.", "The chair insisted that the vote be postponed.", "Требование, не констатация.", ["The chair insisted that the vote should be postponed"]),
            fill("I propose that we ___ not seal the crate yet. (do / subjunctive)", "not", "That we not seal — отрицание без don't.", ["do not"]),
            mc("If I ___ in your place, I would freeze the branch.", ["was", "were", "am"], "were", "Were-subjunctive."),
        ],
        [
            fill("Вставьте форму to be: It is crucial that the samples ___ labelled tonight. (be)", "be", "Be + V3 в пассиве."),
            mc("Выберите форму to be: Far ___ it from me to delay the launch.", ["is", "be", "was"], "be", "Формула Far be it from me."),
            xf("Перепишите требование через requested that + subjunctive: She must attend.", "They requested that she attend.", "That + базовая форма."),
            err("It is vital that she remains offline during the test. (предписание)", "It is vital that she remain offline during the test.", "Remain без -s."),
            fill("Вставьте предлог: Were she ___ resign, the deputy would step in. (to)", "to", "Were she to + infinitive."),
            mc("Выберите форму to be: He suggested that the paragraph ___ deleted.", ["is", "be", "being"], "be", "Suggest в значении рекомендации + subjunctive."),
        ],
    ),
    module(
        "impersonal-passive",
        "Безличный и личный пассив репортажа",
        "It is said that…, he is said to…, there is believed to be…",
        23,
        "Снять автора слуха с сцены",
        lesson(
            "Репортажный пассив отдаляет источник: важно содержание, а не кто сказал. Две главные схемы: безличная It is said / believed / rumoured / estimated that + клауза и личная Subject + is said / thought / reported + to-infinitive. Если после that есть there, возможен There is said to be…. Перфектный инфинитив относит репортируемое в прошлое. Это ядро академического и журнального регистра C1.",
            [
                rule(
                    "It + passive + that",
                    "It is widely assumed that the ferry will skip Tuesday. It has been suggested that the beam was underspecified. Подлежащее it не указывает на вещь — это синтаксическая заглушка.",
                    [
                        ex("It is rumoured that the foundry will close in March.", "Ходят слухи, что литейный цех закроют в марте."),
                        ex("It was estimated that the backlog would last six weeks.", "По оценкам, отставание растянулось бы на шесть недель."),
                    ],
                ),
                rule(
                    "Личный пассив + инфинитив",
                    "The foundry is rumoured to be closing in March. She is thought to have declined the prize. Выбирайте простой инфинитив для одновременности и to have + V3 для предшествования.",
                    [
                        ex("The skipper is said to distrust automatic pilots in fog.", "Говорят, шкипер не доверяет автопилоту в тумане."),
                        ex("Two crates are reported to have gone missing at the hub.", "Сообщают, что на узле пропали две клети."),
                    ],
                ),
                rule(
                    "There-схема и модальный оттенок",
                    "There is believed to be a second ledger. There are said to have been witnesses. Модальность можно встроить: She is rumoured to have been about to resign. Избегайте двойного that: She is said that she…",
                    [
                        ex("There is thought to be a sandbar just east of the marker.", "Считается, что сразу к востоку от знака есть коса."),
                        ex("There are said to have been three unlogged landings.", "Говорят, было три незафиксированные посадки."),
                    ],
                ),
            ],
            compare=[
                {"left": "People say the editor has resigned.", "right": "The editor is said to have resigned.", "note": "Личный пассив убирает people и ставит редактора темой."},
                {"left": "It is believed that there is a leak.", "right": "There is believed to be a leak.", "note": "Вторая схема короче и типичнее для сводок."},
            ],
            watch_out=[
                "He is said that he left — ошибка; либо It is said that he left, либо He is said to have left.",
                "They are rumoured they… — нужна связка to + infinitive.",
            ],
            remember="Либо it + that-клауза, либо подлежащее + to-infinitive. Прошлое репортируемого — to have + V3. There is said to be… для существования.",
        ),
        [
            mc("___ that the tide tables were misprinted.", ["The office is said", "It is said", "There is said"], "It is said", "Безличная схема с that."),
            fill("She is believed ___ have withdrawn the complaint. (to)", "to", "Личный пассив + перфектный инфинитив."),
            xf("Сверните: People think he lives aboard the barge.", "He is thought to live aboard the barge.", "Is thought + to-infinitive."),
            err("They are rumoured that they sold the quay.", "They are rumoured to have sold the quay.", "To have + V3, не that после личного пассива."),
            fill("There is said ___ be a spare impeller in the locker. (to)", "to", "There is said to be."),
            mc("The samples are reported ___ overnight.", ["to freeze", "to have been frozen", "freezing"], "to have been frozen", "Пассив уже совершён."),
        ],
        [
            fill("Вставьте вопросительное / относительное слово: It has been suggested ___ we split the consignment. (that)", "that", "It + passive + that."),
            mc("Выберите пропущенное слово: ___ are believed to have been two unlogged dives.", ["It", "There", "They"], "There", "There are believed to have been."),
            xf("Безлично: The foundry will close. (rumour, present)", "It is rumoured that the foundry will close.", "It is rumoured that…"),
            err("He is said he declined the knighthood.", "He is said to have declined the knighthood.", "To have + V3."),
            fill("Вставьте форму to be: The deputy is thought ___ acting chair until June. (be)", "to be", "Одновременная роль — простой инфинитив."),
            mc("Выберите модальный глагол (will/would): It was estimated that the repair ___ six weeks.", ["to last", "would last", "lasting"], "would last", "После that нужна полная клауза, не инфинитив."),
        ],
    ),
    module(
        "hedging-modality",
        "Хеджирование и эпистемическая модальность",
        "Seem, appear, tend, may well, it could be argued — как не утверждать жёстче данных.",
        25,
        "Оставлять зазор между фактом и выводом",
        lesson(
            "Хедж — языковой зазор, который отделяет утверждение от полной ответственности за него. На C1 это не «вода», а этика точности: seem / appear, tend to, may well, might conceivably, it could be argued, the data suggest rather than prove. Эпистемические модальные оценивают знание, не обязанность. Слишком много хеджей размывает тезис; слишком мало — выдаёт догадку за факт.",
            [
                rule(
                    "Seem / appear / tend и raising",
                    "She seems to have missed the briefing. There appears to be a second leak. Tend to описывает склонность, не единичный случай. Эти глаголы «поднимают» подлежащее из нижней клаузы: It seems that she missed → She seems to have missed.",
                    [
                        ex("The mix appears to have been bounced too hot.", "Похоже, сведение выгрузили со слишком горячим уровнем."),
                        ex("Early drafts tend to over-explain the method.", "Ранние черновики обычно слишком подробно объясняют метод."),
                    ],
                ),
                rule(
                    "Шкала may / might / could и усилители",
                    "May well = вполне возможно и даже правдоподобно. Might conceivably / could arguably — ещё осторожнее. Cannot easily be ruled out — академический ход. Should в хедже значит «по ожиданиям модели», не приказ.",
                    [
                        ex("The delay may well reflect a customs backlog rather than a shortage.", "Задержка вполне может отражать затор на таможне, а не нехватку."),
                        ex("The anomaly could arguably be an artefact of the sensor housing.", "Аномалию, пожалуй, можно счесть артефактом корпуса датчика."),
                    ],
                ),
                rule(
                    "Безличные рамки аргумента",
                    "It could be argued that…, One possible reading is…, The figures would appear to suggest… Would здесь не будущее, а дистанцирование. Избегайте I think в академическом абзаце, если можно поставить данные субъектом: The pattern suggests…",
                    [
                        ex("It might be objected that the sample is coastal-only.", "Могут возразить, что выборка исключительно прибрежная."),
                        ex("The logs would appear to contradict the verbal briefing.", "Журналы, судя по всему, противоречат устному брифингу."),
                    ],
                ),
            ],
            compare=[
                {"left": "The beam failed because of the washer.", "right": "The beam appears to have failed because of the washer.", "note": "Справа вывод помечен как интерпретация."},
                {"left": "This may be the cause.", "right": "This may well be the cause.", "note": "May well повышает правдоподобие, оставаясь хеджем."},
            ],
            watch_out=[
                "I think maybe it could possibly perhaps — стопка хеджей уничтожает тезис.",
                "Seem + that сразу после лица: She seems that she… — ошибка; нужно She seems to… или It seems that she…",
            ],
            remember="Сначала сила данных, потом сила модального. Seem/appear + to. May well — уверенный хедж. Рамки it could be argued держат дистанцию.",
        ),
        [
            mc("The crate ___ to have been resealed.", ["seems", "must need", "tends it"], "seems", "Seem + to have + V3."),
            fill("The delay may ___ be a roster clash. (well)", "well", "May well + infinitive."),
            xf("Поднимите подлежащее: It appears that they skipped the dry run.", "They appear to have skipped the dry run.", "Appear + to have + V3."),
            err("She seems that she distrusts the autopilot.", "She seems to distrust the autopilot.", "Seem + to-infinitive.", ["It seems that she distrusts the autopilot"]),
            fill("It could be ___ that the sample is biased. (argue)", "argued", "It could be argued that."),
            mc("Early cuts ___ to linger on establishing shots.", ["may well", "tend", "must"], "tend", "Tend to о склонности."),
        ],
        [
            fill("Вставьте нужную форму (appear): There ___ to be a second leak behind the lining. (appear)", "appears", "There appears to be."),
            mc("Выберите пропущенное слово: The figures would ___ to suggest a seasonal dip.", ["appear", "must", "tend that"], "appear", "Would appear to suggest — дистанцирование."),
            xf("Осторожнее: This is an artefact.", "This could be an artefact.", "Could хеджирует.", ["This might be an artefact", "This may be an artefact"]),
            err("The data prove maybe the washer failed.", "The data suggest the washer may have failed.", "Prove слишком силён при maybe; suggest + may have."),
            fill("Вставьте нужную форму (conceivably): He might ___ have missed the only marked channel. (conceivably)", "conceivably", "Might conceivably + have + V3."),
            mc("Выберите пропущенное слово: ___ possible reading is that the log was backfilled.", ["It", "One", "There"], "One", "One possible reading is…"),
        ],
    ),
    module(
        "nominalization",
        "Номинализация",
        "Как превратить процесс в имя и зачем это академическому абзацу.",
        22,
        "Глагол прячется в существительное",
        lesson(
            "Номинализация переводит процесс или качество в существительное: decide → decision, refuse → refusal, unstable → instability. Академический и канцелярский английский любит такие имена: они позволяют упаковать уже известное действие в топик и двигаться к оценке. Цена — тяжесть и размытые роли (кто сделал?). Хороший C1-текст чередует живой глагол и имя, а не заменяет все глаголы на of-цепочки.",
            [
                rule(
                    "От глагола и прилагательного к имени",
                    "Продуктивные суффиксы: -tion/-sion, -ment, -al, -ance/-ence, -ity, -ness. The committee decided X → The committee's decision to X. They refused to sign → their refusal to sign. Сохраняйте валентность: decision to / decision that / refusal of.",
                    [
                        ex("Their withdrawal from the tender surprised no one.", "Их отзыв заявки никого не удивил."),
                        ex("The instability of the emulsion ruined the last batch.", "Нестабильность эмульсии испортила последнюю партию."),
                    ],
                ),
                rule(
                    "Of-фразы, родительный и скрытый агенс",
                    "The destruction of the samples (кем?) можно раскрыть: the technicians' destruction of the samples / destruction of the samples by the technicians. Если агенс важен для ответственности, не прячьте его. Цепочки of of of — сигнал переписать глаголами.",
                    [
                        ex("The postponement of the launch by the harbour master angered the skippers.", "Отсрочка выхода гаванским капитаном разозлила шкиперов."),
                        ex("Her insistence on a paper trail delayed the payment.", "Её настойчивость относительно бумажного следа задержала платёж."),
                    ],
                ),
                rule(
                    "Когда лучше оставить глагол",
                    "Инструкции, рассказ, живой абзац выигрывают от finite verb: We sealed the hatch. Номинализация уместна, когда процесс уже введён и становится темой следующего предложения: This sealing, however, trapped moisture.",
                    [
                        ex("We measured the sag twice. This measurement later became Exhibit C.", "Мы дважды измерили провис. Это измерение позже стало приложением C."),
                        ex("Do not write: the undertaking of an inspection of the hull by the surveyor — write The surveyor inspected the hull.", "Канцелярит лучше разжать."),
                    ],
                ),
            ],
            compare=[
                {"left": "They decided to freeze the branch.", "right": "Their decision to freeze the branch…", "note": "Справа решение уже может стать подлежащим следующего хода."},
                {"left": "Because the emulsion was unstable, the batch failed.", "right": "Emulsion instability caused the batch to fail.", "note": "Имя короче, но теряется оттенок because."},
            ],
            watch_out=[
                "The doing of the making of — пустая номинализация. Если нет нового смыслового узла, верните глагол.",
                "Не забывайте артикли и число: a decision, two refusals; information без a.",
            ],
            remember="Имя упаковывает процесс в топик. Верните агенса, если важна ответственность. Чередуйте с живыми глаголами.",
        ),
        [
            mc("They withdrew → their ___ from the tender.", ["withdraw", "withdrawal", "withdrawingness"], "withdrawal", "Withdraw → withdrawal."),
            fill("The committee's ___ to postpone angered the crew. (decide)", "decision", "Decision to + infinitive."),
            xf("Номинализуйте: They refused to sign the clause.", "their refusal to sign the clause", "Refusal to + infinitive."),
            err("The inspecting of the hull by the surveyor was done.", "The surveyor inspected the hull.", "Пустую номинализацию разжимаем в глагол."),
            fill("___ of the samples by heat made the assay useless. (destroy)", "Destruction", "Destruction of + by-агенс."),
            mc("Unstable → ___ of the emulsion", ["unstability", "instability", "unstablement"], "instability", "Unstable → instability."),
        ],
        [
            fill("Вставьте нужную форму (insist): Her ___ on a paper trail delayed payment. (insist)", "insistence", "Insistence on."),
            mc("Which is the lightest academic rewrite of We measured the sag?", ["The undertaking of a measurement of the sag was performed by us.", "This measurement of the sag…", "The being measured of the sag…"], "This measurement of the sag…", "Короткое имя как топик, без канцелярита."),
            xf("Имя: They postponed the launch.", "the postponement of the launch", "Postponement of."),
            err("Informations about the leak were scarce.", "Information about the leak was scarce.", "Information неисчисляемое."),
            fill("Вставьте нужную форму (fail): They failed to notify us → their ___ to notify us. (fail)", "failure", "Failure to."),
            mc("Choose the version that keeps the agent clear.", ["the destruction of the samples", "the technicians' destruction of the samples", "destruction occurring"], "the technicians' destruction of the samples", "Родительный называет агенса."),
        ],
    ),
    module(
        "ellipsis-substitution",
        "Эллипсис и замена",
        "So / neither, do so, one / ones, усечённые ответы и сравнительные пропуски.",
        21,
        "Не повторять то, что уже в воздухе",
        lesson(
            "Связный английский постоянно что-то опускает (ellipsis) или заменяет местоимением / do so / so / neither (substitution). Это не небрежность, а грамматика данного: повтор полной группы звучит тяжело и иногда меняет смысл. C1 требует контролировать, какой кусок восстановления однозначен. Если восстановление двоится — эллипсис запрещён.",
            [
                rule(
                    "So / neither / nor и краткие согласия",
                    "So do I, So have they, Neither was the deputy. Порядок: so / neither + вспомогательный + подлежащее. Если вспомогательных нет в исходной реплике, берём do/does/did. Too / either — без инверсии: I do too, I don't either.",
                    [
                        ex("The skipper distrusts the autopilot. — So does the pilot.", "Шкипер не доверяет автопилоту. — И лоцман тоже."),
                        ex("I haven't logged the dive. — Neither have I.", "Я не занёс погружение в журнал. — И я тоже."),
                    ],
                ),
                rule(
                    "Do so и one / ones",
                    "Do so заменяет всё сказуемое целиком, часто формально: Those who wish to object may do so in writing. One / ones заменяет исчисляемое существительное: the green one, the ones on the top shelf. So может заменять that-клаузу после believe / expect / say: I expect so.",
                    [
                        ex("If you need to override the lock, do so before dusk.", "Если нужно обойти замок, сделайте это до сумерек."),
                        ex("Pass me the cracked jar, not the sealed ones.", "Передай треснувшую банку, не запечатанные."),
                    ],
                ),
                rule(
                    "Сравнительный и ответный эллипсис",
                    "She edits faster than he does / than him (разг.). They left, and we did too. В сравнительных нельзя опускать так, чтобы подлежащее слилось: She likes the intern more than the editor — двусмысленно (больше, чем редактор любит / больше, чем любит редактора). Тогда оставьте глагол.",
                    [
                        ex("The afternoon tide ran higher than the morning tide did.", "Дневной прилив был выше, чем утренний."),
                        ex("A: Will they renew? B: I should think so.", "— Они продлят? — Думаю, да."),
                    ],
                ),
            ],
            compare=[
                {"left": "I need a spare impeller. — I need a spare impeller too.", "right": "I need a spare impeller. — So do I.", "note": "Справа стандартное согласие без полного повтора."},
                {"left": "She likes the intern more than the editor.", "right": "She likes the intern more than the editor does.", "note": "Справа ясно: сравнение субъектов, не объектов."},
            ],
            watch_out=[
                "So I do — эмфатическое подтверждение («и правда»), не согласие «я тоже». Для «я тоже» — So do I.",
                "Do so плохо заменяет be и have в значении обладания; там нужен другой вспомогательный.",
            ],
            remember="So / neither + вспомогательный + подлежащее. Do so = всё действие. One — исчисляемый повтор. Если смысл двоится, верните глагол.",
        ),
        [
            mc("The deputy hasn't signed. — ___ the chair.", ["So hasn't", "Neither has", "Neither hasn't"], "Neither has", "Neither + has + подлежащее."),
            fill("Those who wish to object may ___ so in writing. (do)", "do", "Do so."),
            xf("Согласие: I distrust automatic backups. (she)", "So does she.", "So + does + she."),
            err("Pass me the green. I don't want the red one glass.", "Pass me the green one. I don't want the red one.", "One замещает glass/исчисляемое."),
            fill("A: Are they docking tonight? B: I expect ___.", "so", "So замещает that-клаузу."),
            mc("She photographs the quay more than ___. (сравнить субъектов)", ["the intern", "the intern does", "intern"], "the intern does", "Глагол снимает двусмысленность."),
        ],
        [
            fill("Вставьте quantifier (some/any/much…): I can't read the log. — ___ can the intern.", "Neither", "Neither can + subject."),
            mc("Выберите вспомогательный глагол: So ___ I — если исходная фраза They have finished.", ["do", "have", "did"], "have", "Повторяем have."),
            xf("Замените повтор: She sealed the jars, and I sealed the jars too.", "She sealed the jars, and I did too.", "Did too."),
            err("So I do need a spare — в значении «я тоже».", "So do I need a spare.", "Для «тоже» инверсия: So do I.", ["So do I."]),
            fill("Вставьте пропущенное слово: Keep the dry plates; recycle the warped ___.", "ones", "Ones = plates."),
            mc("Выберите пропущенное слово: He said he would override the lock, and he ___.", ["did so", "so did", "did it so"], "did so", "Do so замещает override the lock."),
        ],
    ),
    module(
        "advanced-conditionals",
        "Продвинутые условные",
        "Provided, as long as, but for, were it not for, inverted if и even if.",
        27,
        "Условие без простого if",
        lesson(
            "C1 расширяет условные союзным аппаратом и инверсией. Provided (that) / providing, as long as, on condition that задают ограничение-разрешение. Unless — единственное препятствие, не простой синоним if not во всех контекстах. But for + noun и were it not for вводят единственный спасительный или губительный фактор. Even if не равняется even though: первое гипотетично, второе — уступительный факт.",
            [
                rule(
                    "Provided, as long as, on condition that, unless",
                    "You may board provided your pass is dated today. As long as подчёркивает длящееся условие. Unless = if not, но плохо стыкуется с would в вежливом предложении и с already-true фактами, где нужен if… not.",
                    [
                        ex("We will release the cut provided that legal signs off by noon.", "Мы выпустим монтаж при условии, что юристы завизируют до полудня."),
                        ex("The drone can fly as long as the wind stays below twelve knots.", "Дрон может лететь, пока ветер ниже двенадцати узлов."),
                    ],
                ),
                rule(
                    "But for, if it weren't / hadn't been for, инверсия",
                    "But for the sandbar, we would have gone aground. If it hadn't been for her note, we would have shipped the wrong crate. Were it not for / Had it not been for — формальные двойники. Should / were / had без if см. также inversion-full.",
                    [
                        ex("But for a jammed pulley, the sail would have come down cleanly.", "Если бы не заклинивший блок, парус лег бы чисто."),
                        ex("Had it not been for the spare gasket, the pump would have thrown oil.", "Если бы не запасная прокладка, насос выбросил бы масло."),
                    ],
                ),
                rule(
                    "Even if, even though, given that, suppose",
                    "Even if the fog lifts, we will not cross — условие может быть ложным. Even though the fog has lifted, we will not cross — факт. Given that вводит данность как основание. Suppose / supposing открывает мысленный эксперимент.",
                    [
                        ex("Even if the client waives the fee, the clause stays.", "Даже если клиент откажется от сбора, пункт останется."),
                        ex("Given that the tide turns at 16:10, we should be off the wall by 15:40.", "Учитывая, что прилив сменится в 16:10, нам сойти со стенки к 15:40."),
                    ],
                ),
            ],
            compare=[
                {"left": "If you don't have a pass, you can't board.", "right": "Unless you have a pass, you can't board.", "note": "Здесь unless уместен: нет пропуска — единственный блокер."},
                {"left": "Even if it rains, the market stays open.", "right": "Even though it is raining, the market is open.", "note": "If — гипотеза; though — уже идёт дождь."},
            ],
            watch_out=[
                "Unless you wouldn't mind — калька; для вежливости If you wouldn't mind.",
                "But for + клауза (But for we left) невозможно; после but for только именная группа.",
            ],
            remember="Provided / as long as = разрешение под условием. But for + имя = единственный фактор. Even if ≠ even though. Unless не универсальный if not.",
        ),
        [
            mc("You may use the loft ___ you lock the hatch.", ["unless", "provided", "but for"], "provided", "Provided вводит условие-разрешение."),
            fill("___ for the spare impeller, we would have drifted. (but)", "But", "But for + NP."),
            xf("Инверсия: If it had not been for her note, we would have shipped the wrong crate.", "Had it not been for her note, we would have shipped the wrong crate.", "Had it not been for."),
            err("Even though the fog lifts tomorrow, we will not cross. (гипотеза)", "Even if the fog lifts tomorrow, we will not cross.", "Tomorrow + гипотеза = even if."),
            fill("The drone can fly ___ long as gusts stay moderate.", "as", "As long as."),
            mc("___ that the beam already sagged, a second load is unwise.", ["Provided", "Given", "Unless"], "Given", "Given that = данность."),
        ],
        [
            fill("Вставьте нужную форму (unless): ___ you hold a dated pass, you cannot board. (unless)", "Unless", "Unless + положительное условие."),
            mc("Выберите since или for: Were it not ___ the sandbar, the channel would be obvious.", ["for", "to", "that"], "for", "Were it not for."),
            xf("Факт-уступка: It is raining, but the market is open.", "Even though it is raining, the market is open.", "Even though + факт."),
            err("But for we had a spare gasket, the pump failed.", "But for a spare gasket, the pump would have failed.", "But for + NP и условный результат.", ["Had it not been for a spare gasket, the pump would have failed"]),
            fill("Вставьте предлог: We will film on the wall ___ condition that the wind drops. (on)", "on", "On condition that."),
            fill("Вставьте нужную форму (fail / open plan): Suppose the generator ___ — which bank do we switch to? (fail / open plan)", "fails", "Открытый рабочий сценарий: suppose + Present Simple."),
        ],
    ),
    module(
        "complex-noun-phrases",
        "Сложные именные группы",
        "Пре- и постмодификация, причастия, of-цепочки и относительные «хвосты».",
        24,
        "Как собрать тяжёлое подлежащее и не потерять глагол",
        lesson(
            "Академическое подлежащее на C1 редко бывает голым существительным. Его собирают из детерминатива, премодификаторов (прилагательные, существительные-классификаторы, причастия) и постмодификаторов (of-фразы, предложные группы, относительные и инфинитивные обороты). Главный навык — видеть голову группы и не согласовывать глагол с ближайшим существительным справа. Второй навык — не строить цепочку, которую читатель не может разобрать с одного раза.",
            [
                rule(
                    "Премодификация и классификаторы",
                    "Порядок ближе к голове всё конкретнее: those three damaged harbour-wall floodlights. Существительное-классификатор обычно в единственном: a tide table, не tides table, если это не устоявшееся множественное (a goods train). Дефисы помогают: a well-argued objection.",
                    [
                        ex("The two remaining salt-stained canvas covers were useless.", "Два оставшихся просоленных парусиновых чехла были бесполезны."),
                        ex("A last-minute legal objection froze the release.", "Возражение юристов в последнюю минуту заморозило выпуск."),
                    ],
                ),
                rule(
                    "Постмодификация: of, причастие, инфинитив, relative",
                    "The decision of the harbour master to delay the sailing that had already been announced… Голова — decision. Причастие справа: the samples stored in aisle C. Инфинитив: the need to relabel every jar. Relative: the need which legal flagged.",
                    [
                        ex("The refusal of the foundry to honour the last invoice delayed the parts.", "Отказ литейки оплатить последний счёт задержал детали."),
                        ex("Anyone hoping to board after dusk must radio the wall.", "Любой, кто надеется сесть на борт после сумерек, должен вызвать стенку по рации."),
                    ],
                ),
                rule(
                    "Согласование и читаемость",
                    "The quality of the recordings is… — глагол к quality, не recordings. Если постмодификаторов больше трёх, разбейте на два предложения или вынесите of-группу в which-клаузу. Одна именная группа — одна коммуникативная задача.",
                    [
                        ex("The accuracy of the tide tables issued in March is now in doubt.", "Точность мартовских таблиц приливов теперь под вопросом."),
                        ex("Better: The March tide tables are inaccurate. Their errors delayed two crossings.", "Два коротких предложения яснее одной перегруженной группы."),
                    ],
                ),
            ],
            compare=[
                {"left": "the damaged floodlights on the harbour wall", "right": "the harbour-wall floodlights that were damaged", "note": "Слева сначала состояние, потом место; справа класс, потом relative."},
                {"left": "The results of the tests were leaked.", "right": "The results of the tests was leaked.", "note": "Голова results — множественное; was — ошибка согласования."},
            ],
            watch_out=[
                "Согласование с ближайшим существительным (proximity error): The set of plates were… — нужно was, если голова set.",
                "a documents archive — классификатор обычно без -s: a document archive.",
            ],
            remember="Найдите голову группы — к ней глагол. Премодификаторы уточняют класс; постмодификаторы добавляют отношения. Тяжесть больше трёх хвостов — делите.",
        ),
        [
            mc("The quality of the recordings ___ impressive.", ["are", "is", "be"], "is", "Голова quality — единственное число."),
            fill("A ___ table hung by the radio. (tide)", "tide", "Классификатор в единственном числе."),
            xf("Соберите группу: two / remaining / covers / canvas / salt-stained", "two remaining salt-stained canvas covers", "Числительное → причастие состояния → материал → голова."),
            err("The set of wet plates were stacked too soon.", "The set of wet plates was stacked too soon.", "Голова set."),
            fill("Anyone ___ to board after dusk must radio. (hope)", "hoping", "Постмодификация V-ing."),
            mc("Choose the more readable pair.", ["the decision of the harbour master to delay the already announced sailing of the evening freight ferry", "The harbour master delayed the evening freight ferry. The sailing had already been announced."], "The harbour master delayed the evening freight ferry. The sailing had already been announced.", "Два предложения яснее перегруженной NP."),
        ],
        [
            fill("Вставьте предлог: The refusal of the foundry ___ honour the invoice delayed parts. (to)", "to", "Refusal to + infinitive."),
            mc("Выберите пропущенное слово: those three ___ objections", ["well argued", "well-argued", "well-argue"], "well-argued", "Дефис у составного премодификатора."),
            xf("Голова + relative: the need / legal flagged the need", "the need which legal flagged", "Need + which-клауза.", ["the need that legal flagged"]),
            err("A documents archive sat in the loft.", "A document archive sat in the loft.", "Классификатор без -s."),
            fill("Вставьте форму to be: The accuracy of the tables issued in March ___ now in doubt. (be)", "is", "Голова accuracy."),
            mc("Выберите форму пассива: the samples ___ in aisle C", ["storing", "stored", "store"], "stored", "Пассивный постмодификатор."),
        ],
    ),
    module(
        "reporting-verb-patterns",
        "Модели глаголов передачи речи",
        "Accuse of, warn against, insist on, threaten to, suggest that / -ing — валентность репортажа.",
        26,
        "Какой глагол какую конструкцию требует",
        lesson(
            "Глаголы передачи речи на C1 различаются не только смыслом (упрёк, угроза, совет), но и обязательным дополнением. Accuse somebody of -ing, congratulate somebody on -ing, warn somebody against -ing / not to, threaten to, refuse to, insist on -ing / that, suggest -ing / that (но не suggest somebody to). Ошибка почти всегда в предлоге или в лишнем to. Учите глагол пакетом с моделью, не изолированным переводом.",
            [
                rule(
                    "Предлог + -ing",
                    "Accuse of, suspect of, criticise for, praise for, apologise for, congratulate on, insist on, warn against, dream of, prevent somebody from. Герундий называет чужое или своё действие как факт-событие.",
                    [
                        ex("They accused the intern of leaking the stills.", "Они обвинили интерна в сливе кадров."),
                        ex("She apologised for having frozen the wrong branch.", "Она извинилась за то, что заморозила не ту ветку."),
                    ],
                ),
                rule(
                    "To-infinitive и that-клауза",
                    "Threaten, refuse, promise, offer, claim + to. Remind / warn somebody to. Insist / suggest / recommend / demand + that (+ subjunctive / should). Suggest -ing возможно без адресата: She suggested postponing.",
                    [
                        ex("The contractor threatened to halt the pour.", "Подрядчик пригрозил остановить заливку."),
                        ex("He reminded us to log the dive before changing tanks.", "Он напомнил занести погружение в журнал до смены баллонов."),
                    ],
                ),
                rule(
                    "Типичные ловушки",
                    "Suggest somebody to do — калька. Explain somebody the problem — нужно explain the problem to somebody. Tell vs say: tell somebody that; say that / say to somebody. Blame somebody for; blame something on somebody.",
                    [
                        ex("Legal suggested postponing the release, not *suggested us to postpone.", "Suggest + -ing или that, не объект + to."),
                        ex("She explained the sag to the surveyor.", "Explain something to somebody."),
                    ],
                ),
            ],
            compare=[
                {"left": "She suggested that we postpone.", "right": "She suggested postponing.", "note": "Оба верны; нет адресата-объекта перед to."},
                {"left": "He warned us not to cross.", "right": "He warned us against crossing.", "note": "To и against -ing близки; against чаще о линии поведения."},
            ],
            watch_out=[
                "Suggest her to wait, recommend him to — в стандарте C1 заменяются that / -ing.",
                "Insist to do — ошибка; insist on doing / insist that.",
            ],
            remember="Учите пакет: глагол + предлог + форма. Suggest/recommend без somebody to. Explain something to somebody.",
        ),
        [
            mc("They accused her ___ leaking the stills.", ["to", "of", "for"], "of", "Accuse of -ing."),
            fill("The contractor threatened ___ halt the pour. (to)", "to", "Threaten to."),
            xf("Suggest без that: She said we should postpone the release.", "She suggested postponing the release.", "Suggest + -ing."),
            err("He suggested us to radio the wall.", "He suggested that we radio the wall.", "Не suggest somebody to.", ["He suggested radioing the wall"]),
            fill("She congratulated the intern ___ spotting the mismatch. (on)", "on", "Congratulate on."),
            mc("I insist ___ seeing the unredacted file.", ["to", "on", "for"], "on", "Insist on -ing."),
        ],
        [
            fill("Вставьте нужную форму (against): He warned us ___ crossing after dusk. (against)", "against", "Warn against -ing."),
            mc("Выберите пропущенное слово: She explained ___ the surveyor.", ["the sag to", "to the sag", "the surveyor the sag"], "the sag to", "Explain something to somebody — в опции «the sag to»."),
            xf("Перепишите с blame … on …: They said the washer caused the failure.", "They blamed the failure on the washer.", "Blame something on somebody/something."),
            err("Legal recommended him to freeze the branch.", "Legal recommended that he freeze the branch.", "Recommend + that + subjunctive.", ["Legal recommended freezing the branch"]),
            fill("Вставьте предлог: She refused ___ countersign the minutes. (to)", "to", "Refuse to."),
            mc("Выберите пропущенное слово: He reminded us ___ the dive before changing tanks.", ["logging", "to log", "of log"], "to log", "Remind somebody to do."),
        ],
    ),
]
