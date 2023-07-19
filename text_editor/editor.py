```python
from text_editor.document import Document

class Editor:
    def __init__(self, document):
        if isinstance(document, Document):
            self.document = document
        else:
            raise TypeError("Expected instance of Document")

    def edit_text(self, position, new_text):
        if not isinstance(position, int) or position < 0 or position > len(self.document.text):
            raise ValueError("Invalid position")
        if not isinstance(new_text, str):
            raise TypeError("New text must be a string")

        self.document.text = self.document.text[:position] + new_text + self.document.text[position + len(new_text):]

    def add_text(self, new_text):
        if not isinstance(new_text, str):
            raise TypeError("New text must be a string")

        self.document.text += new_text

    def remove_text(self, start_position, end_position):
        if not isinstance(start_position, int) or start_position < 0 or start_position > len(self.document.text):
            raise ValueError("Invalid start position")
        if not isinstance(end_position, int) or end_position < 0 or end_position > len(self.document.text):
            raise ValueError("Invalid end position")

        self.document.text = self.document.text[:start_position] + self.document.text[end_position:]
```