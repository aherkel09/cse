---
title: Shipping Cost
description: Check the shipping cost of an order
day: 03
num: 3
---

# Day {{ page.day }} - Exercise {{page.num }}: {{ page.description }}

<script src="/cse/day03/shipping.js"></script>

```javascript
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
}
```

<button type="button" onclick="getPretaxAmount()">Enter Order Details</button>
