var cameraSet = document.getElementById('camera-set');

for (var x = 1; x <= 88; x++) {

    var img = document.createElement('IMG');
    img.id = "movie" + x
    img.src = "/static/img/movie-camera-off-white.png";
    cameraSet.appendChild(img);
}


var highlighted = false


var reset = function() {
    for (var x = 1; x <= 88; x++) {
        var img = document.getElementById("movie" + x);
        img.src = "/static/img/movie-camera-off-white.png";
    }

    highlighted = false;
    
}


var currentID = ""
var currentCrewID = ""

var workerLinks = document.getElementsByClassName("crew-name")
// var workerDetails = document.getElementsByClassName("crew")

// debugger
for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('click', function(e) {
        e.preventDefault();
        // console.log(this.id)
        // debugger
        var sel = this.id + '-context'
        if(document.getElementById(sel).style.display == 'inline') {
            document.getElementById(sel).style.display = 'none'
        } else {
            document.getElementById(sel).style.display = 'inline'
        }

        if(currentID != '' && currentID != this.id) {
            document.getElementById(currentID).className = 'crew-name'
            reset()
        }

        currentID = this.id

        if(currentCrewID != '' && currentCrewID != sel) {
            document.getElementById(currentCrewID).style.display = 'none'
            reset()
        }

        currentCrewID = sel

        if (highlighted) {
            this.className = 'crew-name'
            reset();
            return;
        }

        highlighted = true;
        this.className = 'crew-name-black'
        var number = this.getAttribute("data-number");
        for(var x = 1; x <= number; x++) {
          var img = document.getElementById("movie" + x);
          img.src = "/static/img/movie-camera-black.png"
        }
    })
};


var workerLinks = document.getElementsByClassName("cast-name")

for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('click', function(e) {
        e.preventDefault();

        if(currentID != '' && currentID != this.id) {
            document.getElementById(currentID).className = 'cast-name'
            reset()
        }

        currentID = this.id
        var sel = this.id + '-context'
        if(document.getElementById(sel).style.display == 'inline') {
            document.getElementById(sel).style.display = 'none'
        } else {
            document.getElementById(sel).style.display = 'inline'
        }

        if(currentID != '' && currentID != this.id) {
            document.getElementById(currentID).className = 'cast-name'
            reset()
        }

        currentID = this.id

        if(currentCrewID != '' && currentCrewID != sel) {
            document.getElementById(currentCrewID).style.display = 'none'
            reset()
        }

        currentCrewID = sel

        if (highlighted) {
            this.className = 'cast-name'
            reset();
            return;
        }

        highlighted = true;
        this.className = 'cast-name-black'
        var number = this.getAttribute("data-number");
        for(var x = 1; x <= number; x++) {
          var img = document.getElementById("movie" + x);
          img.src = "/static/img/movie-camera-black.png"
        }
    })
};


var workerLinks = document.getElementsByClassName("coworker-of-note")
// debugger
for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('click', function(e) {
        e.preventDefault();
        // debugger

        if(currentID != '' && currentID != this.id) {
            document.getElementById(currentID).className = 'coworker-of-note'
            reset()
        }

        currentID = this.id

        if (highlighted) {
            this.className = 'coworker-of-note'
            reset();
            return;
        }

        highlighted = true;
        this.className = 'of-note-black'
        var number = this.getAttribute("data-number");
        for(var x = 1; x <= number; x++) {
          var img = document.getElementById("movie" + x);
          img.src = "/static/img/movie-camera-black.png"
        }
    })
};



