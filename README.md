# Text Editor with OpenAI Integration

This is a text editor application that uses OpenAI to generate novel length documents. 

## Features

- Text editing capabilities
- Generate novel length documents using OpenAI
- Save and load documents

## Installation

1. Clone this repository.
2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

Run the main script to start the application:

```
python src/main.py
```

## Testing

To run the tests, use the following command:

```
python -m unittest discover tests
```

## Files

- `src/main.py`: The main script that runs the application.
- `src/editor_window.py`: Contains the EditorWindow class for UI interactions.
- `src/document.py`: Contains the Document class for storing and manipulating text data.
- `src/text_processing.py`: Contains functions for text processing.
- `src/openai_integration.py`: Contains the OpenAIIntegration class for interacting with the OpenAI API.
- `src/utils.py`: Contains utility functions.
- `resources/ui/editor_window.ui`: The UI layout for the editor window.
- `resources/styles/styles.css`: The CSS styles for the UI.
- `tests/test_document.py`: Tests for the Document class.
- `tests/test_text_processing.py`: Tests for the text processing functions.
- `tests/test_openai_integration.py`: Tests for the OpenAIIntegration class.
- `tests/test_utils.py`: Tests for the utility functions.
- `requirements.txt`: Contains the required dependencies.
