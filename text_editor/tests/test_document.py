import unittest
from text_editor.document import Document

class TestDocument(unittest.TestCase):

    def setUp(self):
        self.document = Document()

    def test_add_text(self):
        self.document.add_text("Hello, world!")
        self.assertEqual(self.document.text, "Hello, world!")

    def test_remove_text(self):
        self.document.add_text("Hello, world!")
        self.document.remove_text(0, 5)
        self.assertEqual(self.document.text, ", world!")

if __name__ == '__main__':
    unittest.main()