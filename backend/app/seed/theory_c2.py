"""Expanded C2 grammar theory (Russian explanations, English examples).

Theoretical explanations are written in an academic grammar-reference style while remaining readable.
The original page-building helpers and **...** key-term convention are preserved.
"""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

C2_THEORY = {
    "information-structure": lesson(
        "На уровне C2 грамматический выбор определяется не только синтаксической правильностью, но и **информационной структурой** высказывания: тем, что уже известно из контекста, что вводится как новое, что находится в фокусе и какой элемент говорящий делает наиболее заметным. Английский сохраняет сравнительно фиксированный порядок слов, поэтому информационная упаковка часто достигается специальными конструкциями — **there-constructions**, **extraposition**, пассивом, **it-clefts**, **wh-clefts** и дислокацией.\n\nДве фундаментальные тенденции — **end-focus** и **end-weight**. Новый, контрастивный или особенно важный материал часто получает финальную позицию, а длинная синтаксическая группа стремится располагаться после более коротких элементов. Это сильные предпочтения, а не абсолютные запреты: контраст, ритм, жанр и уже установленная тема могут оправдать другой порядок. Важно различать **grammatical subject**, **topic** и **focus**: эти понятия могут совпадать, но не обязаны.",
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
            rule(
                "Topic, focus и контрастивный фокус",
                "**Topic** — то, о чём строится высказывание; **focus** — компонент, несущий наиболее значимую новую или контрастивную информацию. Topic может быть вынесен влево и связан с местоимением внутри клаузы. Контрастивный focus часто получает финальную позицию и может сопровождаться *not X but Y*. Интонация дополнительно определяет фокус в устной речи.",
                [
                    ex("As for the missing washer, the inquiry had already ruled it out.", "As for создаёт внешний topic."),
                    ex("The inquiry blamed the missing washer, not the steel grade.", "Последний компонент получает contrastive focus."),
                ],
            ),
            rule(
                "Extraposition и formal it",
                "В **extraposition** тяжёлая clause переносится вправо, а *it* занимает позицию формального подлежащего. Это отличается от referential *it*: в *It was surprising that the figures changed* it не обозначает отдельный предмет. Extraposition особенно естественна с оценочными прилагательными и reporting predicates, но прямая конструкция тоже возможна.",
                [
                    ex("That the figures had changed was surprising.", "Грамматически корректно, но тяжело в начале."),
                    ex("It was surprising that the figures had changed.", "Extraposition облегчает обработку."),
                    ex("It was on the desk.", "Referential it, не extraposition."),
                ],
            ),
            rule(
                "There-construction и agreement",
                "**There** вводит существование или появление нового референта: *There is a problem*. В более формальной прозе возможны *There remains one issue, There appears to be a discrepancy*. В стандартном письме согласование обычно ориентируется на postposed subject: *There seems to be one error*, но *There seem to be several errors*. Когда существительное уже является темой, обычный SVO часто естественнее.",
                [
                    ex("There appears to be a discrepancy in the second ledger.", "Новое существование discrepancy."),
                    ex("There appear to be three discrepancies.", "Plural subject → appear."),
                    ex("The discrepancy appears to be minor.", "Уже известная тема → SVO."),
                ],
                tables=[
                    table(["Средство", "Основная функция", "Типичная мотивация"], [["there", "ввести существование", "новый референт"], ["it + that/to", "extraposition", "тяжёлая clause"], ["passive", "переназначить тему", "patient уже дан"], ["cleft", "выделить focus", "контраст"]]),
                ],
            ),
        compare=[
            {"left": "That the foundry withdrew surprised no one.", "right": "It surprised no one that the foundry withdrew.", "note": "Справа end-weight."},
            {"left": "A sandbar is just east of the marker.", "right": "There is a sandbar just east of the marker.", "note": "There типичнее для первого введения."},
        ],
        watch_out=[
            "Абзац с that-клаузы-подлежащего без нужды тяжелит чтение.",
            "Пассив ради пассива сбивает агенса.",
            "End-focus/end-weight — сильные предпочтения, а не абсолютные запреты.",
            "Topic, grammatical subject и focus могут быть разными элементами.",

        ],
        remember="Данное влево, новое и тяжёлое вправо. There — существование, it — вынос, пассив и клефт — переназначение темы.",
    ),
    "aspect-contrasts": lesson(
        "На уровне C2 **tense and aspect** следует рассматривать как систему выбора временной точки отсчёта и перспективы на ситуацию. Временная форма сообщает, где ситуация расположена относительно момента речи или другой точки, а аспект показывает, как она представлена: как факт или целое, как развёрнутый процесс, как состояние, как завершённая ситуация с актуальной связью или как процесс, продолжающийся до определённого момента.\n\n**Simple** обычно представляет ситуацию целостно, как факт, состояние, привычку или последовательный эпизод. **Progressive** выделяет внутреннее протекание, временность или ограниченность периода и иногда добавляет эмоциональную оценку. **Perfect** устанавливает связь между более ранним событием и последующей точкой отсчёта; **perfect progressive** дополнительно подчёркивает длительность, повторяемость или накопленный процесс.\n\nВыбор аспекта зависит и от лексического значения глагола. **Stative verbs** обычно не употребляются в progressive, но многие глаголы меняют аспектуальный класс в другом значении: *think, have, see, feel, taste, smell*. Аналогично **used to**, **would** и **habitual will** частично пересекаются, но кодируют разные типы привычности.",
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
            rule(
                "Stative verbs и смена значения",
                "После глаголов состояния progressive обычно не употребляется, но правило семантическое. *Think* = 'считать' обычно stative, *think about* = 'обдумывать' dynamic; *have* = possession stative, *have lunch* dynamic; *see* может означать perception или arranged meeting. Поэтому список stative verbs нельзя применять как механический запрет.",
                [
                    ex("I think the estimate is wrong.", "Think = иметь мнение."),
                    ex("I am thinking about the revised estimate.", "Think = обдумывать."),
                    ex("She has a cottage on the quay.", "Have = владеть."),
                    ex("She is having lunch with the survey team.", "Have = принимать пищу."),
                ],
                callouts=[callout("Корректнее говорить: stative meaning обычно не допускает progressive.", "warn")],
            ),
            rule(
                "Perfect и законченная временная рамка",
                "Present Perfect устанавливает связь с настоящей точкой отсчёта, поэтому с завершёнными периодами *yesterday, last year, in 2019, two hours ago* обычно выбирается Past Simple. С незавершёнными периодами (*today, this week, so far*) и опытом без закрытой даты Perfect естественен.",
                [
                    ex("We have checked the valves twice this morning.", "Период this morning ещё релевантен как текущий."),
                    ex("We checked the valves twice yesterday.", "Завершённый период."),
                    ex("Have you ever inspected a dry dock?", "Опыт без конкретной даты."),
                ],
                tables=[table(["Контекст", "Обычно", "Почему"], [["yesterday / in 2019", "Past Simple", "период закрыт"], ["today / this week", "Present Perfect", "период открыт"], ["ever / never", "Present Perfect", "опыт без закрытой даты"]])],
            ),
            rule(
                "Used to, would и habitual will",
                "**Used to** обозначает прошлое состояние или повторяющееся действие. **Would** в привычном прошлом обычно описывает повторяющееся событие в уже установленном контексте, но не чистое состояние. **Habitual will** относится к типичному поведению в настоящем и может выражать раздражение: *She will leave the door open*.",
                [
                    ex("The quay used to belong to the foundry.", "Past state."),
                    ex("Every Friday the siren would mark the pour.", "Repeated past event."),
                    ex("She will leave the door open.", "Present habitual behaviour."),
                ],
            ),
        compare=[
            {"left": "I lived in Cork for a year.", "right": "I have lived in Cork, so the accent doesn't throw me.", "note": "Закрытый отрезок vs опыт как нынешний ресурс."},
            {"left": "She always leaves mugs on the scanner.", "right": "She is always leaving mugs on the scanner.", "note": "Continuous добавляет раздражение."},
        ],
        watch_out=[
            "Would know / would own в привычном прошлом — ошибка.",
            "Perfect + закрывающая дата.",
            "Stative verb может допускать progressive при смене значения.",
            "Present Perfect обычно не выбирается с завершённой конкретной датой прошлого.",

        ],
        remember="Аспект — ракурс. Progressive ограничивает или окрашивает. Perfect держит связь с точкой. Would не обслуживает прошлые состояния.",
    ),
    "register-metaphor": lesson(
        "На уровне C2 **register** — это соответствие языковой формы аудитории, жанру, цели и социальной ситуации. Формально корректная конструкция может быть неуместной, если она слишком разговорна для отчёта или, наоборот, чрезмерно канцелярска для живой реплики. Академический английский не равен максимально сложному английскому: номинализация, пассив и редкая лексика полезны только тогда, когда они выполняют определённую дискурсивную функцию.\n\nОсобое внимание требуется к средствам, связанным с жанром: **shall** характерно для нормативных документов и ряда формальных предложений, *hereby/thereof/therein* — для юридико-официальной речи, а **get-passive** обычно разговорнее **be-passive**. При этом ни одна из этих форм не является автоматически «правильной» или «неправильной»: значение определяется контекстом.\n\nМетафоры требуют отдельного контроля. Многие выражения (*raise a question, address an issue, fall within the scope*) уже лексикализованы. Свежая авторская метафора должна оставаться семантически совместимой с остальным текстом; случайное смешение нескольких образных доменов создаёт **mixed metaphor** и часто снижает ясность.",
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
            rule(
                "Formal does not mean complex",
                "Номинализация, пассив и редкая лексика полезны, если они организуют информацию, но чрезмерное усложнение может скрывать агенса и ухудшать читаемость. Хороший академический стиль допускает простую конструкцию, когда она точнее.",
                [
                    ex("The committee rejected the proposal after reviewing the evidence.", "Формально и прозрачно."),
                    ex("The rejection of the proposal followed a review of the evidence.", "Номинализация уместна, если rejection уже является темой."),
                ],
            ),
            rule(
                "Passive, get-passive и agent",
                "**Be-passive** нейтрален и часто используется в отчётах; **get-passive** разговорнее и может подчёркивать изменение состояния или результат: *He got promoted*. Пассив не следует выбирать только потому, что он 'академический': если agent важен, активная конструкция часто яснее.",
                [
                    ex("The samples were relabelled after the audit.", "Neutral formal passive."),
                    ex("He got promoted after the audit.", "Conversational get-passive."),
                ],
            ),
            rule(
                "Жанровая специализация форм",
                "**Shall** особенно характерно для правил, договоров и нормативных формулировок; *hereby, thereof, therein* имеют юридико-официальную специализацию. *Whom* сохраняется прежде всего после предлогов и в формальной письменной речи. Такие элементы не следует искусственно добавлять в обычный академический текст.",
                [
                    ex("The tenant shall notify the owner within seven days.", "Normative/contractual shall."),
                    ex("The person to whom I spoke was the auditor.", "Formal whom after a preposition."),
                    ex("The person who I spoke to was the auditor.", "Neutral modern alternative."),
                ],
            ),
            rule(
                "Mixed metaphor и lexicalised metaphor",
                "Лексикализованные метафоры (*raise a question, address an issue, fall within the scope*) обычно уже воспринимаются как обычные коллокации. Свежая метафора создаёт отдельный образный домен; смешение нескольких несовместимых доменов в одном фрагменте создаёт **mixed metaphor**. В художественном тексте это может быть намеренным приёмом, но в академическом обычно снижает точность.",
                [
                    ex("The proposal opens the door to further research.", "Устойчивый образ."),
                    ex("The argument sailed into a fog and baked the reader.", "Смешение доменов."),
                ],
            ),
        compare=[
            {"left": "We were unable to obtain a spare impeller.", "right": "We couldn't get a spare impeller.", "note": "Одинаковая пропозиция; слева отчёт, справа смена."},
            {"left": "The stills got leaked.", "right": "The stills were leaked.", "note": "Слева get-passive (разговорнее); справа be-passive (нейтральнее)."},
        ],
        watch_out=[
            "Hereby + gonna — внутриабзацный слом регистра.",
            "Живая метафора без продолжения выглядит случайной.",
            "Formal не означает unnecessarily complex.",
            "Жанрово маркированную форму не следует использовать без жанровой причины.",

        ],
        remember="Сначала аудитория, потом форма. Пары obtain/get — не синонимы по тону. Одна метафорическая линия на абзац.",
    ),
    "advanced-cohesion": lesson(
        "**Cohesion** — система формальных языковых связей между частями текста: местоименная референция, лексические цепочки, эллипсис, замещение, союзы и дискурсивные коннекторы. **Coherence** относится к более широкой логической и концептуальной организации. Хороший C2-текст требует и того и другого: читатель должен понимать не только логическую связь идей, но и то, к каким словам и событиям отсылают короткие анафорические элементы.\n\nОсобенно важен **reference tracking**. *It, this, that, they* могут ссылаться на существительное, группу слов или целую ситуацию. Если потенциальных антецедентов несколько, голое *this* или *it* создаёт неоднозначность; часто точнее использовать **this + noun**. В академическом тексте искусственное избегание повторов также опасно: точный термин нередко лучше случайного синонима.\n\nНужно различать грамматические классы средств связи. **And, but, so** непосредственно соединяют клаузы, тогда как **however, therefore, nevertheless, in contrast** обычно являются самостоятельными дискурсивными элементами. Их нельзя соединять с двумя finite clauses простой запятой по модели coordinating conjunction.",
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
            rule(
                "Anaphora, cataphora и ambiguous reference",
                "**Anaphora** отсылает назад: *The valve failed. It was replaced.* **Cataphora** допускает местоимение перед своим референтом: *When he arrived, John inspected the valve.* В сложной прозе неоднозначная ссылка опаснее повторения: если *it/this/they* имеет два возможных антецедента, существительное обычно предпочтительнее.",
                [
                    ex("The valve failed. It was replaced within an hour.", "Очевидная анафора."),
                    ex("When he arrived, John inspected the valve.", "Cataphoric reference."),
                    ex("The valve damaged the housing, and it was replaced.", "Неоднозначно: it может иметь два антецедента."),
                ],
            ),
            rule(
                "This/that как ссылка на событие",
                "*This* и *that* могут отсылать к целой предыдущей ситуации, а не только к существительному. Конструкция **this + noun** часто делает интерпретацию явнее: *The survey was cancelled. This cancellation caused delays.* Это особенно полезно, когда предыдущая клауза содержит несколько возможных сущностей.",
                [
                    ex("The survey was cancelled. This cancellation caused delays.", "Явно назван тип референта."),
                    ex("The survey was cancelled. This caused delays.", "Ссылка на целое событие."),
                ],
            ),
            rule(
                "Lexical cohesion: repetition vs synonymy",
                "Лексическая цепочка может строиться повтором, близким термином или гиперонимом. В техническом тексте точный повтор часто лучше искусственного синонима: *valve → component* может быть менее точным. Гипероним (*fog → weather*) полезен, когда обобщение действительно нужно.",
                [
                    ex("The valve failed. The valve was replaced.", "Повтор термина повышает техническую точность."),
                    ex("Fog delayed the crossing. The weather also affected the flight.", "Hypernym broadens the lexical chain."),
                ],
            ),
            rule(
                "Connectors и logical relations",
                "**Moreover/furthermore** добавляют аргумент; **however/nevertheless** выражают контраст или уступку; **therefore/thus** вводят вывод; **otherwise** указывает альтернативное следствие. Выбор коннектора должен соответствовать логической связи, а не просто разнообразить начало предложения.",
                [
                    ex("The evidence was incomplete; however, the committee proceeded.", "Concessive/contrastive connector."),
                    ex("The evidence was incomplete, but the committee proceeded.", "But — coordinating conjunction."),
                    ex("The evidence was incomplete; therefore, a second audit was requested.", "Therefore — result."),
                ],
                tables=[table(["Средство", "Класс", "Связь"], [["but", "conjunction", "contrast"], ["so", "conjunction", "result"], ["however", "conjunctive adverbial", "contrast"], ["therefore", "conjunctive adverbial", "result"]])],
            ),
            rule(
                "Ellipsis и parallelism",
                "Эллипсис удаляет материал, который легко восстанавливается: *The first team inspected the valves, and the second the pumps.* Такая компактность полезна, пока структура однозначна. При смене времени или полярности повтор глагольной группы часто повышает ясность.",
                [
                    ex("The first team inspected the valves, and the second the pumps.", "Gapping in coordination."),
                    ex("We could have waited, but we did not.", "Отрицательная форма делает реконструкцию ясной."),
                ],
            ),
        compare=[
            {"left": "The tables were reprinted, however two crossings failed.", "right": "The tables were reprinted; however, two crossings failed.", "note": "Коннектор требует точки / точки с запятой."},
            {"left": "Fog delayed us. This was annoying.", "right": "Fog delayed us. This delay wrecked the drone window.", "note": "This + noun точнее указывает на событие."},
        ],
        watch_out=[
            "Голый this при двух возможных антецедентах.",
            "However как союз без точки/;.",
            "Не допускать неоднозначного it/this/they.",
            "Точный повтор технического термина может быть лучше искусственного синонима.",

        ],
        remember="Цепочка должна быть восстановима. This + noun безопаснее голого this. However — коннектор; but — союз.",
    ),
    "distancing-evidentiality": lesson(
        "**Эвиденциальность (evidentiality)** — выражение источника информации и отношения говорящего к её подтверждённости. В английском нет обязательной эвиденциальной морфологии, однако академическая и журналистская речь регулярно кодирует источник и степень дистанции с помощью **according to, reportedly, allegedly, apparently, I gather, I understand, seem/appear** и репортажного пассива.\n\nНа C2 важно различать **source**, **epistemic commitment** и **attribution**. *According to the report* называет источник, но не гарантирует истинность его утверждения. *Reportedly* сообщает о наличии сообщения без обязательного указания источника. *Allegedly* особенно характерно для спорных утверждений и обвинений и явно дистанцирует автора от их истинности. *Apparently* чаще представляет вывод из доступных признаков.\n\n**Seem/appear + perfect infinitive** выражает вывод о предшествующем событии: *She seems to have left*. **She is said to have left** — уже reporting passive, то есть информация приписывается неназванному источнику. Избыточное накопление нескольких маркеров дистанции обычно ухудшает стиль: один точно выбранный уровень часто эффективнее трёх.",
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
            rule(
                "Source, certainty и attribution",
                "**According to X** называет источник; **apparently** и **seem/appear** часто маркируют вывод; **allegedly** дистанцирует автора от спорного утверждения; **certainly/clearly** повышают авторскую уверенность. Эти функции не следует смешивать: источник и степень уверенности — разные параметры.",
                [
                    ex("According to the report, the figure is inaccurate.", "Источник назван."),
                    ex("Apparently, the figure is inaccurate.", "Inference from available evidence."),
                    ex("The figure is certainly inaccurate.", "Strong authorial commitment."),
                ],
            ),
            rule(
                "Reportedly, allegedly, apparently",
                "**Reportedly** сообщает о наличии сообщения; **allegedly** особенно естественно для обвинений и спорных фактов; **apparently** часто означает 'судя по имеющимся признакам'. Замена одного маркера другим может менять юридическую и прагматическую интерпретацию.",
                [
                    ex("Reportedly, the plant will close in October.", "Сообщение без названного источника."),
                    ex("The contractor allegedly falsified the figures.", "Дистанция от обвинения."),
                    ex("Apparently, the plant has already closed.", "Вывод из признаков."),
                ],
            ),
            rule(
                "Seem/appear + perfect infinitive",
                "*She seems to know* описывает текущее состояние или одновременно релевантную ситуацию. *She seems to have left* выражает вывод о событии, предшествующем моменту вывода. Это не обязательно hearsay: говорящий может формировать вывод самостоятельно.",
                [
                    ex("She seems to know the answer.", "Current state."),
                    ex("She seems to have left already.", "Earlier completed event."),
                ],
            ),
            rule(
                "Reporting passive",
                "В моделях **It is said that...** и **She is said to...** источник не называется. Если reported event предшествует моменту сообщения, используется perfect infinitive: *She is said to have left*. Такая конструкция типична для журналистской и формальной письменной речи.",
                [
                    ex("It is said that the minutes were altered.", "Impersonal reporting passive."),
                    ex("The secretary is said to have altered the minutes.", "Personal reporting passive + perfect infinitive."),
                ],
            ),
        compare=[
            {"left": "She leaked the stills.", "right": "She allegedly leaked the stills.", "note": "Справа автор не берёт факт на себя."},
            {"left": "Reportedly the foundry will close.", "right": "According to the union bulletin, the foundry will close.", "note": "According to именует источник."},
        ],
        watch_out=[
            "Allegedly о погоде или расписании звучит как обвинение.",
            "I guess снижает академический регистр.",
            "According to X = источник; это не то же самое, что certainty.",
            "Allegedly особенно маркирует спорные утверждения и обвинения.",

        ],
        remember="Один слой дистанции. Allegedly — про вину. According to — про источник. Seem/appear + perfect — вывод без свидетеля.",
    ),
    "marked-word-order": lesson(
        "Нейтральный английский характеризуется относительно фиксированным порядком **SVO**, поэтому заметное отклонение от него обычно имеет дискурсивную или стилистическую мотивацию. На уровне C2 маркированный порядок используется для управления фокусом, темой, тяжестью группы, ритмом повествования и сценическим представлением.\n\nК основным средствам относятся **it-clefts**, **wh-clefts**, левая и правая дислокация, **heavy NP shift** и несколько типов инверсии. Эти конструкции нельзя считать свободными вариантами одной и той же структуры: каждая имеет собственные синтаксические ограничения. Например, cleft выделяет информационный фокус, left dislocation создаёт внешний topic с местоименным повтором, а heavy NP shift мотивирован длиной и сложностью группы.\n\nОсобенно важно различать **subject–auxiliary inversion** и **subject–verb inversion**. После отрицательных или ограничительных элементов (*never, rarely, only then, under no circumstances*) используется вспомогательный глагол; в locative/narrative inversion возможна модель *place + lexical verb + subject*. Начальное обстоятельство само по себе инверсию не вызывает.",
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
            rule(
                "Negative and restrictive fronting",
                "После **never, rarely, seldom, little, only then, under no circumstances** и подобных ограничительных элементов в формальном стиле используется инверсия auxiliary и subject: *Never have I seen...* Если auxiliary нет, появляется *do/did*: *Only then did we realise...*. Обычное обстоятельство в начале предложения такой инверсии не вызывает.",
                [
                    ex("Never have I seen such a discrepancy.", "Negative fronting + inversion."),
                    ex("Only then did the discrepancy become apparent.", "Do-support for inversion."),
                    ex("After the meeting, we left early.", "No inversion after ordinary adverbial."),
                ],
            ),
            rule(
                "Locative / narrative inversion",
                "В описательной и повествовательной прозе пространственная рамка может предшествовать глаголу и новому subject: *On the wall hung a map*. Такая инверсия помогает сначала представить сцену, а затем ввести объект. Она не является обычным разговорным вопросительным порядком и зависит от типа глагола и информационной структуры.",
                [
                    ex("On the wall hung a map of the old harbour.", "Place + lexical verb + new subject."),
                    ex("Down the quay came the pilot boat.", "Narrative movement."),
                ],
            ),
            rule(
                "Cleft constructions и информационный фокус",
                "**It-cleft** выделяет X: *It was X that Y*. **Wh-cleft** организует высказывание через wh-clause: *What caused the leak was X*. Reverse wh-cleft (*X was what caused the leak*) возможен, но более маркирован. Cleft следует использовать для реального управления фокусом, а не как формальный признак продвинутого уровня.",
                [
                    ex("It was the missing washer that caused the leak.", "Focus on washer."),
                    ex("What caused the leak was the missing washer.", "Wh-cleft."),
                    ex("The missing washer was what caused the leak.", "Reverse wh-cleft; more marked."),
                ],
            ),
            rule(
                "Left/right dislocation и afterthought",
                "**Left dislocation** выносит topic влево и сохраняет его местоимением: *That clause, I would not sign it*. **Right dislocation** помещает уточнение после завершённой структуры: *They never came back, the wet plates*. Эти модели особенно характерны для разговорной речи и стилизованного повествования.",
                [
                    ex("That clause, I would not sign it.", "Left-dislocated topic + resumptive pronoun."),
                    ex("They never came back, the wet plates.", "Right-dislocated afterthought."),
                ],
            ),
        compare=[
            {"left": "We sent the letter to legal.", "right": "We sent to legal the entire unredacted correspondence from March.", "note": "Сдвиг оправдан только тяжестью."},
            {"left": "The intern spotted the mismatch.", "right": "The intern, she spotted the mismatch.", "note": "Справа устный топик; в отчёте — шум."},
        ],
        watch_out=[
            "Heavy shift местоимения — ошибка, не стиль.",
            "Маркировать только по делу.",
            "Начальное обстоятельство само по себе не вызывает инверсию.",
            "Heavy NP shift не является свободным перемещением любого дополнения.",

        ],
        remember="SVO — нейтраль. Клефт — фокус. Дислокация — устный топик. Heavy shift — только тяжёлая группа.",
    ),
    "determiners-precision": lesson(
        "На уровне C2 **determiners** кодируют не только определённость, но и структуру множества, распределение внимания и логический охват высказывания. Поэтому **each, every, all, both, either, neither, any** нельзя рассматривать как простые синонимы количества.\n\n**Each** концептуализирует членов множества по отдельности; **every** представляет множество как класс с полным покрытием; **all** обозначает совокупность. **Both** относится ровно к двум элементам. В основном значении **either** и **neither** также предполагают два релевантных варианта. Важно различать determiner slot и местоименную конструкцию: *every sample*, но *every one of the samples*; *each sample* и *each of the samples*.\n\nСогласование должно соответствовать грамматическому центру: *Each of the samples was...*, *Every sample was...*, *All the samples were...*. Разговорные варианты встречаются, но академический и экзаменационный стандарт предпочитает последовательное нормативное согласование.",
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
            rule(
                "Each vs every",
                "**Each** может употребляться как determiner и как pronoun: *each sample, each of the samples, each was labelled*. **Every** требует singular count noun в обычной конструкции: *every sample*. Для *of + plural* используется *every one of the samples*. Each сильнее подчёркивает индивидуальных членов, every — полный охват класса.",
                [
                    ex("Each of the samples was labelled separately.", "Individual distribution."),
                    ex("Every sample was labelled before shipment.", "Full class coverage."),
                    ex("Every one of the samples was labelled.", "Every one + of + plural."),
                ],
            ),
            rule(
                "All, whole и both",
                "**All** обозначает совокупность: *all the samples*. **Whole** рассматривает один объект или период целиком: *the whole report, the whole day*. **Both** относится ровно к двум: *both samples, both of the samples*. С singular count noun whole обычно требует determiner: *the whole report*.",
                [
                    ex("All the samples were contaminated.", "Совокупность."),
                    ex("The whole sample was contaminated.", "Один объект целиком."),
                    ex("Both samples were contaminated.", "Ровно два."),
                ],
            ),
            rule(
                "Either / neither и отрицание",
                "В основном значении **either** и **neither** относятся к двум вариантам. *Either option is acceptable* = любой один из двух; *Neither option is acceptable* = ни один. В отрицательной конструкции *I don't want either option* также означает, что ни один из рассматриваемых вариантов не нужен. После *neither* дополнительное *not* в стандартной конструкции не требуется.",
                [
                    ex("Either route will get us there.", "One of the two routes is sufficient."),
                    ex("Neither route is safe at night.", "Neither of the two is safe."),
                    ex("I don't want either route.", "Negative polarity."),
                ],
            ),
            rule(
                "Any: polarity и free choice",
                "В вопросах и отрицаниях **any** обычно означает неопределённое количество: *Do you have any evidence? I don't have any evidence.* В утвердительном предложении *Any member may object* any может выражать **free choice** — 'любой, безразлично какой'. Эти значения требуют различать polarity и свободный выбор.",
                [
                    ex("Do you have any evidence?", "Interrogative polarity."),
                    ex("I don't have any evidence.", "Negative polarity."),
                    ex("Any member may object.", "Free-choice any."),
                ],
            ),
            rule(
                "Such, so, the very и what little",
                "**Such** определяет noun phrase: *such a delay, such delays*. **So** обычно модифицирует adjective/adverb: *so long, so quickly*. **The very + noun** усиливает идентификацию. **What little + uncountable noun** означает 'то небольшое количество, которое имелось'.",
                [
                    ex("It was such a delay that the ferry missed the tide.", "Such + a + singular count noun."),
                    ex("The evidence was so weak that the claim was withdrawn.", "So + adjective."),
                    ex("What little evidence we had was inconclusive.", "What little + uncountable noun."),
                ],
            ),
        compare=[
            {"left": "Each sample was dated.", "right": "Every sample was dated.", "note": "Each — «по одному»; every — «без исключений»."},
            {"left": "Either of the keys opens the loft.", "right": "Both of the keys are needed for the loft.", "note": "Either — один достаточен; both — нужны два."},
        ],
        watch_out=[
            "Neither … don't — двойное отрицание.",
            "Every of the samples — ошибка.",
            "Every of the samples — ошибка; every one of the samples — нормативно.",
            "Neither уже отрицательно; дополнительный not обычно не нужен.",

        ],
        remember="Each — поштучно (each of). Every — покрытие класса. Either/neither — ровно два. The very — идентичность; quite the — оценка типа.",
    ),
    "advanced-complementation": lesson(
        "**Complementation** описывает синтаксические модели, которые слово допускает после себя. На уровне C2 важно запоминать не только значение лексемы, но и её **valency / complementation pattern**: какие дополнения она принимает, в какой форме и в каком порядке. Семантически близкие слова могут выбирать разные модели: *explain something to somebody*, но *tell somebody something*; *suggest doing / suggest that...*, но не стандартное *suggest somebody to do...*.\n\nОсобое значение имеют различия между **that-clauses**, infinitival clauses и gerund-participial clauses, а также между **raising** и **control**. В raising-конструкции субъект матричной клаузы семантически принадлежит нижней предикации: *She seems to know*. В control-конструкции контролирующий участник является аргументом матричного глагола: *They persuaded her to leave*.\n\n**Extraposition** решает другую задачу: тяжёлая clause переносится вправо, а позиция подлежащего заполняется формальным *it*: *It was a mistake to leave early*. Поэтому продвинутый анализ должен учитывать не только форму, но и valency, семантические роли и информационную нагрузку.",
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
            rule(
                "Remember, regret и смысл complementation",
                "Несколько моделей после одного глагола могут быть грамматически допустимы, но различаться по смыслу. *Remember to lock* относится к действию, которое ещё нужно выполнить; *remember locking* — к воспоминанию о завершённом действии. *Regret to inform* — формальная формула перед сообщением; *regret doing* — сожаление о прошлом действии.",
                [
                    ex("Remember to lock the gate.", "Action still to be performed."),
                    ex("I remember locking the gate.", "Memory of completed action."),
                    ex("We regret to inform you that the bid was unsuccessful.", "Formal reporting formula."),
                    ex("We regret rejecting the bid.", "Regret about a past action."),
                ],
            ),
            rule(
                "Suggest, recommend, prevent, accuse",
                "Некоторые глаголы имеют строго определённые модели. **Suggest** и **recommend** допускают *-ing* и *that-clause*; стандартное *suggest somebody to do* не используется. **Prevent somebody from -ing** и **accuse somebody of -ing** требуют соответствующих предлогов.",
                [
                    ex("They suggested delaying the launch.", "Suggest + -ing."),
                    ex("They suggested that the launch should be delayed.", "Suggest + that-clause."),
                    ex("The rule prevented them from entering.", "Prevent + object + from -ing."),
                    ex("The report accused him of altering the figures.", "Accuse + object + of -ing."),
                ],
            ),
            rule(
                "Explain, tell и promise",
                "**Explain** обычно строится как *explain something to somebody*, тогда как **tell** допускает *tell somebody something*. **Promise** обычно является subject-control verb: *She promised to return*, где she — и обещающий, и подразумеваемый субъект return. Управление нельзя механически переносить из русского языка.",
                [
                    ex("They explained the problem to me.", "Explain + object + to + recipient."),
                    ex("They told me the problem.", "Tell + recipient + object."),
                    ex("She promised to return before noon.", "Subject control."),
                ],
            ),
            rule(
                "Raising vs control: диагностика",
                "В **raising** матричный предикат не даёт поднятому NP собственной semantic role: *She seems to know*. Поэтому возможен вариант с expletive *it*: *It seems that she knows*. В **control** субъект или объект матричного глагола является его аргументом и контролирует подразумеваемый субъект infinitive: *They persuaded her to leave*.",
                [
                    ex("She seems to know the answer.", "Raising."),
                    ex("It seems that she knows the answer.", "Raising counterpart with expletive it."),
                    ex("They persuaded her to leave.", "Object control."),
                ],
                tables=[table(["Конструкция", "Матрица", "Диагностический признак"], [["raising", "seem/appear", "it possible: It seems that…"], ["object control", "persuade/tell", "object controls infinitive subject"], ["subject control", "promise/try", "subject controls infinitive subject"]])],
            ),
            rule(
                "Noun complementation",
                "Существительные также имеют собственные модели: **fact + that**, **decision + to-infinitive**, **ability + to-infinitive**, **difficulty (in) + -ing**, **chance of + -ing / chance that...**. Ошибка *the fact to withdraw* возникает из переноса модели *decision to...* на другое существительное.",
                [
                    ex("The fact that they withdrew surprised no one.", "Fact + that-clause."),
                    ex("Their ability to adapt saved the project.", "Ability + to-infinitive."),
                    ex("We had difficulty in obtaining a spare part.", "Difficulty + in + -ing."),
                    ex("There is a chance of finding another route.", "Chance + of + -ing."),
                ],
            ),
            rule(
                "Extraposition after adjectives and nouns",
                "После оценочных adjectives и некоторых nouns тяжёлая clause может выноситься вправо: *It was unfortunate that the launch was delayed; It was a mistake to leave early*. Прямая структура возможна, но часто тяжелее. Extraposition также следует отличать от raising: *It is likely that she will decline* и *She is likely to decline* семантически близки, но синтаксически различны.",
                [
                    ex("It was unfortunate that the launch was delayed.", "Extraposed that-clause."),
                    ex("It was a mistake to leave early.", "Extraposed to-infinitive."),
                    ex("She is likely to decline.", "Raising adjective."),
                    ex("It is likely that she will decline.", "Extraposition with likely."),
                ],
            ),
        compare=[
            {"left": "She is likely to decline.", "right": "It is likely that she will decline.", "note": "Raising vs extraposition — одна вероятность."},
            {"left": "I'm sorry to interrupt.", "right": "I'm sorry that we interrupted.", "note": "To — жест сейчас; that — факт-событие."},
        ],
        watch_out=[
            "The fact to withdraw — слот не тот.",
            "Explain me / suggest her to — чужой контроль.",
            "Учить слово вместе с его valency и complement pattern.",
            "Raising и control различаются семантическими ролями, а не только переводом.",

        ],
        remember="Слово + слот. Raising поднимает подлежащее. It выносит тяжёлый комплемент. Sorry to ≠ sorry that.",
    ),
}
