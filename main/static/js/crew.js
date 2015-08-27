var cameraSet = document.getElementById('camera-set');

for (var x = 1; x <= 88; x++) {

    var img = document.createElement('IMG');
    img.id = "movie" + x
    img.src = "/static/img/movie-camera-gray.png";
    cameraSet.appendChild(img);
}


// THIS IS NOT A GOOD SOLUTION AT ALL
// But. I wanted to use pure Javascript for 
// something -- for speed but also for learning. 
// There is a way to get this to repeat for each id 
// or each element in a class without writing it 
// all out AND I WILL FIND IT. AT SOME POINT. 
// CLEARLY NOT TONIGHT.

var fresholtz = 46
var wallin = 30
var minkler = 23
var lane = 12
var frankovich = 12
var jones = 12
var gaspar = 11
var tyler = 11
var pollack = 6
var grusin = 8
var brooks = 2
var qjones = 6
var bernstein = 6
var morricone = 1

var highlighted = false

var reset = function() {
    for (var x = 1; x <= 88; x++) {
        var img = document.getElementById("movie" + x);
        img.src = "/static/img/movie-camera-gray.png";
    }

    highlighted = false;
    
}

// Top eight:
var fresholtzBtn = document.getElementById("fresholtz");
fresholtzBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= fresholtz; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var wallinBtn = document.getElementById("wallin");
wallinBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= wallin; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var minklerBtn = document.getElementById("minkler");
minklerBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= minkler; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var laneBtn = document.getElementById("lane");
laneBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= lane; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var frankovichBtn = document.getElementById("frankovich");
frankovichBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= frankovich; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var jonesBtn = document.getElementById("jones");
jonesBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= jones; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var gasparBtn = document.getElementById("gaspar");
gasparBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= gaspar; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var tylerBtn = document.getElementById("tyler");
tylerBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= tyler; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


// Others of note:
var pollackBtn = document.getElementById("pollack");
pollackBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= pollack; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var grusinBtn = document.getElementById("grusin");
grusinBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= grusin; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var brooksBtn = document.getElementById("brooks");
brooksBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= brooks; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});


var qjonesBtn = document.getElementById("qjones");
qjonesBtn.addEventListener('click', function(e) {
    e.preventDefault();

    if (highlighted) {
        reset();
        return;
    }

    highlighted = true;
    for ( var x = 1; x <= qjones; x++) {
    var img = document.getElementById("movie" + x);
    img.src = "/static/img/movie-camera-black.png"
    }
});

    