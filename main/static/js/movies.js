
$('.revealmovie').click(function(e) {
    e.preventDefault();
    $('.movie-details').fadeOut('fast')
    if ($(this).next().is(":visible")) {
        $(this).next().fadeOut('fast')
    } else {
        $(this).next().fadeIn('fast')
    }
});


$('.backdrop').click(function(e) {
    $('.movie-details').fadeOut()
    e.stopPropagation();
});


$('.movie-details-inner').click(function(e) {
    $('.movie-details').fadeOut('fast')
});


$(document).ready(function(){
    $('[data-title="show-title"]').tooltip
});
