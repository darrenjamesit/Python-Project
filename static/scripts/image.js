var currentImg = 0;
var images = document.getElementById("image-container").getElementsByTagName("img");

function toggleImages() {
    console.log(currentImg)
    // hide the currently displayed image
    images[currentImg].style.display = "none";
    images[currentImg].style.visibility = "hidden";

    // update the index of the next image to be displayed
    currentImg = (currentImg + 1) % images.length;

    // show the next image in sequence
    images[currentImg].style.display = "block";
    images[currentImg].style.visibility = "visible";
}