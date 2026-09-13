"""Enriched word-order lesson theory."""

from app.seed.helpers import callout, ex, lesson, pair, rule, table

WO_THEORY = {
    "word-order-a1": lesson(
        "В утвердительном предложении английский держит жёсткий порядок: **подлежащее → сказуемое → дополнение → место → время**. Это база A1: сначала кто делает, потом что делает, затем с чем и где/когда.",
        [
            rule(
                "Утверждение S–V–O",
                "В нейтральном стиле дополнение не ставят перед глаголом. Обстоятельства места и времени обычно в конце.",
                [
                    ex("They watch films.", "Они смотрят фильмы."),
                    ex("Tom opens the door.", "Том открывает дверь."),
                    ex("We meet at six.", "Мы встречаемся в шесть."),
                ],
                tables=[
                    table(
                        ["Слот", "Что стоит", "Пример"],
                        [
                            ["1", "подлежащее (S)", "They"],
                            ["2", "глагол (V)", "watch"],
                            ["3", "дополнение (O)", "films"],
                            ["4–5", "место → время", "at home / in the evening"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Tea I drink.", "I drink tea.", "Дополнение не выносят перед глаголом в нейтральном стиле."),
                ],
            ),
            rule(
                "Вопросы Present Simple",
                "Do/Does + подлежащее + V1. Wh-слово встаёт впереди. После does глагол без **-s**.",
                [
                    ex("Do they speak English?", "Они говорят по-английски?"),
                    ex("What does he want?", "Чего он хочет?"),
                    ex("Where do you live?", "Где ты живёшь?"),
                ],
                tables=[
                    table(
                        ["Тип", "Порядок"],
                        [
                            ["Общий вопрос", "Do/Does + S + **V1**?"],
                            ["Специальный", "Wh + do/does + S + **V1**?"],
                        ],
                    ),
                ],
            ),
            rule(
                "Наречия частоты",
                "Перед смысловым глаголом: She often cooks. После be: She is never late.",
                [
                    ex("I usually walk home.", "Я обычно иду домой пешком."),
                    ex("She is never late.", "Она никогда не опаздывает."),
                    ex("He never eats meat.", "Он никогда не ест мясо."),
                ],
                callouts=[
                    callout("Частота: **перед** смысловым глаголом, **после** be.", "key"),
                ],
            ),
        ],
        compare=[
            {"left": "She often cooks.", "right": "She is often late.", "note": "Перед смысловым глаголом vs после be."},
        ],
        watch_out=[
            "Не ставят do перед подлежащим в утверждении.",
            "В вопросе после does глагол без **-s**.",
            "I every day check email — время/частоту ставят на место.",
        ],
        remember="**S–V–O**. Вопросы: Do/Does + S + V1. Частота — перед V или после be.",
    ),
    "word-order-a2": lesson(
        "На A2 порядок слов остаётся S–V–O, но добавляются Continuous-формы и более гибкие обстоятельства. Объектные местоимения стоят сразу после глагола. Место обычно раньше времени.",
        [
            rule(
                "Place before time",
                "Сначала место, затем время. Если переставить, фраза звучит тяжелее или неестественно.",
                [
                    ex("We stayed at a hotel last week.", "Мы жили в отеле на прошлой неделе."),
                    ex("We arrive at the station at noon.", "Мы прибываем на станцию в полдень."),
                ],
                tables=[
                    table(
                        ["Порядок обстоятельств", "Пример"],
                        [
                            ["место → время", "in Paris in 2019"],
                            ["не наоборот в нейтральном стиле", "× in 2019 in Paris (тяжелее)"],
                        ],
                    ),
                ],
            ),
            rule(
                "Questions with be + V-ing",
                "Вспомогательный be выходит вперёд, смысловой глагол с -ing остаётся после подлежащего.",
                [
                    ex("Is he cooking dinner?", "Он готовит ужин?"),
                    ex("What are you doing?", "Что ты делаешь?"),
                ],
            ),
            rule(
                "Objects and pronouns",
                "Give me the book / Give the book to me. С it/them предпочтительно: Give it to me.",
                [
                    ex("Send them the file.", "Отправь им файл."),
                    ex("Send it to me.", "Отправь это мне."),
                    ex("Pass me the salt.", "Передай мне соль."),
                ],
                pairs=[
                    pair("Give to me it.", "Give it to me.", "Объектное местоимение держится рядом с глаголом."),
                ],
            ),
        ],
        compare=[
            {"left": "Give me the keys.", "right": "Give the keys to me.", "note": "Два допустимых порядка; с it лучше Give it to me."},
        ],
        watch_out=[
            "Не: Give to me it.",
            "В Continuous-вопросе нужен be впереди, не do.",
            "Место обычно раньше времени.",
        ],
        remember="Место → время. Continuous-вопрос: be + S + V-ing. Местоимение-объект рядом с глаголом.",
    ),
    "word-order-b1": lesson(
        "На B1 порядок слов становится гибче: два дополнения, косвенные вопросы без инверсии, начальные обстоятельства для эмфазы. База S–V–O не исчезает — меняется то, что можно вынести вперёд осознанно.",
        [
            rule(
                "Два дополнения",
                "Give someone something / Give something to someone. Buy her a gift / Buy a gift for her. С местоимениями чаще схема с to/for: Give it to Sam.",
                [
                    ex("She sent me a message.", "Она прислала мне сообщение."),
                    ex("She sent a message to me.", "Она прислала сообщение мне."),
                    ex("They bought a ticket for us.", "Они купили нам билет."),
                ],
                tables=[
                    table(
                        ["Схема", "Пример"],
                        [
                            ["V + person + thing", "Give Sam the keys."],
                            ["V + thing + to/for + person", "Give the keys to Sam."],
                            ["с местоимением it/them", "Give **it** to Sam."],
                        ],
                    ),
                ],
                pairs=[
                    pair("Give to her it.", "Give it to her.", "Местоимение-объект держится рядом с глаголом."),
                ],
            ),
            rule(
                "Косвенные вопросы",
                "Порядок как в утверждении: Can you tell me where the station is? Не where is the station внутри косвенного вопроса. If/whether — для yes/no.",
                [
                    ex("Can you tell me where the station is?", "Подскажешь, где станция?"),
                    ex("I wonder if they are ready.", "Интересно, готовы ли они."),
                    ex("Could you tell me what time it starts?", "Не подскажете, во сколько начинается?"),
                ],
                tables=[
                    table(
                        ["Прямой вопрос", "Косвенный / вложенный"],
                        [
                            ["Where is the station?", "… where the station **is**"],
                            ["Where does she live?", "… where she lives"],
                            ["Are they ready?", "… **if/whether** they are ready"],
                        ],
                    ),
                ],
                pairs=[
                    pair("Tell me where is it.", "Tell me where it is.", "Инверсию вопроса во вложении снимают."),
                ],
            ),
            rule(
                "Начальные обстоятельства и акцент",
                "Yesterday we left early / We left early yesterday — оба возможны; начало фразы сильнее подсвечивает время. Не ломают S–V без причины: не Yesterday left we early.",
                [
                    ex("Yesterday we left early.", "Вчера мы ушли рано."),
                    ex("In the end they agreed.", "В итоге они согласились."),
                    ex("On Friday she finally sent the report.", "В пятницу она наконец отправила отчёт."),
                ],
                callouts=[
                    callout("Сдвиг обстоятельства в начало возможен для акцента, но ядро **S–V–O** обычно сохраняется.", "tip"),
                ],
            ),
        ],
        compare=[
            {"left": "Where is the station?", "right": "Tell me where the station is.", "note": "Прямой вопрос с инверсией vs косвенный без инверсии."},
        ],
        watch_out=[
            "Tell me where is it — лишняя инверсия.",
            "Give to her it — порядок местоимений.",
            "Не выносят глагол перед подлежащим без конструкции вроде Never have I… (это уже B2+).",
        ],
        remember="Два дополнения — по схеме. Косвенный вопрос — без инверсии. Вперёд выносят обстоятельство, не ломая S–V.",
    ),
}
