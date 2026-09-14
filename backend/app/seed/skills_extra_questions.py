"""Append-only extra skill questions for existing reading/listening/dialogue items."""

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


EXTRA_QUESTIONS_BY_SLUG: dict[str, list[dict]] = {
    "reading-a1-morning-bus": [
        _choice("What time does Lena wake up?", "at seven", ["at six", "at seven", "at eight", "at nine"], "at seven"),
        _choice("Who does she smile at in the office?", "the receptionist", ["the driver", "the receptionist", "Anna", "her sister"], "the receptionist"),
    ],
    "reading-a1-new-neighbour": [
        _choice("What does Omar's flat have?", "a little balcony", ["a garage", "a little balcony", "a pool", "two kitchens"], "a little balcony"),
        _choice("What does Omar put on the windowsill?", "a plant", ["a cake", "a plant", "keys", "a lamp"], "a plant"),
    ],
    "reading-a1-market-day": [
        _choice("What does Maya plan for lunch?", "a simple salad", ["soup only", "a simple salad", "pizza", "fish"], "a simple salad"),
        _choice("Why does she like market days?", "they feel calm and useful", ["they are free", "they feel calm and useful", "they are loud", "shops are closed"], "they feel calm and useful"),
    ],
    "reading-a2-library-card": [
        _choice("Who showed Denis the catalogue?", "the librarian", ["his uncle", "the librarian", "a classmate", "a seller"], "the librarian"),
        _choice("Where does he sometimes read?", "near the window", ["in a cafe", "near the window", "on the bus", "only at home"], "near the window"),
    ],
    "reading-a2-rainy-picnic": [
        _choice("What did they pack in the morning?", "sandwiches and a ball", ["only water", "sandwiches and a ball", "books", "a tent"], "sandwiches and a ball"),
        _choice("What did they stop for on the way home?", "hot chocolate", ["ice cream", "hot chocolate", "pizza", "tea only"], "hot chocolate"),
    ],
    "reading-a2-office-plant": [
        _choice("How often did Irina water it at first?", "every Monday", ["every day", "every Monday", "never", "only Fridays"], "every Monday"),
        _choice("What do colleagues do on Fridays?", "wipe the leaves and turn the pot", ["throw the plant away", "wipe the leaves and turn the pot", "stop talking", "move desks"], "wipe the leaves and turn the pot"),
    ],
    "reading-b1-night-shift": [
        _choice("What is Sofia's job?", "a nurse", ["a teacher", "a nurse", "a driver", "a cook"], "a nurse"),
        _choice("What does she do on free mornings?", "sleeps until noon and walks in the park", ["works another shift", "sleeps until noon and walks in the park", "flies abroad", "studies all night"], "sleeps until noon and walks in the park"),
    ],
    "reading-b1-second-hand-bike": [
        _choice("Where did Pavel practise at first?", "on quiet streets near his home", ["on a highway", "on quiet streets near his home", "at the airport", "indoors only"], "on quiet streets near his home"),
        _choice("What did he buy for safety?", "lights and a simple lock", ["a radio", "lights and a simple lock", "a new car", "nothing"], "lights and a simple lock"),
    ],
    "reading-b2-community-garden": [
        _choice("What did residents plant?", "beans, herbs, and sunflowers", ["only weeds", "beans, herbs, and sunflowers", "wheat fields", "palm trees"], "beans, herbs, and sunflowers"),
        _choice("Who did they ask for permission?", "the council", ["tourists", "the council", "a school", "nobody"], "the council"),
    ],
    "reading-b2-remote-week": [
        _choice("What did Nadia spend extra time on?", "cooking and an online course", ["commuting more", "cooking and an online course", "night shifts", "parking"], "cooking and an online course"),
        _choice("What did she book on remote mornings?", "focus time", ["more meetings", "focus time", "travel", "parties"], "focus time"),
    ],
    "reading-a1-lost-keys": [
        _choice("Where does Tim's sister find the keys?", "on the kitchen table", ["in the bathroom", "on the kitchen table", "under the bed", "in the car"], "on the kitchen table"),
        _choice("What reminder does Tim set?", "to always use the hook", ["to buy new keys", "to always use the hook", "to leave late", "to hide the fruit"], "to always use the hook"),
    ],
    "reading-a1-pet-goldfish": [
        _choice("Where does Nora keep the bowl?", "away from the hot window", ["in the freezer", "away from the hot window", "outside", "under the bed"], "away from the hot window"),
        _choice("What does caring for the pet help her feel?", "responsible and calm", ["angry", "responsible and calm", "hungry", "bored"], "responsible and calm"),
    ],
    "reading-a1-birthday-card": [
        _choice("Where does Rita buy the flowers?", "at the corner shop", ["at the airport", "at the corner shop", "online only", "at school"], "at the corner shop"),
        _choice("What do they read together twice?", "the card", ["a novel", "the card", "a map", "emails"], "the card"),
    ],
    "reading-a2-train-ticket": [
        _choice("What seat does Anton choose?", "a morning seat by the window", ["an evening seat", "a morning seat by the window", "standing only", "the back row"], "a morning seat by the window"),
        _choice("What does he buy at the station?", "tea", ["a bike", "tea", "a plant", "nothing"], "tea"),
    ],
    "reading-a2-burnt-toast": [
        _choice("What did Lara open after the smoke?", "the window", ["the fridge", "the window", "a shop", "a suitcase"], "the window"),
        _choice("What lesson does she decide about multitasking?", "it is not always faster", ["it is always better", "it is not always faster", "it never fails", "it replaces timers"], "it is not always faster"),
    ],
    "reading-a2-weekend-hike": [
        _choice("What did they pack?", "water, sandwiches, and a small first-aid kit", ["only phones", "water, sandwiches, and a small first-aid kit", "a tent only", "books"], "water, sandwiches, and a small first-aid kit"),
        _choice("What was the trail like on the way down?", "muddy", ["icy forever", "muddy", "closed", "underwater"], "muddy"),
    ],
    "reading-b1-language-exchange": [
        _choice("Where do Katya and Diego meet?", "in a quiet café", ["at a stadium", "in a quiet café", "on a plane", "at a factory"], "in a quiet café"),
        _choice("Which languages do they practise?", "English and Spanish", ["only Russian", "English and Spanish", "only Latin", "Chinese only"], "English and Spanish"),
    ],
    "reading-b1-thrift-jacket": [
        _choice("What kind of jacket did Masha find?", "a warm wool jacket", ["a raincoat only", "a warm wool jacket", "a school uniform", "a plastic coat"], "a warm wool jacket"),
        _choice("Where did she wear it?", "to a winter market", ["to the beach", "to a winter market", "to a pool", "nowhere"], "to a winter market"),
    ],
    "reading-b1-food-bank": [
        _choice("What does Oleg sort?", "donated cans", ["tickets", "donated cans", "phones", "books only"], "donated cans"),
        _choice("What do breaks include?", "strong coffee", ["loud music only", "strong coffee", "exams", "travel"], "strong coffee"),
    ],
    "reading-b2-podcast-habit": [
        _choice("Where does Ilya listen?", "on the tram", ["only at weekends", "on the tram", "during meetings", "in class tests"], "on the tram"),
        _choice("What speed did he use at first?", "0.9", ["2.0", "0.9", "5.0", "no audio"], "lowered the speed to 0.9"),
    ],
    "reading-b2-coworking-trial": [
        _choice("What did the day pass include?", "a desk, fast Wi‑Fi, and unlimited tea", ["a hotel bed", "a desk, fast Wi‑Fi, and unlimited tea", "a free car", "nothing"], "a desk, fast Wi‑Fi, and unlimited tea"),
        _choice("What did she protect with headphones?", "deep-work hours", ["lunch noise only", "deep-work hours", "the kitchen", "weekends"], "deep-work hours"),
    ],
    "reading-b2p-invoice-delay": [
        _choice("How late was the payment at first?", "five days", ["one year", "five days", "one hour", "never"], "five days"),
        _choice("What tone did Dana keep?", "polite but firm", ["angry only", "polite but firm", "silent", "joking"], "polite but firm"),
    ],
    "reading-b2-urban-noise": [
        _choice("What building problem started the group?", "late-night renovations", ["missing parks", "late-night renovations", "no buses", "closed shops"], "late-night renovations"),
        _choice("Where did the manager post a schedule?", "in the lobby", ["online only forever", "in the lobby", "nowhere", "at school"], "in the lobby"),
    ],
    "reading-c1-attention-economy": [
        _choice("What do phones train the mind to treat as emergencies?", "unfinished tasks", ["finished books", "unfinished tasks", "silent modes", "long walks"], "unfinished tasks"),
        _choice("What is one hygiene habit mentioned?", "batching email twice a day", ["checking feeds hourly", "batching email twice a day", "more badges", "always-on alerts"], "batching email twice a day"),
    ],
    "reading-c1-climate-adaptation": [
        _choice("Which adaptation measures are listed?", "shade trees, reflective roofs, and cooling centres", ["only billboards", "shade trees, reflective roofs, and cooling centres", "closing schools forever", "banning parks"], "shade trees, reflective roofs, and cooling centres"),
        _choice("What do careful reports say adaptation and mitigation are?", "partners", ["enemies", "partners", "identical", "irrelevant"], "partners"),
    ],
    "reading-c1-translation-tradeoffs": [
        _choice("What may a freer translation blur?", "a cultural reference", ["paper size", "a cultural reference", "page numbers", "fonts"], "a cultural reference"),
        _choice("What can machine tools still require?", "a human who understands context", ["no review", "a human who understands context", "only speed", "random swaps"], "a human who understands context"),
    ],
    "reading-c2-epistemic-humility": [
        _choice("What does humility ask about a claim?", "what would falsify it", ["how to hide doubt", "what would falsify it", "how to sound certain", "who to mock"], "what would falsify it"),
        _choice("What can humility coexist with?", "expertise", ["ignorance only", "expertise", "certainty as theatre", "refusal to know"], "expertise"),
    ],
    "reading-c2-platform-governance": [
        _choice("What kind of problem is governance described as?", "a design problem as much as a moral one", ["only a moral problem", "a design problem as much as a moral one", "only a sales problem", "unsolvable forever"], "a design problem as much as a moral one"),
        _choice("What should ordinary users be able to understand?", "what speech the platform will actually host", ["secret rules only", "what speech the platform will actually host", "nothing practical", "only ads"], "what speech the platform will actually host"),
    ],
    "reading-c2-slow-expertise": [
        _choice("What is one partial remedy mentioned?", "better signalling of uncertainty", ["hiding doubt", "better signalling of uncertainty", "faster slogans", "banning experts"], "better signalling of uncertainty"),
        _choice("What can slow expertise still remain?", "available, legible, and respected", ["hidden forever", "available, legible, and respected", "banned", "unreadable"], "available, legible, and respected"),
    ],
    "listening-a1-weather-note": [
        _choice("Where is the wind stronger?", "near the river", ["in the shop", "near the river", "at school", "underground"], "near the river"),
        _choice("When may it feel colder?", "in the evening", ["at noon only", "in the evening", "never", "in summer only"], "in the evening"),
    ],
    "listening-a1-shop-hours": [
        _choice("How can you pay on other days?", "by card near the till", ["only cash outside", "by card near the till", "by cheque only", "for free"], "by card near the till"),
        _choice("Who helps with sizes?", "a member of staff", ["a robot", "a member of staff", "nobody", "the mayor"], "a member of staff"),
    ],
    "listening-a1-meet-friend": [
        _choice("What should you do if the train is late?", "send a short message", ["cancel forever", "send a short message", "wait a year", "go home silently"], "send a short message"),
        _choice("Where can they walk after meeting?", "to the café", ["to the airport", "to the café", "to school only", "nowhere"], "to the café"),
    ],
    "listening-a2-kitchen-tip": [
        _choice("What should you do before draining?", "taste a piece", ["throw it away", "taste a piece", "add ice", "call a friend"], "taste a piece"),
        _choice("How should you serve the pasta?", "hot", ["frozen", "hot", "raw", "dry only"], "hot"),
    ],
    "listening-a2-missed-call": [
        _choice("When will Mark be free?", "around two o'clock", ["at midnight only", "around two o'clock", "next year", "never"], "around two o'clock"),
        _choice("What alternative does he offer?", "email", ["a letter by ship", "email", "a fax only", "nothing"], "email"),
    ],
    "listening-a2-bus-delay": [
        _choice("What can passengers do?", "wait at this stop or check the board", ["drive the bus", "wait at this stop or check the board", "cancel the city", "walk to another country"], "wait at this stop or check the board"),
        _choice("Where does the next service go toward?", "the square", ["the airport only", "the square", "the riverbed", "nowhere"], "the square"),
    ],
    "listening-b1-museum-rules": [
        _choice("Where should food and drinks stay?", "outside the galleries", ["on the exhibits", "outside the galleries", "in lockers with bags only", "nowhere allowed ever"], "outside the galleries"),
        _choice("Where can you ask for help?", "near the information desk", ["outside the city", "near the information desk", "only online forever", "in the cloakroom dark"], "near the information desk"),
    ],
    "listening-b1-project-update": [
        _choice("Where should comments go?", "in the shared document", ["on paper only", "in the shared document", "nowhere", "by post"], "in the shared document"),
        _choice("When are comments needed?", "before noon", ["next year", "before noon", "after Thursday forever", "never"], "before noon"),
    ],
    "listening-b2-city-survey": [
        _choice("Where are paper forms available?", "at the library", ["at the airport", "at the library", "nowhere", "only online forever"], "at the library"),
        _choice("What will feedback help plan?", "safer routes for next year", ["higher rents only", "safer routes for next year", "closing parks", "fewer bikes"], "safer routes for next year"),
    ],
    "listening-b2-apartment-viewing": [
        _choice("What does the building have?", "a quiet courtyard and a locked bicycle room", ["a noisy factory", "a quiet courtyard and a locked bicycle room", "no doors", "only offices"], "a quiet courtyard and a locked bicycle room"),
        _choice("What should you bring if you like the flat?", "your documents", ["pets only", "your documents", "furniture today", "nothing"], "your documents"),
    ],
    "listening-a1-bakery-order": [
        _choice("What bag is requested?", "a paper bag", ["a plastic suitcase", "a paper bag", "no bag", "a box of metal"], "a paper bag"),
        _choice("Where will the pie be eaten?", "at work", ["on the bus roof", "at work", "never", "at school only"], "at work"),
    ],
    "listening-a1-gym-hours": [
        _choice("What should members bring?", "a towel and clean indoor shoes", ["a bike only", "a towel and clean indoor shoes", "food for sale", "nothing"], "a towel and clean indoor shoes"),
        _choice("What may close earlier some days?", "the pool area", ["the whole city", "the pool area", "the street", "never anything"], "the pool area"),
    ],
    "listening-a1-phone-battery": [
        _choice("Why is the charger needed?", "to send one message before the meeting", ["to play games all night", "to send one message before the meeting", "to sell the phone", "for no reason"], "to send one message before the meeting"),
        _choice("When will the charger be returned?", "at twenty percent", ["never", "at twenty percent", "next year", "after the phone dies"], "at twenty percent"),
    ],
    "listening-a2-laundry-note": [
        _choice("Where is the detergent?", "under the sink", ["on the roof", "under the sink", "outside", "in the fridge"], "under the sink"),
        _choice("Why move clothes when it beeps?", "to keep the laundry room free for a new wash", ["to hide them", "to keep the laundry room free for a new wash", "to sell them", "for no reason"], "to keep the laundry room free for a new wash"),
    ],
    "listening-a2-parcel-pickup": [
        _choice("Until when is pickup open on weekdays?", "until seven", ["until noon only", "until seven", "never", "all night every day"], "until seven"),
        _choice("What if the locker does not open?", "ask the desk for help", ["leave forever", "ask the desk for help", "break it", "call a friend abroad"], "ask the desk for help"),
    ],
    "listening-a2-class-cancel": [
        _choice("What is still due on Monday?", "homework from last week", ["nothing", "homework from last week", "a new exam only", "fees tomorrow"], "homework from last week"),
        _choice("Where should students check for room changes?", "the group chat", ["a newspaper", "the group chat", "nowhere", "the river"], "the group chat"),
    ],
    "listening-b1-flight-gate": [
        _choice("What should passengers have ready?", "boarding pass and passport", ["only cash", "boarding pass and passport", "a bike", "nothing"], "boarding pass and passport"),
        _choice("Who may board first when invited?", "families with children and passengers who need assistance", ["nobody special", "families with children and passengers who need assistance", "only pilots", "tourists without tickets"], "families with children and passengers who need assistance"),
    ],
    "listening-b1-password-reset": [
        _choice("What should you not do with the link?", "share it with anyone", ["open it yourself", "share it with anyone", "ignore spam forever without reading", "save it publicly"], "share it with anyone"),
        _choice("Where should you contact support?", "from the official website only", ["from random emails", "from the official website only", "on social media ads", "nowhere"], "from the official website only"),
    ],
    "listening-b1-recycling-tip": [
        _choice("Where can batteries be collected?", "at the supermarket entrance", ["in food waste", "at the supermarket entrance", "in the sink", "outside randomly"], "at the supermarket entrance"),
        _choice("What can clean paper go with?", "cardboard", ["batteries", "cardboard", "food", "glass only forever"], "cardboard"),
    ],
    "listening-b2-standup-blocker": [
        _choice("What will the speaker tidy while waiting?", "error messages on the login screen", ["the office kitchen only", "error messages on the login screen", "the rent notice", "nothing"], "error messages on the login screen"),
        _choice("When should people with a sandbox key message?", "after the call", ["never", "after the call", "next year", "before hiring"], "after the call"),
    ],
    "listening-b2-rent-notice": [
        _choice("What should emails include?", "your flat number", ["only emojis", "your flat number", "nothing", "a photo of lunch"], "your flat number"),
        _choice("What costs does the increase cover?", "higher heating costs", ["party costs", "higher heating costs", "new logos", "nothing"], "higher heating costs"),
    ],
    "listening-b2p-workshop-brief": [
        _choice("What should comments be like?", "kind and specific", ["rude and vague", "kind and specific", "silent forever", "only emoji"], "kind and specific"),
        _choice("What will each pair share at the end?", "one useful tip", ["nothing", "one useful tip", "a full essay", "phone numbers only"], "one useful tip"),
    ],
    "listening-b2-library-quiet-policy": [
        _choice("Where is group work welcome after booking?", "in rooms three and four", ["on the silent floor only", "in rooms three and four", "outside forever", "nowhere"], "in rooms three and four"),
        _choice("What is required for audio on personal devices?", "headphones", ["speakers", "headphones", "nothing", "staff approval for every song"], "headphones"),
    ],
    "listening-c1-research-briefing": [
        _choice("What preference beat fully remote when office days were clear?", "hybrid schedules", ["no work", "hybrid schedules", "night shifts only", "commutes of five hours"], "hybrid schedules"),
        _choice("Who was under-sampled?", "night-shift workers", ["people under forty", "night-shift workers", "urban respondents", "managers only"], "night-shift workers"),
    ],
    "listening-c1-mediation-opening": [
        _choice("What happens after each person speaks?", "a summary of what was heard", ["a vote to punish", "a summary of what was heard", "immediate solutions only", "ending the session"], "a summary of what was heard"),
        _choice("How long can a break be if emotions rise?", "five minutes", ["one day", "five minutes", "no breaks", "one hour minimum"], "five minutes"),
    ],
    "listening-c1-policy-memo-audio": [
        _choice("What must managers publish each Monday?", "team coverage on a shared calendar", ["salaries publicly", "team coverage on a shared calendar", "nothing", "holiday photos"], "team coverage on a shared calendar"),
        _choice("What will be reviewed after the pilot?", "missed handovers and customer response times", ["only logos", "missed handovers and customer response times", "weather", "fonts"], "missed handovers and customer response times"),
    ],
    "listening-c2-ethics-review": [
        _choice("What must recruitment materials disclose?", "participation will not affect clinical care", ["payment is unlimited", "participation will not affect clinical care", "no consent needed", "audio is public"], "participation will not affect clinical care"),
        _choice("When is secondary analysis permitted?", "only for aims listed in the protocol appendix", ["for any later idea", "only for aims listed in the protocol appendix", "never", "only after deletion"], "only for aims listed in the protocol appendix"),
    ],
    "listening-c2-macro-brief": [
        _choice("What is stickier than goods inflation in the brief?", "services inflation", ["house prices only", "services inflation", "nothing", "fuel forever"], "services inflation"),
        _choice("What should clients with long liabilities keep?", "liquidity for opportunities if volatility spikes", ["no cash ever", "liquidity for opportunities if volatility spikes", "only headlines", "zero duration"], "liquidity for opportunities if volatility spikes"),
    ],
    "listening-c2-editorial-standards": [
        _choice("What should happen if anonymity questions cannot be answered?", "delay publication", ["publish anyway", "delay publication", "delete archives", "blame readers"], "delay publication"),
        _choice("What is not enough for a correction note?", "a vague note that details were updated", ["a specific visible correction", "a vague note that details were updated", "naming the figure", "prompt timing"], "a vague note that details were updated"),
    ],
    "dialogue-a1-coffee-order": [
        _choice("Does the customer want sugar?", "no sugar", ["lots of sugar", "no sugar", "only honey", "unknown"], "no sugar"),
        _gap("Customer: A little ___, no sugar.", "milk", accepted=["milk"], explanation="milk"),
    ],
    "dialogue-a1-asking-time": [
        _choice("Until when is the museum open?", "until six o'clock", ["until noon", "until six o'clock", "all night", "it is closed"], "until six o'clock"),
        _gap("B: Go straight, then turn ___ at the lights.", "right", accepted=["right"], explanation="right"),
    ],
    "dialogue-a1-bus-stop": [
        _choice("How often does bus seven come?", "about every ten minutes", ["once a day", "about every ten minutes", "never", "hourly only at night"], "about every ten minutes"),
        _gap("Local: No, you can pay by ___ on the bus.", "card", accepted=["card"], explanation="card"),
    ],
    "dialogue-a2-doctor-appointment": [
        _choice("What should Elena bring?", "ID and a list of medicines", ["only cash", "ID and a list of medicines", "a bike", "nothing"], "ID and a list of medicines"),
        _gap("Patient: Can I get an SMS ___?", "reminder", accepted=["reminder"], explanation="reminder"),
    ],
    "dialogue-a2-returning-item": [
        _choice("What size does the customer want instead?", "a larger size", ["a smaller size", "a larger size", "no size", "kids size"], "a larger size"),
        _gap("Staff: The fitting rooms are on the ___.", "left", accepted=["left"], explanation="left"),
    ],
    "dialogue-a2-group-project": [
        _choice("When will they meet to practise?", "on Thursday", ["on Monday only", "on Thursday", "never", "next year"], "on Thursday"),
        _gap("Nina: I'll book a quiet ___ for twenty minutes.", "room", accepted=["room"], explanation="room"),
    ],
    "dialogue-b1-job-interview": [
        _choice("What would the candidate add next time?", "earlier warning emails", ["nothing", "earlier warning emails", "longer delays", "silence"], "earlier warning emails"),
        _gap("Candidate: I fixed the client updates ___, then logged the supplier issue.", "first", accepted=["first"], explanation="first"),
    ],
    "dialogue-b1-flatmate-chores": [
        _choice("What should they buy tomorrow?", "more bin bags", ["flowers", "more bin bags", "a sofa", "nothing"], "more bin bags"),
        _gap("Jordan: A simple ___ will help guests too.", "checklist", accepted=["checklist"], explanation="checklist"),
    ],
    "dialogue-b2-customer-complaint": [
        _choice("What ticket number is mentioned?", "4821", ["1000", "4821", "9999", "12"], "4821"),
        _gap("Agent: I'll email the ___ link tonight.", "tracking", accepted=["tracking"], explanation="tracking"),
    ],
    "dialogue-b2-travel-plan": [
        _choice("When will they reserve the museum?", "midday, after coffee", ["at midnight", "midday, after coffee", "never", "before dawn only"], "midday, after coffee"),
        _gap("Leo: I'll download the offline ___.", "map", accepted=["map"], explanation="map"),
    ],
    "dialogue-a1-hotel-checkin": [
        _choice("When does breakfast start?", "at seven", ["at noon", "at seven", "at midnight", "never"], "at seven"),
        _gap("Reception: The password is on the key ___.", "card", accepted=["card"], explanation="card"),
    ],
    "dialogue-a1-buying-stamps": [
        _choice("How many stamps does the customer take?", "three", ["one", "three", "ten", "none"], "three"),
        _gap("Clerk: Drop it in the blue ___ by the door.", "box", accepted=["box"], explanation="box"),
    ],
    "dialogue-a1-finding-toilet": [
        _choice("How far is the toilet?", "about one minute on foot", ["one hour", "about one minute on foot", "outside the city", "unknown"], "about one minute on foot"),
        _gap("Guard: Show the ___ at the door.", "receipt", accepted=["receipt"], explanation="receipt"),
    ],
    "dialogue-a2-allergy-order": [
        _choice("What does the soup have instead of nuts?", "cream", ["nuts", "cream", "shellfish", "nothing"], "cream"),
        _gap("Guest: Could I have the salad without ___ instead?", "cheese", accepted=["cheese"], explanation="cheese"),
    ],
    "dialogue-a2-library-fine": [
        _choice("How much is the fine?", "two pounds", ["five pounds", "two pounds", "free", "ten pounds"], "two pounds"),
        _gap("Librarian: Two renewals if nobody else ___ the book.", "requests", accepted=["requests"], explanation="requests"),
    ],
    "dialogue-a2-gym-membership": [
        _choice("How long can the membership be frozen?", "up to four weeks", ["one day", "up to four weeks", "one year always", "never"], "up to four weeks"),
        _gap("Staff: Your pass works from this ___.", "evening", accepted=["evening"], explanation="evening"),
    ],
    "dialogue-b1-deadline-push": [
        _choice("What arrived late?", "the sales numbers", ["the holiday", "the sales numbers", "the office keys", "nothing"], "the sales numbers"),
        _gap("Priya: I'll post it in the channel by ___.", "five", accepted=["five"], explanation="five"),
    ],
    "dialogue-b1-lost-tourist": [
        _choice("When is a tram better?", "only if it starts raining", ["always", "only if it starts raining", "never", "at night only"], "only if it starts raining"),
        _gap("Local: The station entrance is under the big ___.", "clock", accepted=["clock"], explanation="clock"),
    ],
    "dialogue-b1-phone-plan": [
        _choice("What does the customer choose?", "the roaming pack", ["a new number", "the roaming pack", "nothing", "a lower plan"], "the roaming pack"),
        _gap("Advisor: You'll get a confirmation ___ shortly.", "SMS", accepted=["SMS", "sms", "text"], explanation="SMS"),
    ],
    "dialogue-b2-salary-talk": [
        _choice("When is the follow-up?", "on Friday", ["on Monday", "on Friday", "next year", "never"], "on Friday"),
        _gap("Employee: I already drafted a one-page ___.", "summary", accepted=["summary"], explanation="summary"),
    ],
    "dialogue-b2-landlord-repair": [
        _choice("When will the plumber come?", "tomorrow morning between nine and eleven", ["next month", "tomorrow morning between nine and eleven", "tonight only", "never"], "tomorrow morning between nine and eleven"),
        _gap("Tenant: I'll send two ___ now.", "photos", accepted=["photos"], explanation="photos"),
    ],
    "dialogue-b2p-mentor-feedback": [
        _choice("What should the closing ask become?", "one sentence", ["a long poem", "one sentence", "no ask", "ten slides"], "one sentence"),
        _gap("Mentor: Also shorten the closing ask to one ___.", "sentence", accepted=["sentence"], explanation="sentence"),
    ],
    "dialogue-b2-conference-room": [
        _choice("Until when is the glass room free?", "until half past", ["all evening", "until half past", "only at noon", "never"], "until half past"),
        _gap("Ben: I'll also attach last week's ___.", "notes", accepted=["notes"], explanation="notes"),
    ],
    "dialogue-c1-vendor-negotiation": [
        _choice("What weekend support does the buyer accept?", "remote weekend support", ["no support", "remote weekend support", "on-site only weekends", "none"], "remote weekend support"),
        _gap("Buyer: Send the redline by ___ and we'll sign next week.", "Thursday", accepted=["Thursday"], explanation="Thursday"),
    ],
    "dialogue-c1-academic-feedback": [
        _choice("What should the student state about the method?", "what it uniquely contributes", ["nothing", "what it uniquely contributes", "only fonts", "page count"], "what it uniquely contributes"),
        _gap("Student: Understood. I can send a revised draft on ___.", "Monday", accepted=["Monday"], explanation="Monday"),
    ],
    "dialogue-c1-incident-retro": [
        _choice("What should also happen when error rates exceed two percent?", "page a second person", ["ignore alerts", "page a second person", "delete logs", "end the retro"], "page a second person"),
        _gap("Facilitator: We'll review actions next ___.", "Tuesday", accepted=["Tuesday"], explanation="Tuesday"),
    ],
    "dialogue-c2-editorial-dispute": [
        _choice("What must the headline mirror?", "the narrower claim", ["the strongest rumor", "the narrower claim", "a joke", "nothing"], "the narrower claim"),
        _gap("Lawyer: Send the revised draft within the ___.", "hour", accepted=["hour"], explanation="hour"),
    ],
    "dialogue-c2-board-strategy": [
        _choice("How long is the proposed discount test?", "ninety days", ["one day", "ninety days", "ten years", "forever"], "ninety days"),
        _gap("Chair: Document the decision in the ___ before we adjourn.", "minutes", accepted=["minutes"], explanation="minutes"),
    ],
    "dialogue-c2-climate-panel": [
        _choice("What metric should journalists watch next summer?", "excess deaths during heatwaves", ["only logos", "excess deaths during heatwaves", "stock prices only", "rainfall jokes"], "excess deaths during heatwaves"),
        _gap("Economist: And whether cooling centres are actually ___ after dark.", "reachable", accepted=["reachable"], explanation="reachable"),
    ],
}


def apply_extra_questions(items: list[dict]) -> int:
    """Append EXTRA questions whose prompts are not already on the item. Returns count added."""
    added = 0
    for item in items:
        extras = EXTRA_QUESTIONS_BY_SLUG.get(item["slug"]) or []
        if not extras:
            continue
        questions = item.setdefault("questions", [])
        have = {q.get("prompt") for q in questions if q.get("prompt")}
        for q in extras:
            prompt = q.get("prompt") or ""
            if not prompt or prompt in have:
                continue
            questions.append(q)
            have.add(prompt)
            added += 1
    return added

