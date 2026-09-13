"""Longer original passages + C1/C2 skill items for lEarNinG.

All texts are written for this product. Apply via apply_longform() after base lists load.
"""

from __future__ import annotations


# --- Body upgrades (preserve facts used by existing questions) --------------

READING_BODIES: dict[str, str] = {
    "reading-a1-morning-bus": (
        "Every morning Lena wakes up at seven. She drinks tea and eats bread with cheese. "
        "She puts on her coat, checks her bag, and leaves the flat while the street is still quiet.\n\n"
        "Then she takes the bus to work. The bus is often full, but she finds a seat near the window. "
        "She looks at the trees and feels calm before a busy day. Sometimes she reads a short message from her sister.\n\n"
        "At the office she smiles at the receptionist and starts her computer. "
        "The short ride helps her begin the day without hurry."
    ),
    "reading-a1-new-neighbour": (
        "Omar moves into a small flat on Green Street. The rooms are bright, and there is a little balcony with two chairs. "
        "On the first day his neighbour Anna knocks on the door. She brings a cake and says hello.\n\n"
        "Omar smiles and invites her for coffee next week. They talk about the shops nearby and the best time to use the laundry room. "
        "He thinks the building feels friendly already.\n\n"
        "In the evening Omar unpacks boxes and puts a plant on the windowsill. "
        "He is tired, but he is happy to have a kind neighbour so soon."
    ),
    "reading-a1-market-day": (
        "On Saturday Maya goes to the outdoor market. The air smells of fruit and warm bread. "
        "She buys tomatoes, apples, and fresh bread. She asks about the price and counts her coins carefully.\n\n"
        "The seller gives her a free orange because she is a regular customer. Maya thanks him and puts everything in a cloth bag. "
        "Then she walks home slowly and plans a simple salad for lunch.\n\n"
        "At home she washes the tomatoes and places the orange in a bowl. "
        "She likes market days because they feel calm and useful."
    ),
    "reading-a1-lost-keys": (
        "This morning Tim cannot find his keys. He looks under the sofa and in his jacket. "
        "He checks the hallway shelf and even the bathroom, feeling a little worried about being late.\n\n"
        "His sister finds them on the kitchen table next to a bowl of fruit. "
        "Tim laughs and puts the keys on a small hook by the door.\n\n"
        "Before he leaves, he tells his sister thank you and sets a reminder to always use the hook. "
        "A calm morning is easier when keys have one clear place."
    ),
    "reading-a1-pet-goldfish": (
        "Nora has a small goldfish in a glass bowl. Every evening she gives it a little food. "
        "She changes the water once a week and keeps the bowl away from the hot window.\n\n"
        "The fish swims slowly and Nora watches it after homework. "
        "Sometimes she draws the goldfish in her notebook when she needs a short break.\n\n"
        "Caring for the pet is simple, but it helps Nora feel responsible and calm after a long school day."
    ),
    "reading-a1-birthday-card": (
        "Tomorrow is Grandma's birthday. Rita buys a bright card and writes a short message. "
        "She also buys yellow flowers at the corner shop and hides them in a bag until evening.\n\n"
        "In the evening the family sings and Grandma smiles for a long time. "
        "They take a photo near the cake and read the card together twice.\n\n"
        "Rita feels happy that a small gift and kind words can make the whole room warmer."
    ),
    "reading-a2-library-card": (
        "Last month Denis got a library card. He wanted quiet books about travel and science. "
        "The librarian showed him how to search the catalogue and how long he could keep a book.\n\n"
        "Now he borrows two books every fortnight and returns them on time. "
        "Sometimes he reads in a corner seat near the window, and sometimes he takes notes on his phone.\n\n"
        "He says the library saves him money and helps him learn new words. "
        "It also gives him a calm place when the city feels too noisy."
    ),
    "reading-a2-rainy-picnic": (
        "The family planned a picnic by the lake. In the morning the sky was clear, so they packed sandwiches and a ball. "
        "The children were excited and sang in the car.\n\n"
        "At noon dark clouds arrived and cold rain started. They ran to the car and ate inside while listening to music. "
        "Nobody was angry. They joked that indoor picnics can be fun too.\n\n"
        "On the way home they stopped for hot chocolate. "
        "The day was different from the plan, but it still felt like a family adventure."
    ),
    "reading-a2-office-plant": (
        "Someone left a small plant on the shared desk. At first nobody watered it, and the soil became dry. "
        "Then Irina brought a cup of water every Monday.\n\n"
        "Soon the leaves became greener, and people started smiling at the plant. "
        "Now the team takes turns caring for it. They call it 'Office Friend'.\n\n"
        "On Fridays someone wipes the leaves and turns the pot toward the light. "
        "A quiet plant has become a small reason for colleagues to talk."
    ),
    "reading-a2-train-ticket": (
        "Anton needed a train ticket to visit his uncle. At the station he chose a morning seat by the window. "
        "The clerk asked for his ID and printed a paper ticket with a QR code.\n\n"
        "Anton saved the PDF on his phone as a backup and arrived twenty minutes early. "
        "He bought tea, checked the platform board twice, and found his carriage without hurry.\n\n"
        "On the train he watched the fields and thought about stories he would share with his uncle. "
        "A little preparation made the trip feel easy."
    ),
    "reading-a2-burnt-toast": (
        "Lara wanted a quick breakfast before work. She put bread in the toaster and opened her emails. "
        "A minute later she smelled smoke. The toast was black, so she opened the window and made porridge instead.\n\n"
        "While the porridge cooked, she cleaned the toaster tray and poured a glass of water. "
        "She set a louder timer on her phone for next time.\n\n"
        "Lara still arrived at work on time, laughing about the small kitchen lesson. "
        "Multitasking, she decided, is not always faster."
    ),
    "reading-a2-weekend-hike": (
        "On Sunday four friends hiked a forest trail near the river. They packed water, sandwiches, and a small first-aid kit. "
        "The morning air was cool, and birds were loud in the trees.\n\n"
        "After two hours they reached a viewpoint and took photos of the valley. "
        "They rested, shared fruit, and checked the map before walking down.\n\n"
        "On the way down it got muddy, but nobody fell, and they promised to return in spring. "
        "Tired legs felt worth it for the quiet day outside the city."
    ),
    "reading-b1-night-shift": (
        "Sofia works as a nurse on the night shift three times a week. The hospital corridor is quieter after midnight, "
        "but alarms still break the silence. She checks patients, writes short notes, and drinks strong tea to stay alert.\n\n"
        "Between rounds she talks softly with colleagues and updates charts on a shared computer. "
        "Some nights feel long, especially when several patients need help at once.\n\n"
        "On her free mornings she sleeps until noon and then walks in the park. "
        "She admits the schedule is hard, yet she likes helping people when few others are around. "
        "The work teaches her to stay calm under pressure."
    ),
    "reading-b1-second-hand-bike": (
        "After months of crowded buses, Pavel decided to buy a second-hand bike. "
        "He checked the brakes, the tyres, and the chain at a small workshop before paying. "
        "The seller explained a few maintenance tips and wished him safe rides.\n\n"
        "For the first week Pavel practised on quiet streets near his home. "
        "He bought lights and a simple lock, then planned a safer route to the office.\n\n"
        "Now Pavel cycles to the office and arrives earlier — and less tired — than before. "
        "He also enjoys the fresh air, even on cool mornings."
    ),
    "reading-b1-language-exchange": (
        "Once a week Katya meets Diego in a quiet café for a language exchange. "
        "For thirty minutes they speak only English; then they switch to Spanish. "
        "They correct each other gently and write useful phrases in a shared notebook.\n\n"
        "Sometimes they bring short articles or funny videos and explain new words in simple sentences. "
        "The meetings feel friendly, not like a formal exam.\n\n"
        "After three months Katya feels braver ordering food abroad, and Diego finally understands Russian jokes in class. "
        "Both say the exchange works because they show up every week."
    ),
    "reading-b1-thrift-jacket": (
        "Masha prefers thrift shops because she likes unique clothes and lower prices. "
        "Last Saturday she found a warm wool jacket that fitted perfectly after a small repair to the zipper.\n\n"
        "She washed it carefully and wore it to a winter market. "
        "The jacket kept her warm while she looked at handmade candles and drank tea from a paper cup.\n\n"
        "Two friends asked where she bought it, and she happily shared the shop's address. "
        "For Masha, second-hand shopping is both practical and creative."
    ),
    "reading-b1-food-bank": (
        "Every other Saturday Oleg volunteers at a local food bank. He sorts donated cans, checks expiry dates, and packs boxes for families. "
        "The work is physical, but the team chat is friendly and breaks include strong coffee.\n\n"
        "New volunteers learn the shelf system quickly, and regulars know which items are needed most that week. "
        "Oleg likes the clear tasks and the quiet sense of purpose.\n\n"
        "Oleg says the shift reminds him how small actions can reduce stress for neighbours who are short on time and money. "
        "He plans to keep the Saturday habit through winter."
    ),
    "reading-b2-community-garden": (
        "Behind the apartment block there used to be an empty yard full of weeds. "
        "A group of residents asked the council for permission to start a community garden. "
        "They raised funds for soil and tools, then planted beans, herbs, and sunflowers.\n\n"
        "Children water the beds after school, and in late summer they share harvest baskets. "
        "Meetings are short and practical: who buys seeds, who repairs the fence, who writes updates for the group chat.\n\n"
        "The project has not removed every problem in the neighbourhood, but people talk to each other more often now. "
        "Even residents who do not garden stop to ask about the tomatoes."
    ),
    "reading-b2-remote-week": (
        "For one week Nadia’s team worked entirely from home. Without the commute she gained almost two hours a day, "
        "which she spent cooking proper lunches and finishing a short online course.\n\n"
        "Still, she missed quick hallway chats that often solved small problems faster than long emails. "
        "She also noticed that video calls needed clearer agendas than casual desk conversations.\n\n"
        "On Friday the team agreed to keep two remote days and three office days — a compromise that felt practical rather than perfect. "
        "Nadia booked focus time on remote mornings and left office days for workshops and brainstorming."
    ),
    "reading-b2-podcast-habit": (
        "Instead of scrolling social media on the tram, Ilya started listening to short science podcasts. "
        "He chooses episodes under twenty minutes so he can finish one before his stop.\n\n"
        "At first the hosts spoke too quickly, so he lowered the speed to 0.9 and kept a notes app for new terms. "
        "When a word appeared again in a later episode, he felt a small win.\n\n"
        "After two months he notices he remembers more vocabulary and feels less restless during delays. "
        "A simple audio habit replaced empty scrolling without feeling like extra homework."
    ),
    "reading-b2-coworking-trial": (
        "Vera tested a coworking space for one week because her flat felt too quiet for deep work. "
        "The day pass included a desk, fast Wi‑Fi, and unlimited tea. She liked the focus rooms but disliked the noisy kitchen at noon.\n\n"
        "She also noticed that short chats near the coffee machine gave her ideas for client emails. "
        "Still, she protected deep-work hours with headphones and a clear task list.\n\n"
        "On Friday she bought a part-time membership for three mornings a week — enough structure without losing her home office entirely. "
        "Balance, not a full escape from home, was what she needed."
    ),
    "reading-b2p-invoice-delay": (
        "When a client's payment was five days late, Dana checked her sent folder before writing an angry message. "
        "She discovered the invoice had landed in spam and the purchase order number was missing from the subject line.\n\n"
        "She resent a clearer PDF, copied the accounts team, and proposed a 48-hour confirmation window. "
        "The tone stayed polite but firm, with exact dates and a single call-to-action.\n\n"
        "The money arrived the next morning; Dana later added a checklist so the same mix-up would be less likely. "
        "A calm process protected the relationship better than a sharp email would have."
    ),
}

