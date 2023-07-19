```python
import openai
from marshmallow import Schema, fields

class OpenAIResponseSchema(Schema):
    id = fields.Str()
    object = fields.Str()
    created = fields.Int()
    model = fields.Str()
    choices = fields.List(fields.Dict())

class OpenAIIntegration:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_text(self, prompt, max_length=500):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_length
        )
        response_schema = OpenAIResponseSchema()
        result = response_schema.load(response)
        return result['choices'][0]['text']['content']
```
