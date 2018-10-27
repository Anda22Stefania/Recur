/*request.get('http://api.reimaginebanking.com/atms?key=351388794358970b8ed7ec1790b2004a').end(function(res){
    foo(res.status);
    bar(res.body); //do something
});*/
var id = "5bd46141322fa06b67793ea2";
var accounts = [];
var subscriptions = {};

$.ajax({
  type: "GET",
  url: "http://api.reimaginebanking.com/accounts?key=351388794358970b8ed7ec1790b2004a",
  success: function(result){
    var accounts = result;
    //console.log(accounts);
  }
});


$.ajax({
  type: "GET",
  url: "http://api.reimaginebanking.com/atms?key=351388794358970b8ed7ec1790b2004a",
  success: function(result){
    //alert(result.data[1].name);
  }
});

<<<<<<< HEAD
function getAllPurchases(id)
{
  var url = "http://api.reimaginebanking.com/accounts/" + id + "/purchases?key=351388794358970b8ed7ec1790b2004a";
  console.log(url);
  $.ajax({
    type: "GET",
    url: url,
    success: function(result){
      console.log(result);
      return result;
    },
    error: function(result){
      alert(error);
    }
  });
}

function getSubscriptions(accountId)
{
  $.ajax({
    type: GET,
    url: "localhost/api/subscriptions/" + accountId,
    success: function(result) {
      console.log(result);
    },
    error: function(result){
      console.log(result);
    }
  });
}

alert(getAllPurchases(id));
var table = document.getElementById("subscriptions");
var rowCount = table.rows.length;
var row = table.insertRow(rowCount);
var cell1 = row.insertCell();
cell1.innerHTML = "HI";
=======
function getCustomerAccounts(id) {
    var url = "http://api.reimaginebanking.com/customers/" + {id} + "/accounts?key=c4a0166d7cd592202bf2bd0bf909b21b";
    $.ajax(
        {
            type: "GET",
            url: url,
            success: function(results){
                var customerAccounts = result;
                console.log(customerAccounts);
            }
        }
    )
}
>>>>>>> 807d4fe980ac6662eed2c2cc9b028d4288feeaec
