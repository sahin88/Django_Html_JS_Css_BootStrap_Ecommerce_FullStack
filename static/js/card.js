
var updtBttns= document.getElementsByClassName('update-card');
for(let i =0; i<updtBttns.length; i++){
    updtBttns[i].addEventListener('click', function(){
        var productId=this.dataset.product;
        var action=this.dataset.action;
       console.log('prodId',productId,'action',action,user)
        if(user=='AnonymousUser'){
            addCookieItem(productId, action);
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function addCookieItem(productId,action){
    console.log('User did not logged in ........',productId, action);

    if (action == 'add'){
        if (cart[productId]==undefined){
            cart[productId]={'quantity':1}
        }
        else{
            cart[productId]['quantity']+=1;
        }
    }
    if (action=='remove'){
        console
        cart[productId]['quantity'] -= 1;
        if(cart[productId]['quantity']<=0){
            delete cart[productId]
        }
    }
    

    document.cookie="cart="+JSON.stringify(cart)+";domain=;path=/"
    location.reload()
}

function updateUserOrder(productId, action){
    var url='/update_Item/';

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,},
        body:JSON.stringify({
            productId:productId,action:action
        })
        
        

    }).then((response)=>{
         return response.json();
    }).then((data)=>{
        location.reload()
    })
}

var bigOne=document.querySelector(".photo_left img");
var allImages=document.querySelectorAll(".photo_right img");
allImages.forEach(image=>{image.addEventListener('mouseover',()=>{
    console.log("omage:;",bigOne, image.src)
    bigOne.src= image.src
})})








