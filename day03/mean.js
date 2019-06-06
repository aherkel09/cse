function computeMean(numbers, meanType) {
  var types = ['arithmetic', 'geometric'];
  var counter = 0;
  var mean;
  
  if (!numbers.length) {
    return 'No numbers were entered';
  } else if (meanType == 0) { // arithmetic mean
    for (var n in numbers) {
      counter += Number(numbers[n]);
    }
    mean = counter / numbers.length;
  } else if (meanType == 1) { // geometric mean
    counter += 1 // start counter at 1
    for (var n in numbers) {
      counter *= numbers[n];
    }
    mean = counter ** (1/numbers.length);
  }

  return 'The ' + types[meanType] + ' mean of ' + numbers + ' is ' + mean;    
}

function getMeanNumbers(error=false) {
  if (error) {
    alert('Error: please enter only numbers');
  }
  
  var numbers = []
  
  while (numbers.length < 4) {
    var newNum = prompt('Please enter a number: ');
    if (!isNaN(newNum)) {
      numbers.push(newNum);
    }
  }
  
  var meanType = prompt('Enter 0 to compute the arithmetic mean, or 1 to compute the geometric mean: ')
  
  if (meanType == 0 || meanType == 1) {
    return alert(computeMean(numbers, meanType));
  } else {
    return getNumbers(error=true);
  }
}
