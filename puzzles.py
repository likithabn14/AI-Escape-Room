import random

# ==========================================================
# RANDOM RIDDLES
# ==========================================================

RIDDLES = [

    {
        "question": "I speak without a mouth and hear without ears. What am I?",
        "answer": "echo",
        "hints": [
            "You hear it in valleys.",
            "It repeats what you say.",
            "Mountains are famous for it."
        ]
    },

    {
        "question": "The more you take, the more you leave behind. What are they?",
        "answer": "footsteps",
        "hints": [
            "Think while walking.",
            "You leave them on sand.",
            "Shoes make them."
        ]
    },

    {
        "question": "What has keys but can't open locks?",
        "answer": "piano",
        "hints": [
            "It makes music.",
            "It has black and white keys.",
            "Mozart played one."
        ]
    },

    {
        "question": "What gets wetter as it dries?",
        "answer": "towel",
        "hints": [
            "Used after bathing.",
            "Found in bathrooms.",
            "It dries you."
        ]
    },

    {
        "question": "What has one eye but cannot see?",
        "answer": "needle",
        "hints": [
            "Used for sewing.",
            "Thread passes through it.",
            "Tailors use it."
        ]
    },

    {
        "question": "What has many teeth but cannot bite?",
        "answer": "comb",
        "hints": [
            "Used every morning.",
            "It helps your hair.",
            "Found near mirrors."
        ]
    },

    {
        "question": "What is full of holes but still holds water?",
        "answer": "sponge",
        "hints": [
            "Used for washing.",
            "Soft and absorbs water.",
            "Found in kitchens."
        ]
    },

    {
        "question": "I have cities but no houses, rivers but no water and forests but no trees. What am I?",
        "answer": "map",
        "hints": [
            "Used while travelling.",
            "Shows countries.",
            "Google also has one."
        ]
    },

    {
        "question": "What can travel around the world while staying in one corner?",
        "answer": "stamp",
        "hints": [
            "Used with letters.",
            "Found on envelopes.",
            "Post offices sell it."
        ]
    },

    {
        "question": "What comes once in a minute, twice in a moment and never in a thousand years?",
        "answer": "m",
        "hints": [
            "It is not a number.",
            "Think about letters.",
            "Count the letter appearances."
        ]
    }

]


def random_riddle():
    return random.choice(RIDDLES)


# ==========================================================
# MATH PUZZLE
# ==========================================================

MATH_PUZZLES = [

{
    "question":"25 + 15 = ?",
    "answer":40,
    "hints":[
        "Addition",
        "25+10=35",
        "35+5=40"
    ]
},

{
    "question":"12 × 8 = ?",
    "answer":96,
    "hints":[
        "Multiply",
        "12×4=48",
        "Double it"
    ]
},

{
    "question":"100 ÷ 5 = ?",
    "answer":20,
    "hints":[
        "Division",
        "Half of 100 is 50",
        "50÷2=25? Think again."
    ]
}

]

def random_math():
    return random.choice(MATH_PUZZLES)

# ==========================================================
# CAESAR CIPHER
# ==========================================================

# ==========================================================
# CAESAR CIPHER
# ==========================================================

CAESAR_PUZZLES = [

{
    "question":"Decode: KHOOR (Shift -3)",
    "answer":"hello",
    "hints":[
        "Move every letter back by 3.",
        "K becomes H.",
        "It's a greeting."
    ]
},

{
    "question":"Decode: ZRUOG (Shift -3)",
    "answer":"world",
    "hints":[
        "Move every letter back by 3.",
        "Z becomes W.",
        "The Earth is also called this."
    ]
},

{
    "question":"Decode: FRGH (Shift -3)",
    "answer":"code",
    "hints":[
        "Shift back 3 letters.",
        "F becomes C.",
        "Programmers write this."
    ]
}

]

def random_caesar():
    return random.choice(CAESAR_PUZZLES)


# ==========================================================
# EMOJI PUZZLES
# ==========================================================

EMOJI_PUZZLES = [

{
    "question":"🐝 + 🍯 = ?",
    "answer":"honey",
    "hints":[
        "The first emoji is an insect.",
        "The second emoji is sweet.",
        "Bees make it."
    ]
},

{
    "question":"🍎 + 🥧 = ?",
    "answer":"apple pie",
    "hints":[
        "First emoji is a fruit.",
        "Second is a dessert.",
        "A famous pie."
    ]
},

{
    "question":"🌧️ + 🌈 = ?",
    "answer":"rainbow",
    "hints":[
        "Appears after rain.",
        "Has seven colours.",
        "Seen in the sky."
    ]
}

]

def random_emoji():
    return random.choice(EMOJI_PUZZLES)


# ==========================================================
# LOGIC PUZZLES
# ==========================================================

LOGIC_PUZZLES = [

{
    "question":"A farmer has 17 sheep. All but 9 die. How many are left?",
    "answer":"9",
    "hints":[
        "Read carefully.",
        "Only 9 survive.",
        "Count the living sheep."
    ]
},

{
    "question":"How many months have 28 days?",
    "answer":"12",
    "hints":[
        "Not just February.",
        "Every month has at least 28 days.",
        "Count all the months."
    ]
},

{
    "question":"What comes after Monday?",
    "answer":"tuesday",
    "hints":[
        "Think of the week.",
        "Second day.",
        "Starts with T."
    ]
}

]

def random_logic():
    return random.choice(LOGIC_PUZZLES)


