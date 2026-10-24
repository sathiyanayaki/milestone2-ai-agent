
import re


def get_college_info():
    return {
        "college": "Rajalakshmi Institute of Technology",
        "course": "Artificial Intelligence and Machine Learning"
    }


def calculate(expression):
    allowed_operations = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: (
            a / b if b != 0 else "Cannot divide by zero"
        )
    }

    operation, a, b = expression

    if operation in allowed_operations:
        return allowed_operations[operation](a, b)

    return "Unknown operation"


def answer_question(question):
    question = question.lower().strip()

    # Tool 1: Retrieve college information
    if "college" in question or "course" in question:
        return get_college_info()

    # Tool 2: Perform calculations using numbers in the question
    match = re.search(
        r"\b(add|subtract|multiply|divide)\s+(-?\d+(?:\.\d+)?)\s+(?:and|by)\s+(-?\d+(?:\.\d+)?)",
        question
    )

    if match:
        operation = match.group(1)
        a = float(match.group(2))
        b = float(match.group(3))
        return calculate((operation, a, b))

    # Do not invent answers when information is unavailable
    return "I don't have enough information to answer that question."


if __name__ == "__main__":
    print("Addition:", answer_question("add 20 and 30"))
    print("Subtraction:", answer_question("subtract 20 and 5"))
    print("Multiplication:", answer_question("multiply 4 and 6"))
    print("Division:", answer_question("divide 20 by 4"))

    print("Unknown:", answer_question("Who is the president of Mars?"))

    print("College tool:", get_college_info())
    print("Calculator tool:", calculate(("add", 10, 5)))

    print("College question:", answer_question("Tell me about my college"))

    question = "Tell me about my college"
    answer1 = answer_question(question)
    answer2 = answer_question(question)

    print("First answer:", answer1)
    print("Second answer:", answer2)
    print("Consistency test passed:", answer1 == answer2)
