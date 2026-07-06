import streamlit as st
import pandas as pd
import random
import time
import os
from datetime import datetime

from streamlit.components.v1 import html
from streamlit_extras.let_it_rain import rain

from puzzles import *

# ---------------- PAGE ---------------- #

st.set_page_config(
    page_title="AI Escape Room",
    page_icon="🧩",
    layout="wide"
)

LEADERBOARD = "leaderboard.csv"

if not os.path.exists(LEADERBOARD):
    pd.DataFrame(
        columns=["Name", "Score", "Completed At"]
    ).to_csv(LEADERBOARD, index=False)

# ---------------- SESSION ---------------- #

defaults = {

    "started": False,

    "name": "",

    "score": 0,

    "lives": 5,

    "hint_tokens": 3,

    "hint_level": 0,

    "stage": 0,

    "won": False,

    "game_over": False,

    "start_time": None,

    "time_limit": 300,

    "riddle": random_riddle(),

    "math": random_math(),

    "caesar": random_caesar(),

    "emoji": random_emoji(),

    "logic": random_logic()

}

for k, v in defaults.items():

    if k not in st.session_state:

        st.session_state[k] = v

# ---------------- CSS ---------------- #

st.markdown("""
<style>

html,body,.stApp{

background:#050505;

color:white;

}

.block-container{

padding-top:1rem;

}

.title{

text-align:center;

font-size:60px;

font-weight:bold;

color:#00ffe7;

text-shadow:0px 0px 20px cyan;

}

.subtitle{

text-align:center;

color:#bbbbbb;

font-size:20px;

margin-bottom:20px;

}

.card{

background:#101010;

padding:25px;

border-radius:18px;

border:2px solid cyan;

box-shadow:0px 0px 20px rgba(0,255,255,.25);

}

.stage{

font-size:34px;

text-align:center;

color:#00ffe7;

font-weight:bold;

}

.question{

font-size:22px;

margin-top:15px;

margin-bottom:20px;

}

.metric{

text-align:center;

font-size:18px;

font-weight:bold;

color:#00ffe7;

}

.stButton>button{

width:100%;

background:#00ffe7;

color:black;

font-weight:bold;

border-radius:10px;

border:none;

height:3em;

}

.stTextInput input{

background:#111;

color:white;

}

</style>

""", unsafe_allow_html=True)

# ---------------- INTRO ---------------- #

if not st.session_state.started:

    html("""

    <div style="text-align:center;margin-top:40px;">

    <h1 style="font-size:70px;
    color:#00ffe7;
    animation:glow 1s infinite alternate;">

    AI ESCAPE ROOM

    </h1>

    <h3 style="color:white">

    Solve every puzzle before time runs out.

    </h3>

    </div>

    <style>

    @keyframes glow{

    from{ text-shadow:0 0 10px cyan;}

    to{ text-shadow:0 0 35px cyan;}

    }

    </style>

    """, height=220)

    st.markdown("##")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        name = st.text_input(
            "Enter Your Name"
        )

        if st.button("🚀 Start Game"):

            if name.strip() == "":

                st.warning("Enter your name.")

                st.stop()

            st.session_state.name = name

            st.session_state.started = True

            st.session_state.start_time = time.time()

            st.rerun()

    st.stop()

# ---------------- TIMER ---------------- #

elapsed = int(time.time() - st.session_state.start_time)

remaining = st.session_state.time_limit - elapsed

if remaining <= 0:

    remaining = 0

    st.session_state.game_over = True

minutes = remaining // 60

seconds = remaining % 60

# ---------------- HEADER ---------------- #

