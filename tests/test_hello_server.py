
import unittest

from hello_server import say_hello, search_notes, read_hello_note


class TestNotesSearchMCPServer(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(
            say_hello("Vishnu"),
            "Hello, Vishnu! Welcome to MCP."
        )

    def test_search_notes_finds_matching_text(self):
        result = search_notes("first MCP test")
        self.assertIn("hello.txt", result)
        self.assertIn("Hello! This is my first MCP test file.", result)

    def test_search_notes_empty_query(self):
        self.assertEqual(
            search_notes("   "),
            "Please enter a search query."
        )

    def test_search_notes_no_match(self):
        self.assertEqual(
            search_notes("unique_text_that_does_not_exist_12345"),
            "No matching notes found."
        )

    def test_read_hello_note(self):
        result = read_hello_note()
        self.assertIn(
            "Hello! This is my first MCP test file.",
            result
        )


if __name__ == "__main__":
    unittest.main()
