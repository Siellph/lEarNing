"""Extra practice/test banks keyed by module slug + generic CEFR pads.

Practice and test banks are intentionally separate: expanders never copy practice into tests.
"""

from app.seed.helpers import err, fill, match, mc, order, xf

# --- Per-module extras (high-traffic A1 topics) ---

EXTRA_PRACTICE: dict[str, list] = {
    "articles-a1": [
        fill("I bought ___ umbrella.", "an", "Umbrella — гласный звук."),
        fill("___ Earth goes round the sun.", "The", "Уникальный объект."),
        mc("She wants ___ orange.", ["a", "an", "the"], "an", "Orange — гласный звук."),
        err("He is a honest man.", "He is an honest man.", "Honest начинается с гласного звука."),
        fill("Open ___ window, please. (конкретное)", "the", "Оба видят окно.", ["Open the window", "Open the window."]),
        mc("I don't drink ___ coffee.", ["a", "an", "— (нулевой)"], "— (нулевой)", "Неисчисляемое в общем смысле."),
        order("Соберите: door / the / close", "Close the door.", "Повелительное + the."),
        fill("She is ___ teacher.", "a", "Профессия в ед.ч. — a/an."),
        xf("Вставьте: ___ Alps are high.", "The Alps are high.", "Горные цепи — the."),
        match("Соотнесите: a / an / the", ["a book", "an hour", "the moon"], "a book=a; an hour=an; the moon=the", "Звук и уникальность."),
        fill("Pass me ___ pen on the desk.", "the", "Конкретная ручка."),
        err("I saw a interesting film.", "I saw an interesting film.", "Interesting — гласный звук."),
        fill("___ water is cold. (эта, в стакане)", "The", "Конкретная порция."),
        mc("___ cats like fish. (вообще)", ["The", "A", "— (нулевой)"], "— (нулевой)", "Класс в общем."),
        fill("Close ___ door.", "the", "Конкретная дверь.", ["Close the door", "Close the door."]),
    ],
    "nouns-plurals": [
        fill("one knife — two ___", "knives", "f/fe → ves."),
        mc("mouse →", ["mouses", "mice", "mouse"], "mice", "Особая форма."),
        err("three childs", "three children", "children."),
        order("Слова: are / children / happy / the", "The children are happy.", "The + N + be + adj."),
        fill("one leaf — many ___", "leaves", "f → ves."),
        mc("This ___ is mine.", ["books", "book", "bookes"], "book", "Ед.ч. this + N."),
        xf("Напишите форму множественного числа: one person → ?", "people", "Особая форма."),
        fill("two ___ of bread", "loaves", "loaf → loaves."),
        err("five deers", "five deer", "deer не меняется."),
        fill("a story — three ___", "stories", "y → ies."),
    ],
    "past-simple-verbs": [
        fill("She ___ home early. (go)", "went", "go — went — gone."),
        mc("They ___ the window. (break, past)", ["breaked", "broke", "broken"], "broke", "V2."),
        err("He buyed a ticket.", "He bought a ticket.", "buy — bought."),
        fill("I ___ the email yesterday. (write)", "wrote", "write — wrote — written."),
        order("Соберите: did / you / see / her", "Did you see her?", "Did + V1."),
        xf("Напишите форму Past Simple: make → ?", "made", "make — made — made."),
        fill("We ___ lunch at 2. (have)", "had", "have — had — had."),
        mc("She ___ the keys. (find, past)", ["finded", "found", "founded"], "found", "find — found."),
        fill("He ___ to Paris last year. (fly)", "flew", "fly — flew — flown."),
        err("They taked the bus.", "They took the bus.", "take — took."),
    ],
    "word-order-a1": [
        order("Соберите: she / tea / drinks / often", "She often drinks tea.", "Подлежащее + частота + V."),
        fill("They ___ in London. (live)", "live", "S + V + place."),
        mc("Правильный порядок:", ["Likes she coffee?", "Does she like coffee?", "She does like coffee?"], "Does she like coffee?", "Do/Does + S + V1."),
        err("I every day go there.", "I go there every day.", "Частота в конце или перед V."),
        order("Слова: is / the / on / book / table / the", "The book is on the table.", "S + be + prep + place."),
        fill("___ you speak English?", "Do", "Do + you + V1."),
        xf("Переставьте: rarely / he / smiles", "He rarely smiles.", "Наречие частоты перед смысловым V."),
        match("Части предложения", ["She", "reads", "books"], "She=S; reads=V; books=O", "SVO."),
    ],
}

