```python
import unittest
from unittest.mock import patch
from src.openai_integration import OpenAIIntegration, OpenAIResponseSchema

class TestOpenAIIntegration(unittest.TestCase):

    def setUp(self):
        self.openai_api = OpenAIIntegration()

    @patch('src.openai_integration.openai')
    def test_generate_text(self, mock_openai):
        mock_openai.Completion.create.return_value = {
            'choices': [{'text': 'Test text'}]
        }

        response = self.openai_api.generate_text('Test prompt')
        self.assertEqual(response, 'Test text')

    def test_openai_response_schema(self):
        schema = OpenAIResponseSchema()
        data = {
            'choices': [{'text': 'Test text'}]
        }
        result = schema.load(data)
        self.assertEqual(result, {'text': 'Test text'})

if __name__ == '__main__':
    unittest.main()
```