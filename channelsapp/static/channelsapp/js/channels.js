const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

// onmessage - An event listener to be called when a message is received from the server.
chatSocket.onmessage = function(e) {
    // JSON.parse() converts the JSON object back into the original object,
    // then examine and act upon its contents.
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').innerText += data.author + " " + new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
    document.querySelector('#chat-log').innerHTML += '<br>';
    document.querySelector('#chat-log').innerText += data.message;
};

// onclose - An event listener to be called when the connection is closed.
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    if (message === '') return;

    // Send the msg object as a JSON-formatted string.
    chatSocket.send(JSON.stringify({
        'message': message,
        'author': $("#username").text(),
    }));

    // Blank the text input element, ready to receive the next line of text from the user.
    messageInputDom.value = '';
};