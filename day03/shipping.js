function shippingCost(totalPretax) {
  if (totalPretax >= 100) {
    alert("Free Shipping!");
  } else {
    alert(totalPretax * 0.1);
  }
}

function getPretaxAmount(){
  var pretax = prompt("Enter the total pre-tax amount of order:").replace('$', '');
  
  if (!isNaN(pretax)) {
    return shippingCost(pretax);
  } else {
    alert('Error: please enter only numbers');
    return getPretaxAmount();
}
