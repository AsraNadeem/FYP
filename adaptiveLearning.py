def ask_question(question, expected_answer):
    user_answer = input(question + "\nYour answer: ").strip().lower()
    return user_answer == expected_answer

def determine_learning_level(quiz_scores):
    if quiz_scores['beginner'] >= 1:
        return 'Beginner'
    else:
        return 'Advanced'

def main():
    quiz_questions = {
        'beginner': [
            {"question": "What is the opposite of 'hot'?", "answer": "cold"},
            {"question": "What is the past tense of 'go'?", "answer": "went"}
        ],
        'advanced': [
            {"question": "What is the plural of 'child'?", "answer": "children"},
            {"question": "What is the present perfect tense of 'eat'?", "answer": "eaten"}
        ]
    }

    quiz_scores = {'beginner': 0}

    print("Welcome to the English Language Quiz!")
    print("You will be asked a series of questions to determine your learning level.")

    # Beginner level questions
    for question_data in quiz_questions['beginner']:
        if ask_question(question_data['question'], question_data['answer']):
            quiz_scores['beginner'] += 1

    # Determine learning path
    learning_path = determine_learning_level(quiz_scores)
    print(f"Your learning path is: {learning_path}")

    # Reset beginner score if learning path is advanced
    if learning_path == 'Advanced':
        quiz_scores['beginner'] = 0

    # Advanced level questions if applicable
    if learning_path == 'Advanced':
        print("Welcome to the advanced level questions!")
        for question_data in quiz_questions['advanced']:
            if ask_question(question_data['question'], question_data['answer']):
                quiz_scores['advanced'] = 1  # Set to 1 if answered correctly

    print("Quiz complete!")

if __name__ == "__main__":
    main()
