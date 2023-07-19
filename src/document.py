```python
import os
import json
from typing import Optional

class DocumentSchema:
    def __init__(self, text: str):
        self.text = text

class Document:
    def __init__(self, filepath: Optional[str] = None):
        self.filepath = filepath
        self.data = DocumentSchema(text="")

    def load(self, filepath: Optional[str] = None):
        if filepath:
            self.filepath = filepath
        if self.filepath and os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                self.data = DocumentSchema(text=f.read())
        else:
            self.data = DocumentSchema(text="")

    def save(self, filepath: Optional[str] = None):
        if filepath:
            self.filepath = filepath
        if self.filepath:
            with open(self.filepath, 'w') as f:
                f.write(self.data.text)

    def update_text(self, text: str):
        self.data.text = text

    def get_text(self) -> str:
        return self.data.text
```