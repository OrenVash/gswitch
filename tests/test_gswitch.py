import io
import sys
import unittest
from unittest.mock import patch
import importlib.machinery
import os

def load_gswitch():
    """Dynamically load the gswitch script as a module."""
    # Find the path to the gswitch script relative to this test file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gswitch_path = os.path.join(base_dir, "gswitch")

    loader = importlib.machinery.SourceFileLoader("gswitch", gswitch_path)
    return loader.load_module()

gswitch = load_gswitch()

class TestGSwitch(unittest.TestCase):
    def test_ask_input_happy_path(self):
        prompt = "Enter something: "
        user_input = "  hello world  \n"
        expected_output = "hello world"

        with patch("sys.stdin", io.StringIO(user_input)):
            with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                result = gswitch.ask_input(prompt)

                self.assertEqual(result, expected_output)
                self.assertEqual(mock_stdout.getvalue(), prompt)

    def test_ask_input_empty(self):
        prompt = "> "
        user_input = "\n"
        expected_output = ""

        with patch("sys.stdin", io.StringIO(user_input)):
            with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                result = gswitch.ask_input(prompt)

                self.assertEqual(result, expected_output)
                self.assertEqual(mock_stdout.getvalue(), prompt)

    def test_ask_input_whitespace_only(self):
        prompt = "Input: "
        user_input = "   \n"
        expected_output = ""

        with patch("sys.stdin", io.StringIO(user_input)):
            with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                result = gswitch.ask_input(prompt)

                self.assertEqual(result, expected_output)
                self.assertEqual(mock_stdout.getvalue(), prompt)

if __name__ == "__main__":
    unittest.main()
