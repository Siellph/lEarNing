"""Enriched C2 grammar theory (Russian explanations, English examples).

Tone: impersonal / descriptive Russian. No direct address to the learner.
"""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

C2_THEORY = {
    "information-structure": lesson(
        "На C2 грамматика подчиняется **упаковке информации**. Английский предпочитает ставить данное ближе к началу, а новое, тяжёлое и фокусное — к концу (**end-focus**, **end-weight**).\n\nТема не всегда равна подлежащему: её задают there-конструкцией, it-выносом, пассивом или клефтом. Формально верное предложение «звучит криво», если тяжёлая группа стоит слишком рано.",
        [
            rule(
                "Данное → новое",
                "После введения объект стремится влево: The gasket had perished. This failure threw oil… Новое и контрастное любит финальную позицию. Короткое данное + тяжёлое новое читается легче, чем наоборот.",
                [
                    ex("A spare impeller sat in the locker. That impeller later saved the crossing.", "Сначала введение, затем данное impeller в теме."),
                    ex("The inquiry blamed not the steel grade but a missing washer.", "Контрастный фокус уходит в конец."),
                    ex("The unsent postcard was found in the top drawer, not the archive box.", "Тема — открытка; пассив держит её слева."),
                ],
                tables=[
                    table(
                        ["Задача", "Схема", "Эффект"],
                        [
                            ["ввести существование", "There is / remains…", "новое справа"],
                            ["вынести тяжёлую клаузу", "It + V + that / to…", "end-weight"],
                            ["тема = пациенс", "пассив", "данное влево"],
                            ["контрастный фокус", "it-cleft / wh-cleft", "фокусное окно"],
                        ],
                    ),
                ],
            ),
            rule(
                "End-weight",
                "It is essential to relabel every jar that left aisle C… — it держит заглушку, пока тяжёлый инфинитив идёт в конец. There is a sandbar… вводит новое существование.",
                [
                    ex("It surprised no one that the foundry withdrew from the tender.", "That-клауза тяжелее; её выносят вправо."),
                    ex("There remains a second ledger whose entries were never cross-checked.", "There открывает сцену; ledger — новое."),
                ],
                pairs=[
                    pair("That the foundry withdrew surprised no one.", "It surprised no one that the foundry withdrew.", "Справа вес распределён по-английски."),
                    pair("Is a sandbar just east of the marker.", "There is a sandbar just east of the marker.", "Первое введение — there."),
                ],
            ),
            rule(
                "Выбор схемы под тему",
                "Если тема — пациенс, пассив естественен. Если тема — существование, there. Если нужно удержать оценку при длинном источнике: It is rumoured that… Ломать схему только ради контраста.",
                [
                    ex("It was the intern, not the editor, who froze the wrong branch.", "Клефт ставит контраст в фокусное окно."),
                    ex("It is essential to relabel every jar that left aisle C before Thursday's assay.", "It снимает тяжёлый инфинитив с позиции подлежащего."),
                ],
                callouts=[
                    callout("Перед правкой два вопроса: что уже известно и что должно оказаться в конце фразы?", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "That the foundry withdrew surprised no one.", "right": "It surprised no one that the foundry withdrew.", "note": "Справа end-weight."},
            {"left": "A sandbar is just east of the marker.", "right": "There is a sandbar just east of the marker.", "note": "There типичнее для первого введения."},
        ],
        watch_out=[
            "Абзац с that-клаузы-подлежащего без нужды тяжелит чтение.",
            "Пассив ради пассива сбивает агенса.",
        ],
        remember="Данное влево, новое и тяжёлое вправо. There — существование, it — вынос, пассив и клефт — переназначение темы.",
    ),
    "aspect-contrasts": lesson(
        "На C2 выбор аспекта редко диктуется «правилом учебника» в чистом виде: говорящий комментирует, **как** видит ситуацию — как целостную, развёрнутую, релевантную к точке или как ограниченный отрезок.\n\nProgressive может сделать статив временным. Perfect связывает событие с более поздней точкой. Would и used to расходятся по состоянию vs действию.",
        [
            rule(
                "Simple против Progressive",
                "She edits documentaries — устойчивая роль. She is editing a piece on the harbour — ограниченный проект. You are always leaving mugs… — эмоциональная оценка повтора, не расписание.",
                [
                    ex("He stands on ceremony with funders, but tonight he is standing them a drink.", "Привычная сдержанность vs разовое поведение."),
                    ex("The emulsion is smelling odd this morning — we should stop the batch.", "Временный признак, не словарный статив smell."),
                    ex("She is editing a piece on the harbour this month.", "Ограниченный проект — Progressive."),
                ],
                tables=[
                    table(
                        ["Выбор", "Сигнал", "Комментарий"],
                        [
                            ["Simple", "роль / факт / привычка", "целостный взгляд"],
                            ["Progressive", "временный отрезок / эмоция", "ограничение или окраска"],
                            ["Perfect", "связь с точкой later/now", "не просто «раньше»"],
                            ["used to", "закрытое прошлое + состояние/действие", "больше нет"],
                            ["would (habit)", "повтор действий в нарративе", "не состояния"],
                            ["habitual will", "типичное поведение сейчас", "не будущее"],
                        ],
                    ),
                ],
            ),
            rule(
                "Perfect: релевантность",
                "Have done помечает результат, опыт или «до сейчас». Past Simple закрывает эпизод в его времени. Progressive perfect — длительность или раздражающий повтор до точки.",
                [
                    ex("She has declined three fellowships, so the rumour is stale.", "Серия отказов объясняет нынешний слух."),
                    ex("She declined the 2019 fellowship and took the foundry job.", "Закрытый биографический кадр."),
                    ex("I have been chasing that invoice all week.", "Длительность до сейчас."),
                ],
                pairs=[
                    pair("I have had the lock changed last May.", "I had the lock changed last May.", "Дата last May закрывает эпизод."),
                    pair("I would own a barge in those days.", "I used to own a barge in those days.", "Владение — состояние, used to."),
                ],
            ),
            rule(
                "Used to, would и habitual will",
                "Used to закрывает действия и состояния. Would — только повтор действий в уже заданном мире. Habitual will: She will leave mugs on the scanner — типичное поведение, часто с укором.",
                [
                    ex("The quay used to belong to the foundry; every Friday the siren would mark the pour.", "Состояние — used to; повтор действия — would."),
                    ex("He will insist on a paper trail, even for a two-line email.", "Типичная привычка, не план."),
                ],
                callouts=[
                    callout("Present Perfect + точная законченная дата прошлого (in 2019) в стандарте ломает связь с now.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "I lived in Cork for a year.", "right": "I have lived in Cork, so the accent doesn't throw me.", "note": "Закрытый отрезок vs опыт как нынешний ресурс."},
            {"left": "She always leaves mugs on the scanner.", "right": "She is always leaving mugs on the scanner.", "note": "Continuous добавляет раздражение."},
        ],
        watch_out=[
            "Would know / would own в привычном прошлом — ошибка.",
            "Perfect + закрывающая дата.",
        ],
        remember="Аспект — ракурс. Progressive ограничивает или окрашивает. Perfect держит связь с точкой. Would не обслуживает прошлые состояния.",
    ),
    "register-metaphor": lesson(
        "C2 требует не только «правильной» формы, но и формы, **уместной в ситуации**. Регистр — согласование грамматики, лексики и метафоры с аудиторией.\n\nАкадемический английский полон стёртых метафор; живая авторская метафора должна быть контролируемой.",
        [
            rule(
                "Грамматические маркеры регистра",
                "Формально: shall в правилах, were-subjunctive, инверсия, номинализации, whom после предлога, in the event that. Разговорно: going to, got to, эллипсис подлежащего. Смешение в одном абзаце выдаёт сбой контроля.",
                [
                    ex("In the event of generator failure, switch to the battery bank.", "Канцелярия инструкции: in the event of + имя."),
                    ex("If the generator dies, just flip to the batteries.", "Тот же смысл в устной смене."),
                ],
                tables=[
                    table(
                        ["Формальнее", "Разговорнее", "Зона"],
                        [
                            ["obtain / enquire", "get / ask", "лексика"],
                            ["commence / terminate", "start / kill (жаргон)", "протокол vs смена"],
                            ["prior to", "before", "время"],
                            ["sufficient", "enough", "мера"],
                            ["be-passive", "get-passive", "залог"],
                            ["whom after prep", "who / that", "относительные"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Hereby I gonna freeze the branch.", "I hereby freeze the branch.", "Hereby не стыкуется с gonna."),
                    pair("A number of several crates went missing.", "A number of crates went missing.", "Не складывать a number of и several."),
                ],
            ),
            rule(
                "Лексико-грамматические пары",
                "Не «чем длиннее, тем лучше»: sufficient в протоколе уместен, в реплике коллеге — холоден. Get-passive разговорнее be-passive.",
                [
                    ex("The assay commenced at 06:40 and was terminated at 07:15.", "Протокол любит commence / terminate."),
                    ex("We started the assay at twenty to seven and killed it at quarter past.", "Лабораторный жаргон смены."),
                    ex("We couldn't get a spare impeller.", "Разговорный близнец we were unable to obtain…"),
                ],
            ),
            rule(
                "Метафора как связка",
                "Стёртые метафоры безопасны: raise a question, fall outside the scope. Смешение доменов в одном предложении создаёт катахрезу. Авторская метафора работает, если проведена через абзац.",
                [
                    ex("The claim does not survive contact with the tide tables.", "Один домен, стёртый жест."),
                    ex("Avoid: The skeleton of the chapter then sailed into a fog of numbers and baked the reader.", "Три домена сразу ломают тон."),
                ],
                callouts=[
                    callout("Сначала аудитория, потом форма. Одна метафорическая линия на абзац.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "We were unable to obtain a spare impeller.", "right": "We couldn't get a spare impeller.", "note": "Одинаковая пропозиция; слева отчёт, справа смена."},
            {"left": "The stills got leaked.", "right": "The stills were leaked.", "note": "Get-passive разговорнее."},
        ],
        watch_out=[
            "Hereby + gonna — внутриабзацный слом регистра.",
            "Живая метафора без продолжения выглядит случайной.",
        ],
        remember="Сначала аудитория, потом форма. Пары obtain/get — не синонимы по тону. Одна метафорическая линия на абзац.",
    ),
    "advanced-cohesion": lesson(
        "**Связность (cohesion)** — видимые нити между предложениями: местоимения, лексические цепочки, эллипсис, коннекторы. **Coherence** — логика, которую нити обслуживают.\n\nОшибка C2 часто не в союзе, а в разрыве референциальной цепи: this указывает в пустоту, moreover стоит там, где нужен contrast.",
        [
            rule(
                "Референция и лексические цепочки",
                "The gasket → this part → the failed component → it. This + noun надёжнее голого this, если антецедент — целая ситуация. Не открывать the inquiry, если inquiry ещё не введена.",
                [
                    ex("A washer was missing. This omission, not the steel grade, explained the sag.", "This + noun пакует предыдущее предложение в тему."),
                    ex("Fog delayed the crossing. The weather also ruined the drone flight.", "The weather — гипероним к fog."),
                ],
                tables=[
                    table(
                        ["Средство", "Роль", "Риск"],
                        [
                            ["the + N", "данное уже в дискурсе", "the без введения"],
                            ["this + N", "упаковать ситуацию", "голый this при двух антецедентах"],
                            ["гипероним", "подняться по цепочке", "слишком широкий скачок"],
                            ["however / therefore", "коннектор между предложениями", "как союз без точки/;"],
                            ["but / so", "союз клауз", "перепутать с коннектором"],
                        ],
                    ),
                ],
            ),
            rule(
                "Коннекторы и союзы",
                "However / nevertheless — уступка между предложениями. Therefore / thus — вывод. In contrast — противопоставление. However не заменяет союз между двумя finite-клаузами без точки или точки с запятой.",
                [
                    ex("The tables were reprinted; however, two crossings had already failed.", "However после точки с запятой — коннектор."),
                    ex("The tables were reprinted, but two crossings had already failed.", "But соединяет клаузы напрямую."),
                ],
                pairs=[
                    pair("The tables were reprinted, however two crossings failed.", "The tables were reprinted; however, two crossings failed.", "However не союз между finite-клаузами."),
                    pair("The inquiry concluded the washer failed. (не введена)", "An inquiry concluded the washer failed.", "Первое упоминание — a/an."),
                ],
            ),
            rule(
                "Абзацный эллипсис и повтор",
                "Повтор головы группы может быть ритмом инструкции. В анализе предпочтительнее варьировать. Эллипсис глагольной группы рискован при смене полярности без опоры.",
                [
                    ex("Legal flagged the clause. Editorial flagged it too.", "It держит clause; too закрывает параллель."),
                    ex("We could have waited for slack water. We did not.", "Вторая клауза восстанавливает wait однозначно."),
                ],
                callouts=[
                    callout("Moreover в контрасте и however в простом добавлении — сбой логической метки, не «стиль».", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "The tables were reprinted, however two crossings failed.", "right": "The tables were reprinted; however, two crossings failed.", "note": "Коннектор требует точки / точки с запятой."},
            {"left": "Fog delayed us. This was annoying.", "right": "Fog delayed us. This delay wrecked the drone window.", "note": "This + noun точнее указывает на событие."},
        ],
        watch_out=[
            "Голый this при двух возможных антецедентах.",
            "However как союз без точки/;.",
        ],
        remember="Цепочка должна быть восстановима. This + noun безопаснее голого this. However — коннектор; but — союз.",
    ),
    "distancing-evidentiality": lesson(
        "**Эвиденциальность** — маркировка источника знания. Английский не имеет обязательной эвиденциальной флексии, но C2-проза кодирует дистанцию: reportedly, allegedly, according to, I gather, seem / appear + perfect, пассив репортажа.\n\n**Allegedly** сильнее отделяет от ответственности, чем **reportedly**. **According to** именует источник.",
        [
            rule(
                "Наречия и рамки источника",
                "Reportedly the foundry will close — слух без имени. Allegedly she leaked the stills — обвинение, к которому автор не присоединяется. According to the harbour log…",
                [
                    ex("Allegedly the stills left the lab on a personal drive.", "Якобы кадры ушли из лаборатории на личном диске."),
                    ex("According to the night clerk, the fob never came back.", "По словам ночного дежурного, брелок так и не вернули."),
                    ex("Reportedly the foundry will close.", "По сообщениям, цех закроют — без имени источника."),
                ],
                tables=[
                    table(
                        ["Маркер", "Источник", "Дистанция"],
                        [
                            ["reportedly", "неназванный слух", "средняя"],
                            ["allegedly", "обвинение без присоединения", "высокая / юридическая"],
                            ["according to X", "именованный X", "груз на X"],
                            ["I gather / understand", "косвенный вывод", "вежливая"],
                            ["seem / appear + perfect", "вывод без свидетеля", "эпистемическая"],
                            ["is said / alleged to…", "репортажный пассив", "без автора слуха"],
                        ],
                    ),
                ],
            ),
            rule(
                "I gather / seem to have",
                "I gather they have withdrawn — вывод из косвенных сигналов. I understand — часто институциональное «сообщили». She seems to have declined — вывод о прошлом без прямого свидетеля.",
                [
                    ex("I gather the second ledger was never cross-checked.", "Как можно понять, вторую книгу так и не сверили."),
                    ex("The skipper appears to have ignored the second beacon.", "Похоже, шкипер проигнорировал второй огонь."),
                ],
                pairs=[
                    pair("I guess the second ledger was never cross-checked.", "I gather the second ledger was never cross-checked.", "В академическом тоне gather / understand точнее guess."),
                    pair("Allegedly the ferry leaves at 06:10 every Tuesday.", "The ferry leaves at 06:10 every Tuesday.", "Allegedly не для нейтрального расписания."),
                ],
            ),
            rule(
                "Пассив слуха",
                "It is alleged that…, She is alleged to have… Штабелировать осторожность (It has been reported that she is alleged…) обычно избыточно — один слой дистанции.",
                [
                    ex("It is alleged that the minutes were backfilled after the vote.", "Утверждается, что протокол дописали после голосования."),
                    ex("Two landings are said to have gone unlogged.", "Говорят, две посадки не попали в журнал."),
                ],
                callouts=[
                    callout("Один слой дистанции обычно достаточен. Allegedly — про вину; according to — про источник.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "She leaked the stills.", "right": "She allegedly leaked the stills.", "note": "Справа автор не берёт факт на себя."},
            {"left": "Reportedly the foundry will close.", "right": "According to the union bulletin, the foundry will close.", "note": "According to именует источник."},
        ],
        watch_out=[
            "Allegedly о погоде или расписании звучит как обвинение.",
            "I guess снижает академический регистр.",
        ],
        remember="Один слой дистанции. Allegedly — про вину. According to — про источник. Seem/appear + perfect — вывод без свидетеля.",
    ),
    "marked-word-order": lesson(
        "Канон английского — **SVO**. Любое отклонение маркировано: фокус, afterthought, тяжесть или сценичность.\n\nC2 владеет клефтами, левой/правой дислокацией, **heavy NP shift** и повествовательной инверсией. Приём без мотива читается как ошибка, не как стиль.",
        [
            rule(
                "Клефт и псевдоклефт",
                "It-cleft контрастирует: It was the washer that failed. Wh-cleft готовит определение: What failed was the washer. Reverse wh-cleft (The washer is what failed) — редко, обычно в устном уточнении.",
                [
                    ex("It was not the steel but the missing washer that failed.", "Контраст внутри it-cleft."),
                    ex("What the inquiry could not explain was the two missing hours.", "Псевдоклефт держит тяжёлое объяснение справа."),
                ],
                tables=[
                    table(
                        ["Приём", "Мотив", "Регистр"],
                        [
                            ["it-cleft", "контрастный фокус", "устный и письменный"],
                            ["wh-cleft", "подготовить определение", "нейтральный+"],
                            ["левая дислокация", "топик + резюме-местоимение", "устный"],
                            ["правая дислокация", "afterthought", "устный"],
                            ["heavy NP shift", "тяжёлое дополнение вправо", "письменный ok"],
                            ["place + V + NP", "сцена", "повествование"],
                        ],
                    ),
                ],
            ),
            rule(
                "Дислокация",
                "Левая: That gasket, I wouldn't trust it — топик вынесен, местоимение держит синтаксис. Правая: They never came back, the wet plates — уточнение после мысли. В прозе дислокация почти всегда слишком устная.",
                [
                    ex("That clause, I will not sign it.", "Левая дислокация: топик + резюме-местоимение."),
                    ex("They never came back, the wet plates.", "Правая дислокация как afterthought."),
                ],
                pairs=[
                    pair("We sent to legal it.", "We sent it to legal.", "Местоимение не сдвигается вправо."),
                    pair("What failed it was the washer.", "What failed was the washer.", "Псевдоклефт без лишнего it."),
                ],
            ),
            rule(
                "Heavy NP shift и сценическая инверсия",
                "We sent to legal [the entire unredacted correspondence…]. Тяжёлое дополнение уходит за предложную группу. Down the quay came the pilot boat — сцена. Лёгкое не сдвигают.",
                [
                    ex("She attributed to fatigue the series of mislabels in aisle C.", "Тяжёлый объект после attribute to."),
                    ex("Beside the radio hung a tide table nobody had updated since March.", "Обстоятельство + hung + тяжёлое подлежащее."),
                ],
                callouts=[
                    callout("Двойная маркировка (клефт + дислокация + инверсия) в одном предложении перегружает сигнал.", "warn"),
                ],
            ),
        ],
        compare=[
            {"left": "We sent the letter to legal.", "right": "We sent to legal the entire unredacted correspondence from March.", "note": "Сдвиг оправдан только тяжестью."},
            {"left": "The intern spotted the mismatch.", "right": "The intern, she spotted the mismatch.", "note": "Справа устный топик; в отчёте — шум."},
        ],
        watch_out=[
            "Heavy shift местоимения — ошибка, не стиль.",
            "Маркировать только по делу.",
        ],
        remember="SVO — нейтраль. Клефт — фокус. Дислокация — устный топик. Heavy shift — только тяжёлая группа.",
    ),
    "determiners-precision": lesson(
        "На C2 определители — **кванторы с логикой**, а не «артикли посложнее». **Each** смотрит на членов по одному, **every** — на класс как полное покрытие, **all** — на совокупность.\n\n**Either / neither** — двучленное множество. **Both** — ровно два. **The very** — идентичность; **quite the** — оценка типа.",
        [
            rule(
                "Each, every, all, any",
                "Each of the samples was labelled — поштучно. Every sample was labelled — покрытие класса. All the samples were — совокупность. Any в утверждении часто значит «даже один»: Any leak will abort the dive.",
                [
                    ex("Each of the six objections received a one-line reply.", "Каждое из шести возражений — по отдельности."),
                    ex("Every hatch on this deck seals against rain, not against a green sea.", "Покрытие класса hatch."),
                ],
                tables=[
                    table(
                        ["Определитель", "Множество", "Согласование / слот"],
                        [
                            ["each", "по одному", "each of + plural; глагол часто sg"],
                            ["every", "полное покрытие", "every + sg; не every of"],
                            ["all", "совокупность", "all (the) + plural"],
                            ["either", "один из двух", "either + sg"],
                            ["neither", "ни один из двух", "neither + sg; без второго отрицания"],
                            ["both", "ровно два", "both (of) + plural"],
                            ["the very + N", "тот самый", "идентичность"],
                            ["quite the + N", "оценка типа", "иронично/хвалебно"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Every of the samples was labelled.", "Each of the samples was labelled.", "Every of невозможно; every one of — можно."),
                    pair("Neither beacon weren't lit.", "Neither beacon was lit.", "Neither уже отрицателен."),
                ],
            ),
            rule(
                "Both, either, neither, half",
                "Either beacon will do — один из двух. Neither beacon was lit — глагол обычно единственный. Half (of) the stills…; half of it / them требует of.",
                [
                    ex("Either route clears the sandbar; neither is marked for night.", "Любой из двух путей; ни один не размечен для ночи."),
                    ex("Half the emulsion had already split when we opened the drum.", "Половина как мера массы/объёма."),
                    ex("Both beacons were lit.", "Оба огня горели."),
                ],
            ),
            rule(
                "Such, the very, quite the",
                "Such a delay / such delays. The very page we needed had been torn out. Quite the diplomat — оценка экземпляра как типа. What little time we had vanished…",
                [
                    ex("The very gasket I had boxed as a spare was already perished.", "Та самая прокладка."),
                    ex("She is quite the skipper in a cross-wind.", "Ещё та шкиперша в боковом ветре."),
                ],
                callouts=[
                    callout("Ошибки здесь звучат как сбой мышления, не как акцент: either при трёх вариантах, neither… don't.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "Each sample was dated.", "right": "Every sample was dated.", "note": "Each — «по одному»; every — «без исключений»."},
            {"left": "Either of the keys opens the loft.", "right": "Both of the keys are needed for the loft.", "note": "Either — один достаточен; both — нужны два."},
        ],
        watch_out=[
            "Neither … don't — двойное отрицание.",
            "Every of the samples — ошибка.",
        ],
        remember="Each — поштучно (each of). Every — покрытие класса. Either/neither — ровно два. The very — идентичность; quite the — оценка типа.",
    ),
    "advanced-complementation": lesson(
        "**Комплементация** — обязательные продолжения слова: proud that / of -ing / to; decide to / that / wh-; the fact that / the decision to.\n\nНа C2 путают не времена, а **слоты**. Raising-глаголы поднимают подлежащее из нижней клаузы. Extraposition оставляет it и выносит that / to вправо.",
        [
            rule(
                "Прилагательные: that, to, -ing, of",
                "Aware / convinced + that. Bound / likely + to. Busy / worth + -ing. Proud / capable + of -ing. Sorry to interrupt (жест сейчас) vs sorry that we interrupted (оценка факта).",
                [
                    ex("Legal is aware that the clause will be challenged.", "Aware that + клауза."),
                    ex("The beam is liable to sag if we add a second load.", "Liable to + infinitive — риск."),
                    ex("She is busy relabelling the stills.", "Busy + -ing."),
                ],
                tables=[
                    table(
                        ["Левая голова", "Слот", "Пример"],
                        [
                            ["aware / convinced", "that", "aware that…"],
                            ["likely / bound / due", "to + V1", "likely to decline"],
                            ["busy / worth", "-ing", "busy filing"],
                            ["proud / capable / afraid", "of -ing", "capable of sealing"],
                            ["sorry", "to / that", "разный смысл"],
                            ["decision", "to / that", "decision to withdraw"],
                            ["fact", "that (не to)", "the fact that…"],
                            ["chance", "of -ing / that", "chance of winning"],
                        ],
                    ),
                ],
            ),
            rule(
                "Глаголы: контроль и raising",
                "Want / persuade / tell — object control: We told her to wait (она ждёт). Promise — subject control (часто лучше promise that…). Seem / appear / prove — raising. Wonder / decide / explain + wh. Не: explain me why.",
                [
                    ex("They persuaded the skipper to wait for slack water.", "Object control: skipper waits."),
                    ex("The mix proved to have been bounced too hot.", "Raising: the mix не агенс prove."),
                    ex("They explained to me why the beam sagged.", "Explain to somebody + wh."),
                ],
                pairs=[
                    pair("They explained me why the beam sagged.", "They explained to me why the beam sagged.", "Explain to somebody."),
                    pair("The fact to withdraw surprised no one.", "The fact that they withdrew surprised no one.", "Fact that, не fact to."),
                ],
            ),
            rule(
                "Существительные и extraposition",
                "Decision to / that; chance of -ing / that; fact that. Ability to; difficulty (in) -ing. It is a pity that… / It was a mistake to… Raising vs extraposition: She is likely to decline / It is likely that she will decline.",
                [
                    ex("Their decision to withdraw left the tender uncontested.", "Decision to + infinitive."),
                    ex("It was a mistake to freeze the branch before legal signed.", "Extraposed to-infinitive after mistake."),
                    ex("She is likely to decline.", "Raising: likely + to."),
                ],
                callouts=[
                    callout("Учить слово вместе со слотом. Sorry to ≠ sorry that. Raising поднимает подлежащее; it выносит тяжёлый комплемент вправо.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "She is likely to decline.", "right": "It is likely that she will decline.", "note": "Raising vs extraposition — одна вероятность."},
            {"left": "I'm sorry to interrupt.", "right": "I'm sorry that we interrupted.", "note": "To — жест сейчас; that — факт-событие."},
        ],
        watch_out=[
            "The fact to withdraw — слот не тот.",
            "Explain me / suggest her to — чужой контроль.",
        ],
        remember="Слово + слот. Raising поднимает подлежащее. It выносит тяжёлый комплемент. Sorry to ≠ sorry that.",
    ),
}
