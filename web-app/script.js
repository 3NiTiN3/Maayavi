$(document).ready(function() {
    $('#send-btn').click(function() {
        var userInput = $('#user-input').val();
        $('#chat-container').append('<p><strong>You:</strong> ' + userInput + '</p>');
        $('#user-input').val('');

        $.ajax({
            type: 'POST',
            url: '/chat',
            data: {user_input: userInput},
            success: function(data) {
                $('#chat-container').append('<p><strong>Maayavi:</strong> ' + data.response + '</p>');
            }
        });
    });
});
