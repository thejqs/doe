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