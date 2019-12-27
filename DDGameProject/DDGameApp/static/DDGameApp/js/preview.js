console.log("preview");

var img = new Image();
img.src = loadmap();
// img.width = 1000;
console.log("Drawing Game");
var canvas = document.getElementById("mycanvas");
var ctx = canvas.getContext("2d");
ctx.drawImage(img, 0, 0, 1000, 500);

function loadmap(map) {
    return map;
}