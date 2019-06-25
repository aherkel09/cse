---
title: Common Elements
description: Enter two arrays to see what elements they have in common
day: 04
num: 3
---

# Day {{ page.day }} - Exercise {{page.num }}: {{ page.description }}

<script src="/cse/day04/commonElements.js"></script>

```javascript
function getCommonElements(arr1, arr2) {
	var commonElements = [];
	for (var a in arr1) { // uses one loop
		if (arr2.includes(arr1[a])) { // uses built-in includes() function
			commonElements.push(arr1[a]);
		}
	}
	return commonElements;
}

function getTwoArrays() {
	var firstArray = prompt('Enter an array of objects separated by a comma:').split(', ');
	var secondArray = prompt('Enter a second array:').split(', ');
	
	try {
		alert('The arrays you entered share: ' + getCommonElements(firstArray, secondArray));
	} catch(error) {
		console.log(error);
	}
}
```

<button type="button" onclick="getTwoArrays()">Enter Arrays</button>
