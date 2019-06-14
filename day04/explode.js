function explode(string) {
  var charList = [];
  for (var s in string) {
    charList.push(string[s]);
  }
  
  return charList;
}

function getUserString() {
  var string = prompt('Please enter a string:');
  
  try {
    alert(explode(string));
  } catch(error) {
    console.log(error);
  }
}
