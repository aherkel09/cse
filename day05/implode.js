function implode(list) {
  var alpha = 'abcdefghijklmnopqrstuvwxyz';
  var imploded = [];
  
  for (var l in list) {
    var chars = '';
    for (var a in alpha) {
      if (list[l].includes(alpha[a]) && !chars.includes(alpha[a])) {
        chars += alpha[a];
      }
    }
    imploded.push(chars);
  }
  
  return imploded;
}

function getStringToImplode() {
  var strings = prompt('Please enter a list of strings separated by a comma:');
  
  try {
    var stringList = strings.toLowerCase().replace(/\s/g, '').split(',');
    alert(implode(stringList));
  } catch(error) {
    console.log(error);
  }
}
