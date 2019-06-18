function advanceThreeLetters(string) {
  var alpha = 'abcdefghijklmnopqrstuvwxyz';
  var caps = alpha.toUpperCase();
  advanced = ''
  
  for (var s in string) {
    if (alpha.includes(string[s]) || caps.includes(string[s])) {
      for (var a in alpha) {
        if (alpha[a] == string[s] && a <= 22) {
          advanced += alpha[Number(a) + 3];
        } else if (alpha[a] == string[s]) {
          advanced += alpha[Number(a) - 23];
        } else if (caps[a] == string[s] && a <= 22) {
          advanced += caps[Number(a) + 3];
        } else if (caps[a] == string[s]) {
          advanced += caps[Number(a) - 23];
        }
      }
    } else {
      advanced += string[s]
    }
  }
  
  return advanced;
}

function getWordsToReverse() {
  var words = prompt('Please enter a string of words to reverse:');
  
  try {
    advanceThreeLetters(words);
  } catch(error) {
    console.log('Error:', error);
  }
}
