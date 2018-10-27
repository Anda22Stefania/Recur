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

function getAllPurchases(id)
{
  var url = "http://api.reimaginebanking.com/accounts/" + id + "/purchases?key=351388794358970b8ed7ec1790b2004a";
  console.log(url);
  $.ajax({
    type: "GET",
    url: url,
    success: function(result){
      //console.log(result);
      return result;
    },
    error: function(result){
      alert(error);
    }
  });
}
//Function to get fixed recurring costs
function getSubscriptions(accountId)
{
  $.ajax({
    type: 'GET',
    url: "http://localhost:5000/api/subscriptions/" + accountId,
    success: function(result) {
      putElementsIntoTable(result, "recurring");
    },
    error: function(result){
      console.log(result);
    }
  });
}
//Function to get varying recurring costs

function getIrregularRecurringPurchases(accountId)
{
  $.ajax({
    type: 'GET',
    url: "http://localhost:5000/api/irregular/" + accountId,
    success: function(result) {
      putElementsIntoTable(result, "non-recurring");
    },
    error: function(result){
      console.log(result);
    }
  });
}

// method to take the elements of a vector and add them in the table
function putElementsIntoTable(elementsArray, tableID)
{
  //get the table id
  var table = document.getElementById(tableID);
  for(var index = 0; index < elementsArray.length; index++)
  {
    console.log(elementsArray[index]);
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
    var cell1 = row.insertCell();
    cell1.innerHTML = elementsArray[index].merchant.name;
    var cell2 = row.insertCell();
    cell2.innerHTML = elementsArray[index].amount;
    var cell3 = row.insertCell();
    cell3.innerHTML = elementsArray[index].purchase_date;
  }
}


// hard coded vctor for recurring table
var testVector1 = [{name:"Netflix", cost:12, date:"26-11-2018"},
                   {name:"Amazon Prime", cost:8, date:"15-11-2018"},
                   {name:"Giffgaff", cost:7.50, date:"10-11-2018"},
                   {name:"Rent", cost:300, date:"1-11-2018"}];
// hard coded vctor for non-recurring table
var testVector2 = [{name:"Tesco", cost:12, date:"25.10.2018"},
                   {name:"Lidl", cost:6, date:"15-10-2018"},
                   {name:"Subway", cost:5, date:"20-10-2018"},
                   {name:"Subway", cost:2, date:"24-10-2018"}];

// call the putElementsIntoTable method
//putElementsIntoTable(testVector1, "recurring");
//putElementsIntoTable(testVector2, "non-recurring");
getSubscriptions("5bd46141322fa06b67793ea2");
getIrregularRecurringPurchases("5bd46141322fa06b67793ea2");
