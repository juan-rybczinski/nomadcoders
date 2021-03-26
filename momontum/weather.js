const API_KEY = "919e8cb0ce6f09c109a8c73a70f677a5";
const COORDS = "coords";

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
}

function handGeoError() {
  console.log("Can't access geo location!");
}

function askForCoords() {
  navigator.geolocation.getCurrentPosition(handGeoSuccess, handGeoError);
}

function init() {
  const coords = localStorage.getItem(COORDS);
  if (coords === null) {
    askForCoords();
  }
}

init();
