const weather = document.querySelector(".js-weather");

const API_KEY = "919e8cb0ce6f09c109a8c73a70f677a5";
const COORDS = "coords";

function getWeather(lat, lon) {
  fetch(
    `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (json) {
      const temp = json.main.temp;
      const place = json.name;
      weather.innerText = `${temp} @ ${place}`;
    });
}

function saveCoords(coordsObj) {
  console.log(coordsObj);
  localStorage.setItem(COORDS, JSON.stringify(coordsObj));
}

function handGeoSuccess(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  const coordsObj = {
    latitude,
    longitude,
  };
  saveCoords(coordsObj);
  getWeather(latitude, longitude);
}

function handGeoError() {
  console.log("Can't access geo location!");
}

function askForCoords() {
  navigator.geolocation.getCurrentPosition(handGeoSuccess, handGeoError);
}

function init() {
  const loadedCoords = localStorage.getItem(COORDS);
  if (loadedCoords === null) {
    askForCoords();
  } else {
    const parsedCoords = JSON.parse(localStorage.getItem(COORDS));
    getWeather(parsedCoords.latitude, parsedCoords.longitude);
  }
}

init();
