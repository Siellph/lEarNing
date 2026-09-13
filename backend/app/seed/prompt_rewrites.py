# -*- coding: utf-8 -*-
"""Old→new prompt rewrites for clearer transform/rewrite instructions.

Used by expand.rewrite_known_prompts to patch live DB rows without wiping data.
Seed sources should already contain the *new* prompts; this map migrates legacy text.
"""

# Exact old prompt → new prompt (Exercises, TestQuestions, ExamQuestions).
PROMPT_REWRITES: dict[str, str] = {
    # --- Flagship feedback case ---
    "Past Simple: She has already called the clinic. Add last Tuesday.": (
        "Перепишите в Past Simple и добавьте в предложение маркер «last Tuesday»: "
        "She has already called the clinic."
    ),
    # --- A1 / plurals / possessives ---
    "one man → ?": "Напишите форму множественного числа: one man → ?",
    "one of / best / bakeries / the / city / in / the": (
        "Соберите предложение (one of the + превосходная): "
        "one of / best / bakeries / the / city / in / the"
    ),
    "Замените: I know Anna. → I know ___.": (
        "Замените имя на объектное местоимение: I know Anna. → I know ___."
    ),
    "our house → это дом ___": "Напишите абсолютное притяжательное: our house → это дом ___",
    "that car → множественное": "Сделайте множественное число: that car → ?",
    "these photos → единственное": "Сделайте единственное число: these photos → ?",
    "I → форма перед существительным": "Напишите притяжательное перед существительным: I → ?",
    "this box → множественное": "Сделайте множественное число: this box → ?",
    "they → перед существительным": "Напишите притяжательное перед существительным: they → ?",
    "those men → единственное": "Сделайте единственное число: those men → ?",
    "one person → ?": "Напишите форму множественного числа: one person → ?",
    "this child → plural subject": (
        "Сделайте подлежащее во множественном числе: this child → ?"
    ),
    "make → past": "Напишите форму Past Simple: make → ?",
    "bring → past": "Напишите форму Past Simple: bring → ?",
    # --- A2 conditionals ---
    "First Conditional: she / miss / the bus / she / not leave / now": (
        "Составьте First Conditional (If + Present, will): "
        "she / miss / the bus / she / not leave / now"
    ),
    "Zero: ice / float / you / drop / it / in water": (
        "Составьте Zero Conditional (If + Present, Present): "
        "ice / float / you / drop / it / in water"
    ),
    # --- B1 ---
    "Second: I don't have a balcony. I don't grow tomatoes.": (
        "Составьте Second Conditional из двух фактов: "
        "I don't have a balcony. I don't grow tomatoes."
    ),
    "Third: I didn't save the draft. I lost the chapter.": (
        "Составьте Third Conditional из двух фактов: "
        "I didn't save the draft. I lost the chapter."
    ),
    "'I don't like fennel.' → She said…": (
        "Передайте косвенной речью от She said: 'I don't like fennel.'"
    ),
    "'Can you swim?' → He asked… (me)": (
        "Передайте косвенным вопросом от He asked me: 'Can you swim?'"
    ),
    "'Why are you laughing?' → She asked…": (
        "Передайте косвенным вопросом от She asked: 'Why are you laughing?'"
    ),
    "Defining: That's the café. We found the cat there.": (
        "Объедините в defining relative clause с where: "
        "That's the café. We found the cat there."
    ),
    # --- B2 / C1 / C2 ---
    "Wh-cleft: The humidity damaged the prints.": (
        "Перепишите как wh-cleft (What … was …): The humidity damaged the prints."
    ),
    "Blame: They said the washer caused the failure. → They blamed the failure…": (
        "Перепишите с blame … on …: They said the washer caused the failure."
    ),
    "Требование: She must attend. → They requested that…": (
        "Перепишите требование через requested that + subjunctive: She must attend."
    ),
    "Уточните this: Fog delayed us. This was annoying. → This ___ wrecked the drone window.": (
        "Уточните this (this + N): Fog delayed us. This was annoying. "
        "→ This ___ wrecked the drone window."
    ),
    "Heavy shift: We sent the entire unredacted correspondence from March to legal.": (
        "Сделайте heavy NP shift (вынесите тяжёлое дополнение в конец): "
        "We sent the entire unredacted correspondence from March to legal."
    ),
    "Raising: It is likely that she will decline.": (
        "Перепишите с raising (She is likely to …): It is likely that she will decline."
    ),
    "Extraposition: To freeze the branch before legal signed was a mistake.": (
        "Перепишите с extraposition (It was a mistake to …): "
        "To freeze the branch before legal signed was a mistake."
    ),
    "Принуждение: The coach insisted we rerun the scene. → The coach ___ us rerun the scene.": (
        "Перепишите с make + person + bare infinitive: "
        "The coach insisted we rerun the scene. → The coach ___ us rerun the scene."
    ),
    "Формально: the stool she perched on → the stool ___ she perched.": (
        "Перепишите формально (предлог + which): "
        "the stool she perched on → the stool ___ she perched."
    ),
    # --- extra exams ---
    "Second conditional: I don't have money. I don't buy it.": (
        "Составьте Second Conditional из двух фактов: "
        "I don't have money. I don't buy it."
    ),
    "Mixed conditional: I didn't study. I don't have a job now.": (
        "Составьте Mixed Conditional (past → present): "
        "I didn't study. I don't have a job now."
    ),
    "Cleft: Mary sent the email.": (
        "Перепишите как it-cleft (It was … who …): Mary sent the email."
    ),
    "Fronting: I have never felt so cold.": (
        "Перепишите с фронтированием Never … (инверсия): I have never felt so cold."
    ),
    "Reduced relative: Students who are taught well succeed.": (
        "Сократите relative clause (Students taught …): "
        "Students who are taught well succeed."
    ),
    "Inversion: The speech was so dull that people left.": (
        "Перепишите с инверсией So … that: The speech was so dull that people left."
    ),
    "Ellipsis reply: A: She can dance. B: And sing too.": (
        "Дополните эллипсис в ответе B (And so can / And … too): "
        "A: She can dance. B: And sing too."
    ),
    # --- topic_banks_adv ---
    "Just now finished: I ___ the report. (finish)": (
        "Вставьте Present Perfect (только что закончили): I ___ the report. (finish)"
    ),
    "Earlier past: When I arrived, the train ___ . (leave)": (
        "Вставьте Past Perfect (к моему приходу уже): When I arrived, the train ___ . (leave)"
    ),
    "2nd: If we lived nearer → we ___ meet more often.": (
        "Second Conditional: вставьте would: If we lived nearer → we ___ meet more often."
    ),
    "3rd: If they had invited me → I ___ have gone.": (
        "Third Conditional: вставьте would: If they had invited me → I ___ have gone."
    ),
    "'I am busy' → He said he ___ busy.": (
        "Косвенная речь: вставьте сдвиг времени: 'I am busy' → He said he ___ busy."
    ),
    "'Are you OK?' → He asked if I ___ OK.": (
        "Косвенный вопрос: вставьте форму: 'Are you OK?' → He asked if I ___ OK."
    ),
    "Passive: They built the bridge.": "Перепишите в Passive: They built the bridge.",
    "Defining: students + study hard →": (
        "Составьте defining relative clause: students + study hard → ?"
    ),
    "enjoy + ?": "Какая форма после enjoy: enjoy + ? (-ing / to)",
    "They were late, ___ they?": "Добавьте question tag: They were late, ___ they?",
    "Passive: Someone has stolen my bike.": (
        "Перепишите в Passive: Someone has stolen my bike."
    ),
    "Past cause → present: If we had left earlier, we ___ be there now.": (
        "Mixed Conditional (прошлое → настоящее): вставьте would: "
        "If we had left earlier, we ___ be there now."
    ),
    "Reporting: People believe she left → She is believed ___ left.": (
        "Перепишите reporting passive: People believe she left → She is believed ___ left."
    ),
    "Causative: Someone cleaned my car.": (
        "Перепишите в causative (have/get something done): Someone cleaned my car."
    ),
    "After she finished → ___ finished, she left.": (
        "Замените на participle clause: After she finished → ___ finished, she left."
    ),
    "Emphasis on time: I met her in 2019 → It was in 2019 ___ I met her.": (
        "Сделайте it-cleft на время: I met her in 2019 → It was in 2019 ___ I met her."
    ),
    "I'd sooner ___ at home. (stay)": (
        "Вставьте форму после I'd sooner: I'd sooner ___ at home. (stay)"
    ),
    "Quantified: many of ___ were late": (
        "Вставьте местоимение после many of: many of ___ were late"
    ),
    "since 2018: We ___ here. (live)": (
        "Вставьте Present Perfect (since 2018): We ___ here. (live)"
    ),
    "How long: ___ you been learning French?": (
        "Начните вопрос How long: ___ you been learning French?"
    ),
    "By midnight: They ___ . (leave)": (
        "Вставьте Future Perfect (by midnight): They ___ . (leave)"
    ),
    "Результат: If they had asked → I ___ have agreed.": (
        "Third Conditional: вставьте would: If they had asked → I ___ have agreed."
    ),
    "'We have finished' → They said they ___ finished.": (
        "Косвенная речь: вставьте сдвиг: 'We have finished' → They said they ___ finished."
    ),
    "'Can you drive?' → She asked if I ___ drive.": (
        "Косвенный вопрос: вставьте форму: 'Can you drive?' → She asked if I ___ drive."
    ),
    "Passive: They cancelled the show.": "Перепишите в Passive: They cancelled the show.",
    "Defining: the people + live next door": (
        "Составьте defining relative clause: the people + live next door"
    ),
    "finish + ?": "Какая форма после finish: finish + ? (-ing / to)",
    "I don't have a car → I wish I ___ a car.": (
        "Перепишите желание с wish: I don't have a car → I wish I ___ a car."
    ),
    "They've left, ___ they?": "Добавьте question tag: They've left, ___ they?",
    "Wish: I don't know → I wish I ___.": (
        "Перепишите желание с wish: I don't know → I wish I ___."
    ),
    "Жалоба на настоящее: I don't know → I wish I ___.": (
        "Жалоба на настоящее с wish: I don't know → I wish I ___."
    ),
    "If we had left earlier → we ___ be there now.": (
        "Mixed Conditional: вставьте would: If we had left earlier → we ___ be there now."
    ),
    "Past regret: I wish I ___ gone.": (
        "Вставьте Past Perfect после wish (сожаление о прошлом): I wish I ___ gone."
    ),
    "Weak past: They ___ have missed the turn. (might)": (
        "Вставьте модальный вывод о прошлом (might have): They ___ have missed the turn."
    ),
    "Unnecessary: You ___ have bought so much. (needn't)": (
        "Вставьте needn't have (действие было лишним): You ___ have bought so much."
    ),
    "People think he lied → He is thought ___ lied.": (
        "Перепишите reporting passive: People think he lied → He is thought ___ lied."
    ),
    "Someone painted our house → We ___ our house painted.": (
        "Перепишите в causative: Someone painted our house → We ___ our house painted."
    ),
    "Reduced: the people who live here → the people ___ here": (
        "Сократите relative clause: the people who live here → the people ___ here"
    ),
    "Had-inversion: If I had known → ___ I known": (
        "Сделайте инверсию Had + S: If I had known → ___ I known"
    ),
    "It-cleft time: It was in 2019 ___ we met.": (
        "Вставьте связку it-cleft: It was in 2019 ___ we met."
    ),
    "Background: Birds ___ . (sing)": (
        "Вставьте Past Continuous (фон): Birds ___ . (sing)"
    ),
    "I'd sooner ___ alone. (be)": (
        "Вставьте форму после I'd sooner: I'd sooner ___ alone. (be)"
    ),
    "many of ___ applied": "Вставьте местоимение после many of: many of ___ applied",
    # --- topic_banks_c ---
    "Front object: His advice I ignored. → смысл": (
        "Объясните фронтирование объекта одной фразой: His advice I ignored."
    ),
    "Suggest: She suggested that he ___ earlier. (arrive)": (
        "Вставьте subjunctive после suggested that: She suggested that he ___ earlier. (arrive)"
    ),
    "Strong → hedged: The plan will fail → The plan ___ fail.": (
        "Ослабьте утверждение (hedge): The plan will fail → The plan ___ fail."
    ),
    "Nominalise: They refused → their ___": (
        "Сделайте номинализацию: They refused → their ___"
    ),
    "Avoid repeat: She bought one and I bought one → I bought ___ too.": (
        "Избегите повтора (one/so): She bought one and I bought one → I bought ___ too."
    ),
    "Had-inversion: If she had known → ___ she known": (
        "Сделайте инверсию Had + S: If she had known → ___ she known"
    ),
    "Postmodify: the report + published yesterday": (
        "Добавьте постмодификатор: the report + published yesterday → ?"
    ),
    "warn: She warned me ___ go alone. (not to)": (
        "Вставьте not to после warn: She warned me ___ go alone."
    ),
    "Contrast: I lived there (finished) vs I ___ there since 2010.": (
        "Вставьте Present Perfect для контраста: I lived there (finished) vs I ___ there since 2010."
    ),
    "Neutral→formal: get → ___": "Подберите более формальный синоним: get → ___",
    "Contrast linker: On the ___ hand…": "Вставьте связку контраста: On the ___ hand…",
    "Source: According ___ the report…": "Вставьте предлог: According ___ the report…",
    "Front: The yacht sailed into the bay. → Into the bay ___ the yacht.": (
        "Сделайте фронтирование PP + инверсию: "
        "The yacht sailed into the bay. → Into the bay ___ the yacht."
    ),
    "Adjective + to: likely / unlikely → He is likely ___ win.": (
        "Вставьте to-infinitive после likely: He is likely ___ win."
    ),
    "Cleft: I need rest → What I need ___ rest.": (
        "Сделайте wh-cleft: I need rest → What I need ___ rest."
    ),
    "Passive: It is important that he ___ informed. (be)": (
        "Вставьте subjunctive passive: It is important that he ___ informed. (be)"
    ),
    "People say she left → She is said ___ left.": (
        "Перепишите reporting passive: People say she left → She is said ___ left."
    ),
    "Hedge noun: There is a ___ that costs will rise.": (
        "Вставьте hedge-существительное: There is a ___ that costs will rise."
    ),
    "fail → ___": "Сделайте номинализацию: fail → ___",
    "Neither: I don't agree → Neither ___ I.": (
        "Перепишите с Neither + aux + S: I don't agree → Neither ___ I."
    ),
    "Were it not ___ your help, we'd fail.": (
        "Вставьте предлог: Were it not ___ your help, we'd fail."
    ),
    "Premodify: surprisingly + high + costs": (
        "Соберите premodification: surprisingly + high + costs → ?"
    ),
    "discourage: They discouraged us ___ applying. (from)": (
        "Вставьте from после discourage: They discouraged us ___ applying."
    ),
    "Concession: Hard ___ she tried, she failed.": (
        "Вставьте as/though в concession fronting: Hard ___ she tried, she failed."
    ),
    "Temporary vs permanent: stay / live": (
        "Выберите глагол для временного vs постоянного: stay / live — что для temporary?"
    ),
    "Informal 'a lot of' → formal": (
        "Замените informal «a lot of» на формальный вариант → ?"
    ),
    "Additive: In ___, …": "Вставьте additive linker: In ___, …",
    "Seem: The plan ___ to have failed.": (
        "Вставьте seems/appears: The plan ___ to have failed."
    ),
    "Front PP: On the desk ___ a letter.": (
        "Вставьте глагол при фронтировании PP: On the desk ___ a letter."
    ),
    "Adj + prep: capable ___ solving": "Вставьте предлог: capable ___ solving",
    # --- topic_banks_upper ---
    "Сейчас: I work → Continuous": (
        "Перепишите в Present Continuous: I work → ?"
    ),
    "Спонтанно: The phone is ringing. → I ___ get it.": (
        "Спонтанное решение: вставьте will: The phone is ringing. → I ___ get it."
    ),
    "good → сравнительная": "Напишите сравнительную степень: good → ?",
    "interesting → превосходная": "Напишите превосходную степень: interesting → ?",
    "apple → неисчисляемое? нет →": (
        "Исчисляемое apple: напишите форму с артиклем или множественное → ?"
    ),
    "Обязанность: wear a uniform → You ___ wear a uniform.": (
        "Выразите обязанность (have to/must): wear a uniform → You ___ wear a uniform."
    ),
    "First: If we leave now → we ___ catch the bus.": (
        "First Conditional: вставьте will: If we leave now → we ___ catch the bus."
    ),
    "Passive: They clean the room.": "Перепишите в Passive: They clean the room.",
    "Примета: The baby is crying. → He ___ wake up Dad.": (
        "Примета/намерение: вставьте be going to: The baby is crying. → He ___ wake up Dad."
    ),
    "bad → сравнительная": "Напишите сравнительную степень: bad → ?",
    "far → превосходная (BrE)": "Напишите превосходную степень (BrE): far → ?",
    "Отрицание: some →": "В отрицании замените some → ?",
    "First: If I miss the bus → I ___ take a taxi.": (
        "First Conditional: вставьте will: If I miss the bus → I ___ take a taxi."
    ),
    "Passive: Someone locked the door.": "Перепишите в Passive: Someone locked the door.",
    # --- word_order ---
    "Косвенно: 'Where do you work?' → He asked where I ___.": (
        "Косвенный вопрос: вставьте порядок слов: 'Where do you work?' → He asked where I ___."
    ),
    "'Are you ready?' → She asked if I ___ ready.": (
        "Косвенный вопрос: вставьте форму: 'Are you ready?' → She asked if I ___ ready."
    ),
    # --- b2 mixed (already partly RU but terse arrows) ---
    "Смешайте: прошлый отказ от курса → сейчас нет сертификата. If I / take / the course → I / have / a certificate now.": (
        "Составьте Mixed Conditional (прошлое условие → нынешний результат). "
        "Факт: прошлый отказ от курса → сейчас нет сертификата. "
        "Слова: If I / take / the course ; I / have / a certificate now."
    ),
    "Смешайте: он не бережлив (сейчас) → вчера истратил всю премию.": (
        "Составьте Mixed Conditional (устойчивая черта сейчас → прошлый результат): "
        "он не бережлив (сейчас) → вчера истратил всю премию."
    ),
}

