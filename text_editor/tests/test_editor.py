import unittest
from text_editor.editor import Editor
from text_editor.document import Document

class TestEditor(unittest.TestCase):

    def setUp(self):
        self.document = Document()
        self.editor = Editor(self.document)

    def test_edit_text(self):
        initial_text = "This is a test document."
        self.document.add_text(initial_text)
        self.editor.edit_text(5, "was")
        expected_text = "This was a test document."
        self.assertEqual(self.document.get_text(), expected_text)

if __name__ == "__main__":
    unittest.main()