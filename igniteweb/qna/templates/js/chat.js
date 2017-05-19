$(document.ready).on('#user_input', 'keypress', function(event){
$(document.ready).onkeypress('#user_input', function(event){
    if(event.which == 13 & $('#user_input').val() != ''){
           appendUserResponseToChatbox();
           ajaxCall();
    }
});

function ajaxCall(){
    var target = $('#user_input');
    var question = target_obj.val().trim();
        $.ajax({
        	url: "demo_test.txt",// URL INPUT
        	type: 'get', // cHECK GET
            data: {"question": question}

            success: function(response){
            // resposnse = {"status": "success", "bot_repsonse": "try if yourself"}
            appendBotResponseToChatbox(response);
        }

        });
    }

function appendBotResponseToChatbox(response){

}


function appendUserResponseToChatbox(){

}


