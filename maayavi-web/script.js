function sendInput() {
    let userInput = document.getElementById('user-input').value; 

    fetch('/process_input', {
        method: 'POST',
        body: JSON.stringify({ userInput: userInput }) // Send data as JSON
    })
    .then(response => response.text())
    .then(responseText => {
        document.getElementById('ai-response').textContent = responseText;
    });
}
