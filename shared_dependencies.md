1. Exported Variables:
   - `editor_window`: Instance of the EditorWindow class, used across multiple files for UI interactions.
   - `document`: Instance of the Document class, used for storing and manipulating the text data.
   - `openai_api`: Instance of the OpenAIIntegration class, used for interacting with the OpenAI API.

2. Data Schemas:
   - `DocumentSchema`: Schema for the document data, used in `document.py` and `test_document.py`.
   - `OpenAIResponseSchema`: Schema for the response from OpenAI API, used in `openai_integration.py` and `test_openai_integration.py`.

3. DOM Element IDs:
   - `textArea`: The main text area in the editor window.
   - `generateButton`: Button to generate text using OpenAI.
   - `saveButton`: Button to save the current document.
   - `loadButton`: Button to load a document.

4. Message Names:
   - `generateText`: Message sent to trigger text generation using OpenAI.
   - `saveDocument`: Message sent to save the current document.
   - `loadDocument`: Message sent to load a document.

5. Function Names:
   - `generate_text()`: Function to generate text using OpenAI, used in `main.py`, `openai_integration.py`, and `test_openai_integration.py`.
   - `save_document()`: Function to save the current document, used in `main.py`, `document.py`, and `test_document.py`.
   - `load_document()`: Function to load a document, used in `main.py`, `document.py`, and `test_document.py`.
   - `update_text_area()`: Function to update the text area in the editor window, used in `main.py` and `editor_window.py`.

6. Shared Libraries:
   - `PyQt5`: Used for creating the UI, used in `main.py` and `editor_window.py`.
   - `openai`: Used for interacting with the OpenAI API, used in `openai_integration.py` and `test_openai_integration.py`.
   - `unittest`: Used for writing tests, used in all `test_*.py` files.