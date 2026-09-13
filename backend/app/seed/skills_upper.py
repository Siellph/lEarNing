"""Original C1/C2 (+ a few mid-level) skill materials for lEarNinG."""

from __future__ import annotations


def _q(kind: str, prompt: str, answer: str, **extra) -> dict:
    row = {"kind": kind, "prompt": prompt, "answer": answer, "explanation": extra.get("explanation", "")}
    if "options" in extra:
        row["options"] = extra["options"]
    if "accepted" in extra:
        row["accepted"] = extra["accepted"]
    if "speak" in extra:
        row["speak"] = extra["speak"]
    return row


def _choice(prompt: str, answer: str, options: list[str], explanation: str = "") -> dict:
    return _q("choice", prompt, answer, options=options, explanation=explanation)


def _dictation(prompt: str, answer: str, speak: str, accepted: list[str] | None = None, explanation: str = "") -> dict:
    return _q(
        "dictation",
        prompt,
        answer,
        speak=speak,
        accepted=accepted or [answer],
        explanation=explanation,
    )


def _gap(prompt: str, answer: str, accepted: list[str] | None = None, explanation: str = "") -> dict:
    return _q("fill_gap", prompt, answer, accepted=accepted or [answer], explanation=explanation)


EXTRA_READING: list[dict] = [
    {
        "slug": "reading-b2-urban-noise",
        "title": "Шум в городе",
        "description": "Как соседи договариваются о тишине.",
        "kind": "reading",
        "level_code": "B2",
        "body": (
            "After months of late-night renovations in the building next door, residents of Maple Court formed a small working group. "
            "They did not want a confrontation; they wanted predictable quiet hours and a clearer channel for complaints.\n\n"
            "The group met the site manager with a short list: no drilling after eight in the evening, advance notices for weekend work, "
            "and a shared phone number for urgent issues. The manager agreed to most points and posted a schedule in the lobby.\n\n"
            "Noise did not disappear overnight, but people stopped arguing in the stairwell. "
            "Several neighbours said the written plan made the inconvenience feel temporary rather than endless."
        ),
        "keywords": [
            {"en": "renovation", "ru": "ремонт"},
            {"en": "predictable", "ru": "предсказуемый"},
            {"en": "drilling", "ru": "сверление"},
            {"en": "inconvenience", "ru": "неудобство"},
        ],
        "questions": [
            _choice("What did residents want most?", "predictable quiet hours", ["free rent", "predictable quiet hours", "a new café", "louder music"], "predictable quiet hours"),
            _choice("When should drilling stop?", "after eight in the evening", ["at noon", "after eight in the evening", "never", "only on Mondays"], "no drilling after eight"),
            _choice("What changed socially?", "fewer stairwell arguments", ["everyone moved out", "fewer stairwell arguments", "the building closed", "noise doubled"], "stopped arguing in the stairwell"),
        ],
    },
    {
        "slug": "reading-c1-attention-economy",
        "title": "Экономика внимания",
        "description": "Эссе о привычках уведомлений.",
        "kind": "reading",
        "level_code": "C1",
        "body": (
            "Modern phones are designed to interrupt. A badge, a vibration, a preview line — each signal is small, yet together they train the mind "
            "to treat unfinished tasks as emergencies. Writers who study attention argue that the cost is not only lost minutes, but a thinner ability "
            "to stay with a difficult idea until it becomes clear.\n\n"
            "Some professionals now practise 'notification hygiene': disabling non-essential alerts, batching email twice a day, and keeping one app "
            "off the home screen entirely. The point is not digital purity. It is recovering enough unbroken time to do work that cannot be done "
            "in fragments — drafting, coding, analysing, or simply reading a long article without glancing away.\n\n"
            "Critics reply that constant availability is a job requirement. That may be true in certain roles, yet even then the question remains "
            "who designs the defaults. If tools assume interruption is normal, people must invent their own friction. "
            "A quieter device does not guarantee deeper thought, but a noisy one almost guarantees shallower thought."
        ),
        "keywords": [
            {"en": "interrupt", "ru": "прерывать"},
            {"en": "hygiene", "ru": "гигиена (привычек)"},
            {"en": "batch", "ru": "группировать / пакетировать"},
            {"en": "friction", "ru": "трение / намеренное затруднение"},
            {"en": "default", "ru": "настройка по умолчанию"},
        ],
        "questions": [
            _choice("What do attention writers say is lost besides minutes?", "ability to stay with difficult ideas", ["battery life only", "ability to stay with difficult ideas", "friends", "Wi‑Fi"], "thinner ability to stay with a difficult idea"),
            _choice("What is 'notification hygiene' an example of?", "batching email and disabling alerts", ["buying more phones", "batching email and disabling alerts", "posting more often", "ignoring sleep"], "disabling… batching email"),
            _choice("What do critics claim?", "constant availability can be required", ["phones are illegal", "constant availability can be required", "reading is useless", "defaults never matter"], "job requirement"),
            _choice("What does a noisy device almost guarantee?", "shallower thought", ["deeper thought", "shallower thought", "perfect focus", "no meetings"], "almost guarantees shallower thought"),
        ],
    },
    {
        "slug": "reading-c1-climate-adaptation",
        "title": "Адаптация к климату",
        "description": "Статья о городских мерах, не только о выбросах.",
        "kind": "reading",
        "level_code": "C1",
        "body": (
            "Cities facing hotter summers increasingly discuss adaptation alongside emission cuts. Shade trees, reflective roofs, and public cooling centres "
            "do not replace the need to reduce greenhouse gases, but they can protect vulnerable residents while longer reforms take effect.\n\n"
            "Effective plans tend to combine engineering with social mapping. A heatwave kills more people in poorly insulated flats than in offices with air conditioning; "
            "therefore outreach to elderly neighbours and night-time shelter options matter as much as new asphalt recipes. "
            "Some councils publish simple checklists in several languages so that advice reaches beyond official websites.\n\n"
            "Sceptics worry that adaptation language can become an excuse to delay mitigation. The more careful municipal reports treat the two as partners: "
            "cut emissions where possible, and harden daily life where impacts are already visible. "
            "In that framing, a tree-lined street is both a comfort measure and a long-term investment in liveable density."
        ),
        "keywords": [
            {"en": "adaptation", "ru": "адаптация"},
            {"en": "mitigation", "ru": "смягчение (выбросов) / митигация"},
            {"en": "vulnerable", "ru": "уязвимый"},
            {"en": "insulated", "ru": "утеплённый / изолированный"},
            {"en": "outreach", "ru": "работа с населением / охват"},
        ],
        "questions": [
            _choice("What do hotter cities discuss besides cutting emissions?", "adaptation", ["only tourism", "adaptation", "closing schools forever", "banning trees"], "adaptation alongside emission cuts"),
            _choice("Where can heatwaves be deadlier?", "poorly insulated flats", ["air-conditioned offices", "poorly insulated flats", "parks only", "museums"], "poorly insulated flats"),
            _choice("What do careful reports say about adaptation and mitigation?", "they should work as partners", ["adaptation replaces mitigation", "they should work as partners", "neither matters", "only asphalt matters"], "treat the two as partners"),
        ],
    },
    {
        "slug": "reading-c1-translation-tradeoffs",
        "title": "Компромиссы перевода",
        "description": "О точности, стиле и аудитории.",
        "kind": "reading",
        "level_code": "C1",
        "body": (
            "Translators rarely choose between 'right' and 'wrong' alone; they choose among competing goods. A literal rendering may preserve structure yet sound stiff. "
            "A freer version may read smoothly while blurring a cultural reference that the author meant to keep sharp.\n\n"
            "Audience changes the balance. A legal contract demands caution and consistency; a children's story demands rhythm and clarity. "
            "Machine tools can accelerate drafts, but they still require a human who understands why a joke fails in the target language or why a technical term must stay fixed across chapters.\n\n"
            "Good briefing helps. When clients explain which risks matter most — tone, terminology, or speed — translators can defend decisions instead of guessing. "
            "In that sense, translation is less a mechanical swap of words than a negotiated responsibility for meaning."
        ),
        "keywords": [
            {"en": "literal", "ru": "буквальный"},
            {"en": "rendering", "ru": "вариант перевода / передача"},
            {"en": "blur", "ru": "размывать"},
            {"en": "consistency", "ru": "последовательность / единообразие"},
            {"en": "briefing", "ru": "бриф / вводные"},
        ],
        "questions": [
            _choice("What do translators often choose among?", "competing goods", ["only typos", "competing goods", "fonts", "airports"], "competing goods"),
            _choice("What does a legal contract demand?", "caution and consistency", ["jokes only", "caution and consistency", "maximum freedom", "no terminology"], "caution and consistency"),
            _choice("What helps translators defend decisions?", "clear client briefing on risks", ["ignoring the client", "clear client briefing on risks", "faster machines alone", "random tone"], "Good briefing helps"),
        ],
    },
    {
        "slug": "reading-c2-epistemic-humility",
        "title": "Эпистемическая скромность",
        "description": "Размышление о границах уверенности.",
        "kind": "reading",
        "level_code": "C2",
        "body": (
            "Epistemic humility is not the refusal to know; it is the discipline of noticing how knowledge was produced. "
            "A confident claim may rest on a narrow sample, a misleading graph, or a definition that silently excludes awkward cases. "
            "Humility asks what would falsify the claim, who was not measured, and which assumptions are doing the heaviest work.\n\n"
            "In public debate the opposite habit is common: certainty as performance. Speakers treat doubt as weakness and nuance as delay. "
            "Yet institutions that cannot revise themselves — laboratories, courts, newsrooms — eventually fail the public they claim to serve. "
            "Revision is not hypocrisy when evidence changes; it is the point of inquiry.\n\n"
            "Practised well, humility coexists with expertise. A surgeon can be decisive in theatre and still cautious about a new study’s sample size. "
            "A journalist can publish under deadline and still flag what remains unverified. "
            "The skill is to match the strength of language to the strength of grounds, especially when the audience wants simple villains and neat endings.\n\n"
            "Without that match, persuasion becomes theatre and learning stalls. With it, disagreement can remain sharp without becoming dishonest."
        ),
        "keywords": [
            {"en": "epistemic", "ru": "эпистемический / относящийся к знанию"},
            {"en": "falsify", "ru": "опровергать / фальсифицировать (гипотезу)"},
            {"en": "nuance", "ru": "нюанс / тонкость"},
            {"en": "revision", "ru": "пересмотр"},
            {"en": "grounds", "ru": "основания (для утверждения)"},
        ],
        "questions": [
            _choice("What is epistemic humility mainly about?", "noticing how knowledge was produced", ["refusing all knowledge", "noticing how knowledge was produced", "speaking louder", "avoiding expertise"], "discipline of noticing how knowledge was produced"),
            _choice("What does the text call certainty-as-performance?", "a common opposite habit in debate", ["scientific method", "a common opposite habit in debate", "humility", "surgery"], "opposite habit is common: certainty as performance"),
            _choice("When is revision not hypocrisy?", "when evidence changes", ["never", "when evidence changes", "only in fiction", "when audiences demand it for entertainment"], "when evidence changes"),
            _choice("What should language strength match?", "the strength of grounds", ["the loudest speaker", "the strength of grounds", "the shortest headline", "the oldest book"], "match the strength of language to the strength of grounds"),
        ],
    },
    {
        "slug": "reading-c2-platform-governance",
        "title": "Управление платформами",
        "description": "Статья о правилах, масштабе и прозрачности.",
        "kind": "reading",
        "level_code": "C2",
        "body": (
            "Large digital platforms govern speech at a scale no traditional publisher could manage by hand. "
            "Automated filters catch some harms quickly, yet they also misfire: satire flagged as abuse, urgent medical posts slowed, "
            "or coordinated campaigns slipping through because they adapt faster than classifiers.\n\n"
            "Governance therefore becomes a design problem as much as a moral one. Who appeals a takedown? How long does review take? "
            "Are rules published in plain language, or buried in documents that only specialists read? "
            "Transparency reports help, but only if they reveal error rates and regional differences rather than vanity metrics.\n\n"
            "Regulators face a parallel dilemma. Heavy-handed mandates can push companies toward over-removal, chilling legitimate debate. "
            "Hands-off approaches leave users exposed to scams and harassment. The more promising experiments combine clear illegal-content duties "
            "with procedural rights for users and independent audits of high-risk systems.\n\n"
            "No policy will satisfy every constituency. The test is whether a regime can correct itself when evidence of bias or failure accumulates — "
            "and whether ordinary users can understand, in practice, what speech the platform will actually host."
        ),
        "keywords": [
            {"en": "classifier", "ru": "классификатор (модель)"},
            {"en": "takedown", "ru": "удаление контента"},
            {"en": "chilling", "ru": "охлаждающий (эффект на речь)"},
            {"en": "audit", "ru": "аудит"},
            {"en": "constituency", "ru": "группа интересов / электорат"},
        ],
        "questions": [
            _choice("What can automated filters also do?", "misfire on satire or urgent posts", ["never err", "misfire on satire or urgent posts", "replace all laws", "end debate"], "they also misfire"),
            _choice("When are transparency reports useful?", "when they show error rates and regional differences", ["only vanity metrics", "when they show error rates and regional differences", "when secret", "never"], "error rates and regional differences"),
            _choice("What risk do heavy-handed mandates create?", "over-removal chilling debate", ["perfect speech", "over-removal chilling debate", "no scams ever", "no platforms"], "over-removal, chilling legitimate debate"),
            _choice("What is the practical test of a regime?", "whether it can correct itself and users understand rules", ["whether everyone is happy", "whether it can correct itself and users understand rules", "whether filters are secret", "whether satire is banned"], "correct itself… users can understand"),
        ],
    },
    {
        "slug": "reading-c2-slow-expertise",
        "title": "Медленная экспертиза",
        "description": "Почему глубина плохо стыкуется с лентой новостей.",
        "kind": "reading",
        "level_code": "C2",
        "body": (
            "Expertise is often slow in ways that media cycles dislike. A careful epidemiologist waits for better data; a careful historian resists a viral claim "
            "that flattens a century into a slogan. Meanwhile timelines reward speed, certainty, and emotional clarity.\n\n"
            "The mismatch creates a market for pseudo-expertise: confident voices who summarise complex fields in a tone of finality. "
            "Some are simply mistaken; others are strategically simplifying for attention. Audiences, tired of complexity, may prefer the cleaner story "
            "even when it is less accurate.\n\n"
            "One partial remedy is better signalling. When specialists explain confidence intervals, competing hypotheses, or what would change their mind, "
            "they teach the public how knowledge works rather than only what to believe today. Institutions can help by rewarding correction and "
            "by refusing to treat every unfinished debate as a personal failure.\n\n"
            "Slow expertise will never dominate every feed. It can still remain available, legible, and respected — if we stop confusing volume with validity."
        ),
        "keywords": [
            {"en": "epidemiologist", "ru": "эпидемиолог"},
            {"en": "flatten", "ru": "уплощать / упрощать до плоского"},
            {"en": "pseudo-expertise", "ru": "псевдоэкспертиза"},
            {"en": "hypothesis", "ru": "гипотеза"},
            {"en": "validity", "ru": "обоснованность / валидность"},
        ],
        "questions": [
            _choice("What do media cycles dislike about expertise?", "that it is often slow", ["that it is free", "that it is often slow", "that it uses data", "that historians exist"], "Expertise is often slow"),
            _choice("What does the market for pseudo-expertise reward?", "confident finality over complexity", ["long footnotes only", "confident finality over complexity", "silence", "peer review alone"], "tone of finality"),
            _choice("What is one partial remedy?", "specialists signalling uncertainty and revision conditions", ["banning all media", "specialists signalling uncertainty and revision conditions", "faster slogans", "hiding corrections"], "explain… what would change their mind"),
            _choice("What should we stop confusing?", "volume with validity", ["speed with kindness", "volume with validity", "history with geography", "feeds with food"], "stop confusing volume with validity"),
        ],
    },
]


