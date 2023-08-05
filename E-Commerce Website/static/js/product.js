const productImages = document.querySelectorAll(".product-images img"); // selecting all image thumbs
const productImageSlide = document.querySelector(".image-slider"); // seclecting image slider element

let activeImageSlide = 0; // default slider image

productImages.forEach((item, i) => { // loopinh through each image thumb
    item.addEventListener('click', () => { // adding click event to each image thumbnail
        productImages[activeImageSlide].classList.remove('active'); // removing active class from current image thumb
        item.classList.add('active'); // adding active class to the current or clicked image thumb
        productImageSlide.style.backgroundImage = `url('${item.src}')`; // setting up image slider's background image
        activeImageSlide = i; // updating the image slider variable to track current thumb
    })
})

const sizeBtns = document.querySelectorAll('.size-radio-btn'); // selecting size buttons
let checkedBtn = 0; // current selected button

sizeBtns.forEach((item, i) => { // looping through each button
    item.addEventListener('click', () => { // adding click event to each 
        sizeBtns[checkedBtn].classList.remove('check'); // removing check class from the current button
        item.classList.add('check'); // adding check class to clicked button
        checkedBtn = i; // upading the variable
    })
})

const colorBtns = document.querySelectorAll('.color-radio-btn'); // selecting size buttons
checkedBtn = 0; // current selected button

colorBtns.forEach((item, i) => { // looping through each button
    item.addEventListener('click', () => { // adding click event to each 
        colorBtns[checkedBtn].classList.remove('check'); // removing check class from the current button
        item.classList.add('check'); // adding check class to clicked button
        checkedBtn = i; // upading the variable
    })
})


function addToCart(){
    var color = $("form[id='color']").find(":radio:checked").val();
    var size = $("form[id='size']").find(":radio:checked").val();
    var id = document.getElementById('Id').innerHTML;
    var brand = document.getElementById('brand').innerHTML;
    var des = document.getElementById('des').innerHTML;
    var price = document.getElementById('price').innerHTML;
    var name = document.getElementById('name').innerHTML;
    data = {
        'color': color,
        'size': size,
        'id': id,
        'brand': brand,
        'des': des,
        'price': price,
        'name': name
    }
    $.ajax({
        url:'/product/' + id,
        type: 'POST',
        data: data,
        success: function(){
            alert("Added to Cart");
        }
      });
}

function redirect(){
    var color = $("form[id='color']").find(":radio:checked").val();
    var id = document.getElementById('Id').innerHTML;
    document.getElementById("image-slider").style.backgroundImage = "url('/static/img/" + id + "/" + color + "/1.png')";
    document.getElementById('image1').src = "/static/img/" + id + "/" + color + "/1.png";
    document.getElementById('image2').src = "/static/img/" + id + "/" + color + "/2.png";
    document.getElementById('image3').src = "/static/img/" + id + "/" + color + "/3.png";
    document.getElementById('image4').src = "/static/img/" + id + "/" + color + "/4.png";
}