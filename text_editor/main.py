```python
from text_editor.editor import Editor
from text_editor.openai_interface import OpenAIInterface
from text_editor.document import Document

def main():
    document = Document()
    editor = Editor(document)
    openai_interface = OpenAIInterface(document)

    while True:
        user_input = input("Enter command: ")
        if user_input == "quit":
            break
        elif user_input == "edit":
            text = input("Enter text to edit: ")
            editor.edit_text(text)
        elif user_input == "generate":
            openai_interface.generate_text()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
```