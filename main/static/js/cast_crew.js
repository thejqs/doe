var cameraSet = document.getElementById('camera-set');

for (var x = 1; x <= 88; x++) {

    var img = document.createElement('IMG');
    img.id = "movie" + x
    img.src = "/static/img/movie-camera-gray.png";
    cameraSet.appendChild(img);
}


var highlighted = false


var reset = function() {
    for (var x = 1; x <= 88; x++) {
        var img = document.getElementById("movie" + x);
        img.src = "/static/img/movie-camera-gray.png";
    }

    highlighted = false;
    
}


var workerLinks = document.getElementsByClassName("crew-name")
// debugger
for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('click', function(e) {
        e.preventDefault();
        // debugger
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

