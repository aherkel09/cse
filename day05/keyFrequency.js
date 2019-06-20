function getKeyFrequency(data, key) {
  var freq = 0;
  for (var d in data) {
    if (d == key) {
      freq ++;
    }
  }
    
  return key + ' occurs ' + freq + ' time(s).';
}

function getKeyData() {
  var dictionary = prompt('Please enter key/value pairs (e.g., key1: value1, key2: value2): ');
  var key = prompt('Enter a value to see how frequently it occurs: ');

  try {
    var data = {};
    var key_val = dictionary.split(', ');

    for (var k=0; k < key_val.length; k++) {
      var split = key_val[k].split(': ');
      data[split[0]] = split[1];
    }

    alert(getKeyFrequency(data, key));
  } catch(error) {
    console.log('Error:', error);
  }
}
