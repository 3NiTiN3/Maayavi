function sendQuestion() {
    const userInput = document.getElementById('user_input').value;
    
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const maayaviResponseDiv = document.getElementById('maayavi_response');
        maayaviResponseDiv.innerHTML = data.answer;
    })
    .catch(error => console.error('Error:', error));
}
