---
title: Total Cost
description: Get the total cost for multiple items
---

# {{ page.description }}

<script src="/cse/day03/totalCost.js"></script>

```javascript
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
```

<button type="button" onclick="getUserPurchase()">Enter Values</button>
