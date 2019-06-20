function getKeysFromValue(data, value) {
  var keys = [];
  for (var d in data) {
    if (data[d] == value) {
      keys.push(d);
    }
  }
    
  return value + ' is paired with: ' + keys;
}

function getData() {
  var dictionary = prompt('Please enter key/value pairs (e.g., key1: value1, key2: value2): ');
  var value = prompt('Enter a value to see how frequently it occurs: ');

  try {
    var data = {};
    var key_val = dictionary.split(', ');

    for (var k=0; k < key_val.length; k++) {
      var split = key_val[k].split(': ');
      data[split[0]] = split[1];
    }

    alert(getKeysFromValue(data, value));
  } catch(error) {
    console.log('Error:', error);
  }
}
