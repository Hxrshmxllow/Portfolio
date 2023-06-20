function keyboard(){
    var key = event.key;
}

function addLetter(letter){
    $.post('/addLetter', {'data': letter});
}