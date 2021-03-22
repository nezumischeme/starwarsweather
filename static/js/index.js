var city = prompt("Please enter your city.");
city = city.replace(/\s/g, '+')
planetText = document.getElementById('planet');
temperText = document.getElementById('tempText');
let request = new XMLHttpRequest();
request.open('GET', '/api/' + city);
request.responseType = 'json';
request.onload = function() {
    planetText.innerHTML = "It's like " + request.response['planet'] + " out there.";
    temperText.innerHTML = `Temp: ${request.response['tempC']}C or ${request.response['tempF']}F.`;
};
request.send();