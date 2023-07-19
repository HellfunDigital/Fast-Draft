```python
import openai
from .document import Document

class OpenAIInterface:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_text(self, document: Document, prompt: str, max_length: int = 1000):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=max_length
            )
            document.add_text(response.choices[0].text.strip())
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        return True
```