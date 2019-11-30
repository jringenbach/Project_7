function add_new_message(papy_is_talking, text_message){
    //We get the chat-box-container that contains all the messages of the chat
    chat_box_container = document.getElementById('chat-box-container');

    //We add a new message into the chat box
    chat_box = document.createElement('div');
    new_message = document.createElement('div');

    // We set a different style depending if the message comes from papy or the user
    if (papy_is_talking){
        new_message.className = "col-5 align-self-end grandpy-message";
        chat_box.className = "row justify-content-end chat-box-line";
    }else{
        new_message.className = "col-5 align-self-start order-first user-message";
        chat_box.className = "row justify-content-start chat_box_line";
    }     
    
    //We create a new text_zone with the content of the message
    new_text_node = document.createTextNode(text_message);
    new_text_node.className = "message";

    //We add everything to the DOM
    new_message.appendChild(new_text_node);
    chat_box.appendChild(new_message);
    chat_box_container.appendChild(chat_box);
}

//We get the form
let form = document.getElementById("question-form");

form.addEventListener("submit", function(e){
    e.preventDefault();
    let message = document.getElementById("question-input");
    let message_text = message.value;
    add_new_message(false, message_text);
    console.log(message_text)

    ajaxPost("/grandpytalk", {text : message_text},
        function (reponse) {
            // Affichage dans la console en cas de succès
            console.log(JSON.parse(reponse));
            data = JSON.parse(reponse);
            add_new_message(true, data["content"]["extract"]);

        }, true
    );

});



