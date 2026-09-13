"""CEFR word-order modules injected idempotently by slug."""

from app.seed.helpers import SOURCES, err, fill, lesson, match, mc, module, order, rule, xf, ex

WORD_ORDER_MODULES = [
    {
        **module(
            "word-order-a1",
            "Порядок слов в простом предложении",
            "Базовый порядок S–V–O, вопросы с do/does, место наречий частоты и обстоятельств.",
            25,
            "Кто — что делает — с чем",
            lesson(
                "В утвердительном предложении английский держит жёсткий порядок: подлежащее → сказуемое → дополнение → место → время. Это ядро A1 по CEFR и British Council Grammar.",
                [
                    rule(
                        "Утверждение S–V–O",
                        "I drink tea. She reads books. Нельзя ставить дополнение перед глаголом: *Tea I drink — ошибка в нейтральном стиле.",
                        [ex("They watch films.", "Они смотрят фильмы."), ex("Tom opens the door.", "Том открывает дверь.")],
                    ),
                    rule(
                        "Вопросы Present Simple",
                        "Do/Does + подлежащее + V1: Do you live here? Does she work? Wh-слово встаёт впереди: Where do you live?",
                        [ex("Do they speak English?", "Они говорят по-английски?"), ex("What does he want?", "Чего он хочет?")],
                    ),
                    rule(
                        "Наречия частоты",
                        "Перед смысловым глаголом: She often cooks. После be: She is never late. Обстоятельства места и времени обычно в конце.",
                        [ex("I usually walk home.", "Я обычно иду домой пешком."), ex("We meet at six.", "Мы встречаемся в шесть.")],
                    ),
                ],
                watch_out=["Не ставьте do перед подлежащим в утверждении.", "В вопросе после does глагол без -s."],
                remember="S–V–O. Вопросы: Do/Does + S + V1. Частота — перед V или после be.",
            ),
            [
                order("Соберите: drinks / coffee / she / every morning", "She drinks coffee every morning.", "S + V + O + time."),
                fill("___ you like jazz?", "Do", "Do + you + V1."),
                mc("Правильный порядок:", ["Often she is late.", "She is often late.", "She often is late."], "She is often late.", "Частота после be."),
                err("Lives he in Berlin?", "Does he live in Berlin?", "Does + S + V1."),
                order("Слова: the / window / open / please", "Please open the window.", "Please + imperative + O."),
                fill("She is ___ rarely late. (be)", "is", "be + частота."),
                xf("Переставьте: at home / stay / they / usually", "They usually stay at home.", "S + frequency + V + place."),
                match("Роли в I read books", ["I", "read", "books"], "I=S; read=V; books=O", "SVO."),
                fill("Where ___ she work?", "does", "Wh + does + S + V1."),
                err("I every day check email.", "I check email every day.", "Время в конце или частота перед V."),
            ],
            [
                order("Соберите: never / eats / meat / he", "He never eats meat.", "S + frequency + V + O."),
                fill("___ she play tennis?", "Does", "Does + she + V1."),
                mc("Выберите верное:", ["What you want?", "What do you want?", "What does you want?"], "What do you want?", "Wh + do + you."),
                err("She can the piano play.", "She can play the piano.", "can + V1 + O."),
                order("Слова: on / table / is / the / bag / the", "The bag is on the table.", "S + be + place."),
                fill("They ___ in Spain. (live)", "live", "S + V + place."),
                xf("Сделайте вопрос: You know her.", "Do you know her?", "Do + S + V1."),
                match("Вопрос", ["Does", "Tom", "drive"], "Does=aux; Tom=S; drive=V", "Does + S + V1."),
                fill("I am ___ late. (часто / never)", "never", "be + частота."),
                err("Go you to school?", "Do you go to school?", "Do + S + V1."),
            ],
        ),
        "level_code": "A1",
        "sources": SOURCES,
    },
    {
        **module(
            "word-order-a2",
            "Порядок слов: Continuous, вопросы и дополнения",
            "Место объектных местоимений, вопросы с be/V-ing, порядок place–time.",
            22,
            "Расширяем базовый каркас",
            lesson(
                "На A2 порядок слов остаётся S–V–O, но добавляются Continuous-формы и более гибкие обстоятельства. Объектные местоимения стоят сразу после глагола: Give it to me.",
                [
                    rule(
                        "Place before time",
                        "I met her in Paris in 2019 — сначала место, затем время.",
                        [ex("We stayed at a hotel last week.", "Мы жили в отеле на прошлой неделе.")],
                    ),
                    rule(
                        "Questions with be + V-ing",
                        "Are you working? What is she doing? Вспомогательный be выходит вперёд.",
                        [ex("Is he cooking dinner?", "Он готовит ужин?")],
                    ),
                    rule(
                        "Objects and pronouns",
                        "Give me the book / Give the book to me. С it/them предпочтительно: Give it to me.",
                        [ex("Send them the file.", "Отправь им файл.")],
                    ),
                ],
                watch_out=["Не: Give to me it.", "В Continuous смысловой глагол с -ing остаётся после be."],
                remember="Место → время. Be выходит в вопрос. Местоимение-объект рядом с глаголом.",
            ),
            [
                order("Соберите: yesterday / in / park / the / walked / we", "We walked in the park yesterday.", "place before time."),
                fill("Выберите форму to be: ___ you listening?", "Are", "Are + S + V-ing."),
                mc("Give ___ the keys.", ["to me", "me", "I"], "me", "Give + me + N."),
                err("She is cook dinner now.", "She is cooking dinner now.", "be + V-ing."),
                order("Слова: to / me / send / it", "Send it to me.", "it перед to-фразе."),
                fill("What ___ they doing?", "are", "Wh + be + S + V-ing."),
                xf("Переставьте: at noon / arrive / we / at the station", "We arrive at the station at noon.", "place → time."),
                match("Continuous вопрос", ["Is", "she", "reading"], "Is=aux; she=S; reading=V-ing", "Be + S + V-ing."),
            ],
            [
                order("Соберите: last night / home / stayed / they", "They stayed home last night.", "S + V + place + time."),
                fill("___ he working today?", "Is", "Is + he + V-ing."),
                mc("Pass ___ the salt.", ["I", "me", "my"], "me", "Объектное местоимение."),
                err("I met in 2020 her.", "I met her in 2020.", "O перед временем."),
                order("Слова: doing / what / you / are", "What are you doing?", "Wh + be + S + V-ing."),
                fill("Put ___ on the shelf. (it)", "it", "Object pronoun after V."),
                xf("Сделайте вопрос: She is waiting.", "Is she waiting?", "Be + S + V-ing."),
                fill("We talked ___ the cafe ___ Monday. (in / on)", "in / on", "in + place, on + day.", ["in/on"]),
            ],
        ),
        "level_code": "A2",
        "sources": SOURCES,
    },
    {
        **module(
            "word-order-b1",
            "Гибкий порядок: дополнения, косвенная речь, emphasis",
            "Два дополнения, reported questions, начальные обстоятельства.",
            24,
            "Когда порядок слегка сдвигается",
            lesson(
                "На B1 появляются конструкции с двумя дополнениями и косвенными вопросами без инверсии: She asked where I lived — не where did I live.",
                [
                    rule(
                        "Double object",
                        "Give someone something / Give something to someone. С местоимениями чаще to/for.",
                        [ex("I sent Anna the link.", "Я отправил Анне ссылку.")],
                    ),
                    rule(
                        "Reported questions",
                        "Порядок как в утверждении: He asked what time it was.",
                        [ex("She wondered if we were ready.", "Она думала, готовы ли мы.")],
                    ),
                    rule(
                        "Fronted adverbials",
                        "Обстоятельство можно вынести вперёд для акцента: Yesterday we left early — без инверсии на B1.",
                        [ex("In the morning I check the roster.", "Утром я сверяю график.")],
                    ),
                ],
                watch_out=["В косвенном вопросе нет do/does/did.", "Не путайте Give me it с Give it to me."],
                remember="Косвенный вопрос = прямой порядок. Два объекта: sb sth или sth to sb.",
            ),
            [
                order("Соберите: the / map / me / show", "Show me the map.", "V + sb + sth."),
                fill("She asked where I ___. (live, past)", "lived", "Reported: Past."),
                mc("He told ___ the news.", ["to us", "us", "we"], "us", "tell + sb."),
                err("She asked where did I go.", "She asked where I went.", "Без инверсии."),
                order("Слова: yesterday / early / left / we", "Yesterday we left early.", "Fronted time."),
                fill("I gave the keys ___ Lena.", "to", "sth to sb."),
                xf("Косвенный вопрос: вставьте порядок слов: 'Where do you work?' → He asked where I ___.", "worked", "Present → Past."),
                match("Reported", ["asked", "if", "we were free"], "asked=verb; if=linker; we were free=clause", "if + statement order."),
            ],
            [
                order("Соберите: to / Tom / sent / I / the / file", "I sent the file to Tom.", "sth to sb."),
                fill("They wondered ___ we had left.", "if", "if/whether.", ["whether"]),
                mc("Tell ___ your plan.", ["to me", "me", "I"], "me", "tell + sb + sth."),
                err("He asked what did she want.", "He asked what she wanted.", "Statement order."),
                order("Слова: in June / open / the / cafe / will", "In June the cafe will open.", "Fronted time + S + will + V."),
                fill("She made ___ a coffee.", "me", "make + sb + sth."),
                xf("Косвенный вопрос: вставьте форму: 'Are you ready?' → She asked if I ___ ready.", "was", "are → was."),
                fill("Pass the message ___ the desk.", "to", "to + recipient."),
            ],
        ),
        "level_code": "B1",
        "sources": SOURCES,
    },
]
