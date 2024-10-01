// script.js
function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        appendMessage("You: " + userInput);
        processUserInput(userInput);
        document.getElementById("user-input").value = "";
    }
}

function appendMessage(message) {
    var chatBox = document.getElementById("chat-box");
    var messageElement = document.createElement("div");
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function processUserInput(userInput) {
    // Send user input to server for processing
    fetch('/process_input', {
        method: 'POST',
        body: JSON.stringify({ message: userInput }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("Bot: " + data.response);
        // If the response requires storing customer details, prompt user
        if (data.store_details) {
            var name = prompt("Please enter your name:");
            var phoneNumber = prompt("Please enter your phone number:");
            // Send customer details to server for storage
            fetch('/store_details', {
                method: 'POST',
                body: JSON.stringify({ name: name, phoneNumber: phoneNumber }),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        }
    });
}