---
title: Every Other
description: Get every other character of a string
day: 05
num: 5
---

# Day {{ page.day }} - Exercise {{page.num }}: {{ page.description }}

<script src="/cse/day05/everyOther.js"></script>

```javascript
function everyOther(string) {
  var everyOther = '';
  for (var c = 0; c < string.length; c += 2) {
    everyOther += string[c];
  }
  return everyOther;
}

function getStringToSlice() {
  var string = prompt('Please enter a string:');
  
  try {
    return alert(everyOther(string));
  } catch(error) {
    return console.log(error);
  }
}
```

<button type="button" onclick="getStringToSlice()">Enter String</button>
