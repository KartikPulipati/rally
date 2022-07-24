const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws' + (window.location.protocol === "https" ? "w" : "") + '://'
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
    let a = "<span class=\"author\">" + data.author + "</span> <span class=\"message\">" + data.message + "</span> <span class=\"time\">" +new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) + "</span>";
    $('#chat-log').append("<div class=\"set\">" + a + "<br></div>")
    // autoscroll
    .scrollTop(function() { return this.scrollHeight; });

};
$('#chat-log').scrollTop(function() { return this.scrollHeight; }); // autoscroll

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

$("#start-poll").click(() => {
    $("#poll-form").show();
    $("#start-poll").hide();
});

$(".vote-button").click(function() {
    const poll_id = $(this).attr("data-poll-id");
    const choice_id = $(this).attr("data-choice-id");
    $(".vote-button").filter(function() {
        return $(this).is("[data-poll-id='" + poll_id + "']");
    }).hide();
    const choiceelement = $(".choice-number").filter(function() {
        return $(this).is("[data-choice-id='" + choice_id + "']");
    })
    choiceelement.text(parseInt(choiceelement.text()) + 1);
    $.ajax({
        url: '/channels/poll-vote',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').first().val(),
            poll_id: poll_id,
            choice_id: choice_id,
        },
    });
});