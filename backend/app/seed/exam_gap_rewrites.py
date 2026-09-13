# -*- coding: utf-8 -*-
"""Exam / fill-blank prompt rewrites: bare English gaps → Russian task + sentence.

Merged into PROMPT_REWRITES by prompt_rewrites.py (or applied here and extended).
"""

EXAM_GAP_REWRITES: dict[str, str] = {
    # --- A1 core exam ---
    "I ___ from Canada. (be)": "Вставьте форму to be: I ___ from Canada.",
    "She ___ in Lisbon. (live)": "Вставьте глагол в Present Simple: She ___ in Lisbon. (live)",
    "___ a cat on the sofa.": "Выберите правильный вариант: ___ a cat on the sofa.",
    "She ___ play the piano.": (
        "Вставьте модальный глагол can (умение): She ___ play the piano."
    ),
    "I ___ ill last week. (be)": "Вставьте форму to be в Past Simple: I ___ ill last week.",
    "She ___ a new laptop last month.": (
        "Выберите форму Past Simple: She ___ a new laptop last month."
    ),
    "I ___ going to start a course.": (
        "Вставьте форму to be в конструкции be going to: I ___ going to start a course."
    ),
    "The cat is ___ the box. (внутри)": (
        "Выберите предлог места (внутри): The cat is ___ the box."
    ),
    # --- A2 core exam ---
    "While I ___ dinner, the phone rang.": (
        "Выберите время глагола: While I ___ dinner, the phone rang."
    ),
    "I have never ___ to Japan. (be)": (
        "Вставьте третью форму глагола (Present Perfect): I have never ___ to Japan. (be)"
    ),
    "How ___ milk is left?": "Выберите quantifier: How ___ milk is left?",
    "If it rains, we ___ stay at home.": (
        "Вставьте will (First Conditional): If it rains, we ___ stay at home."
    ),
    "I ___ walk to school when I was little.": (
        "Выберите форму used to: I ___ walk to school when I was little."
    ),
    "There isn't ___ sugar.": (
        "Вставьте any/some в отрицании: There isn't ___ sugar."
    ),
    "This book is ___ than that one.": (
        "Выберите сравнительную степень: This book is ___ than that one."
    ),
    "You ___ see a doctor. (совет)": (
        "Вставьте модальный глагол совета (should): You ___ see a doctor."
    ),
    # --- B1 core exam ---
    "I ___ this book last year.": (
        "Выберите время (Past Simple vs Present Perfect): I ___ this book last year."
    ),
    "She has been ___ here since Monday. (work)": (
        "Вставьте -ing форму (Present Perfect Continuous): She has been ___ here since Monday. (work)"
    ),
    "He said he ___ tired.": (
        "Выберите форму в косвенной речи: He said he ___ tired."
    ),
    "I've lived here ___ 2018.": "Вставьте since или for: I've lived here ___ 2018.",
    "The film was so ___ that I left.": (
        "Выберите прилагательное (-ed / -ing): The film was so ___ that I left."
    ),
    "I wish I ___ taller. (be)": (
        "Вставьте форму после wish: I wish I ___ taller. (be)"
    ),
    "Take an umbrella. It ___ rain.": (
        "Выберите модальный глагол возможности: Take an umbrella. It ___ rain."
    ),
    "She looks ___ her little brother. (заботится)": (
        "Вставьте частицу phrasal verb look ___ (заботится): She looks ___ her little brother."
    ),
    # --- B2 core exam ---
    "If I had known, I ___ you.": (
        "Выберите форму в Third Conditional: If I had known, I ___ you."
    ),
    "You should have ___ her. (tell)": (
        "Вставьте третью форму после should have: You should have ___ her. (tell)"
    ),
    "The roof is leaking. We'll ___ soon.": (
        "Выберите каузатив have something done: The roof is leaking. We'll ___ soon."
    ),
    "By next June she ___ have finished the course.": (
        "Вставьте will (Future Perfect): By next June she ___ have finished the course."
    ),
    "I remember ___ the door. (помню, что сделал это)": (
        "Выберите форму после remember (воспоминание о прошлом): I remember ___ the door."
    ),
    "She must have ___ the train. (miss)": (
        "Вставьте третью форму после must have: She must have ___ the train. (miss)"
    ),
    "___ the delay, we arrived on time.": (
        "Выберите Despite / Although: ___ the delay, we arrived on time."
    ),
    "I wish you ___ make so much noise. (would)": (
        "Вставьте would после wish (раздражение): I wish you ___ make so much noise."
    ),
    # --- C1 core exam ---
    "Not only ___ late, he also forgot the files.": (
        "Выберите инверсию после Not only: Not only ___ late, he also forgot the files."
    ),
    "It's time we ___ home. (go)": (
        "Вставьте Past Simple после It's time: It's time we ___ home. (go)"
    ),
    "He is said ___ a fortune.": (
        "Выберите форму после is said: He is said ___ a fortune."
    ),
    "I'd rather you ___ that. (not do)": (
        "Вставьте форму после I'd rather you: I'd rather you ___ that. (not do)"
    ),
    "Unlikely ___ it may seem, the plan worked.": (
        "Выберите as в уступительной конструкции: Unlikely ___ it may seem, the plan worked."
    ),
    "Having ___ the report, she left. (finish)": (
        "Вставьте третью форму после Having: Having ___ the report, she left. (finish)"
    ),
    "The committee insisted that she ___ present.": (
        "Выберите subjunctive после insisted that: The committee insisted that she ___ present."
    ),
    "Scarcely had we sat down ___ the fire alarm went off.": (
        "Вставьте when после Scarcely: Scarcely had we sat down ___ the fire alarm went off."
    ),
    # --- C2 core exam ---
    "Much ___ I admire her, I cannot agree.": (
        "Выберите as в уступке Much ___: Much ___ I admire her, I cannot agree."
    ),
    "Had I ___ the truth, I would have acted sooner. (know)": (
        "Вставьте третью форму после Had I: Had I ___ the truth, I would have acted sooner. (know)"
    ),
    "He might well have ___ the email.": (
        "Выберите третью форму после might well have: He might well have ___ the email."
    ),
    "No sooner had the doors opened ___ the crowd rushed in.": (
        "Вставьте than после No sooner: No sooner had the doors opened ___ the crowd rushed in."
    ),
    "I'd just as soon you ___ here.": (
        "Выберите форму после I'd just as soon you: I'd just as soon you ___ here."
    ),
    "Far from ___ the problem, the new rule made it worse. (solve)": (
        "Вставьте герундий после Far from: Far from ___ the problem, the new rule made it worse. (solve)"
    ),
    "Were it not ___ your help, we would have failed.": (
        "Выберите предлог: Were it not ___ your help, we would have failed."
    ),
    "I would sooner ___ than lie. (leave)": (
        "Вставьте голый инфинитив после would sooner: I would sooner ___ than lie. (leave)"
    ),
    # --- EXTRA A1 ---
    "They ___ students.": "Выберите форму to be: They ___ students.",
    "___ she at home?": "Вставьте форму to be в вопросе: ___ she at home?",
    "I bought ___ university guidebook.": (
        "Выберите артикль: I bought ___ university guidebook."
    ),
    "There ___ some milk.": "Вставьте is/are: There ___ some milk.",
    "See you ___ Friday.": "Выберите предлог времени: See you ___ Friday.",
    "Yesterday they ___ football. (play)": (
        "Вставьте Past Simple: Yesterday they ___ football. (play)"
    ),
    # --- EXTRA A2 ---
    "Look! She ___ a yellow coat today.": (
        "Выберите время (Present Continuous): Look! She ___ a yellow coat today."
    ),
    "I ___ already finished. (have)": (
        "Вставьте have/has (Present Perfect): I ___ already finished."
    ),
    "You ___ to wear a helmet here.": (
        "Выберите модальную конструкцию обязанности: You ___ to wear a helmet here."
    ),
    "If you heat ice, it ___. (melt)": (
        "Вставьте Present Simple (Zero Conditional): If you heat ice, it ___. (melt)"
    ),
    "This is the ___ film I have ever seen.": (
        "Выберите превосходную степень: This is the ___ film I have ever seen."
    ),
    "She isn't old ___ to drive.": (
        "Вставьте enough: She isn't old ___ to drive."
    ),
    # --- EXTRA B1 ---
    "I ___ my keys. I can't find them.": (
        "Выберите время (результат сейчас): I ___ my keys. I can't find them."
    ),
    "They ___ dinner when we arrived. (have)": (
        "Вставьте Past Continuous: They ___ dinner when we arrived. (have)"
    ),
    "The windows ___ yesterday.": (
        "Выберите Past Passive: The windows ___ yesterday."
    ),
    "I've been waiting ___ an hour.": (
        "Вставьте for или since: I've been waiting ___ an hour."
    ),
    "She suggested ___ a taxi.": (
        "Выберите форму после suggested: She suggested ___ a taxi."
    ),
    "He's the doctor ___ helped us.": (
        "Вставьте относительное местоимение: He's the doctor ___ helped us."
    ),
    # --- EXTRA B2 ---
    "I'm having my hair ___ tomorrow.": (
        "Выберите форму в каузативе have something done: I'm having my hair ___ tomorrow."
    ),
    "She can't have ___ the news. She looks calm. (hear)": (
        "Вставьте третью форму после can't have: She can't have ___ the news. (hear)"
    ),
    "Not until midnight ___ the truth.": (
        "Выберите инверсию после Not until: Not until midnight ___ the truth."
    ),
    "I'd rather you ___ here. (stay)": (
        "Вставьте Past Simple после I'd rather you: I'd rather you ___ here. (stay)"
    ),
    "By the time we arrived, the film ___.": (
        "Выберите Past Perfect: By the time we arrived, the film ___."
    ),
    "She is thought ___ abroad. (live, сейчас)": (
        "Вставьте to-infinitive после is thought: She is thought ___ abroad. (live)"
    ),
    # --- EXTRA C1 ---
    "Should you need help, ___ me.": (
        "Выберите форму после Should you need help: Should you need help, ___ me."
    ),
    "It is essential that he ___ on time. (arrive)": (
        "Вставьте subjunctive после essential that: It is essential that he ___ on time. (arrive)"
    ),
    "Only then ___ how serious it was.": (
        "Выберите инверсию после Only then: Only then ___ how serious it was."
    ),
    "Were she ___ apply, she would get it. (to)": (
        "Вставьте to в Were she to…: Were she ___ apply, she would get it."
    ),
    "The results appear ___ leaked.": (
        "Выберите perfect infinitive после appear: The results appear ___ leaked."
    ),
    "Much as I ___ him, I disagree. (like)": (
        "Вставьте глагол: Much as I ___ him, I disagree. (like)"
    ),
    # --- EXTRA C2 ---
    "Come what ___, we finish tonight.": (
        "Выберите may в идиоме: Come what ___, we finish tonight."
    ),
    "Выберите may в идиоме Come what ___: Come what ___, we finish tonight.": (
        "Выберите may в идиоме: Come what ___, we finish tonight."
    ),
    "Suffice it ___ say the plan failed.": (
        "Вставьте to: Suffice it ___ say the plan failed."
    ),
    "He is not so much a teacher ___ a performer.": (
        "Выберите as в not so much … as: He is not so much a teacher ___ a performer."
    ),
    "Be that as it ___.": "Вставьте may: Be that as it ___.",
    "Be that as it ___, we continue.": (
        "Вставьте may: Be that as it ___, we continue."
    ),
    "The more he explained, ___ confused I became.": (
        "Выберите the more в the…, the…: The more he explained, ___ confused I became."
    ),
    "Had it not ___ for her, we would have quit. (be)": (
        "Вставьте been: Had it not ___ for her, we would have quit. (be)"
    ),
    # --- A1 can module (practice/test) ---
    "___ I use your phone?": "Вставьте Can (разрешение): ___ I use your phone?",
    "Birds ___ fly.": "Вставьте модальный глагол can: Birds ___ fly.",
    "He ___ not swim.": "Вставьте can перед not: He ___ not swim.",
    "___ you help me?": "Выберите модальный глагол просьбы: ___ you help me?",
    "We ___ hear you.": "Выберите отрицание модального can: We ___ hear you.",
    "I ___ see the sea from here.": (
        "Выберите can (возможность): I ___ see the sea from here."
    ),
    "She ___ speak Japanese, but she ___ write it well.": (
        "Выберите пару can / can't: She ___ speak Japanese, but she ___ write it well."
    ),
}
