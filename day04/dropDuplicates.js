function dropDuplicates(arr1, arr2) {
  for (var a in arr2) {
    if (arr1.includes(arr2[a])) {
      arr1.splice(arr1.indexOf(arr2[a]), 1);
    }
  }
  
  return arr1;
}

function getItems() {
  var first = prompt('Please enter a list of items separated by a comma:').replace(/\s/g, '').split(',');
  var second = prompt('Please enter another list of items separated by a comma:').replace(/\s/g, '').split(',');
  
  try {
    alert(dropDuplicates(first, second));
  } catch(error) {
    console.log(error);
  }
}
