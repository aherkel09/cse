function dropDuplicates(arr1, arr2) {
  for (var a in arr1) {
    if (arr2.includes(arrl[a])) {
      arr1.splice(a, 1);
    }
  }
  
  return arr1;
}

function getItems() {
  var first = prompt('Please enter a list of items separated by a comma:');
  var second = prompt('Please enter another list of items separated by a comma:');
  
  try {
    alert(dropDuplicates(first, second));
  } catch(error) {
    console.log(error);
  }
}
