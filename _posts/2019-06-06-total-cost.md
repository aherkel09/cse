---
title: Total Cost
description: Get the total cost for multiple items
---

# {{ page.description }}

<script src="/cse/day03/totalCost.js"></script>

```javascript
function totalCost(price, num){
  var totalCost = price*num;
    alert(totalCost);
}
function getTotal(){
 var price = prompt("Please enter price of item.");
 var number = prompt("Please enter number of items.");
  totalCost(price, number);
}
```

<button type="button" onclick="getTotal()">Enter Values</button>
