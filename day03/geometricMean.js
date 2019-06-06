function geometricMean(numbers) {
  var product = 1;
  
  for (var n in numbers) {
    product *= numbers[n];
  }
  
  if (numbers.length) {
    var mean = product ** (1/numbers.length);
    return 'The geometric mean of ' + numbers + ' is ' + mean;
  } else {
    return 'No numbers were entered';
  }
}

function getGeoNumbers() {
  var counter = 0;
  var numbers_list = prompt('Enter a list of numbers separated by a space: ').split(' ');
  
  for (var l in numbers_list) {
    counter += isNaN(numbers_list[l]);
  }
  
  if (counter > 0) {
    alert('Error: please enter only numbers');
  } else if (counter == 0) {
    alert(geometricMean(numbers_list));
  }
}
