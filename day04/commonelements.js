function common(one, two) {
	var commonArr = [];
	for (var i = 0; i < one.length; i = i + 1) {
		for (var j = 0; j < two.length; j = j + 1) {
			if (one[i] == two[j]) {
				commonArr.push(one[i]);
			}
		}
	}
	console.log(commonArr);
}
