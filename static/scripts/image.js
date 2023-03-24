var images = {{ images | tojson }};
var index = 0;

function nextImage() {
  index++;
  if (index >= images.length) {
    index = 0;
  }
  document.getElementById("image").src = images[index];
}