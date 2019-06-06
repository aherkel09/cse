function ldl_level(level) {
  var level_range = {
    100: 'optimal',
    130: 'near optimal',
    160: 'borderline',
    190: 'high',
  }
  
  for (r in level_range) {
    if (level < r) {
      return level_range[r];
    }
  }
  
  return 'very high';
}

function get_level() {
  var ldl = prompt('Please enter your LDL level: ')
  
  try {
    var level = ldl_level(Math.abs(Number(ldl)));
    alert('Your LDL level is ' + level);
  } catch {
    alert('Error: please enter only numbers');
  }
}
