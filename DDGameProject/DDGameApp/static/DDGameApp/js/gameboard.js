console.log("game on");
var x = 0;
var y = 0;
var gap = 25;
function drawline() {
    var canvas = document.getElementById("mycanvas");
    var ctx = canvas.getContext("2d");
    while (x <= 1000){
        ctx.moveTo(x, 0);
        ctx.lineTo(x, 500);
        ctx.stroke();
        x = x + gap;
    }
    while (y <= 500){
        ctx.moveTo(0, y);
        ctx.lineTo(1000, y);
        ctx.stroke();
        y = y + gap;
    }
}

// var canvas = document.getElementById("mycanvas");
// var ctx = canvas.getContext("2d");
// ctx.beginPath();
// ctx.arc(95,50,40,0,2*Math.PI);
// ctx.stroke();

