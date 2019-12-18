let NUM_MAP = 0;

function add_map_to_message(lng, lat, title){
    //We get the chat-box-container that contains all the messages of the chat
    chat_box = document.getElementById('chat-box');

    //We add a new message into the chat box
    chat_message = document.createElement('section');
    chat_box.className = "message";
    new_message = document.createElement('section');
    new_message.className = "message grandpy-message";
    map_div = document.createElement("div");
    NUM_MAP += 1
    map_div.className = "map";
    map_div.id = "map"+String(NUM_MAP);
    console.log(map_div.id)

    //We add everything to the DOM
    new_message.appendChild(map_div);
    chat_box.appendChild(new_message);

    //We create our map
    var map = L.map("map"+String(NUM_MAP)).setView([lat, lng], 13);

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
    chat_box = document.getElementById('chat-box');

    new_message = document.createElement('section');

    // We set a different style depending if the message comes from papy or the user
    if (papy_is_talking){
        new_message.className = "message grandpy-message";
    }else{
        new_message.className = "message user-message";
    }     
    
    //We create a new text_zone with the content of the message
    new_text_node = document.createTextNode(text_message);
    new_text_node.className = "message";

    //We add everything to the DOM
    new_message.appendChild(new_text_node);
    chat_box.appendChild(new_message);
    new_message.scrollIntoView();
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

            //If there was an error while getting the information on google maps or wikipedia
            if ("error_message" in data){
                add_new_message(true, data["error_message"]);
            }

            else{
                //We add the map and the test in two seperate messages
                add_map_to_message(data["coordinates"]["lng"], data["coordinates"]["lat"], data["content"]["title"]);
                add_new_message(true, data["content"]["extract"]);
            }

            message.value = "";

        }, true
    );

});