st.markdown(
    "<div class='title'>AI ESCAPE ROOM</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"<div class='subtitle'>Welcome, {st.session_state.name}</div>",
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown(
        f"<div class='metric'>⏳ {minutes:02}:{seconds:02}</div>",
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"<div class='metric'>⭐ Score<br>{st.session_state.score}</div>",
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        f"<div class='metric'>❤️ Lives<br>{st.session_state.lives}</div>",
        unsafe_allow_html=True
    )

with c4:

    st.markdown(
        f"<div class='metric'>💡 Hints<br>{st.session_state.hint_tokens}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------------- HELPERS ---------------- #

def lose_life():

    st.session_state.lives -= 1

    if st.session_state.lives <= 0:

        st.session_state.game_over = True


def next_stage(points=20):

    st.session_state.score += points

    st.session_state.stage += 1

    st.session_state.hint_level = 0

    st.success("Correct!")

    time.sleep(1)

    st.rerun()


def show_hints(hints):

    if st.session_state.hint_tokens <= 0:

        st.warning("No hints remaining.")

        return

    if st.session_state.hint_level >= len(hints):

        st.info("All hints already shown.")

        return

    st.info(
        f"💡 Hint {st.session_state.hint_level+1}: {hints[st.session_state.hint_level]}"
    )

    st.session_state.hint_level += 1

    st.session_state.hint_tokens -= 1

    # ---------------- GAME OVER ---------------- #

if st.session_state.game_over:

    st.error("⏰ Time's up or you've lost all your lives!")

    st.subheader(f"Final Score: {st.session_state.score}")

    if st.button("🔄 Restart"):

        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.rerun()

    st.stop()

# ==========================================================
# STAGE 1 : RANDOM RIDDLE
# ==========================================================

if st.session_state.stage == 0:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(
        "<div class='stage'>Stage 1 - Random Riddle</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='question'>{st.session_state.riddle['question']}</div>",
        unsafe_allow_html=True
    )

    ans = st.text_input(
        "Your Answer",
        key="riddle_answer"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("Submit", key="submit_riddle"):

            if ans.strip().lower() == st.session_state.riddle["answer"].lower():

                next_stage()

            else:

                lose_life()

                st.error("Wrong answer!")

    with c2:

        if st.button("Use Hint", key="hint_riddle"):

            show_hints(st.session_state.riddle["hints"])

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# STAGE 2 : MATH
# ==========================================================

elif st.session_state.stage == 1:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(
        "<div class='stage'>Stage 2 - Math Puzzle</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='question'>{st.session_state.math['question']}</div>",
        unsafe_allow_html=True
    )

    ans = st.text_input(
        "Answer",
        key="math_answer"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("Submit", key="submit_math"):

            if ans.strip() == str(st.session_state.math["answer"]):

                next_stage()

            else:

                lose_life()

                st.error("Wrong answer!")

    with c2:

        if st.button("Use Hint", key="hint_math"):

            show_hints(st.session_state.math["hints"])

    st.markdown("</div>", unsafe_allow_html=True)
# ==========================================================
# STAGE 3 : CAESAR CIPHER
# ==========================================================

elif st.session_state.stage == 2:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(
        "<div class='stage'>Stage 3 - Caesar Cipher</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='question'>{st.session_state.caesar['question']}</div>",
        unsafe_allow_html=True
    )

    ans = st.text_input(
        "Decoded Word",
        key="cipher_answer"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("Submit", key="submit_cipher"):

            if ans.strip().lower() == st.session_state.caesar["answer"].lower():

                next_stage()

            else:

                lose_life()

                st.error("Wrong answer!")

    with c2:

        if st.button("Use Hint", key="hint_cipher"):

            show_hints(st.session_state.caesar["hints"])

    st.markdown("</div>", unsafe_allow_html=True)

 # ==========================================================
# STAGE 4 : EMOJI PUZZLE
# ==========================================================

elif st.session_state.stage == 3:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(
        "<div class='stage'>Stage 4 - Emoji Puzzle</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='question'>{st.session_state.emoji['question']}</div>",
        unsafe_allow_html=True
    )

    ans = st.text_input(
        "Your Answer",
        key="emoji_answer"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("Submit", key="submit_emoji"):

            if ans.strip().lower() == st.session_state.emoji["answer"].lower():

                next_stage()

            else:

                lose_life()

                st.error("Wrong answer!")

    with c2:

        if st.button("Use Hint", key="hint_emoji"):

            show_hints(st.session_state.emoji["hints"])

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# STAGE 5 : LOGIC PUZZLE
# ==========================================================

elif st.session_state.stage == 4:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(
        "<div class='stage'>Stage 5 - Logic Puzzle</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='question'>{st.session_state.logic['question']}</div>",
        unsafe_allow_html=True
    )

    ans = st.text_input(
        "Answer",
        key="logic_answer"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("Submit", key="submit_logic"):

            if ans.strip().lower() == st.session_state.logic["answer"].lower():

                st.session_state.score += 20
                st.session_state.won = True
                st.rerun()

            else:

                lose_life()
                st.error("Wrong answer!")

    with c2:

        if st.button("Use Hint", key="hint_logic"):

            show_hints(st.session_state.logic["hints"])

    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================================
# WIN SCREEN
# ==========================================================

if st.session_state.won:

    rain(
        emoji="🎉",
        font_size=40,
        falling_speed=5,
        animation_length="infinite"
    )

   
    st.success("🎉 Congratulations! You Escaped the AI Escape Room!")

    st.markdown(f"## 🏆 Final Score: {st.session_state.score}")

    st.subheader("Leaderboard")

    leaderboard = pd.read_csv(LEADERBOARD)

    leaderboard.loc[len(leaderboard)] = [
    st.session_state.name,
    st.session_state.score,
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
]

    leaderboard = leaderboard.sort_values(
    by="Score",
    ascending=False
)

    leaderboard.to_csv(
    LEADERBOARD,
    index=False
)

    st.dataframe(
        leaderboard,
        use_container_width=True,
        hide_index=True
    )

    if st.button("🔄 Play Again"):
        
        st.session_state.score = 0
        st.session_state.lives = 5
        st.session_state.hint_tokens = 3
        st.session_state.hint_level = 0
        st.session_state.stage = 0
        st.session_state.won = False
        st.session_state.game_over = False
        st.session_state.start_time = time.time()

        st.session_state.riddle = random_riddle()
        st.session_state.math = random_math()
        st.session_state.caesar = random_caesar()
        st.session_state.emoji = random_emoji()
        st.session_state.logic = random_logic()

        st.rerun()

