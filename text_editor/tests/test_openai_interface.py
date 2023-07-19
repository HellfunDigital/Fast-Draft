import unittest
from text_editor.openai_interface import OpenAIInterface
from text_editor.document import Document

class TestOpenAIInterface(unittest.TestCase):
    def setUp(self):
        self.document = Document()
        self.openai_interface = OpenAIInterface(self.document)

    def test_generate_text(self):
        initial_text = "Once upon a time"
        self.document.add_text(initial_text)
        self.openai_interface.generate_text()
        self.assertNotEqual(self.document.get_text(), initial_text, "Text generation failed")

if __name__ == "__main__":
    unittest.main()