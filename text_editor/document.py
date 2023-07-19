```python
class Document:
    def __init__(self):
        self.text = ""

    def add_text(self, additional_text):
        self.text += additional_text

    def remove_text(self, start_index, end_index):
        if start_index < 0 or end_index > len(self.text):
            raise ValueError("Invalid index range")
        self.text = self.text[:start_index] + self.text[end_index:]

    def get_text(self):
        return self.text
```