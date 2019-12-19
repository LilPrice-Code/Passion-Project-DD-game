console.log("game on");
var x = 0;
var y = 0;
var gap = 50;
function drawboard() {
    console.log("Drawing Game");
    var canvas = document.getElementById("mycanvas");
    var ctx = canvas.getContext("2d");
    ctx.fillStyle="url(https://images.pexels.com/photos/592753/pexels-photo-592753.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940)";
    while (x <= 1000){
        ctx.moveTo(x, 0);
        ctx.lineTo(x, 500);
        ctx.stroke();
        x = x + gap;
    }
    console.log("One Done");
    while (y <= 500){
        ctx.moveTo(0, y);
        ctx.lineTo(1000, y);
        ctx.stroke();
        y = y + gap;
    }
    console.log("Two Done");

}

// var canvas = document.getElementById("mycanvas");
// var ctx = canvas.getContext("2d");
// ctx.beginPath();
// ctx.arc(95,50,40,0,2*Math.PI);
// ctx.stroke();

