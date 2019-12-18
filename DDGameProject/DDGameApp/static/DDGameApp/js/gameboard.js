console.log("game on");

function drawline() {

}
var canvas = document.getElementById("mycanvas");
var ctx = canvas.getContext("2d");
ctx.moveTo(0, 0);
ctx.lineTo(200, 100);
ctx.stroke();

// var canvas = document.getElementById("mycanvas");
// var ctx = canvas.getContext("2d");
// ctx.beginPath();
// ctx.arc(95,50,40,0,2*Math.PI);
// ctx.stroke();

