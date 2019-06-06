function arithmeticMean(numbers) {
  var total = 0;
  
  for (var n in numbers) {
    total += Number(numbers[n]);
  }
  
  var mean = total / numbers.length;
  return 'The arithmetic mean of ' + numbers + ' is ' + mean;
}

function getArithNumbers() {
  var counter = 0;
  var numbers_list = prompt('Enter a list of numbers separated by a space: ').split(' ');
  
  for (var l in numbers_list) {
    counter += isNaN(numbers_list[l]); // adds 1 to counter if non-numeric character in numbers_list
  }
  
  if (counter > 0) {
    alert('Error: please enter only numbers');
  } else if (counter == 0 && numbers_list.length) { // check length to avoid dividing by 0
    alert(arithmeticMean(numbers_list));
  } else {
    alert('No numbers were entered');
  }
}
  
  
