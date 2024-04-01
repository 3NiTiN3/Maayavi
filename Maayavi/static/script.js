function sendMessage() {
    var messageInput = document.getElementById('messageInput');
    var trainingModeCheckbox = document.getElementById('trainingMode');
    var message = messageInput.value.trim();
    if (message === "") return; // Don't send empty messages

    var chatbox = document.getElementById('chatbox');
    var userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.textContent = `You: ${message}`;
    chatbox.appendChild(userMessage);

    if (trainingModeCheckbox.checked) {
        var answer = prompt('Please enter the answer for training:');
        if (answer) {
            fetch('/train', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'question': message,
                    'answer': answer
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Training data saved:', data);
            })
            .catch(error => console.error('Error:', error));
        }
    } else {
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({ 'message': message })
        })
        .then(response => response.json())
        .then(data => {
            var maayaviMessage = document.createElement('div');
            maayaviMessage.className = 'message maayavi-message';
            maayaviMessage.textContent = `Maayavi: ${data.reply}`;
            chatbox.appendChild(maayaviMessage);
            chatbox.scrollTop = chatbox.scrollHeight; // Scroll to latest message
        })
        .catch(error => console.error('Error:', error));
    }

    // Clear the input after sending
    messageInput.value = '';
    updateSendButton(); // Update send button color
    messageInput.focus(); // Set focus back to the input for the next message
}

function updateSendButton() {
    var messageInput = document.getElementById('messageInput');
    var sendButton = document.querySelector('.chat-submit');
    var hasText = messageInput.value.trim().length > 0;

    sendButton.classList.toggle('has-text', hasText);
    var paths = sendButton.querySelectorAll('path');
    paths.forEach(path => {
        path.setAttribute('fill', hasText ? '#6bee49' : 'white');
    });
}

document.addEventListener('DOMContentLoaded', function() {
    var messageForm = document.getElementById('messageForm');
    var messageInput = document.getElementById('messageInput');
    var trainingModeCheckbox = document.getElementById('trainingMode');

    messageInput.addEventListener('input', updateSendButton);

    messageForm.addEventListener('submit', function(event) {
        event.preventDefault();
        sendMessage();
    });

    // Initialize send button color on load
    updateSendButton();
});
