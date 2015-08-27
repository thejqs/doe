// var cameraSet = document.getElementById('camera-set');

// for (var x = 1; x <= 88; x++) {

//     var img = document.createElement('IMG');
//     img.id = "movie" + x
//     img.src = "/static/img/movie-camera-gray.png";
//     cameraSet.appendChild(img);
// }



$('.revealmovie').click(function(e) {
    e.preventDefault();
    $('.movie-details').fadeOut()
    if ($(this).next().is(":visible")) {
        $(this).next().fadeOut()
    } else {
        $(this).next().fadeIn()
    }
});

$('.backdrop').click(function(e) {
    $('.movie-details').fadeOut()
    e.stopPropagation();
});


// $('.movie-camera').on({
//     'click': function() {
//         $('.movie-camera').attr('src', "/static/img/movie-camera-black.png" );
//     }
// });

// var src = $('.camera-gray'[alt="A pictogram icon of a movie camera"]).attr('src');
// var fresholtz = 46
// var wallin = 30
// var minkler = 23
// var lane = 12
// var frankovich = 12
// var jones = 12
// var gaspar = 12
// var tyler = 11
// var pollack = 6
// var grusin = 8
// var brooks = 2
// var qjones = 6
// var bernstein = 6
// var morricone = 1

// var highlighted = false

// var reset = function() {
//     for (var x = 1; x <= 88; x++) {
//         var img = document.getElementById("movie" + x);
//         img.src = "/static/img/movie-camera-gray.png";
//     }

//     highlighted = false;
    
// }


// var fresholtzBtn = document.getElementById("fresholtz");
// fresholtzBtn.addEventListener('click', function(e) {
//     e.preventDefault();

//     if (highlighted) {
//         reset();
//         return;
//     }

//     highlighted = true;
//     for ( var x = 1; x <= fresholtz; x++) {
//     var img = document.getElementById("movie" + x);
//     img.src = "/static/img/movie-camera-black.png"
//     }
// });



// for(var i = 0; i <= frankovich; i++) {
//     $('.movie-camera').on({
//         'click': function(i) {
//             $('.movie-camera').attr('src', "/static/img/movie-camera-black.png" );
//         }
//     });
// };
