from app.seed.helpers import err, ex, fill, lesson, mc, module, rule, xf

C2 = [
    module(
        "information-structure",
        "Информационная структура",
        "Данное и новое, конец фразы как вес, тема–рема, there и it-extraposition.",
        28,
        "Куда английское предложение кладёт новое",
        lesson(
            "На C2 грамматика подчиняется упаковке информации. Английский предпочитает ставить данное (уже введённое) ближе к началу, а новое, тяжёлое и фокусное — к концу (end-focus, end-weight). Тема (то, о чём говорим) не всегда равна подлежащему: её можно задать there-конструкцией, it-выносом, пассивом или клефтом. Ошибка продвинутого уровня — формально верное предложение, которое «звучит криво», потому что тяжёлая группа стоит слишком рано, а лёгкое новое — слишком поздно. Перед правкой спросите: что уже известно читателю и что он должен узнать в конце фразы?",
            [
                rule(
                    "Данное → новое и конец как витрина",
                    "После того как объект введён, он стремится влево: The gasket had perished. This failure threw oil across the deck. Новое и контрастное любит финальную позицию: What threw the oil was a perished gasket. Короткое данное + тяжёлое новое читается легче, чем наоборот.",
                    [
                        ex("A spare impeller sat in the locker. That impeller later saved the crossing.", "Сначала введение, затем данное impeller в теме."),
                        ex("The inquiry blamed not the steel grade but a missing washer.", "Контрастный фокус уходит в конец."),
                    ],
                ),
                rule(
                    "End-weight: тяжёлые группы вправо",
                    "It is essential to relabel every jar that left aisle C before Thursday's assay — it держит подлежащее-заглушку, пока инфинитив (настоящее подлежащее по смыслу) идёт в конец. There is a sandbar just east of the marker вводит новое существование, не указывая на место как на тему.",
                    [
                        ex("It surprised no one that the foundry withdrew from the tender.", "That-клауза тяжелее it surprised; её выносят вправо."),
                        ex("There remains a second ledger whose entries were never cross-checked.", "There opens the scene; ledger — новое."),
                    ],
                ),
                rule(
                    "Выбор схемы под тему",
                    "Если тема — пациенс, пассив естественен: The stills were leaked before the premiere. Если тема — существование, there. Если нужно удержать оценку, а источник длинен: It is rumoured that…. Ломайте схему только ради контраста, не ради «разнообразия».",
                    [
                        ex("The unsent postcard was found in the top drawer, not the archive box.", "Тема — открытка, уже в дискурсе; пассив держит её слева."),
                        ex("It was the intern, not the editor, who froze the wrong branch.", "Клефт ставит контраст в каноническое фокусное окно."),
                    ],
                ),
            ],
            compare=[
                {"left": "That the foundry withdrew surprised no one.", "right": "It surprised no one that the foundry withdrew.", "note": "Слева формально можно; справа вес распределён по-английски."},
                {"left": "A sandbar is just east of the marker.", "right": "There is a sandbar just east of the marker.", "note": "There типичнее для первого введения объекта в сцену."},
            ],
            watch_out=[
                "Не начинайте абзац с that-клаузы-подлежащего без нужды: читатель ждёт тему раньше.",
                "Пассив ради пассива сбивает агенса; выбирайте его, только если пациенс — данная тема.",
                "Не клефтите и не выносите вперёд каждый элемент подряд — фокус работает, когда он редкий.",
            ],
            remember="Данное влево, новое и тяжёлое вправо. There вводит существование, it выносит тяжёлую клаузу, пассив и клефт переназначают тему.",
        ),
        [
            mc("___ surprised no one that the foundry withdrew.", ["This", "It", "There"], "It", "It-extraposition держит that-клаузу справа."),
            fill("___ remains a second ledger. (there)", "There", "There + existentials."),
            xf("Вынесите вес вправо: That the tide turned early complicated the shoot.", "It complicated the shoot that the tide turned early.", "It + verb + that-clause."),
            err("Is a sandbar just east of the marker. (first mention)", "There is a sandbar just east of the marker.", "Первое введение — there."),
            fill("The stills ___ leaked before the premiere. (be / past)", "were", "Пассив держит stills как тему."),
            mc("Where does English prefer the new, heavy constituent?", ["Immediately after the conjunction", "At the end of the clause", "Before the given topic"], "At the end of the clause", "End-weight / end-focus."),
        ],
        [
            fill("Вставьте нужную форму (it): ___ was the intern who froze the wrong branch. (it)", "It", "It-cleft."),
            mc("Выберите вопросительное / относительное слово: A spare impeller sat in the locker. ___ impeller later saved the crossing.", ["A", "That", "There"], "That", "Повтор как данное: that + noun."),
            xf("Сделайте темой открытку: Someone found the unsent postcard in the top drawer.", "The unsent postcard was found in the top drawer.", "Пассив."),
            err("That the beam sagged the inquiry blamed.", "The inquiry blamed the sagging of the beam.", "Нельзя фронтировать that-клаузу как дополнение без схемы.", ["It was the sagging of the beam that the inquiry blamed"]),
            fill("Вставьте форму to be: There ___ a sandbar just east of the marker. (be)", "is", "There is + новое."),
            mc("Choose the version with better end-weight.", ["To relabel every jar that left aisle C before Thursday's assay is essential.", "It is essential to relabel every jar that left aisle C before Thursday's assay."], "It is essential to relabel every jar that left aisle C before Thursday's assay.", "It снимает тяжёлый инфинитив с позиции подлежащего."),
        ],
    ),
    module(
        "aspect-contrasts",
        "Тонкие контрасты аспекта",
        "Simple vs progressive, perfect vs non-perfect, would / used to и стативы в Continuous.",
        26,
        "Вид как комментарий, а не как календарь",
        lesson(
            "На C2 выбор аспекта редко диктуется «правилом учебника» в чистом виде: говорящий комментирует, как он видит ситуацию — как целостную, как развёрнутую, как релевантную к точке отсчёта или как ограниченный отрезок. Progressive может сделать статив временным или нарочито субъективным. Perfect связывает событие с более поздней точкой, а не просто ставит «до». Would и used to расходятся по состоянию vs действию и по нарративной окраски.",
            [
                rule(
                    "Simple против Progressive: взгляд на ситуацию",
                    "She edits documentaries — устойчивая роль. She is editing a piece on the harbour — ограниченный проект. I'm loving this cut — временный вкус, не сломанный статив, а выбор перспективы. You are always leaving mugs on the scanner — эмоциональная оценка повтора, не расписание.",
                    [
                        ex("He stands on ceremony with funders, but tonight he is standing them a drink.", "Привычная сдержанность vs разовое поведение."),
                        ex("The emulsion is smelling odd this morning — we should stop the batch.", "Временный признак, не словарный статив smell.",),
                    ],
                ),
                rule(
                    "Perfect: релевантность, а не «раньше»",
                    "Have done помечает результат, опыт или «до сейчас / до тогда». Past Simple закрывает эпизод в его времени. I have had the lock changed — состояние налицо. I had the lock changed last May — датированный факт. Progressive perfect: длительность, незавершённость или раздражающий повтор до точки: I have been chasing that invoice.",
                    [
                        ex("She has declined three fellowships, so the rumour is stale.", "Серия отказов объясняет нынешний слух."),
                        ex("She declined the 2019 fellowship and took the foundry job.", "Закрытый биографический кадр."),
                    ],
                ),
                rule(
                    "Used to, would и Habitual will",
                    "Used to закрывает и действия, и состояния прошлого. Would — только повтор действий в уже заданном мире. Habitual will / would в настоящем/обобщении: She will leave mugs on the scanner — типичное поведение, часто с лёгким укором. Это не будущее.",
                    [
                        ex("The quay used to belong to the foundry; every Friday the siren would mark the pour.", "Состояние — used to; повтор действия — would."),
                        ex("He will insist on a paper trail, even for a two-line email.", "Типичная привычка, не план."),
                    ],
                ),
            ],
            compare=[
                {"left": "I lived in Cork for a year.", "right": "I have lived in Cork, so the accent doesn't throw me.", "note": "Слева закрытый отрезок; справа опыт как нынешний ресурс."},
                {"left": "She always leaves mugs on the scanner.", "right": "She is always leaving mugs on the scanner.", "note": "Continuous добавляет раздражение, не частотность как факт."},
            ],
            watch_out=[
                "Present Perfect + точная законченная дата прошлого (in 2019) в стандарте ломает связь с now.",
                "Would know / would own в привычном прошлом — ошибка аспекта-состояния.",
            ],
            remember="Аспект — ракурс. Progressive ограничивает или окрашивает. Perfect держит связь с точкой. Would не обслуживает прошлые состояния.",
        ),
        [
            mc("She ___ a piece on the harbour this month. (temporary project)", ["edits", "is editing", "has edit"], "is editing", "Ограниченный проект — Progressive."),
            fill("I ___ chasing that invoice all week. (be / present perfect)", "have been", "Длительность до сейчас."),
            xf("Типичный укор, не будущее: He insists on a paper trail (habit).", "He will insist on a paper trail.", "Habitual will."),
            err("I have had the lock changed last May.", "I had the lock changed last May.", "Дата last May закрывает эпизод — Past Simple."),
            fill("The quay ___ belong to the foundry. (used)", "used to", "Прошлое состояние."),
            mc("You ___ always leaving mugs on the scanner. (annoyance)", ["are", "do", "have"], "are", "Emotive Progressive: are always leaving."),
        ],
        [
            fill("Вставьте нужную форму (decline): She has ___ three fellowships, so the rumour is stale. (decline)", "declined", "Опыт/серия с нынешним выводом."),
            mc("Выберите модальный глагол (will/would): Every Friday the siren ___ mark the pour. (narrative habit)", ["used", "would", "has"], "would", "Повтор действия в заданном прошлом."),
            xf("Закройте эпизод датой: She has declined the 2019 fellowship. (исправьте аспект)", "She declined the 2019 fellowship.", "Past Simple + 2019."),
            err("I would own a barge in those days.", "I used to own a barge in those days.", "Владение — состояние, used to."),
            fill("Вставьте форму to be: The emulsion ___ smelling odd this morning. (be)", "is", "Временный признак в Progressive."),
            mc("Which links a past series to a present conclusion?", ["She declined three fellowships and took a job.", "She has declined three fellowships, so the rumour is stale.", "She would decline three fellowships last decade."], "She has declined three fellowships, so the rumour is stale.", "Perfect + нынешний вывод."),
        ],
    ),
    module(
        "register-metaphor",
        "Регистр и метафора",
        "Формальные и разговорные граммемы; стёртые метафоры академической прозы.",
        24,
        "Один смысл — разная социальная одежда",
        lesson(
            "C2 требует не только «правильной» формы, но и формы, уместной в ситуации. Регистр — согласование грамматики, лексики и метафоры с аудиторией. We were unable to obtain → We couldn't get. The argument does not hold → That idea falls apart. Академический английский полон стёртых метафор движения, зрения и войны (the paper advances, we see, this attacks the claim); живая авторская метафора должна быть контролируемой, иначе тон сбивается в художественность или в канцелярит.",
            [
                rule(
                    "Грамматические маркеры регистра",
                    "Формально: shall в правилах, were-subjunctive, инверсия, номинализации, whom после предлога, upon, in the event that. Разговорно: going to, got to, like как quotative, fronting без инверсии, эллипсис подлежащего в дневнике. Смешение в одном абзаце (Hereby I gonna…) выдаёт сбой контроля.",
                    [
                        ex("In the event of generator failure, switch to the battery bank.", "Канцелярия инструкции: in the event of + имя."),
                        ex("If the generator dies, just flip to the batteries.", "Тот же смысл в устной смене смены."),
                    ],
                ),
                rule(
                    "Лексико-грамматические пары",
                    "Enquire / ask, commence / start, sufficient / enough, prior to / before, a number of / several. Не «чем длиннее, тем лучше»: sufficient в лабораторном протоколе уместен, в реплике коллеге — холоден. Get-passive (got stolen) разговорнее be-passive.",
                    [
                        ex("The assay commenced at 06:40 and was terminated at 07:15.", "Протокол любит commence / terminate."),
                        ex("We started the assay at twenty to seven and killed it at quarter past.", "Лабораторный жаргон смены."),
                    ],
                ),
                rule(
                    "Метафора как связка, не украшение",
                    "Стёртые метафоры безопасны: raise a question, fall outside the scope, a robust finding. Смешение доменов в одном предложении (The finding that sank the argument then blossomed in chapter 4) создаёт катахрезу. Авторская метафора работает, если проведена через абзац, а не вспыхивает один раз.",
                    [
                        ex("The claim does not survive contact with the tide tables.", "Военная стёртость survive contact — приемлемый академический жест, если не копится."),
                        ex("Avoid: The skeleton of the chapter then sailed into a fog of numbers and baked the reader.", "Три домена сразу — скелет, море, кухня — ломают тон."),
                    ],
                ),
            ],
            compare=[
                {"left": "We were unable to obtain a spare impeller.", "right": "We couldn't get a spare impeller.", "note": "Одинаковая пропозици; слева отчёт, справа смена."},
                {"left": "The stills got leaked.", "right": "The stills were leaked.", "note": "Get-passive разговорнее и часто живее по вине/нечаянности."},
            ],
            watch_out=[
                "Hereby + gonna, whom + yeah — внутриабзацный слом регистра.",
                "Живая метафора без продолжения выглядит случайной; стёртую не оживляйте лишними деталями.",
            ],
            remember="Сначала аудитория, потом форма. Пары obtain/get — не синонимы по тону. Одна метафорическая линия на абзац.",
        ),
        [
            mc("Choose the instruction-manual wording.", ["If the generator dies, just flip to the batteries.", "In the event of generator failure, switch to the battery bank.", "Should the genny go kaput, yeah, batteries."], "In the event of generator failure, switch to the battery bank.", "In the event of — формальный маркер."),
            fill("Formal twin of before: ___ to the assay. (prior)", "prior", "Prior to."),
            xf("Понизьте регистр: We were unable to obtain a spare impeller.", "We couldn't get a spare impeller.", "Couldn't get."),
            err("Hereby I gonna freeze the branch.", "I hereby freeze the branch.", "Hereby не стыкуется с gonna.", ["I am going to freeze the branch"]),
            fill("The stills ___ leaked. (get / past, informal)", "got", "Get-passive."),
            mc("Which metaphor is controlled?", ["The claim does not survive contact with the tide tables.", "The skeleton sailed into a fog and baked the reader.", "The finding blossomed, sank, and then galloped."], "The claim does not survive contact with the tide tables.", "Один домен, стёртый жест."),
        ],
        [
            fill("Вставьте форму Past Simple: The assay ___ at 06:40. (commence / past, protocol)", "commenced", "Протокольный commence."),
            mc("Whom is most at home in…", ["a text to a colleague", "a formal relative after a preposition", "quoted speech with yeah"], "a formal relative after a preposition", "Whom жив после предлога в формальном регистре."),
            xf("Формальнее: Ask the harbour master.", "Enquire of the harbour master.", "Enquire of — высокий регистр.", ["Inquire of the harbour master"]),
            err("A number of several crates went missing.", "A number of crates went missing.", "Не складывайте a number of и several."),
            fill("Вставьте quantifier (some/any/much…): Sufficient is the formal twin of ___.", "enough", "Пара sufficient / enough."),
            mc("The argument does not hold. Разговорный близнец:", ["That idea falls apart.", "The contention fails to be sustained.", "One is compelled to reject the thesis."], "That idea falls apart.", "Падение идеи — более устный образ."),
        ],
    ),
    module(
        "advanced-cohesion",
        "Продвинутая связность",
        "Референция, лексические цепочки, коннекторы против союзов, замена на уровне абзаца.",
        27,
        "Как абзац помнит сам себя",
        lesson(
            "Связность (cohesion) — видимые нити между предложениями: местоимения, повтор и синонимическая замена, эллипсис, коннекторы. Coherence — логика, которую нити обслуживают. На C2 ошибка часто не в союзе, а в разрыве референциальной цепи: this указывает в пустоту, the + noun предполагает данное, которого не было, moreover стоит там, где нужен contrast. Коннектор (however, therefore, in contrast) — наречная рамка, часто с запятой; союз (but, so, and) соединяет клаузы синтаксически.",
            [
                rule(
                    "Референция и лексические цепочки",
                    "The gasket → this part → the failed component → it. Цепочка может идти гиперонимом вверх или уточнением вниз. This + noun надёжнее голого this, если антецедент — целая ситуация. Не открывайте the inquiry, если inquiry ещё не введена — сначала a / an или имя собственное.",
                    [
                        ex("A washer was missing. This omission, not the steel grade, explained the sag.", "This + noun пакует предыдущее предложение в тему."),
                        ex("Fog delayed the crossing. The weather also ruined the drone flight.", "The weather — гипероним к fog, цепочка жива."),
                    ],
                ),
                rule(
                    "Коннекторы и союзы",
                    "However / nevertheless / even so — уступка между предложениями. Therefore / consequently / thus — вывод. In contrast / conversely — противопоставление. But / yet могут стоять в начале предложения в современном регистре, но внутри сложного предложения but — союз. Не ставьте however как союз между двумя finite-клаузами без точки или точки с запятой.",
                    [
                        ex("The tables were reprinted; however, two crossings had already failed.", "However после точки с запятой — коннектор, не союз."),
                        ex("The tables were reprinted, but two crossings had already failed.", "But соединяет клаузы напрямую."),
                    ],
                ),
                rule(
                    "Абзацный эллипсис и повтор как приём",
                    "Повтор головы группы (the lock, the lock, the lock) может быть ритмом инструкции. В анализе предпочтительнее варьировать: the lock → the mechanism → this device. Эллипсис глагольной группы на границе предложений рискован, если сменился полярность или модальность: They could have radioed. They didn't. — ясно. They could have. Overnight. — уже нет.",
                    [
                        ex("Legal flagged the clause. Editorial flagged it too.", "It держит clause; too закрывает параллель."),
                        ex("We could have waited for slack water. We did not.", "Вторая клауза восстанавливает wait for slack water однозначно."),
                    ],
                ),
            ],
            compare=[
                {"left": "The tables were reprinted, however two crossings failed.", "right": "The tables were reprinted; however, two crossings failed.", "note": "However не заменяет союз без точки / точки с запятой."},
                {"left": "Fog delayed us. This was annoying.", "right": "Fog delayed us. This delay wrecked the drone window.", "note": "This + noun точнее указывает на событие, не на туман как вещество."},
            ],
            watch_out=[
                "Moreover в контрасте и however в простом добавлении — сбой логической метки.",
                "Голый this в начале абзаца, если прошлое предложение содержит два возможных антецедента.",
            ],
            remember="Цепочка должна быть восстановима. This + noun безопаснее голого this. However — коннектор; but — союз. Меняйте повтор сознательно.",
        ),
        [
            mc("The tables were reprinted; ___, two crossings had already failed.", ["but", "however", "and so"], "however", "После точки с запятой — коннектор however."),
            fill("A washer was missing. ___ omission explained the sag. (this)", "This", "This + noun."),
            xf("Союз вместо коннектора: The tables were reprinted; however, two crossings failed.", "The tables were reprinted, but two crossings failed.", "But + запятая, без however."),
            err("The tables were reprinted, however two crossings failed.", "The tables were reprinted; however, two crossings failed.", "However не союз между finite-клаузами."),
            fill("Fog delayed the crossing. The ___ also ruined the drone flight. (weather)", "weather", "Гипероним в цепочке."),
            mc("Which this is recoverable?", ["Legal flagged the clause and editorial panicked. This was late.", "Legal flagged the clause. This objection arrived after freeze."], "Legal flagged the clause. This objection arrived after freeze.", "Один антецедент + this + noun."),
        ],
        [
            fill("Вставьте пропущенное слово: We could have waited for slack water. We did ___.", "not", "Эллипсис глагольной группы."),
            mc("Choose the contrast marker.", ["moreover", "in contrast", "likewise"], "in contrast", "Противопоставление, не добавление."),
            xf("Уточните this (this + N): Fog delayed us. This was annoying. → This ___ wrecked the drone window.", "This delay wrecked the drone window.", "This + noun."),
            err("The inquiry concluded the washer failed. (inquiry not yet introduced)", "An inquiry concluded the washer failed.", "Первое упоминание — a/an.", ["The harbour inquiry concluded the washer failed"]),
            fill("Вставьте пропущенное слово: Editorial flagged the clause. Legal flagged ___ too.", "it", "It держит clause."),
            mc("Thus in a C2 paragraph most cleanly marks…", ["a contrast with the previous claim", "a consequence of what has just been established", "a change of topic with no inferential link"], "a consequence of what has just been established", "Thus = вывод."),
        ],
    ),
    module(
        "distancing-evidentiality",
        "Дистанцирование и эвиденциальность",
        "Reportedly, allegedly, according to, I gather, пассив слуха и seem + perfect.",
        25,
        "Откуда мы знаем — и насколько близко стоим",
        lesson(
            "Эвиденциальность — маркировка источника знания: видели сами, слышали, вывели, читали. Английский не имеет обязательной эвиденциальной флексии, но C2-проза густо кодирует дистанцию: reportedly, allegedly, according to X, I gather / I understand, seem / appear + perfect, пассив репортажа. Allegedly сильнее отделяет говорящего от ответственности (и юридически осторожнее), чем reportedly. According to называет источник и тем самым перекладывает эпистемический груз.",
            [
                rule(
                    "Наречия и рамки источника",
                    "Reportedly the foundry will close — слух без имени. Allegedly she leaked the stills — обвинение, к которому автор не присоединяется. According to the harbour log, the landing was at 03:10. As per в канцелярии. Under Chatham House rules… — особая рамка цитирования.",
                    [
                        ex("Allegedly the stills left the lab on a personal drive.", "Якобы кадры ушли из лаборатории на личном диске."),
                        ex("According to the night clerk, the fob never came back.", "По словам ночного дежурного, брелок так и не вернули."),
                    ],
                ),
                rule(
                    "I gather / I understand / seem to have",
                    "I gather they have withdrawn — вывод из косвенных сигналов, вежливая дистанция. I understand — часто институциональное «мне сообщили». She seems to have declined — вывод о прошлом без прямого свидетеля. Эти формулы мягче, чем I know.",
                    [
                        ex("I gather the second ledger was never cross-checked.", "Как я понимаю, вторую книгу так и не сверили."),
                        ex("The skipper appears to have ignored the second beacon.", "Похоже, шкипер проигнорировал второй огонь."),
                    ],
                ),
                rule(
                    "Пассив и вложенная чужая речь",
                    "It is alleged that…, She is alleged to have…, There are said to have been witnesses. Можно штабелировать осторожность: It has been reported that she is alleged to have… — обычно избыточно. Выберите один слой дистанции, если нет юридического задания.",
                    [
                        ex("It is alleged that the minutes were backfilled after the vote.", "Утверждается, что протокол дописали после голосования."),
                        ex("Two landings are said to have gone unlogged.", "Говорят, две посадки не попали в журнал."),
                    ],
                ),
            ],
            compare=[
                {"left": "She leaked the stills.", "right": "She allegedly leaked the stills.", "note": "Справа автор не берёт факт на себя."},
                {"left": "Reportedly the foundry will close.", "right": "According to the union bulletin, the foundry will close.", "note": "According to именует источник; reportedly — нет."},
            ],
            watch_out=[
                "Allegedly о погоде или расписании парома звучит как обвинение — не ставьте его на нейтральный факт.",
                "I guess в академическом абзаце снижает регистр; I gather / the data suggest точнее.",
            ],
            remember="Один слой дистанции обычно достаточен. Allegedly — про вину. According to — про источник. Seem/appear + perfect — про вывод без свидетеля.",
        ),
        [
            mc("___ she leaked the stills — speaker refuses the claim.", ["Reportedly", "Allegedly", "Obviously"], "Allegedly", "Allegedly дистанцирует от обвинения."),
            fill("___ to the night clerk, the fob never came back. (according)", "According", "According to + источник."),
            xf("Дистанция вывода: The skipper ignored the second beacon. (appear / past)", "The skipper appears to have ignored the second beacon.", "Appear + to have + V3."),
            err("I guess the second ledger was never cross-checked. (academic tone)", "I gather the second ledger was never cross-checked.", "Gather / understand вместо guess."),
            fill("It is ___ that the minutes were backfilled. (allege)", "alleged", "It is alleged that."),
            mc("Two landings are said ___ unlogged.", ["they went", "to have gone", "going"], "to have gone", "Репортажный пассив + перфектный инфинитив."),
        ],
        [
            fill("Вставьте нужную форму (reportedly): ___ the foundry will close — rumour, no named source. (reportedly)", "Reportedly", "Reportedly без источника."),
            mc("Выберите нужную форму (inference from signals): I ___ they have withdrawn. (inference from signals)", ["know", "gather", "swear"], "gather", "Gather = вывод издалека."),
            xf("Личный пассив слуха: People allege that she leaked the stills.", "She is alleged to have leaked the stills.", "Is alleged + to have + V3."),
            err("Allegedly the ferry leaves at 06:10 every Tuesday. (timetable fact)", "The ferry leaves at 06:10 every Tuesday.", "Allegedly не для нейтрального расписания."),
            fill("Вставьте нужную форму (seem): The skipper ___ to have ignored the second beacon. (seem)", "seems", "Seems to have + V3."),
            mc("According to marks…", ["the speaker's certainty", "a named source", "a legal accusation without a source"], "a named source", "According to + источник."),
        ],
    ),
    module(
        "marked-word-order",
        "Маркированный порядок слов",
        "Клефты, дислокация, heavy NP shift и стилистическая инверсия.",
        26,
        "Ломать SVO только по делу",
        lesson(
            "Канон английского — SVO. Любое отклонение маркировано: оно сигнализирует фокус, послемыслие, тяжесть или сценичность. C2 владеет клефтами, левой и правой дислокацией (That gasket, I wouldn't trust it; I wouldn't trust it, that gasket), сдвигом тяжёлого дополнения вправо (heavy NP shift) и повествовательной инверсией. Приём, использованный без мотива, читается как ошибка, не как стиль.",
            [
                rule(
                    "Клефт и псевдоклефт как разметка фокуса",
                    "It-cleft контрастирует: It was the washer that failed. Wh-cleft готовит определение: What failed was the washer. Reverse wh-cleft (The washer is what failed) кладёт фокус влево — редко, обычно в устном уточнении после непонимания.",
                    [
                        ex("It was not the steel but the missing washer that failed.", "Контраст внутри it-cleft."),
                        ex("What the inquiry could not explain was the two missing hours.", "Псевдоклефт держит тяжёлое объяснение справа."),
                    ],
                ),
                rule(
                    "Дислокация и afterthought",
                    "Левая: The intern, she spotted the mismatch — топик вынесен, местоимение держит синтаксис (разговорно). Правая: She spotted it, the intern — уточнение после мысли. В письменной прозе дислокация почти всегда слишком устная, если это не художественный голос.",
                    [
                        ex("That clause, I will not sign it.", "Левая дислокация: топик + резюме-местоимение."),
                        ex("They never came back, the wet plates.", "Правая дислокация как afterthought."),
                    ],
                ),
                rule(
                    "Heavy NP shift и сценическая инверсия",
                    "We sent to legal [the entire unredacted correspondence from March]. Тяжёлое дополнение уходит за предложную группу. Down the quay came the pilot boat — сцена. Не сдвигайте лёгкое: We sent to legal it — невозможно.",
                    [
                        ex("She attributed to fatigue the series of mislabels in aisle C.", "Тяжёлый объект после attribute to."),
                        ex("Beside the radio hung a tide table nobody had updated since March.", "Обстоятельство + hung + тяжёлое подлежащее."),
                    ],
                ),
            ],
            compare=[
                {"left": "We sent the letter to legal.", "right": "We sent to legal the entire unredacted correspondence from March.", "note": "Сдвиг оправдан только тяжестью второго объекта."},
                {"left": "The intern spotted the mismatch.", "right": "The intern, she spotted the mismatch.", "note": "Справа устный топик; в отчёте это шум."},
            ],
            watch_out=[
                "Heavy shift местоимения и коротких NP — грамматическая ошибка, не стиль.",
                "Двойная маркировка (клефт + дислокация + инверсия) в одном предложении перегружает сигнал.",
            ],
            remember="SVO — нейтраль. Клефт — фокус. Дислокация — устный топик. Heavy shift — только тяжёлая группа. Инверсия — сцена.",
        ),
        [
            mc("___ the washer that failed.", ["It was", "What was it", "That it was"], "It was", "It-cleft."),
            fill("What the inquiry could not explain ___ the two missing hours. (be)", "was", "Wh-cleft + was."),
            xf("Сделайте heavy NP shift (вынесите тяжёлое дополнение в конец): We sent the entire unredacted correspondence from March to legal.", "We sent to legal the entire unredacted correspondence from March.", "Тяжёлый NP после to legal."),
            err("We sent to legal it.", "We sent it to legal.", "Местоимение не сдвигается вправо."),
            fill("That clause, I will not sign ___.", "it", "Левая дислокация требует резюме-местоимения."),
            mc("Beside the radio ___ a tide table nobody had updated.", ["hung", "did hang", "hanging"], "hung", "Сценическая инверсия: place + verb + NP."),
        ],
        [
            fill("Вставьте вопросительное / относительное слово: The washer is ___ failed. (what)", "what", "Reverse wh-cleft: NP is what + verb."),
            mc("They never came back, the wet plates — это…", ["heavy NP shift", "right dislocation", "it-cleft"], "right dislocation", "Afterthought справа."),
            xf("Контрастный клефт: The intern froze the branch (not the editor).", "It was the intern, not the editor, who froze the branch.", "It-cleft + not-фраза."),
            err("What failed it was the washer.", "What failed was the washer.", "Псевдоклефт без лишнего it."),
            fill("Вставьте предлог: She attributed ___ fatigue the series of mislabels in aisle C. (to)", "to", "Attribute to + heavy NP справа."),
            mc("Choose the only motivated shift.", ["We gave to her it.", "She attributed to fatigue the series of mislabels in aisle C.", "I put on the table them."], "She attributed to fatigue the series of mislabels in aisle C.", "Только тяжёлый объект оправдывает shift."),
        ],
    ),
    module(
        "determiners-precision",
        "Определители: точные различия",
        "Each / every / all, either / neither, both / half, such / the very / quite the.",
        23,
        "Маленькое слово, жёсткий квантор",
        lesson(
            "На C2 определители — кванторы с логикой, а не «артикли посложнее». Each смотрит на членов по одному, every — на класс как на полное покрытие, all — на совокупность. Either / neither в двучленном множестве. Both требует ровно два. Such + noun оценивает тип; the very подчёркивает идентичность («тот самый»); quite the + noun — оценка экземпляра (quite the diplomat). Ошибки здесь звучат как сбой мышления, не как акцент.",
            [
                rule(
                    "Each, every, all, any",
                    "Each of the samples was labelled — поштучно, часто с of + plural. Every sample was labelled — полное покрытие класса, без of the, если нет уточнения. All the samples were — совокупность. Any в утверждении часто значит «неважно какой / даже самый слабый»: Any leak will abort the dive.",
                    [
                        ex("Each of the six objections received a one-line reply.", "Каждое из шести возражений — по отдельности."),
                        ex("Every hatch on this deck seals against rain, not against a green sea.", "Покрытие класса hatch."),
                    ],
                ),
                rule(
                    "Both, either, neither, half",
                    "Both (of) the beacons were lit. Either beacon will do — один из двух, неважно какой. Neither beacon was lit — ни один из двух; глагол обычно единственный. Half (of) the stills were unusable; half можно с of и без, но half of it / them требует of.",
                    [
                        ex("Either route clears the sandbar; neither is marked for night.", "Любой из двух путей; ни один не размечен для ночи."),
                        ex("Half the emulsion had already split when we opened the drum.", "Половина как мера массы/объёма."),
                    ],
                ),
                rule(
                    "Such, the very, quite the, what + noun",
                    "Such a delay / such delays. Not such a fool as to… The very page we needed had been torn out. Quite the opposite. Quite the diplomat — ироничная или хвалебная оценка типа. What little time we had vanished in the lock.",
                    [
                        ex("The very gasket I had boxed as a spare was already perished.", "Та самая прокладка."),
                        ex("She is quite the skipper in a cross-wind.", "Ещё та шкиперша в боковом ветре — оценка типа."),
                    ],
                ),
            ],
            compare=[
                {"left": "Each sample was dated.", "right": "Every sample was dated.", "note": "Почти синонимы; each легче читается как «по одному», every — как «без исключений»."},
                {"left": "Either of the keys opens the loft.", "right": "Both of the keys are needed for the loft.", "note": "Either — один достаточен; both — нужны два."},
            ],
            watch_out=[
                "Neither … don't / weren't — двойное отрицание; neither уже отрицателен.",
                "Every of the samples — ошибка; нужно each of или every one of.",
            ],
            remember="Each — поштучно (each of). Every — покрытие класса. Either/neither — ровно два. The very — идентичность; quite the — оценка типа.",
        ),
        [
            mc("___ of the six objections received a reply.", ["Every", "Each", "All"], "Each", "Each of + plural."),
            fill("___ hatch on this deck seals against rain. (every)", "Every", "Every + singular noun."),
            xf("Ни один из двух огней не горел.", "Neither beacon was lit.", "Neither + singular + was."),
            err("Every of the samples was labelled.", "Each of the samples was labelled.", "Every of невозможно.", ["Every one of the samples was labelled"]),
            fill("___ route clears the sandbar. (either)", "Either", "Either + singular."),
            mc("The ___ gasket I had boxed as a spare was perished.", ["very", "such", "either"], "very", "The very + noun = тот самый."),
        ],
        [
            fill("Вставьте нужную форму (half): ___ the emulsion had already split. (half)", "Half", "Half the + noun."),
            mc("Выберите пропущенное слово: She is ___ the skipper in a cross-wind.", ["very", "quite", "such"], "quite", "Quite the + noun."),
            xf("Оба огня горели.", "Both beacons were lit.", "Both + plural.", ["Both of the beacons were lit"]),
            err("Neither beacon weren't lit.", "Neither beacon was lit.", "Neither + единственное утверждение."),
            fill("Вставьте модальный глагол (will/would): Any leak ___ abort the dive. (will)", "will", "Any в утверждении = даже один."),
            mc("Выберите пропущенное слово: What little time we had ___ in the lock.", ["vanish", "vanished", "vanishes yesterday"], "vanished", "What little + noun + Past в рассказе."),
        ],
    ),
    module(
        "advanced-complementation",
        "Продвинутое комплементация",
        "Прилагательные, глаголы и существительные с that / to / -ing / wh; raising и extraposition.",
        28,
        "Какая форма закрывает слот после слова",
        lesson(
            "Комплементация — это обязательные и почти обязательные «продолжения» слова: proud that / proud of -ing / proud to, decide to / decide that / decide wh-, the fact that / the decision to / the chance of -ing. На C2 путают не времена, а слоты. Raising-глаголы (seem, appear, be likely) поднимают подлежащее из нижней клаузы. Extraposition оставляет it и выносит that / to-инфинитив вправо. Одни прилагательные берут только to (bound to), другие — that (aware that), третьи — оба с разным смыслом (sorry to / sorry that).",
            [
                rule(
                    "Прилагательные: that, to, -ing, of",
                    "Aware / convinced / concerned + that. Bound / due / likely / unlikely + to. Busy / worth + -ing. Proud / afraid / capable + of -ing. Sorry to interrupt (о своём действии в момент речи) vs sorry that we interrupted (оценка факта). Likely raising: She is likely to decline vs It is likely that she will decline.",
                    [
                        ex("Legal is aware that the clause will be challenged.", "Aware that + клауза."),
                        ex("The beam is liable to sag if we add a second load.", "Liable to + infinitive — склонность/риск."),
                    ],
                ),
                rule(
                    "Глаголы: контроль, raising, wh-complements",
                    "Want / persuade / tell — object control: We told her to wait (она ждёт). Promise — subject control: We promised her to wait (ждём мы; часто лучше promise that we would). Seem / appear / prove — raising, без агенса-контролёра. Wonder / decide / explain + wh: decide whether / explain why. Не: explain me why.",
                    [
                        ex("They persuaded the skipper to wait for slack water.", "Object control: skipper waits."),
                        ex("The mix proved to have been bounced too hot.", "Raising: the mix is not an agent of prove."),
                    ],
                ),
                rule(
                    "Существительные и extraposition",
                    "Decision to / decision that; chance of -ing / chance that; fact that (не fact to). Ability to; difficulty -ing / difficulty in -ing. It is a pity that… / It was a mistake to… Голое The fact is they left разговорно; в прозе that желателен.",
                    [
                        ex("Their decision to withdraw left the tender uncontested.", "Decision to + infinitive."),
                        ex("It was a mistake to freeze the branch before legal signed.", "Extraposed to-infinitive after mistake."),
                    ],
                ),
            ],
            compare=[
                {"left": "She is likely to decline.", "right": "It is likely that she will decline.", "note": "Raising vs extraposition — одна вероятность, разный синтаксис."},
                {"left": "I'm sorry to interrupt.", "right": "I'm sorry that we interrupted.", "note": "To — о жесте сейчас; that — о факте-событии."},
            ],
            watch_out=[
                "The fact to withdraw, chance to of — слоты не смешиваются как попало.",
                "Explain me the sag, suggest her to wait — контроль и предлог чужого языка.",
            ],
            remember="Учите слово вместе со слотом. Raising поднимает подлежащее. It выносит тяжёлый комплемент вправо. Sorry to ≠ sorry that.",
        ),
        [
            mc("Legal is aware ___ the clause will be challenged.", ["to", "that", "of to"], "that", "Aware that."),
            fill("The beam is liable ___ sag under a second load. (to)", "to", "Liable to + infinitive."),
            xf("Перепишите с raising (She is likely to …): It is likely that she will decline.", "She is likely to decline.", "Likely + to."),
            err("They explained me why the beam sagged.", "They explained to me why the beam sagged.", "Explain to somebody + wh."),
            fill("Their decision ___ withdraw left the tender uncontested. (to)", "to", "Decision to."),
            mc("I'm sorry ___ interrupt — жест в момент речи.", ["that", "to", "of"], "to", "Sorry to + свой жест."),
        ],
        [
            fill("Вставьте нужную форму (relabel): She is busy ___ the stills. (relabel)", "relabelling", "Busy + -ing.", ["relabeling"]),
            mc("Выберите инфинитив: The mix proved ___ bounced too hot.", ["it was", "to have been", "being"], "to have been", "Prove + raising + perfect infinitive."),
            xf("Перепишите с extraposition (It was a mistake to …): To freeze the branch before legal signed was a mistake.", "It was a mistake to freeze the branch before legal signed.", "It + be + noun + to."),
            err("The fact to withdraw surprised no one.", "The fact that they withdrew surprised no one.", "Fact that, не fact to.", ["Their withdrawal surprised no one"]),
            fill("Вставьте предлог: We told her ___ wait for slack water. (to)", "to", "Object control: tell somebody to."),
            mc("Выберите предлог: They persuaded the skipper ___ wait.", ["that", "to", "of"], "to", "Persuade somebody to."),
        ],
    ),
]
