```javascript
// Importing the OpenAI API function
const { callOpenAI } = require('./openai_api.js');

// Document structure schema
const documentStructure = {
  title: '',
  chapters: [],
};

// Function to generate a novel length document
async function generateDocument(prompt, chapterCount) {
  let document = { ...documentStructure, title: prompt };

  for (let i = 0; i < chapterCount; i++) {
    let chapterPrompt = `Chapter ${i+1}: ${prompt}`;
    let chapterContent = await callOpenAI(chapterPrompt);
    document.chapters.push({
      title: `Chapter ${i+1}`,
      content: chapterContent,
    });
  }

  return document;
}

// Exporting the function
module.exports = {
  generateDocument,
};
```