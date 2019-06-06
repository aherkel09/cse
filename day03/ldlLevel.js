function ldlLevel(level) {
  var levelRange = {
    100: 'optimal',
    130: 'near optimal',
    160: 'borderline',
    190: 'high',
  }
  
  for (r in levelRange) {
    if (level < r) {
      return levelRange[r];
    }
  }
  
  return 'very high';
}

function getLevel() {
  var ldl = prompt('Please enter your LDL level: ')
  
  try {
    var level = ldl_level(Math.abs(Number(ldl)));
    alert('Your LDL level is ' + level);
  } catch {
    alert('Error: please enter only numbers');
    getLevel();
  }
}