EXTRA_LISTENING: list[dict] = [
    {
        "slug": "listening-b2-library-quiet-policy",
        "title": "Тишина в библиотеке",
        "description": "Объявление о зонах и звонках.",
        "kind": "listening",
        "level_code": "B2",
        "body": (
            "Please remember that the second floor is a silent study zone. Phone calls should be taken in the stairwell or outside.\n\n"
            "Group work is welcome in rooms three and four after you book them at the desk. "
            "Headphones are required for any audio on personal devices."
        ),
        "keywords": [
            {"en": "silent study", "ru": "тихая учёба / зона тишины"},
            {"en": "stairwell", "ru": "лестничная клетка"},
            {"en": "headphones", "ru": "наушники"},
        ],
        "questions": [
            _choice("Where is the silent zone?", "the second floor", ["the café", "the second floor", "outside only", "room ten"], "second floor is a silent study zone"),
            _choice("Where should phone calls go?", "stairwell or outside", ["silent zone", "stairwell or outside", "group rooms only", "nowhere"], "stairwell or outside"),
            _dictation(
                "Напечатайте правило про наушники.",
                "Headphones are required for any audio on personal devices.",
                "Headphones are required for any audio on personal devices.",
                accepted=[
                    "Headphones are required for any audio on personal devices",
                    "headphones are required for any audio on personal devices",
                ],
            ),
        ],
    },
    {
        "slug": "listening-c1-research-briefing",
        "title": "Брифинг по исследованию",
        "description": "Устный отчёт о выборке и ограничениях.",
        "kind": "listening",
        "level_code": "C1",
        "body": (
            "Our pilot survey reached four hundred and twenty urban respondents, skewed slightly toward people under forty. "
            "We asked about remote-work preferences, commute tolerance, and willingness to pay for a quieter neighbourhood.\n\n"
            "Three findings stand out. First, noise ranked higher than travel time for roughly a third of participants. "
            "Second, hybrid schedules were preferred over fully remote options when managers offered clear office days. "
            "Third, cost still constrained choices more than ideals about green space.\n\n"
            "Please treat the results as directional, not definitive. We under-sampled night-shift workers, and the questionnaire was only in English. "
            "The next round should add a night cohort and a short translated version."
        ),
        "keywords": [
            {"en": "skewed", "ru": "смещённый (о выборке)"},
            {"en": "tolerance", "ru": "терпимость / допустимый уровень"},
            {"en": "directional", "ru": "ориентировочный / указывающий направление"},
            {"en": "cohort", "ru": "когорта / группа выборки"},
        ],
        "questions": [
            _choice("How many respondents were reached?", "four hundred and twenty", ["forty-two", "four hundred and twenty", "four thousand", "twenty"], "four hundred and twenty"),
            _choice("What ranked higher than travel time for about a third?", "noise", ["salary", "noise", "food", "weather"], "noise ranked higher than travel time"),
            _choice("Why are results not definitive?", "under-sampled night-shift workers; English only", ["too many languages", "under-sampled night-shift workers; English only", "no findings", "managers banned surveys"], "under-sampled night-shift… only in English"),
            _dictation(
                "Напечатайте фразу про следующий раунд.",
                "The next round should add a night cohort and a short translated version.",
                "The next round should add a night cohort and a short translated version.",
                accepted=[
                    "The next round should add a night cohort and a short translated version",
                    "the next round should add a night cohort and a short translated version",
                ],
            ),
        ],
    },
    {
        "slug": "listening-c1-mediation-opening",
        "title": "Открытие медиации",
        "description": "Фасилитатор задаёт рамки разговора.",
        "kind": "listening",
        "level_code": "C1",
        "body": (
            "Before we begin, I want to set a few ground rules. Each person will speak without interruption for three minutes. "
            "Then we will summarise what we heard before proposing solutions.\n\n"
            "The goal today is not to declare a winner. It is to identify interests behind positions — what each of you needs in order to feel the agreement is fair. "
            "If emotions rise, we can take a five-minute break rather than escalate.\n\n"
            "Everything said in this room stays confidential unless you both agree otherwise in writing. "
            "Are you willing to proceed on those terms?"
        ),
        "keywords": [
            {"en": "ground rules", "ru": "базовые правила"},
            {"en": "interests", "ru": "интересы (за позициями)"},
            {"en": "escalate", "ru": "обострять / эскалировать"},
            {"en": "confidential", "ru": "конфиденциальный"},
        ],
        "questions": [
            _choice("How long may each person speak without interruption?", "three minutes", ["thirty seconds", "three minutes", "three hours", "all day"], "for three minutes"),
            _choice("What is today's goal?", "identify interests behind positions", ["declare a winner", "identify interests behind positions", "end confidentiality", "skip breaks"], "identify interests behind positions"),
            _choice("When can information leave the room?", "if both agree in writing", ["always", "if both agree in writing", "never ever", "only by phone"], "unless you both agree otherwise in writing"),
            _dictation(
                "Напечатайте вопрос в конце.",
                "Are you willing to proceed on those terms?",
                "Are you willing to proceed on those terms?",
                accepted=["Are you willing to proceed on those terms", "are you willing to proceed on those terms?"],
            ),
        ],
    },
    {
        "slug": "listening-c1-policy-memo-audio",
        "title": "Аудио-мемо по политике",
        "description": "Краткий устный мемо для команды.",
        "kind": "listening",
        "level_code": "C1",
        "body": (
            "This is a short memo on the proposed flexible-hours pilot. Staff may shift their start time by up to ninety minutes if core hours from eleven to three remain covered.\n\n"
            "Managers must publish team coverage on a shared calendar each Monday. "
            "The pilot runs for twelve weeks, after which we will review missed handovers and customer response times.\n\n"
            "Please send objections or edge cases by Thursday noon so legal can update the guidance note."
        ),
        "keywords": [
            {"en": "pilot", "ru": "пилот / пробный запуск"},
            {"en": "core hours", "ru": "основные часы присутствия"},
            {"en": "handover", "ru": "передача дел / смен"},
            {"en": "edge case", "ru": "крайний / пограничный случай"},
        ],
        "questions": [
            _choice("How far may start times shift?", "up to ninety minutes", ["up to nine hours", "up to ninety minutes", "not at all", "all night"], "up to ninety minutes"),
            _choice("What are the core hours?", "eleven to three", ["nine to five only", "eleven to three", "midnight to dawn", "weekends"], "from eleven to three"),
            _choice("How long is the pilot?", "twelve weeks", ["twelve days", "twelve weeks", "twelve years", "one day"], "runs for twelve weeks"),
            _dictation(
                "Напечатайте срок для возражений.",
                "Please send objections or edge cases by Thursday noon so legal can update the guidance note.",
                "Please send objections or edge cases by Thursday noon so legal can update the guidance note.",
                accepted=[
                    "Please send objections or edge cases by Thursday noon so legal can update the guidance note",
                    "please send objections or edge cases by Thursday noon so legal can update the guidance note",
                ],
            ),
        ],
    },
    {
        "slug": "listening-c2-ethics-review",
        "title": "Этический разбор",
        "description": "Устное заключение комиссии.",
        "kind": "listening",
        "level_code": "C2",
        "body": (
            "The ethics board recommends conditional approval of the study. Recruitment materials must disclose that participation will not affect clinical care, "
            "and the consent form should separate research procedures from standard treatment in plain language.\n\n"
            "We also require a clearer data-retention schedule: identifiable audio should be deleted within eighteen months unless a participant renews consent. "
            "Secondary analysis is permitted only for aims listed in the protocol appendix.\n\n"
            "Re-submit the revised packet within three weeks. If those conditions are met, the chair may approve under expedited review without a full reconvening."
        ),
        "keywords": [
            {"en": "disclose", "ru": "раскрывать / сообщать"},
            {"en": "consent", "ru": "согласие"},
            {"en": "retention", "ru": "хранение (данных)"},
            {"en": "expedited", "ru": "ускоренный"},
        ],
        "questions": [
            _choice("What kind of approval is recommended?", "conditional approval", [" unconditional ban", "conditional approval", "secret approval", "no review"], "conditional approval"),
            _choice("How soon should identifiable audio be deleted by default?", "within eighteen months", ["within eighteen days", "within eighteen months", "never", "after ten years only"], "within eighteen months"),
            _choice("When may the chair approve without reconvening?", "if conditions are met (expedited review)", ["always immediately", "if conditions are met (expedited review)", "never", "only after a press conference"], "approve under expedited review"),
            _dictation(
                "Напечатайте срок повторной подачи.",
                "Re-submit the revised packet within three weeks.",
                "Re-submit the revised packet within three weeks.",
                accepted=["Re-submit the revised packet within three weeks", "re-submit the revised packet within three weeks"],
            ),
        ],
    },
    {
        "slug": "listening-c2-macro-brief",
        "title": "Макроэкономический бриф",
        "description": "Аналитик о ставках и рисках.",
        "kind": "listening",
        "level_code": "C2",
        "body": (
            "Markets are pricing a slower path of rate cuts than they did in spring, largely because services inflation has proved stickier than goods inflation. "
            "Our base case still assumes two modest cuts this year, but the balance of risks tilts toward delay if wage growth stays elevated.\n\n"
            "For clients with long liabilities, we prefer not to chase every headline. "
            "Instead, rebalance gradually toward high-quality duration while keeping liquidity for opportunities if volatility spikes.\n\n"
            "Please read the appendix on scenario weights before tomorrow's investment committee. "
            "Questions are welcome in writing by 16:00 so we can address them in the memo addendum."
        ),
        "keywords": [
            {"en": "sticky (inflation)", "ru": "устойчивая / «липкая» (инфляция)"},
            {"en": "base case", "ru": "базовый сценарий"},
            {"en": "duration", "ru": "дюрация"},
            {"en": "volatility", "ru": "волатильность"},
            {"en": "addendum", "ru": "дополнение / аддендум"},
        ],
        "questions": [
            _choice("Why are rate-cut expectations slower than in spring?", "stickier services inflation", ["cheaper goods only", "stickier services inflation", "no markets", "zero wages"], "services inflation has proved stickier"),
            _choice("What is the base case for cuts this year?", "two modest cuts", ["ten emergency cuts", "two modest cuts", "no view", "infinite hikes"], "two modest cuts this year"),
            _choice("What should clients with long liabilities avoid?", "chasing every headline", ["all bonds", "chasing every headline", "liquidity forever", "reading appendices"], "prefer not to chase every headline"),
            _dictation(
                "Напечатайте просьбу про вопросы.",
                "Questions are welcome in writing by 16:00 so we can address them in the memo addendum.",
                "Questions are welcome in writing by 16:00 so we can address them in the memo addendum.",
                accepted=[
                    "Questions are welcome in writing by 16:00 so we can address them in the memo addendum",
                    "questions are welcome in writing by 16:00 so we can address them in the memo addendum",
                ],
            ),
        ],
    },
    {
        "slug": "listening-c2-editorial-standards",
        "title": "Редакционные стандарты",
        "description": "Внутренний аудиогайд для редакции.",
        "kind": "listening",
        "level_code": "C2",
        "body": (
            "When a story relies on a single anonymous source, editors must ask what independent corroboration exists and why anonymity is necessary. "
            "If we cannot answer both questions clearly, we delay publication rather than publish speculative framing.\n\n"
            "Corrections should be prompt, visible, and specific about what changed. "
            "A vague note that 'we updated details' is not enough when a key figure or allegation was wrong.\n\n"
            "Finally, headlines must not overclaim what the body carefully qualifies. "
            "If the article says 'may' and 'according to', the headline cannot quietly upgrade that to certainty."
        ),
        "keywords": [
            {"en": "corroboration", "ru": "подтверждение / корроборация"},
            {"en": "anonymity", "ru": "анонимность"},
            {"en": "allegation", "ru": "утверждение / обвинение (недоказанное)"},
            {"en": "overclaim", "ru": "завышать утверждение"},
        ],
        "questions": [
            _choice("What must editors ask about anonymous sources?", "corroboration and why anonymity is needed", ["only the deadline", "corroboration and why anonymity is needed", "the font size", "ad revenue"], "corroboration… why anonymity is necessary"),
            _choice("What should corrections be?", "prompt, visible, and specific", ["hidden", "prompt, visible, and specific", "poetic only", "delayed a year"], "prompt, visible, and specific"),
            _choice("What must headlines not do?", "overclaim what the body qualifies", ["use verbs", "overclaim what the body qualifies", "match the article", "be short"], "must not overclaim"),
            _dictation(
                "Напечатайте правило про заголовки.",
                "Finally, headlines must not overclaim what the body carefully qualifies.",
                "Finally, headlines must not overclaim what the body carefully qualifies.",
                accepted=[
                    "Finally, headlines must not overclaim what the body carefully qualifies",
                    "finally, headlines must not overclaim what the body carefully qualifies",
                ],
            ),
        ],
    },
]


