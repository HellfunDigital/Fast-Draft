```python
import sys
from PyQt5.QtWidgets import QApplication
from editor_window import EditorWindow
from document import Document
from openai_integration import OpenAIIntegration

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.editor_window = EditorWindow()
        self.document = Document()
        self.openai_api = OpenAIIntegration()

        self.editor_window.textArea.textChanged.connect(self.update_text_area)
        self.editor_window.generateButton.clicked.connect(self.generate_text)
        self.editor_window.saveButton.clicked.connect(self.save_document)
        self.editor_window.loadButton.clicked.connect(self.load_document)

    def run(self):
        self.editor_window.show()
        sys.exit(self.app.exec_())

    def update_text_area(self):
        self.editor_window.textArea.setText(self.document.text)

    def generate_text(self):
        generated_text = self.openai_api.generate_text(self.document.text)
        self.document.text += generated_text
        self.update_text_area()

    def save_document(self):
        self.document.save_document()

    def load_document(self):
        self.document.load_document()
        self.update_text_area()

if __name__ == "__main__":
    app = MainApp()
    app.run()
```