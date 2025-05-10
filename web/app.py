import streamlit as st          # Streamlit library for building web apps
import random                   # Used for generating computer's random choice

# Display a title at the top of the Streamlit app
st.title("🪨📄✂️ Rock, Paper, Scissors")

# Define the available move options
choices = ["Rock", "Paper", "Scissors"]

# Create a radio button for the player to select their move
# Convert the selected choice to lowercase for logic consistency
player_choice = st.radio("Choose your move:", choices).lower()

# This block runs only when the "Play" button is clicked
if st.button("Play"):
    # Randomly select a move for the computer, and normalize it to lowercase
    computer_choice = random.choice(choices).lower()

    # Display both the player's and computer's choices
    st.write(f"**You chose:** {player_choice}")
    st.write(f"**Computer chose:** {computer_choice}")

    # Determine the outcome of the game
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "🎉 You win!"
    else:
        result = "💻 Computer wins!"

    # Display the result prominently
    st.subheader(result)
