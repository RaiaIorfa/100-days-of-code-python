from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("_" * 100)
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number} 🧐")
print("_" * 100)


# NTS: 1. When to AVOID Nested Loops (Direct Paths)
# If your data has a fixed, known structure (like a row in a database or a defined API response), you have a Direct Path. You do not need to loop through properties you already know the names of.
# Example: A list of users where each user has a "name" and "email". You know the keys exist, so use a single loop and pull them out directly.
# 2. When you MUST Use Nested Loops
# You only need nested loops when you are dealing with multi-dimensional grids, or when you must compare every element in a pool against every other element in that same pool.Grid/Coordinate Data (2D Spaces): Rendering a game board (Chess, Tic-Tac-Toe), processing the pixels of an image (rows and columns), or coordinates ($x, y$).