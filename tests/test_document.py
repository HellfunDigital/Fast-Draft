```python
import unittest
from src.document import Document, DocumentSchema

class TestDocument(unittest.TestCase):

    def setUp(self):
        self.document = Document()
        self.document_schema = DocumentSchema()

    def test_save_document(self):
        test_text = "This is a test document."
        self.document.text = test_text
        self.document.save_document("test_document.txt")
        with open("test_document.txt", "r") as file:
            saved_text = file.read()
        self.assertEqual(saved_text, test_text)

    def test_load_document(self):
        test_text = "This is a test document."
        with open("test_document.txt", "w") as file:
            file.write(test_text)
        self.document.load_document("test_document.txt")
        self.assertEqual(self.document.text, test_text)

    def test_document_schema(self):
        test_text = "This is a test document."
        self.document.text = test_text
        serialized = self.document_schema.dump(self.document)
        self.assertEqual(serialized, {"text": test_text})
        deserialized = self.document_schema.load(serialized)
        self.assertEqual(deserialized.text, test_text)

if __name__ == "__main__":
    unittest.main()
```