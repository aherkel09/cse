function common(one, two) {
	var commonArr = [];
	for (var i = 0; i < one.length; i = i + 1) {
		for (var j = 0; j < two.length; j = j + 1) {
			if (one[i] == two[j]) {
				commonArr.push(one[i]);
			}
		}
	}
	return (commonArr);
}

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
