import time
from datetime import datetime, timedelta #class for manipulating dates and times
from simple_spaced_repetition import Card

# Define time intervals in seconds for each difficulty level
INTERVAL_AGAIN = 10  # seconds
INTERVAL_HARD = 30   # seconds
INTERVAL_GOOD = 60   # seconds
INTERVAL_EASY = 120  # seconds

# Define a list of questions (flashcards)
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the boiling point of water?", "answer": "100°C"},
]

# Create a dictionary to hold the cards and their next due time
# Initialize each card with a short interval for testing purposes
cards = {
    i: {"card": Card(), "next_due": datetime.now() + timedelta(seconds=5)} 
    for i in range(len(flashcards))
}

def ask_question(index):
    flashcard = flashcards[index]
    print(f"Question: {flashcard['question']}")
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == flashcard['answer'].strip().lower():
        print("Correct!")
        interval_seconds = INTERVAL_EASY  # Correct answer
    else:
        print(f"Incorrect! The correct answer is {flashcard['answer']}")
        interval_seconds = INTERVAL_AGAIN  # Incorrect answer

    # Update the card based on user's performance
    cards[index]["next_due"] = datetime.now() + timedelta(seconds=interval_seconds)

def run_quiz():
    while True:
        now = datetime.now()
        due_cards = [index for index, data in cards.items() if data["next_due"] <= now]

        if due_cards:
            for index in due_cards:
                ask_question(index)
        else:
            print("No cards due for review now.")
            time.sleep(10)  # Wait for 10 seconds before checking again

if __name__ == "__main__":
    run_quiz()