# Merge exam / fill-blank gap instruction rewrites (A1 can-gap etc.).
from app.seed.exam_gap_rewrites import EXAM_GAP_REWRITES  # noqa: E402
from app.seed.test_gap_rewrites import TEST_GAP_REWRITES  # noqa: E402

for _old, _new in EXAM_GAP_REWRITES.items():
    PROMPT_REWRITES.setdefault(_old, _new)
for _old, _new in TEST_GAP_REWRITES.items():
    PROMPT_REWRITES.setdefault(_old, _new)

# Safety: collapse accidental double-prefixed prompts if any landed in a DB.
_DOUBLE_FIXES = {
    "Перепишите в Перепишите в Passive: They built the bridge.": (
        "Перепишите в Passive: They built the bridge."
    ),
    "Перепишите в Перепишите в Passive: They clean the room.": (
        "Перепишите в Passive: They clean the room."
    ),
    "Перепишите в Перепишите в Passive: Someone locked the door.": (
        "Перепишите в Passive: Someone locked the door."
    ),
    "Перепишите в Перепишите в Passive: Someone has stolen my bike.": (
        "Перепишите в Passive: Someone has stolen my bike."
    ),
    "Перепишите в Перепишите в Passive: They cancelled the show.": (
        "Перепишите в Passive: They cancelled the show."
    ),
    "Косвенная речь: вставьте сдвиг времени: Косвенная речь: вставьте сдвиг времени: 'I am busy' → He said he ___ busy.": (
        "Косвенная речь: вставьте сдвиг времени: 'I am busy' → He said he ___ busy."
    ),
    "Косвенная речь: вставьте сдвиг: Косвенная речь: вставьте сдвиг: 'We have finished' → They said they ___ finished.": (
        "Косвенная речь: вставьте сдвиг: 'We have finished' → They said they ___ finished."
    ),
}
PROMPT_REWRITES.update(_DOUBLE_FIXES)

# Optional explanation overrides when rewriting (old prompt → new explanation).
EXPLANATION_REWRITES: dict[str, str] = {
    "Past Simple: She has already called the clinic. Add last Tuesday.": (
        "Точная дата вытесняет Present Perfect. В ответе обязательно нужен маркер "
        "«last Tuesday»: She called the clinic last Tuesday."
    ),
    "She ___ play the piano.": (
        "Can не меняется по лицам: she can. Нужен именно модальный can, не отрицание don't/doesn't."
    ),
}
