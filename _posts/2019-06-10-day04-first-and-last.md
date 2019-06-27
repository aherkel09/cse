---
title: First & Last
description: Get the first & last elements of an array
day: 04
num: 4
---

# Day {{ page.day }} - Exercise {{page.num }}: {{ page.description }}

<script src="/cse/day04/firstLast.js"></script>

```javascript
function first_last(arr) {
	var newArr = [];
	newArr.push(arr[0]);
	newArr.push(arr[arr.length - 1]);
	console.log(newArr);
}

function firstLast(arr) {
	return [arr[0], arr[arr.length - 1]];
}

function getUserArray() {
	var array = prompt('Please enter an array of items separated by a comma:').split(', ');

	try {
		var firstAndLast = firstLast(array);
		alert(firstAndLast);
	} catch(error) {
		console.log(error);
	}
}
```

<button type="button" onclick="getUserArray()">Enter Array</button>
