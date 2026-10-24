import unittest
from agent import get_college_info, calculate, answer_question


class TestAgent(unittest.TestCase):

    def test_college_tool(self):
        result = get_college_info()
        self.assertIn("college", result)

    def test_calculator_tool(self):
        self.assertEqual(calculate(("add", 10, 5)), 15)

    def test_unknown_question(self):
        result = answer_question("Who is the president of Mars?")
        self.assertIn("don't have enough information", result)

    def test_consistency(self):
        question = "Tell me about my college"
        self.assertEqual(
            answer_question(question),
            answer_question(question)
        )


if __name__ == "__main__":
    unittest.main()