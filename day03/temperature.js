function weather(temperature) {
  if (temperature < 65) {
    alert("cold");
  } else if (temperature > 85) {
    alert("hot");
  } else {
    alert("comfortable");
  }
}

function getTemp() {
  var temp = prompt("Please enter a temperature");
  if (!isNaN(temp)) { // make sure user input number
    return weather(temp);
  } else {
    alert('Error: please enter only numbers');
    return getTemp();
  }
}
