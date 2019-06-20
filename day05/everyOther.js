function everyOther(string) {
  var everyOther = '';
  for (var c = 0; c < string.length; c += 2) {
    everyOther += string[c];
  }
  return everyOther;
}

function getStringToSlice() {
  var string = prompt('Please enter a string:');
  
  try {
    return alert(everyOther(string));
  } catch(error) {
    return console.log(error);
  }
}
