---
title: Check the Temperature
description: Check the Temperature
---

# {{ page.description }}

<script src="/cse/day03/Temperature.js"></script>

```javascript
function totalCost(price, num){
  var totalCost = price*num;
    alert(totalCost);
}
function getTotal(){
  var price = prompt("Please enter price of item.").split('$')[0];
  var number = prompt("Please enter number of items.");
  
  if (!isNaN(price) && !isNaN(number)) {
    totalCost(price, number);
  } else {
    alert('Error: please enter only numbers.');
    getTotal();
}
```

<button type="button" onclick="getTemp()">Enter Temperature</button>
