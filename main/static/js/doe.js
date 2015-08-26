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


$('.movie-camera').on({
    'click': function() {
        $('.movie-camera').attr('src', "/static/img/movie-camera-black.png" );
    }
});

// var src = $('.camera-gray'[alt="A pictogram icon of a movie camera"]).attr('src');