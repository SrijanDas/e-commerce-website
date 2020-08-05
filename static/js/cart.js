var updateBtns = document.getElementsByClassName("update-cart");
var cart_items = cart_items;
// console.log("cart: ", cart_items);
isCartEmpty(cart_items);

function isCartEmpty(cart_items){
  if (cart_items == 0) {
    document.getElementById("cart").innerHTML = ""
    document.getElementById("empty_cart").classList.remove("collapse")
  }
}

for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    
    if (user === "AnonymousUser") {
      addCookieItem(productId, action);
      
    } else {
      updateUserOrder(productId, action);
     
    }
  });
}

function addCookieItem(productId, action){
  // console.log("not logged in");
  if (action == "add") {
    if (cart[productId] == undefined) {
      cart[productId] = { "quantity": 1 };
    } else {
      cart[productId]["quantity"] += 1;
    }
  }

  if (action == "remove") {
    cart[productId]["quantity"] -= 1;
    if (cart[productId]["quantity"] <= 0) {
      delete cart[productId];
    }
  }
  if (action == "remove_item") {   
      delete cart[productId];
  }
  // console.log("Cart:", cart);
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
  location.reload();

};

function updateUserOrder(productId, action) {
  // console.log("User is logged in. Sending data...");

  var url = "/update_cart/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-type": "application/Json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ 'productId': productId, 'action': action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // console.log(("data:", data));
      location.reload();
    })
};


