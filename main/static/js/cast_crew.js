// Pulls in all the camera-icon images in a loop
// TODO: Tie each icon to a specific movie
var cameraSet = document.getElementById('camera-set');

for (var x = 1; x <= 88; x++) {
    var img = document.createElement('IMG');
    img.id = 'movie' + x;
    img.src = '/static/img/movie-camera-off-white.png';
    cameraSet.appendChild(img);
};

var highlighted = false;

// Puts reset of the full icon set into one callable place;
// no, magic numbers are not ideal
var reset = function() {
    for (var x = 1; x <= 88; x++) {
        var img = document.getElementById('movie' + x);
        img.style.display = 'inline';
        img.src = '/static/img/movie-camera-off-white.png';
    };
    highlighted = false;
};

var currentID = ""
var currentCrewID = ""
var workerLinks = document.getElementsByClassName('crew-name')

// This event listener gets more complicated the more complex the page gets.
// There's a better way to do this. Ripe for refactoring.
for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('click', function(e) {
        e.preventDefault();

        // Hits the ID for the contextual data and sets its state
        var select = this.id + '-context'
        if(document.getElementById(select).style.display == 'inline') {
            document.getElementById(select).style.display = 'none'
        } else {
            document.getElementById(select).style.display = 'inline'
        };

        // resets the name class and the icon set on a click on another name
        if(currentID != '' && currentID != this.id) {
            document.getElementById(currentID).className = 'crew-name';
            reset();
        };

        currentID = this.id;

        // resets the name class on a second click on the same name
        if(currentCrewID != '' && currentCrewID != select) {
            document.getElementById(currentCrewID).style.display = 'none'
            reset();
        };

        currentCrewID = select

        // resets the icon set on a second click on the same name
        if (highlighted) {
            this.className = 'crew-name'
            reset();
            return;
        }

        // switches name class on first click for highlighting
        // and displays the the correct number of icons;
        // someday I'll figure out why number + 1 didn't work
        // but number - -1 did.
        highlighted = true;
        this.className = 'crew-name-black'
        var number = this.getAttribute('data-number');
        for(var x = 88; x >= number - -1; x--) {
        var img = document.getElementById('movie' + x)
        img.style.display = 'none';
        // img.src = "/static/img/movie-camera-red.png"
        }
    })
};


// makes sure none of the names have been clicked for mouse event;
// highlights the correct number of images in the full set for each name hovered
for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('mouseenter', function(e) {
        if (document.getElementsByClassName('crew-name-black').length == 0) {
            var cameras = this.getAttribute('data-number');
            for (var x = 1; x <= cameras; x++) {
                var img = document.getElementById('movie' + x)
                img.src = '/static/img/movie-camera-red.png';
            }
        };
    })
};

// YAY FOR MOSTLY REPEATING MYSELF
// refactoring will be fun oh so much fun oh baby
for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('mouseout', function(e) {
        // if (document.getElementsByClassName('crew-name-black').length == 0) {
            var cameras = this.getAttribute('data-number');
            for (var x = 1; x <= cameras; x++) {
                var img = document.getElementById('movie' + x)
                img.src = '/static/img/movie-camera-off-white.png';
            // }
        };
    })
};


// SPEAKING OF REPEATING MYSELF:
// adds the same behavior to the cast page, which has different IDs
// in part because its size-related CSS rules are a bit different;
// Not great, Bob!
var workerLinks = document.getElementsByClassName('cast-name')

for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('click', function(e) {
        e.preventDefault();

        if(currentID != '' && currentID != this.id) {
            document.getElementById(currentID).className = 'cast-name'
            reset()
        }

        currentID = this.id
        var select = this.id + '-context'
        if(document.getElementById(select).style.display == 'inline') {
            document.getElementById(select).style.display = 'none'
        } else {
            document.getElementById(select).style.display = 'inline'
        }

        if(currentID != '' && currentID != this.id) {
            document.getElementById(currentID).className = 'cast-name'
            reset()
        }

        currentID = this.id

        if(currentCrewID != '' && currentCrewID != select) {
            document.getElementById(currentCrewID).style.display = 'none'
            reset()
        }

        currentCrewID = select

        if (highlighted) {
            this.className = 'cast-name'
            reset();
            return;
        }

        highlighted = true;
        this.className = 'cast-name-black'
        var number = this.getAttribute('data-number');
        for(var x = 1; x <= number; x++) {
          var img = document.getElementById('movie' + x).style.display = 'none';
          // img.src = "/static/img/movie-camera-black.png"
        }
    })
};


for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('mouseenter', function(e) {
        if (document.getElementsByClassName('crew-name-black').length == 0) {

            var cameras = 88 - this.getAttribute('data-number');
            for (var x = 1; x <= cameras; x++) {
                var img = document.getElementById('movie' + x)
                img.src = '/static/img/movie-camera-red.png';
            }
        };
    })
};

for(var i = 0; i < workerLinks.length; i++) {
    workerLinks[i].addEventListener('mouseout', function(e) {
        if (this.className == 'cast-name') {
            var cameras = 88 - this.getAttribute('data-number');
            for (var x = 1; x <= cameras; x++) {
                var img = document.getElementById('movie' + x)
                img.src = '/static/img/movie-camera-off-white.png';
            }
        };
    })
};


// var workerLinks = document.getElementsByClassName("coworker-of-note")
// // debugger
// for(var i = 0; i < workerLinks.length; i++) {
//     workerLinks[i].addEventListener('click', function(e) {
//         e.preventDefault();
//         // debugger

//         if(currentID != '' && currentID != this.id) {
//             document.getElementById(currentID).className = 'coworker-of-note'
//             reset()
//         }

//         currentID = this.id

//         if (highlighted) {
//             this.className = 'coworker-of-note'
//             reset();
//             return;
//         }

//         highlighted = true;
//         this.className = 'of-note-black'
//         var number = this.getAttribute("data-number");
//         for(var x = 1; x <= number; x++) {
//           var img = document.getElementById("movie" + x).style.display = 'none';
//           // img.src = "/static/img/movie-camera-black.png"
//         }
//     })
// };
// $(document).ready(function() )
// var makeNarrow = function() {
//   var width = $(window).width()
//   if (width < 799 && width > 420) {
//     $('.crew-coworkers').removeClass('crew-coworkers').addClass('crew-coworkers-narrow');
//     } else {
//       $('.crew-coworkers-narrow').removeClass('crew-coworkers-narrow').addClass('crew-coworkers');
//     }
//   };
//   $(window).resize(makeNarrow());
