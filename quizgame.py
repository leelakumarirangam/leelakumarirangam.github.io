import json
import os

# File to store high scores
SCORE_FILE = "high_scores.json"

# Load high scores
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    else:
        return []

# Save high scores
def save_score(name, score):
    scores = load_scores()
    scores.append({"name": name, "score": score})
    scores.sort(key=lambda x: x["score"], reverse=True)  # Sort by score
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=4)

# List of questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    }
]

# Start the quiz
def start_quiz():
    name = input("Enter your name: ")
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        ans = input("Enter your answer (A/B/C/D): ").upper()
        if ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}")
    print(f"\n{name}, your total score: {score}/{len(questions)}")
    save_score(name, score)
    print_high_scores()

# Show high scores
def print_high_scores():
    print("\n=== High Scores ===")
    scores = load_scores()
    for i, entry in enumerate(scores[:5], start=1):  # top 5
        print(f"{i}. {entry['name']} - {entry['score']}")

# Main menu
def main():
    while True:
        print("\n===== Quiz Game =====")
        print("1. Start Quiz")
        print("2. View High Scores")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            start_quiz()
        elif choice == "2":
            print_high_scores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
