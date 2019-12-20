console.log("game on");
var x = 0;
var y = 0;
var gap = 25;
var x2 = 0;
var y2 = 0;
var gap2 = 25;
var startx = 500;
var starty = 250;
var partylocx = startx ;
var partylocy = starty;
// var toggleon = false;
var img = new Image();
img.src = "https://i.pinimg.com/originals/51/c4/a4/51c4a451db6cde9c927bc55affb01afe.jpg";
// img.width = 1000;
console.log("Drawing Game");
var canvas = document.getElementById("mycanvas");
var ctx = canvas.getContext("2d");
ctx.drawImage(img, 0, 0, 1000, 500);
ctx.fillRect(startx, starty, 25, 25);
ctx.fillStyle = "blue";
cities();
drawgame();
// img.height = 500;
var cityLocts = [{CityName:[]}, {Location:[{X:[]}, {Y:[]}]}];
var numcities = 0;

class Citiesfind {
    constructor(name, xpost, ypost) {
        this.name = name;
        this.xpost = xpost;
        this.ypost = ypost;
    }
}
var cityA = new Citiesfind("Augutus", 300, 200);
var cityB = new Citiesfind("Tron City", 400, 100);
var cityC = new Citiesfind("Chicago", 900, 375);
var cityD = new Citiesfind("Portland", 125, 125);
var cityE = new Citiesfind("Memphis", 350, 450);
var cityF = new Citiesfind("Beertown", 950, 50);
var cityG = new Citiesfind("DeadLands", 750, 425);

cityLocts[0].CityName.push(cityA.name);
cityLocts[1].Location[0].X.push(cityA.xpost);
cityLocts[1].Location[1].Y.push(cityA.ypost);

cityLocts[0].CityName.push(cityB.name);
cityLocts[1].Location[0].X.push(cityB.xpost);
cityLocts[1].Location[1].Y.push(cityB.ypost);

cityLocts[0].CityName.push(cityC.name);
cityLocts[1].Location[0].X.push(cityC.xpost);
cityLocts[1].Location[1].Y.push(cityC.ypost);

cityLocts[0].CityName.push(cityD.name);
cityLocts[1].Location[0].X.push(cityD.xpost);
cityLocts[1].Location[1].Y.push(cityD.ypost);

cityLocts[0].CityName.push(cityE.name);
cityLocts[1].Location[0].X.push(cityE.xpost);
cityLocts[1].Location[1].Y.push(cityE.ypost);

cityLocts[0].CityName.push(cityF.name);
cityLocts[1].Location[0].X.push(cityF.xpost);
cityLocts[1].Location[1].Y.push(cityF.ypost);

cityLocts[0].CityName.push(cityG.name);
cityLocts[1].Location[0].X.push(cityG.xpost);
cityLocts[1].Location[1].Y.push(cityG.ypost);


function cities() {
    ctx.font="25px serif";
    ctx.strokeText("Augutus", 275, 195, 75, 25);
    var city1img = new Image();
    city1img.src = "https://cdn.shopify.com/s/files/1/0090/5072/products/PV6866JJ.jpeg?v=1485394744";
    ctx.drawImage(city1img,300, 200, 25, 25);
    ctx.strokeRect(300, 200, 25, 25);


    ctx.strokeText("Tron City", 375, 95, 75, 25);
    ctx.fillRect(400, 100, 25, 25);

    ctx.strokeText("Chicago", 875, 370, 75, 25);
    ctx.fillRect(900, 375, 25, 25);

    ctx.strokeText("Portland", 100, 120, 75, 25);
    ctx.fillRect(125, 125, 25, 25);

    ctx.strokeText("Memphis", 325, 445, 75, 25);
    ctx.fillRect(350, 450, 25, 25);

    ctx.strokeText("Beertown", 925, 45, 75, 25);
    ctx.fillRect(950, 50, 25, 25);

    ctx.strokeText("Deadlands", 725, 420, 75, 25);
    ctx.fillRect(750, 425, 25, 25);
    ctx.fillStyle= "red"
}
function drawgame() {
    while (x <= 1000) {
        ctx.moveTo(x, 0);
        ctx.lineTo(x, 500);
        ctx.stroke();
        // ctx.strokeStyle = "red";
        x = x + gap;
    }
    console.log("One Done");
    while (y <= 500) {
        ctx.moveTo(0, y);
        ctx.lineTo(1000, y);
        ctx.stroke();
        // ctx.strokeStyle = "yellow";
        y = y + gap;
    }
    console.log("Two Done");
}
function drawboard() {
    while (x2 <= 1000) {
        ctx.moveTo(x2, 0);
        ctx.lineTo(x2, 500);
        ctx.stroke();
        ctx.strokeStyle = "blue";
        x2 = x2 + gap2;
    }
    console.log("three Done");
    while (y2 <= 500) {
        ctx.moveTo(0, y2);
        ctx.lineTo(1000, y2);
        ctx.stroke();
        ctx.strokeStyle = "blue";
        y2 = y2 + gap2;
    }
    console.log("four Done");
}

function moving(move) {
    ctx.clearRect(startx, starty, 25, 25);
    if (move === "up") {
        starty = starty - 25;
    } else if (move === "down") {
        starty = starty + 25;
    } else if (move === "left") {
        startx = startx - 25;
    } else if (move === "right") {
        startx = startx + 25;
    }
    ctx.drawImage(img, 0, 0, 1000, 500);
    ctx.strokeRect(startx, starty, 25, 25);
    partyloc = ctx.strokeRect(startx, starty, 25, 25);
    ctx.strokeStyle = "yellow";
    // drawboard();
    cities();
    partylocx = startx;
    partylocy = starty;
    console.log(partylocx , partylocy);
    console.log(cityLocts[0].CityName[numcities]);
    console.log(cityLocts[1].Location[0].X[1]);
    console.log(cityLocts[1].Location[1].Y[1]);

    // if(startx === cityLocts[1].Location[0].X[0] && starty === cityLocts[1].Location[1].Y[0]){
    //     alert("You have arrived at " + cityLocts[0].CityName[0])
    // }
    // else if(startx === cityLocts[1].Location[0].X[1] && starty === cityLocts[1].Location[1].Y[1]){
    //     alert("You have arrived at " + cityLocts[0].CityName[1])
    // }
    // else if(startx === cityLocts[1].Location[0].X[2] && starty === cityLocts[1].Location[1].Y[2]){
    //     alert("You have arrived at " + cityLocts[0].CityName[2])
    // }

    while(numcities < cityLocts[0].CityName.length){
        if (startx === cityLocts[1].Location[0].X[numcities] && starty === cityLocts[1].Location[1].Y[numcities])
        {
            alert("You have arrived at " + cityLocts[0].CityName[numcities]);
            console.log(numcities);
            break;


        }
        else {
            numcities = numcities + 1;
            console.log(numcities);
        }
    }
    numcities = 0;




}