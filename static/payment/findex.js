//'use strict';
var clientsecret = Math.floor((Math.random() * 10000) + 1);

// Set up Stripe.js and Elements to use in checkout form
var style = {
base: {
  color: "#000",
  lineHeight: '2.4',
  fontSize: '16px'
}
};


var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
ev.preventDefault();

var custName = document.getElementById("custName").value;
var phone = document.getElementById("phone").value;
var custAdd = document.getElementById("custAdd").value;
var paid = document.getElementById("paid").value;


  $.ajax({
    type: "POST",
    url: 'http://127.0.0.1:8000/orders/add/',
    data: {
      order_number: clientsecret,
      csrfmiddlewaretoken: CSRF_TOKEN,
      productid : $('#submit').val(),
      action: "post",
      cusName: custName,
      phone_num: phone,
      add : custAdd,
      paid : paid,
    },
    success: function (json) {
      console.log(json.success)
      window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");

    },
    error: function (xhr, errmsg, err) {},
  });



});