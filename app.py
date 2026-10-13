import random
import streamlit as st

st.set_page_config(page_title="Python Mini Games", page_icon="🎮", layout="centered")
st.title("🎮 Python Mini Games")
st.write("Choose a game below and play it in your browser!")

game = st.sidebar.selectbox("Choose a game", ["Snake, Water, Gun", "Number Guessing"])

if game == "Snake, Water, Gun":
    st.header("🐍 Snake, Water, Gun")
    choice_labels = {"Snake": 1, "Water": -1, "Gun": 0}
    computer_labels = {1: "Snake", -1: "Water", 0: "Gun"}
    user_choice = st.radio("Your choice:", ["Snake", "Water", "Gun"], horizontal=True)

    if st.button("Play round", type="primary"):
        you = choice_labels[user_choice]
        computer = random.choice([-1, 0, 1])
        st.write(f"**You chose:** {user_choice}")
        st.write(f"**Computer chose:** {computer_labels[computer]}")
        if you == computer:
            st.info("It's a draw!")
        elif (you == 1 and computer == -1) or (you == 0 and computer == 1) or (you == -1 and computer == 0):
            st.success("You win! 🎉")
        else:
            st.error("You lose. Try again!")

else:
    st.header("🔢 Number Guessing Game")
    st.write("I picked a number from 1 to 100. Can you guess it?")
    if "target_number" not in st.session_state:
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.guesses = 0
        st.session_state.game_won = False

    guess = st.number_input("Enter your guess", min_value=1, max_value=100, value=50, step=1, disabled=st.session_state.game_won)
    if st.button("Check guess", type="primary", disabled=st.session_state.game_won):
        st.session_state.guesses += 1
        target = st.session_state.target_number
        if guess == target:
            st.session_state.game_won = True
            st.success(f"Correct! 🎉 You guessed {target} in {st.session_state.guesses} attempt(s).")
        elif guess > target:
            st.warning("Lower number, please!")
        else:
            st.warning("Higher number, please!")

    if st.session_state.game_won:
        if st.button("Play again"):
            st.session_state.target_number = random.randint(1, 100)
            st.session_state.guesses = 0
            st.session_state.game_won = False
            st.rerun()
    else:
        st.caption(f"Attempts: {st.session_state.guesses}")
