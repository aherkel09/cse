function shipping(totalPretax){
  if (totalPretax >= 100){
    alert("Free Shipping!");
  }else{
    alert(totalPretax*0.1);
  }
}
function pretaxAmount(){
  var pretax = prompt("Enter the total pre-tax amount of order.");
  
shipping(pretax);
}
