/*request.get('http://api.reimaginebanking.com/atms?key=351388794358970b8ed7ec1790b2004a').end(function(res){
    foo(res.status);
    bar(res.body); //do something
});*/
var id = "";
var accounts = [];
var subscriptions = {};

$.ajax({
  type: "GET",
  url: "http://api.reimaginebanking.com/accounts?key=351388794358970b8ed7ec1790b2004a",
  success: function(result){
    var accounts = result;
    console.log(accounts);
  }
});


$.ajax({
  type: "GET",
  url: "http://api.reimaginebanking.com/atms?key=351388794358970b8ed7ec1790b2004a",
  success: function(result){
    alert(result.data[1].name);
  }
});
