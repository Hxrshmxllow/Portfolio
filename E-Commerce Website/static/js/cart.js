function lowerQuantity(value){
    var quantity = parseInt(document.getElementById('form' + value).value) - 1;
    document.getElementById('form' + value).value = quantity;
    if(quantity == 0){
        data = {
            'item': value
        }
        $.ajax({
            url:'/cart',
            type: 'POST',
            data: data,
            success: function(){
                alert("Removed from Cart");
            }
          });
    }
    else{
        data = {
            'item': value,
            'quantity': quantity
        }
        $.ajax({
            url:'/cart',
            type: 'POST',
            data: data,
            success: function(){
                alert("Updated");
            }
          })
    }
}

function addQuantity(value){
    var quantity = parseInt(document.getElementById('form'+value).value) + 1;
    document.getElementById('form'+value).value = quantity;
    data = {
        'item': value,
        'quantity': quantity
    }
    $.ajax({
        url:'/cart',
        type: 'POST',
        data: data,
        success: function(){
            alert("Updated");
        }
      });
}