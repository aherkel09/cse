---
title: Check the Temperature
description: Check the Temperature
---

<script src="/cse/day03/Temperature.js"></script>

```javascript
function weather(temperature){
  if (temperature < 65){
    alert("cold");
  }else if (temperature > 85){
    alert("hot");
  }else{
    alert("comfortable");
  }
}
function getTemp(){
  var temp = prompt("Please enter a temperature");
  return weather(temp);
}
```

<button type="button" onclick="getTemp()">Enter Temperature</button>
