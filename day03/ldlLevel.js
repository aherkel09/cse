function ldlLevel(level) {
  var levelRange = {
    100: 'optimal',
    130: 'near optimal',
    160: 'borderline',
    190: 'high',
  }
  
  for (var r in levelRange) {
    if (level < r) {
      return levelRange[r];
    }
  }
  
  return 'very high';
}

function getLevel() {
  var ldl = prompt('Please enter your LDL level: ')
  
  try {
    var level = ldlLevel(Math.abs(Number(ldl)));
    alert('Your LDL level is ' + level);
  } catch(err) {
    alert('Error: please enter only numbers');
    console.log(err)
  }
}