EXTRA_TEST: dict[str, list] = {
    "articles-a1": [
        fill("Вставьте артикль: Please shut ___ gate. (одно на участке)", "the", "Конкретный объект.", ["Please shut the gate", "Please shut the gate."]),
        mc("Выберите артикль: I need ___ hour to finish.", ["a", "an", "the"], "an", "Hour — гласный звук."),
        err("She bought a apple.", "She bought an apple.", "Apple — гласный."),
        fill("Вставьте артикль: ___ Nile is long.", "The", "Реки — the."),
        order("Соберите: give / me / salt / the", "Give me the salt.", "Просьба + the."),
        mc("Выберите артикль: He never eats ___ meat.", ["a", "the", "— (нулевой)"], "— (нулевой)", "Общее неисчисляемое."),
        fill("Вставьте артикль: She is ___ university student.", "a", "University — /j/ согласный звук."),
        xf("Любой билет: I need ___ ticket.", "I need a ticket.", "Неопределённый."),
        fill("Вставьте артикль: Look at ___ sky!", "the", "Уникальный объект."),
        err("An useful tip helped me.", "A useful tip helped me.", "Useful — /j/."),
        fill("Вставьте артикль: Put it on ___ shelf. (эта полка)", "the", "Конкретная полка."),
        mc("Выберите артикль: ___ Japanese is difficult. (язык)", ["The", "A", "— (нулевой)"], "— (нулевой)", "Языки без артикля."),
        fill("Вставьте артикль: I saw ___ owl at night.", "an", "Owl — гласный."),
        match("Выберите артикль", ["___ sun", "___ idea", "___ milk (вообще)"], "the; an; —", "Уникальность / впервые / общее."),
        order("Слова: open / door / the", "Open the door.", "Повелительное + the."),
    ],
    "nouns-plurals": [
        fill("Вставьте форму множественного числа: one wolf — two ___", "wolves", "f → ves."),
        mc("tooth →", ["tooths", "teeth", "toothes"], "teeth", "Особая форма."),
        err("many informations", "much information", "information неисчисляемое."),
        fill("Вставьте форму множественного числа: a potato — two ___", "potatoes", "+es после o."),
        order("Соберите: sheep / are / in / field / the", "The sheep are in the field.", "sheep без -s."),
        xf("Сделайте подлежащее во множественном числе: this child → ?", "these children", "this→these, child→children."),
        fill("Вставьте форму множественного числа: one life — several ___", "lives", "f → ves."),
        mc("Выберите форму to be: The police ___ coming.", ["is", "are", "be"], "are", "Police — множественное."),
        fill("Вставьте форму множественного числа: one quiz — two ___", "quizzes", "z → zzes."),
        err("three gooses", "three geese", "goose — geese."),
    ],
    "past-simple-verbs": [
        fill("Вставьте форму Past Simple: They ___ the news. (hear, past)", "heard", "hear — heard — heard."),
        mc("Выберите форму Past Simple: She ___ a letter. (send, past)", ["sended", "sent", "send"], "sent", "send — sent."),
        err("I catched the ball.", "I caught the ball.", "catch — caught."),
        fill("Вставьте форму Past Simple: He ___ the truth. (know, past)", "knew", "know — knew — known."),
        order("Соберите: when / did / leave / they", "When did they leave?", "Wh + did + S + V1."),
        xf("Напишите форму Past Simple: bring → ?", "brought", "bring — brought."),
        fill("Вставьте нужную форму (see): We ___ the museum. (see)", "saw", "see — saw — seen."),
        mc("Выберите форму Past Simple: I ___ my phone. (lose, past)", ["losed", "lost", "losen"], "lost", "lose — lost."),
        fill("Вставьте форму Past Simple: She ___ carefully. (drive, past)", "drove", "drive — drove — driven."),
        err("He putted the bag down.", "He put the bag down.", "put — put — put."),
    ],
    "word-order-a1": [
        order("Соберите: usually / breakfast / I / eat / at 8", "I usually eat breakfast at 8.", "S + frequency + V + O + time."),
        fill("Выберите вспомогательный глагол: ___ she work here?", "Does", "Does + he/she + V1."),
        mc("Выберите верное:", ["Where you live?", "Where do you live?", "Where live you?"], "Where do you live?", "Wh + do + S + V."),
        err("Speaks he French?", "Does he speak French?", "Do/Does в вопросе."),
        order("Слова: never / late / is / she", "She is never late.", "be + частота."),
        fill("Вставьте предлог: They live ___ Moscow.", "in", "in + city."),
        xf("Переставьте: tomorrow / we / leave", "We leave tomorrow.", "Время обычно в конце."),
        match("Роли", ["Do", "you", "swim"], "Do=aux; you=S; swim=V", "Вопрос Present Simple."),
    ],
}

# Deprecated CEFR-wide pads (were injecting off-topic tips into every thin module).
# On-topic pads live in topic_banks.py / EXTRA_* by slug. Kept empty for import compat.
GENERIC_PRACTICE_PAD: dict[str, list] = {}
GENERIC_TEST_PAD: dict[str, list] = {}


def practice_bank_for(slug: str) -> list:
    """Module-specific extras + on-topic topic pads (never CEFR-wide)."""
    from app.seed.topic_banks import TOPIC_PRACTICE

    return list(EXTRA_PRACTICE.get(slug, [])) + list(TOPIC_PRACTICE.get(slug, []))


def test_bank_for(slug: str) -> list:
    from app.seed.topic_banks import TOPIC_TEST

    return list(EXTRA_TEST.get(slug, [])) + list(TOPIC_TEST.get(slug, []))

