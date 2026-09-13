"""Enriched word-order lesson theory."""

from app.seed.helpers import ex, lesson, rule

WO_THEORY = {
    "word-order-a1": lesson(
        "В утвердительном предложении английский держит жёсткий порядок: подлежащее → сказуемое → дополнение → место → время. Это база A1: сначала кто делает, потом что делает, затем с чем и где/когда.",
        [
            rule(
                "Утверждение S–V–O",
                "I drink tea. She reads books. В нейтральном стиле дополнение не ставят перед глаголом: не Tea I drink. Обстоятельства места и времени обычно в конце: They watch films at home in the evening.",
                [
                    ex("They watch films.", "Они смотрят фильмы."),
                    ex("Tom opens the door.", "Том открывает дверь."),
                    ex("We meet at six.", "Мы встречаемся в шесть."),
                ],
            ),
            rule(
                "Вопросы Present Simple",
                "Do/Does + подлежащее + V1: Do you live here? Does she work? Wh-слово встаёт впереди: Where do you live? После does глагол без -s.",
                [
                    ex("Do they speak English?", "Они говорят по-английски?"),
                    ex("What does he want?", "Чего он хочет?"),
                    ex("Where do you live?", "Где ты живёшь?"),
                ],
            ),
            rule(
                "Наречия частоты",
                "Перед смысловым глаголом: She often cooks. После be: She is never late. Не: Often she is late в нейтральном утверждении.",
                [
                    ex("I usually walk home.", "Я обычно иду домой пешком."),
                    ex("She is never late.", "Она никогда не опаздывает."),
                    ex("He never eats meat.", "Он никогда не ест мясо."),
                ],
            ),
        ],
        compare=[
            {"left": "She often cooks.", "right": "She is often late.", "note": "Перед смысловым глаголом vs после be."},
        ],
        watch_out=[
            "Не ставьте do перед подлежащим в утверждении.",
            "В вопросе после does глагол без -s.",
            "I every day check email — время/частоту поставьте на место.",
        ],
        remember="S–V–O. Вопросы: Do/Does + S + V1. Частота — перед V или после be.",
    ),
    "word-order-a2": lesson(
        "На A2 порядок слов остаётся S–V–O, но добавляются Continuous-формы и более гибкие обстоятельства. Объектные местоимения стоят сразу после глагола: Give it to me. Место обычно раньше времени.",
        [
            rule(
                "Place before time",
                "I met her in Paris in 2019 — сначала место, затем время. We stayed at a hotel last week. Если переставить, фраза звучит тяжелее или неестественно.",
                [
                    ex("We stayed at a hotel last week.", "Мы жили в отеле на прошлой неделе."),
                    ex("We arrive at the station at noon.", "Мы прибываем на станцию в полдень."),
                ],
            ),
            rule(
                "Questions with be + V-ing",
                "Are you working? What is she doing? Вспомогательный be выходит вперёд, смысловой глагол с -ing остаётся после подлежащего.",
                [
                    ex("Is he cooking dinner?", "Он готовит ужин?"),
                    ex("What are you doing?", "Что ты делаешь?"),
                ],
            ),
            rule(
                "Objects and pronouns",
                "Give me the book / Give the book to me. С it/them предпочтительно: Give it to me, не Give to me it. Объектное местоимение держится рядом с глаголом.",
                [
                    ex("Send them the file.", "Отправь им файл."),
                    ex("Send it to me.", "Отправь это мне."),
                    ex("Pass me the salt.", "Передай мне соль."),
                ],
            ),
        ],
        compare=[
            {"left": "Give me the keys.", "right": "Give the keys to me.", "note": "Два допустимых порядка; с it лучше Give it to me."},
        ],
        watch_out=[
            "Не: Give to me it.",
            "В Continuous смысловой глагол с -ing остаётся после be + подлежащее.",
            "I met in 2020 her — дополнение раньше времени.",
        ],
        remember="Место → время. Be выходит в вопрос. Местоимение-объект рядом с глаголом.",
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
            ),
            rule(
                "Косвенные вопросы",
                "Порядок как в утверждении: Can you tell me where the station is? Не where is the station внутри косвенного вопроса. If/whether — для yes/no.",
                [
                    ex("Can you tell me where the station is?", "Подскажешь, где станция?"),
                    ex("I wonder if they are ready.", "Интересно, готовы ли они."),
                ],
            ),
            rule(
                "Начальные обстоятельства и акцент",
                "Yesterday we left early / We left early yesterday — оба возможны; начало фразы сильнее подсвечивает время. Не ломайте S–V без причины: не Yesterday left we early.",
                [
                    ex("Yesterday we left early.", "Вчера мы ушли рано."),
                    ex("In the end they agreed.", "В итоге они согласились."),
                ],
            ),
        ],
        compare=[
            {"left": "Where is the station?", "right": "Tell me where the station is.", "note": "Прямой вопрос с инверсией vs косвенный без инверсии."},
        ],
        watch_out=[
            "Tell me where is it — лишняя инверсия.",
            "Give to her it — порядок местоимений.",
            "Не выносите глагол перед подлежащим без конструкции вроде Never have I… (это уже B2+).",
        ],
        remember="Два дополнения — по схеме. Косвенный вопрос — без инверсии. Вперёд выносите обстоятельство, не ломая S–V.",
    ),
}
