from play_game import determine_winner
# Test cases for the determine_winner function

def test_determine_winner():
    assert determine_winner("rock", "scissors") == "player"
    assert determine_winner("rock", "paper") == "computer"
    assert determine_winner("scissors", "scissors") == "tie"
    assert determine_winner("paper", "rock") == "player"
    assert determine_winner("scissors", "paper") == "player"
    assert determine_winner("paper", "scissors") == "computer"
    print("All tests passed!")

test_determine_winner()