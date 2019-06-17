/* FIX ME */
function advanceThreeLetters(string) {
  var alpha = 'abcdefghijklmnopqrstuvwxyz';
  var caps = alpha.toUpperCase();
  advanced = ''
  
  for (var s in string) {
    if (alpha.includes(string[s]) || caps.includes(string[s])) {
      for (var a in alpha) {
        if (alpha[a] == string[s] && a <= 22) {
          advanced += alpha[a + 3];
        } else if (alpha[a] == string[s]) {
          advanced += alpha[a - 23];
        } else if (caps[a] == string[s] && a <= 22) {
          advanced += caps[a + 3];
        } else if (caps[a] == string[s]) {
          advanced += caps[a - 23];
        }
      }
    } else {
      advanced += string[s]
    }
  }
  
  return advanced;
}
  
