var form = document.getElementById("shipping_form");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  document.getElementById("form-button").classList.add("collapse");
  document.getElementById("payment-option").classList.remove("collapse");
  
});

// document.getElementById("make-payment").addEventListener("click", function (e) {
//   submitFormData();
// });

// function submitFormData() {
//   var userFormData = {
//     'name': document.getElementById("name").value,
//     'email': document.getElementById("email").value,
//     'total':total,
//   };

//   var shippingInfo = {
//     'address': document.getElementById("address").value,
//     'city': document.getElementById("city").value,
//     'state': document.getElementById("state").value,
//     'zipcode': document.getElementById("zipcode").value,
//   };

//   var url = "/process_order/";

//   fetch(url, {
//     method: "POST",
//     headers: {
//       "Content-tupe": "application/Json",
//       "X-CSRFToken": csrftoken,
//     },
//     body: JSON.stringify({
//       'form': userFormData,
//       'shipping': shippingInfo,
//     }),
//   })
//     .then((response) => response.json())

//     .then((data) => {
//       console.log("Success:", data);
//       alert("Transition completed");
//       window.location.href = "/";
//     });
// }