LISTENING_BODIES: dict[str, str] = {
    "listening-a1-weather-note": (
        "It is cold today. Please wear a warm jacket.\n\n"
        "The wind is stronger near the river, so a scarf will help if you walk outside. "
        "In the evening it may feel even colder than this morning."
    ),
    "listening-a1-shop-hours": (
        "The shop opens at nine and closes at eight. Sunday is closed.\n\n"
        "On other days you can pay by card near the till. "
        "If you need help finding a size, ask a member of staff."
    ),
    "listening-a1-meet-friend": (
        "Let's meet at the station at five. I will wait near the ticket office.\n\n"
        "If your train is late, send a short message. "
        "We can walk to the café after we meet."
    ),
    "listening-a1-bakery-order": (
        "I would like two fresh rolls and one apple pie, please.\n\n"
        "Could you put them in a paper bag? I will eat the pie later at work. "
        "Thank you."
    ),
    "listening-a1-gym-hours": (
        "The gym opens at six in the morning. It closes at ten at night.\n\n"
        "Please bring a towel and clean indoor shoes. "
        "The pool area may close earlier for cleaning on some days."
    ),
    "listening-a1-phone-battery": (
        "My phone battery is low. May I borrow your charger for ten minutes?\n\n"
        "I need to send one message before the meeting starts. "
        "I will give the charger back as soon as the phone reaches twenty percent."
    ),
    "listening-a2-kitchen-tip": (
        "Boil the water first. Add salt, then put the pasta in. Stir it after two minutes.\n\n"
        "Taste a piece before you drain the pan. When the pasta is soft enough, mix it with a simple sauce and serve it hot."
    ),
    "listening-a2-missed-call": (
        "Hi, it's Mark. I missed your call because I was in a meeting. Call me after lunch, please.\n\n"
        "I will be free around two o'clock. If email is easier, send the details there and I will reply today."
    ),
    "listening-a2-bus-delay": (
        "Bus number twelve is delayed by fifteen minutes. We are sorry for the inconvenience.\n\n"
        "You can wait at this stop or check the board for the next service toward the square. "
        "Thank you for your patience."
    ),
    "listening-a2-laundry-note": (
        "Please move your clothes from the machine when it beeps. I need to start a new wash at seven.\n\n"
        "The detergent is under the sink if you need more. "
        "Thank you for helping keep the laundry room free."
    ),
    "listening-a2-parcel-pickup": (
        "Your parcel is ready at locker B fourteen. Bring your code and ID card.\n\n"
        "The pickup point is open until seven on weekdays. "
        "If the locker does not open, ask the desk for help."
    ),
    "listening-a2-class-cancel": (
        "Today's evening class is cancelled because the teacher is ill. We will catch up next Monday at the same time.\n\n"
        "Please check the group chat for any room changes. "
        "Homework from last week is still due on Monday."
    ),
    "listening-b1-museum-rules": (
        "Please keep your bags in the lockers. Do not touch the exhibits. "
        "Photography without flash is allowed in most rooms.\n\n"
        "Food and drinks stay outside the galleries. "
        "If you need help, ask a member of staff near the information desk."
    ),
    "listening-b1-project-update": (
        "We finished the draft yesterday. Today we need feedback from the design team. "
        "The final version should be ready by Thursday.\n\n"
        "Please leave comments in the shared document before noon so we can adjust the layout. "
        "If anything blocks you, write it in the channel."
    ),
    "listening-b1-flight-gate": (
        "Passengers for flight four one nine to Berlin, please proceed to gate twenty-two. "
        "Boarding begins in fifteen minutes.\n\n"
        "Please have your boarding pass and passport ready. "
        "Families with children and passengers who need assistance may board when we invite them first."
    ),
    "listening-b1-password-reset": (
        "We received a request to reset your password. "
        "If this was you, tap the link in your email within one hour. "
        "If not, ignore this message and keep your current password.\n\n"
        "For safety, do not share the link with anyone. "
        "If you need more help, contact support from the official website only."
    ),
    "listening-b1-recycling-tip": (
        "Rinse plastic containers before recycling. "
        "Flatten cardboard boxes to save space. "
        "Please do not put batteries in the general bin.\n\n"
        "Clean paper can go with cardboard. "
        "There is a small collection point for batteries at the supermarket entrance."
    ),
    "listening-b2-city-survey": (
        "The city is collecting opinions about new bike lanes. "
        "You can fill in the online form until the end of the month. "
        "Results will be published on the official website.\n\n"
        "Paper forms are also available at the library if you prefer not to answer online. "
        "Your feedback will help plan safer routes for next year."
    ),
    "listening-b2-apartment-viewing": (
        "The flat has two bedrooms and a bright kitchen. "
        "The rent includes heating but not electricity. "
        "We can show it tomorrow afternoon if that suits you.\n\n"
        "The building has a quiet courtyard and a locked bicycle room. "
        "If you like the flat, bring your documents so we can discuss the deposit."
    ),
    "listening-b2-standup-blocker": (
        "Yesterday I finished the login tests. "
        "Today I'm stuck waiting for API access from the security team. "
        "If anyone has a spare sandbox key, please message me after the call.\n\n"
        "While I wait, I will tidy the error messages on the login screen and update the test notes."
    ),
    "listening-b2-rent-notice": (
        "From next month the rent will rise by three percent. "
        "The increase covers higher heating costs. "
        "Contact the office before Friday if you need a payment plan.\n\n"
        "Please include your flat number in any email so we can find your contract quickly. "
        "Thank you for reading this notice."
    ),
    "listening-b2p-workshop-brief": (
        "Welcome to today's writing workshop. "
        "Please silence your phones and join the shared document with your real first name. "
        "We will draft for twenty minutes, then swap feedback in pairs.\n\n"
        "Use the timer on the screen and keep comments kind and specific. "
        "At the end we will collect one useful tip from each pair."
    ),
}


def apply_longform(
    reading_items: list[dict],
    listening_items: list[dict],
    dialogue_items: list[dict],
) -> None:
    """Mutate base skill lists: lengthen bodies/lines and append upper-level extras."""
    from app.seed.skills_dialogues_long import DIALOGUE_LINES
    from app.seed.skills_upper import EXTRA_DIALOGUE, EXTRA_LISTENING, EXTRA_READING

    for item in reading_items:
        body = READING_BODIES.get(item["slug"])
        if body:
            item["body"] = body

    for item in listening_items:
        body = LISTENING_BODIES.get(item["slug"])
        if body:
            item["body"] = body

    for item in dialogue_items:
        lines = DIALOGUE_LINES.get(item["slug"])
        if lines:
            item["lines"] = lines

    existing_r = {i["slug"] for i in reading_items}
    existing_l = {i["slug"] for i in listening_items}
    existing_d = {i["slug"] for i in dialogue_items}
    reading_items.extend(x for x in EXTRA_READING if x["slug"] not in existing_r)
    listening_items.extend(x for x in EXTRA_LISTENING if x["slug"] not in existing_l)
    dialogue_items.extend(x for x in EXTRA_DIALOGUE if x["slug"] not in existing_d)

