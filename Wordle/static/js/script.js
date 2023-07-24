function keyboard(){
    data = event.key.toUpperCase();
    /*var Regex="^[A-Za-z]\S*$";
    if(data.length == 1){
        $.post('/', {'data': data});
    }*/

    $.ajax({
        url: '/',
        type: "POST",
        dataType: "json",
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(){
          alert('success');
        },
        error: function(){
          alert('failure');
        }
      });
}

function addLetter(letter){
    //$.post('/', {'data': letter});

    $.ajax({
        url: '/',
        type: "POST",
        dataType: "json",
        contentType: 'application/json',
        data: JSON.stringify(letter),
        success: function(response){
          alert('success');
          data = response
        },
        error: function(){
          alert('failure');
        }
      });
}

