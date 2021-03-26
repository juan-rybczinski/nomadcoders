const body = document.querySelector("body");

const IMG_NUMBER = 3;

function paintImage(imageNumber) {
  const image = new Image();
  image.src = `images/${imageNumber}.jpeg`;
  image.classList.add("bgImage");
  body.prepend(image);
}

function getRandom() {
  const number = Math.floor(Math.random() * 3) + 1;
  return number;
}

function init() {
  const randomNumber = getRandom();
  paintImage(randomNumber);
}

init();