EXTRA_DIALOGUE: list[dict] = [
    {
        "slug": "dialogue-b2-conference-room",
        "title": "Переговорка",
        "description": "Коллеги бронируют комнату и повестку.",
        "kind": "dialogue",
        "level_code": "B2",
        "body": "Office calendar",
        "lines": [
            {"speaker": "Ana", "text": "Is the glass room free at three?", "ru": "Стеклянная комната свободна в три?"},
            {"speaker": "Ben", "text": "Until half past, then marketing has it.", "ru": "До половины, потом маркетинг."},
            {"speaker": "Ana", "text": "Then let's keep our agenda to twenty minutes.", "ru": "Тогда уложимся в двадцать минут."},
            {"speaker": "Ben", "text": "I'll send three bullets: blockers, owners, next steps.", "ru": "Пришлю три пункта: блокеры, владельцы, следующие шаги."},
            {"speaker": "Ana", "text": "Please invite only people who decide, not the whole channel.", "ru": "Зови только тех, кто решает, не весь канал."},
            {"speaker": "Ben", "text": "Agreed. I'll also attach last week's notes.", "ru": "Согласен. Приложу заметки прошлой недели."},
            {"speaker": "Ana", "text": "If we overrun, we move parking-lot items to Friday.", "ru": "Если не уложимся — парковочные темы в пятницу."},
            {"speaker": "Ben", "text": "Perfect. I'll book it now.", "ru": "Отлично. Сейчас забронирую."},
            {"speaker": "Ana", "text": "Thanks. See you at three sharp.", "ru": "Спасибо. В три минута в минуту."},
            {"speaker": "Ben", "text": "See you. I'll bring printed copies just in case.", "ru": "До встречи. На всякий случай распечатки."},
        ],
        "keywords": [
            {"en": "agenda", "ru": "повестка"},
            {"en": "blocker", "ru": "блокер"},
            {"en": "parking-lot", "ru": "парковка тем / отложенные вопросы"},
        ],
        "questions": [
            _choice("How long should the meeting stay?", "twenty minutes", ["two hours", "twenty minutes", "all afternoon", "one minute"], "keep our agenda to twenty minutes"),
            _gap("Ben: I'll send three bullets: blockers, owners, next ___.", "steps"),
            _gap("Ana: If we overrun, we move parking-lot items to ___.", "Friday"),
        ],
    },
    {
        "slug": "dialogue-c1-vendor-negotiation",
        "title": "Переговоры с поставщиком",
        "description": "Сроки, SLA и цена.",
        "kind": "dialogue",
        "level_code": "C1",
        "body": "Procurement call",
        "lines": [
            {"speaker": "Buyer", "text": "We can renew if you tighten the uptime SLA to 99.9 percent.", "ru": "Продлим, если ужесточите SLA аптайма до 99,9%."},
            {"speaker": "Vendor", "text": "That tier costs more unless we drop weekend on-site support.", "ru": "Такой уровень дороже, если не убрать выезд в выходные."},
            {"speaker": "Buyer", "text": "Remote weekend support is enough; on-site can stay weekdays.", "ru": "Удалённой поддержки в выходные хватит; выезд — в будни."},
            {"speaker": "Vendor", "text": "Then we can hold the price and add the higher SLA.", "ru": "Тогда цену удержим и добавим более высокий SLA."},
            {"speaker": "Buyer", "text": "Please put credits for missed targets in the annex.", "ru": "Пропишите кредиты за срывы в приложении."},
            {"speaker": "Vendor", "text": "Standard is five percent of the monthly fee per incident.", "ru": "Стандарт — пять процентов месячной платы за инцидент."},
            {"speaker": "Buyer", "text": "Make it cumulative up to twenty percent.", "ru": "Сделайте накопительно до двадцати процентов."},
            {"speaker": "Vendor", "text": "Agreed, with a joint review after the first quarter.", "ru": "Согласны, с совместным ревью после первого квартала."},
            {"speaker": "Buyer", "text": "Send the redline by Thursday and we'll sign next week.", "ru": "Пришлите редлайн к четвергу — подпишем на следующей неделе."},
            {"speaker": "Vendor", "text": "Will do. Thanks for the clear priorities.", "ru": "Сделаем. Спасибо за ясные приоритеты."},
        ],
        "keywords": [
            {"en": "uptime", "ru": "аптайм / доступность"},
            {"en": "SLA", "ru": "соглашение об уровне сервиса"},
            {"en": "credit", "ru": "кредит / компенсация по SLA"},
            {"en": "redline", "ru": "правка договора / редлайн"},
        ],
        "questions": [
            _choice("What uptime SLA does the buyer want?", "99.9 percent", ["90 percent", "99.9 percent", "100 forever", "none"], "99.9 percent"),
            _gap("Buyer: Please put ___ for missed targets in the annex.", "credits"),
            _gap("Buyer: Make it cumulative up to ___ percent.", "twenty", accepted=["twenty", "20"]),
            _choice("When should the redline arrive?", "by Thursday", ["next year", "by Thursday", "never", "today only orally"], "by Thursday"),
        ],
    },
    {
        "slug": "dialogue-c1-academic-feedback",
        "title": "Обратная связь по статье",
        "description": "Научный руководитель и аспирант.",
        "kind": "dialogue",
        "level_code": "C1",
        "body": "Supervision meeting",
        "lines": [
            {"speaker": "Supervisor", "text": "Your literature review is thorough, but the research gap appears late.", "ru": "Обзор литературы основательный, но пробел исследования появляется поздно."},
            {"speaker": "Student", "text": "Should I move the gap statement into the second section?", "ru": "Перенести формулировку пробела во второй раздел?"},
            {"speaker": "Supervisor", "text": "Yes — and state what your method uniquely contributes.", "ru": "Да — и укажите, в чём уникальный вклад метода."},
            {"speaker": "Student", "text": "The sample is still small. Will reviewers accept a pilot framing?", "ru": "Выборка ещё мала. Примут ли рецензенты рамку пилота?"},
            {"speaker": "Supervisor", "text": "If you are explicit about limits and next steps, yes.", "ru": "Если явно опишете ограничения и следующие шаги — да."},
            {"speaker": "Student", "text": "I'll add a limitations subsection before the conclusion.", "ru": "Добавлю подраздел ограничений перед заключением."},
            {"speaker": "Supervisor", "text": "Also tighten citations where you paraphrase too closely.", "ru": "И ужесточите цитирование там, где пересказ слишком близкий."},
            {"speaker": "Student", "text": "Understood. I can send a revised draft on Monday.", "ru": "Понял. Правку пришлю в понедельник."},
            {"speaker": "Supervisor", "text": "Focus Monday on structure; style can wait one more round.", "ru": "В понедельник — структура; стиль подождёт ещё раунд."},
            {"speaker": "Student", "text": "Thanks — that priority helps.", "ru": "Спасибо — такой приоритет помогает."},
        ],
        "keywords": [
            {"en": "research gap", "ru": "пробел в исследованиях"},
            {"en": "pilot", "ru": "пилотное исследование"},
            {"en": "limitations", "ru": "ограничения"},
            {"en": "paraphrase", "ru": "пересказывать / парафразировать"},
        ],
        "questions": [
            _choice("What appears too late in the draft?", "the research gap", ["the title", "the research gap", "the fonts", "the appendix only"], "research gap appears late"),
            _gap("Student: I'll add a ___ subsection before the conclusion.", "limitations"),
            _gap("Supervisor: Focus Monday on ___; style can wait one more round.", "structure"),
            _choice("When can a small sample be acceptable?", "with explicit limits and next steps", ["never", "with explicit limits and next steps", "if hidden", "only without methods"], "explicit about limits and next steps"),
        ],
    },
    {
        "slug": "dialogue-c1-incident-retro",
        "title": "Ретро после инцидента",
        "description": "Разбор без поиска виноватых.",
        "kind": "dialogue",
        "level_code": "C1",
        "body": "Engineering retro",
        "lines": [
            {"speaker": "Facilitator", "text": "This is a blameless retro. We want causes and fixes, not villains.", "ru": "Это ретро без обвинений. Нужны причины и фиксы, не злодеи."},
            {"speaker": "Oncall", "text": "The alert fired, but the runbook assumed a deprecated endpoint.", "ru": "Алерт сработал, но ранбук ссылался на устаревший endpoint."},
            {"speaker": "Facilitator", "text": "So detection worked; response guidance was stale.", "ru": "Значит, детекция сработала; инструкция ответа устарела."},
            {"speaker": "Dev", "text": "I'll own rewriting the runbook and adding a quarterly review.", "ru": "Возьму перепись ранбука и ежеквартальный пересмотр."},
            {"speaker": "SRE", "text": "We should also page a second person when error rates exceed two percent.", "ru": "И пейджить второго человека, если ошибки выше двух процентов."},
            {"speaker": "Facilitator", "text": "Any customer-facing follow-up still open?", "ru": "Есть ли ещё открытый клиентский follow-up?"},
            {"speaker": "Support", "text": "Status page is updated; two enterprise clients await a written timeline.", "ru": "Статус-страница обновлена; двум enterprise ждём письменный таймлайн."},
            {"speaker": "Facilitator", "text": "Support owns that email by end of day.", "ru": "Support закрывает письмо до конца дня."},
            {"speaker": "Oncall", "text": "I'll attach logs to the ticket for the postmortem draft.", "ru": "Приложу логи к тикету для черновика постмортема."},
            {"speaker": "Facilitator", "text": "Good. We'll review actions next Tuesday.", "ru": "Хорошо. Экшены посмотрим во вторник."},
        ],
        "keywords": [
            {"en": "blameless", "ru": "без поиска виноватых"},
            {"en": "runbook", "ru": "ранбук / инструкция реакции"},
            {"en": "stale", "ru": "устаревший"},
            {"en": "postmortem", "ru": "разбор инцидента / постмортем"},
        ],
        "questions": [
            _choice("What kind of retro is it?", "blameless", ["blameful", "blameless", "secret", "marketing"], "blameless retro"),
            _gap("Oncall: The alert fired, but the ___ assumed a deprecated endpoint.", "runbook"),
            _gap("Facilitator: So detection worked; response guidance was ___.", "stale"),
            _choice("Who rewrites the runbook?", "Dev", ["Support only", "Dev", "customers", "nobody"], "I'll own rewriting the runbook"),
        ],
    },
    {
        "slug": "dialogue-c2-editorial-dispute",
        "title": "Спор в редакции",
        "description": "Публиковать ли расследование сейчас.",
        "kind": "dialogue",
        "level_code": "C2",
        "body": "Newsroom",
        "lines": [
            {"speaker": "Reporter", "text": "We have two sources, but only one document trail is complete.", "ru": "Есть два источника, но полный документальный след — только у одного."},
            {"speaker": "Editor", "text": "Then we cannot lead with the stronger allegation yet.", "ru": "Тогда пока нельзя выносить более жёсткое обвинение в лид."},
            {"speaker": "Reporter", "text": "If we wait, a rival may publish a thinner version first.", "ru": "Если ждём, конкурент может выйти с более тонкой версией."},
            {"speaker": "Editor", "text": "Speed without corroboration is not a scoop; it's a risk transfer to readers.", "ru": "Скорость без подтверждения — не эксклюзив, а перенос риска на читателей."},
            {"speaker": "Lawyer", "text": "I need the contested paragraphs marked before legal sign-off.", "ru": "Нужны помеченные спорные абзацы до юридического ок."},
            {"speaker": "Reporter", "text": "I'll split the piece: publish the documented strand tonight, hold the rest.", "ru": "Разделю материал: задокументированную линию — сегодня, остальное — позже."},
            {"speaker": "Editor", "text": "Good. Headline must mirror the narrower claim.", "ru": "Хорошо. Заголовок должен зеркалить более узкий тезис."},
            {"speaker": "Reporter", "text": "And we'll note what remains under review.", "ru": "И укажем, что ещё на проверке."},
            {"speaker": "Lawyer", "text": "Send the revised draft within the hour.", "ru": "Пришлите правку в течение часа."},
            {"speaker": "Editor", "text": "Ship only after both of us clear the final PDF.", "ru": "Публикуем только после нашего совместного ок по финальному PDF."},
        ],
        "keywords": [
            {"en": "corroboration", "ru": "подтверждение"},
            {"en": "allegation", "ru": "утверждение / обвинение"},
            {"en": "scoop", "ru": "эксклюзив"},
            {"en": "strand", "ru": "линия / нить сюжета"},
        ],
        "questions": [
            _choice("Why can't they lead with the stronger allegation?", "document trail incomplete", ["no sources", "document trail incomplete", "lawyer is on holiday forever", "headline too short"], "only one document trail is complete"),
            _gap("Editor: Speed without ___ is not a scoop.", "corroboration"),
            _gap("Editor: Headline must mirror the ___ claim.", "narrower"),
            _choice("What will the reporter publish tonight?", "the documented strand", ["everything unverified", "the documented strand", "nothing ever", "only a headline"], "documented strand tonight"),
        ],
    },
    {
        "slug": "dialogue-c2-board-strategy",
        "title": "Стратегия на совете",
        "description": "Рост, маржа и риск репутации.",
        "kind": "dialogue",
        "level_code": "C2",
        "body": "Board meeting",
        "lines": [
            {"speaker": "Chair", "text": "Growth is strong, but churn in the mid-market segment is creeping up.", "ru": "Рост сильный, но отток в mid-market ползёт вверх."},
            {"speaker": "CFO", "text": "Discounting won logos, yet contribution margin slipped two points.", "ru": "Скидки дали логотипы, но маржа вклада упала на два пункта."},
            {"speaker": "CMO", "text": "We can rebalance toward retention campaigns instead of net-new spend.", "ru": "Можем сместить бюджет с net-new на удержание."},
            {"speaker": "Chair", "text": "What reputational risk accompanies aggressive win-back emails?", "ru": "Какой репутационный риск у агрессивных win-back писем?"},
            {"speaker": "CMO", "text": "Fatigue and spam complaints if frequency exceeds two per month.", "ru": "Усталость и жалобы на спам, если чаще двух писем в месяц."},
            {"speaker": "CFO", "text": "I propose a ninety-day test with a hard cap on discounts.", "ru": "Предлагаю тест на 90 дней с жёстким потолком скидок."},
            {"speaker": "Chair", "text": "Approved, provided customer-success owns the save playbook.", "ru": "Одобряю, если customer-success ведёт playbook удержания."},
            {"speaker": "CMO", "text": "We'll report cohort retention weekly to the ops channel.", "ru": "Будем еженедельно отчитываться по когортному retention в ops-канал."},
            {"speaker": "CFO", "text": "And freeze new discount tiers until the test concludes.", "ru": "И заморозить новые уровни скидок до конца теста."},
            {"speaker": "Chair", "text": "Document the decision in the minutes before we adjourn.", "ru": "Зафиксируйте решение в протоколе до закрытия."},
        ],
        "keywords": [
            {"en": "churn", "ru": "отток клиентов"},
            {"en": "contribution margin", "ru": "маржа вклада"},
            {"en": "retention", "ru": "удержание"},
            {"en": "cohort", "ru": "когорта"},
        ],
        "questions": [
            _choice("What is creeping up?", "mid-market churn", ["only cash", "mid-market churn", "board holidays", "spam filters forever"], "churn in the mid-market"),
            _gap("CFO: Discounting won logos, yet contribution ___ slipped two points.", "margin"),
            _gap("CFO: I propose a ninety-day test with a hard ___ on discounts.", "cap"),
            _choice("Who must own the save playbook?", "customer-success", ["only the chair", "customer-success", "no one", "competitors"], "customer-success owns the save playbook"),
        ],
    },
    {
        "slug": "dialogue-c2-climate-panel",
        "title": "Панель о климате",
        "description": "Модератор и эксперты о компромиссах политики.",
        "kind": "dialogue",
        "level_code": "C2",
        "body": "Public panel",
        "lines": [
            {"speaker": "Moderator", "text": "Can adaptation spending dilute pressure to cut emissions?", "ru": "Может ли бюджет на адаптацию ослабить давление снижать выбросы?"},
            {"speaker": "Scientist", "text": "It can, if framed as a substitute. It need not, if budgets are ring-fenced separately.", "ru": "Может, если подавать как замену. Не обязательно, если бюджеты раздельно защищены."},
            {"speaker": "Economist", "text": "Political incentives favour visible local cooling projects over abstract tonne reductions.", "ru": "Политические стимулы любят видимые локальные проекты охлаждения больше абстрактных тонн."},
            {"speaker": "Moderator", "text": "So communication design is part of climate policy?", "ru": "Значит, дизайн коммуникации — часть климатической политики?"},
            {"speaker": "Scientist", "text": "Exactly. People need both heat protection now and a credible path to net zero.", "ru": "Именно. Нужна и защита от жары сейчас, и правдоподобный путь к net zero."},
            {"speaker": "Economist", "text": "I'd add distributional checks: who pays, who benefits, who is left outdoors.", "ru": "Добавил бы проверки распределения: кто платит, кто выигрывает, кто остаётся «на улице»."},
            {"speaker": "Moderator", "text": "What metric should journalists watch next summer?", "ru": "Какую метрику журналистам смотреть следующим летом?"},
            {"speaker": "Scientist", "text": "Excess deaths during heatwaves, not only record temperatures.", "ru": "Избыточную смертность в волны жары, не только рекорды температуры."},
            {"speaker": "Economist", "text": "And whether cooling centres are actually reachable after dark.", "ru": "И доступны ли центры охлаждения реально после наступления темноты."},
            {"speaker": "Moderator", "text": "Thank you — we'll take audience questions next.", "ru": "Спасибо — дальше вопросы зала."},
        ],
        "keywords": [
            {"en": "adaptation", "ru": "адаптация"},
            {"en": "ring-fenced", "ru": "целевым образом защищённый (бюджет)"},
            {"en": "distributional", "ru": "распределительный (эффект)"},
            {"en": "excess deaths", "ru": "избыточная смертность"},
        ],
        "questions": [
            _choice("When can adaptation dilute mitigation pressure?", "if framed as a substitute", ["never", "if framed as a substitute", "only in winter", "if ring-fenced"], "if framed as a substitute"),
            _gap("Scientist: It need not, if budgets are ___ separately.", "ring-fenced"),
            _gap("Scientist: … excess ___ during heatwaves, not only record temperatures.", "deaths"),
            _choice("What should journalists also check about cooling centres?", "reachability after dark", ["logo colours", "reachability after dark", "ticket prices for tourists only", "nothing"], "reachable after dark"),
        ],
    },
]

