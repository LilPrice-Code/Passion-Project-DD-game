console.log("preview");
var x2 = 0;
var y2 = 0;
var gap2 = 25;
var startx = 500;
var starty = 250;
var getmap = document.getElementById("map");
var themap = getmap.innerHTML;
console.log(themap);
var img = new Image();
img.src = themap;
console.log("Drawing Game");
var canvas = document.getElementById("mycanvas");
var ctx = canvas.getContext("2d");
ctx.drawImage(img, 0, 0, 1000, 500);

var getcities = document.getElementsByClassName("city");
var getxcord = document.getElementsByClassName("xcord");
var getycord = document.getElementsByClassName("ycord");
var fulllength = getcities.length;
console.log(fulllength);
drawboard();

var cityLocts = [{CityName: []}, {Location: [{X: []}, {Y: []}]}];
var numcities = 0;

class Citiesfind {
    constructor(name, xpost, ypost) {
        this.name = name;
        this.xpost = xpost;
        this.ypost = ypost;
    }
}

function showcities() {
    while (numcities < fulllength) {
        ctx.font = "25px serif";
            ctx.strokeText(getcities.item(numcities).innerHTML, getxcord.item(numcities).innerHTML - 25, getycord.item(numcities).innerHTML - 5, 75, 25);
        ctx.fillRect(getxcord.item(numcities).innerHTML, getycord.item(numcities).innerHTML, 25, 25);
        numcities++;
    }
    console.log(cityLocts);

}

function partyLocation() {
    var newloct = document.getElementById('location');
    console.log("location Check");
    while (numcities < cityLocts[0].CityName.length) {
        if (partylocx === parseInt(cityLocts[1].Location[0].X[numcities]) && partylocy === parseInt(cityLocts[1].Location[1].Y[numcities])) {
            newloct.innerText = "Your Current Position: " + cityLocts[0].CityName[numcities];
            break;


        }
        else{
            newloct.innerText = "Your Current Position: In the Wild";
        }
        numcities = numcities + 1;
    }
    numcities = 0;
}


while (numcities < fulllength) {
    var citynew = new Citiesfind(getcities.item(numcities).innerHTML, getxcord.item(numcities).innerHTML, getycord.item(numcities).innerHTML);
    cityLocts[0].CityName.push(citynew.name);
    cityLocts[1].Location[0].X.push(citynew.xpost);
    cityLocts[1].Location[1].Y.push(citynew.ypost);
    ctx.font = "25px serif";
    ctx.strokeText(getcities.item(numcities).innerHTML, getxcord.item(numcities).innerHTML - 25, getycord.item(numcities).innerHTML - 5, 75, 25);
    ctx.fillRect(getxcord.item(numcities).innerHTML, getycord.item(numcities).innerHTML, 25, 25);


    numcities++;
}
console.log(cityLocts);

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
    ctx.fillRect(startx, starty, 25, 25);
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
    // drawboard();
    showcities();
    partylocx = startx;
    partylocy =starty;
    console.log(partylocx, partylocy);

    numcities = 0;
    partyLocation();
}