function implode(string) {
  var chars = '';
  
  for (var s in string) {
    if (!chars.includes(string[s])) {
      chars += string[s];
    }
  }
  
  return chars;
}

function getStringToImplode() {
  var string = prompt('Please enter a string:');
  
  try {
    alert(implode(string));
  } catch(error) {
    console.log(error);
  }
}
