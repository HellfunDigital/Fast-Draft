```javascript
import { callOpenAI } from './openai_api.js';
import { generateDocument } from './document_generator.js';

window.onload = init;

function init() {
    const generateButton = document.getElementById('generateButton');
    generateButton.addEventListener('click', generateText);
}

function generateText() {
    const textEditor = document.getElementById('textEditor');
    const inputText = textEditor.value;

    const apiRequest = {
        text: inputText
    };

    callOpenAI(apiRequest)
        .then(apiResponse => {
            const documentStructure = generateDocument(apiResponse);
            displayOutput(documentStructure);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while generating the document.');
        });
}

function displayOutput(documentStructure) {
    const outputDisplay = document.getElementById('outputDisplay');
    outputDisplay.textContent = documentStructure.text;
}
```