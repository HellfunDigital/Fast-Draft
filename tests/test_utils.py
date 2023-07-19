```python
import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def test_generate_text(self):
        text = "The quick brown fox"
        result = utils.generate_text(text)
        self.assertIsInstance(result, str)

    def test_save_document(self):
        document = "The quick brown fox jumps over the lazy dog."
        filename = "test.txt"
        utils.save_document(document, filename)
        with open(filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, document)

    def test_load_document(self):
        filename = "test.txt"
        content = utils.load_document(filename)
        with open(filename, 'r') as f:
            expected_content = f.read()
        self.assertEqual(content, expected_content)

    def test_update_text_area(self):
        text = "The quick brown fox jumps over the lazy dog."
        utils.update_text_area(text)
        self.assertEqual(utils.editor_window.textArea.toPlainText(), text)

if __name__ == '__main__':
    unittest.main()
```