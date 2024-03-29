import time

# Quiz questions and answers
questions = [
    {
        "question": "What is the output of the following code?\n\nx = 5\ny = 2\nprint(x // y)",
        "options": ["A. 2.5", "B. 2", "C. 2.0", "D. Error"],
        "correct_answer": "B"
    },
    {
        "question": "What will be the value of x after executing this code?\n\nx = 10\nx += 5\nx *= 2",
        "options": ["A. 30", "B. 25", "C. 35", "D. 20"],
        "correct_answer": "A"
    },
    {
        "question": "What is the output of the following code?\n\nx = [1, 2, 3]\nprint(x[3])",
        "options": ["A. 1", "B. 2", "C. 3", "D. IndexError"],
        "correct_answer": "D"
    },
    {
        "question": "What will be the output of the following code?\n\nx = ['apple', 'banana', 'cherry']\nprint(len(x))",
        "options": ["A. 3", "B. 6", "C. 5", "D. 4"],
        "correct_answer": "A"
    },
    {
        "question": "What is the correct way to create a function in Python?",
        "options": ["A. function myFunction()", "B. def myFunction():", "C. create myFunction()",
                    "D. function = myFunction()"],
        "correct_answer": "B"
    },
    {
        "question": "Which of the following is a correct comment in Python?",
        "options": ["A. /*This is a comment*/", "B. //This is a comment", "C. #This is a comment",
                    "D. <!--This is a comment-->"],
        "correct_answer": "C"
    },
    {
        "question": "What is the output of the following code?\n\nx = True\ny = False\nz = x and y\nprint(z)",
        "options": ["A. True", "B. False", "C. 1", "D. 0"],
        "correct_answer": "B"
    },
    {
        "question": "What is the correct way to open a file named 'data.txt' in read mode?",
        "options": ["A. file = open('data.txt', 'read')", "B. file = open('data.txt')",
                    "C. file = open('data.txt', 'r')", "D. file = open('data.txt', 'readmode')"],
        "correct_answer": "C"
    },
    {
        "question": "What is the output of the following code?\n\nx = 'hello'\nprint(x.upper())",
        "options": ["A. hello", "B. HELLO", "C. Hello", "D. Error"],
        "correct_answer": "B"
    },
    {
        "question": "What is the correct way to check if 'apple' is present in a list named fruits?",
        "options": ["A. if 'apple' in fruits:", "B. if 'apple' exists in fruits:", "C. if fruits contains 'apple':",
                    "D. if 'apple' is in fruits:"],
        "correct_answer": "D"
    },
    {
        "question": "What is the output of the following code?\n\nx = 5\ny = 2\nprint(x // y)",
        "options": ["A. 2.5", "B. 2", "C. 2.0", "D. Error"],
        "correct_answer": "B"
    },
    {
        "question": "What will be the value of x after executing this code?\n\nx = 10\nx += 5\nx *= 2",
        "options": ["A. 30", "B. 25", "C. 35", "D. 20"],
        "correct_answer": "A"
    },
    {
        "question": "What is the output of the following code?\n\nx = [1, 2, 3]\nprint(x[3])",
        "options": ["A. 1", "B. 2", "C. 3", "D. IndexError"],
        "correct_answer": "D"
    },
    {
        "question": "What will be the output of the following code?\n\nx = ['apple', 'banana', 'cherry']\nprint(len(x))",
        "options": ["A. 3", "B. 6", "C. 5", "D. 4"],
        "correct_answer": "A"
    },
    {
        "question": "What is the correct way to create a function in Python?",
        "options": ["A. function myFunction()", "B. def myFunction():", "C. create myFunction()", "D. function = myFunction()"],
        "correct_answer": "B"
    },
    {
        "question": "Which of the following is a correct comment in Python?",
        "options": ["A. /*This is a comment*/", "B. //This is a comment", "C. #This is a comment", "D. <!--This is a comment-->"],
        "correct_answer": "C"
    },
    {
        "question": "What is the output of the following code?\n\nx = True\ny = False\nz = x and y\nprint(z)",
        "options": ["A. True", "B. False", "C. 1", "D. 0"],
        "correct_answer": "B"
    },
    {
        "question": "What is the correct way to open a file named 'data.txt' in read mode?",
        "options": ["A. file = open('data.txt', 'read')", "B. file = open('data.txt')", "C. file = open('data.txt', 'r')", "D. file = open('data.txt', 'readmode')"],
        "correct_answer": "C"
    },
    {
        "question": "What is the output of the following code?\n\nx = 'hello'\nprint(x.upper())",
        "options": ["A. hello", "B. HELLO", "C. Hello", "D. Error"],
        "correct_answer": "B"
    },
    {
        "question": "What is the correct way to check if 'apple' is present in a list named fruits?",
        "options": ["A. if 'apple' in fruits:", "B. if 'apple' exists in fruits:", "C. if fruits contains 'apple':", "D. if 'apple' is in fruits:"],
        "correct_answer": "D"
    }
]

# Timer for the quiz (30 Seconds per question)
quiz_time = 1/2 * 60 * len(questions)


# Quiz function
def take_quiz():
    print("Welcome to the Python Coding Quiz!")
    time.sleep(1)
    print(f"You have {quiz_time // 60} minutes to answer {len(questions)} questions.")
    time.sleep(1)
    print("Let's begin!\n")
    correct_answers = 0
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        for option in question['options']:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question['correct_answer']:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {question['correct_answer']}\n")
        time.sleep(1)

    print("Quiz completed!")
    print(f"You got {correct_answers} out of {len(questions)} questions correct.")


# Run the quiz
if __name__ == "__main__":
    take_quiz()
