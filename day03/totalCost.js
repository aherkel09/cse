function totalCost(price, num) {
  var totalCost = price * num;
  return totalCost;
}

function getUserPurchase() {
  var price = prompt("Please enter the price of the item:").split('$')[1];
  var number = prompt("Please enter the number of items:");
  
  if (!isNaN(price) && !isNaN(number)) {
    alert(totalCost(price, number));
  } else {
    alert('Error: please enter only numbers.');
    getUserPurchase();
  }
}
