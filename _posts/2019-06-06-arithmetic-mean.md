---
title: Arithmetic Mean
description: Calculate the arithmetic mean of a set of numbers
num: 6
---

# {{ page.num }}. {{ page.description }}

<script src="/cse/day03/arithmeticMean.js"></script>

```javascript
function arithmeticMean(numbers) {
  var total = 0;
  
  for (var n in numbers) {
    total += Number(numbers[n]);
  }
  
  if (numbers.length) {
    var mean = total / numbers.length
    return 'The arithmetic mean of ' + numbers + ' is ' + mean;
  }
  
  return 'No numbers were entered';
}

function getArithNumbers() {
  var counter = 0;
  var numbers_list = prompt('Enter a list of numbers separated by a space: ').split(' ');
  
  for (var l in numbers_list) {
    counter += isNaN(numbers_list[l]);
  }
  
  if (counter > 0) {
    alert('Error: please enter only numbers');
  } else if (counter == 0) {
    alert(arithmeticMean(numbers_list));
  }
}
  
  

```

<button type="button" onclick="getArithNumbers()">Enter Numbers</button>