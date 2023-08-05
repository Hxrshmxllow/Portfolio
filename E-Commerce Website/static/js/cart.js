function lowerQuantity(){
    var quantity = parseInt(document.getElementById('form1').value) - 1;
    var item = document.getElementById('brand').value;
    alert(item);
    if(quantity == 0){
        var item = parseInt(document.getElementById('item').value);
        alert(item)
        data = {
            'item': item
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
    document.getElementById('form1').value = quantity;
}

function addQuantity(){
    var quantity = parseInt(document.getElementById('form1').value) + 1;
    document.getElementById('form1').value = quantity;
}