---
title: Geometric Mean
description: Calculate the geometric mean of a set of numbers
num: 7
---

# {{ page.num }}. {{ page.description }}

<script src="/cse/day03/geometricMean.js"></script>

```javascript
function geometricMean(numbers) {
  var product = 1;
  
  for (var n in numbers) {
    product *= Number(numbers[n]);
  }
  
  var mean = product ** (1/numbers.length);
  return 'The geometric mean of ' + numbers + ' is ' + mean;
}

function getGeoNumbers() {
  var counter = 0;
  var numbers_list = prompt('Enter a list of numbers separated by a space: ').split(' ');
  
  for (var l in numbers_list) {
    counter += isNaN(numbers_list[l]); // adds 1 to counter if non-numeric character in numbers_list
  }
  
  if (counter > 0) {
    alert('Error: please enter only numbers');
  } else if (counter == 0 && numbers_list.length) { // check length to avoid dividing by 0
    alert(geometricMean(numbers_list));
  } else {
    alert('No numbers were entered');
  }
}
```

<button type="button" onclick="getGeoNumbers()">Enter Numbers</button>
