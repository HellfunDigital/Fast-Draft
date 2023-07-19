const axios = require('axios');

const apiRequest = {
  engine: 'text-davinci-002',
  prompt: '',
  max_tokens: 1000,
};

async function callOpenAI(prompt) {
  apiRequest.prompt = prompt;

  try {
    const response = await axios.post('https://api.openai.com/v1/engines/davinci-codex/completions', apiRequest, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
      }
    });

    return response.data.choices[0].text.trim();
  } catch (error) {
    console.error(`Error calling OpenAI API: ${error}`);
    throw error;
  }
}

module.exports = {
  callOpenAI
};