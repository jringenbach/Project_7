function add_map_to_message(lng, lat, title){
    //We get the chat-box-container that contains all the messages of the chat
    chat_box_container = document.getElementById('chat-box-container');

    //We add a new message into the chat box
    chat_box = document.createElement('div');
    chat_box.className = "row justify-content-end chat-box-line";
    new_message = document.createElement('div');
    new_message.className = "col-5 align-self-end grandpy-message";
    map_div = document.createElement("div");
    map_div.id = "map";
    map_div.className = "align-self-center";

    //We add everything to the DOM
    new_message.appendChild(map_div);
    chat_box.appendChild(new_message);
    chat_box_container.appendChild(chat_box);

    //We create our map
    var map = L.map("map").setView([lat, lng], 13);

    //We set our tileLayers : we get our tiles from OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    //We create the icon of the marker
    var iconMap = L.icon({
        iconUrl: '/../../static/app/img/map-marker.png',
    
        iconSize:     [38, 38], // size of the icon
        iconAnchor:   [lat, lng], // point of the icon which will correspond to marker's location
        popupAnchor:  [-30, 0] // point from which the popup should open relative to the iconAnchor
    });

    //We place our marker on the location on the map
    L.marker([lat, lng], {icon : iconMap}).addTo(map)
    .bindPopup(title)
    .openPopup();



}

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
            add_map_to_message(data["coordinates"]["lng"], data["coordinates"]["lat"], data["content"]["title"]);
            add_new_message(true, data["content"]["extract"]);

        }, true
    );

});


