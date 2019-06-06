function computeCost(price, numItems) {
  var pretax = price * numItems;
  var shipping = pretax * 0.1;
  var tax = pretax * 0.08;
  
  alert(pretax + shipping + tax);
}

function getOrderDetails() {
  var price = prompt('Enter the price of the item:').replace('$', '');
  var num = prompt('Enter the number of items:');
  
  if (!isNaN(price) && !isNaN(num)) {
    return computeCost(price, num);
  } else {
    alert('Error: please enter only numbers');
    getOrderDetails();
  }
}
  
