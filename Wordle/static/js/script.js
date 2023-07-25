

function keyboard(){
    var key = event.key;
}

function addLetter(letter){
    $.post('/', {'data': letter});
}