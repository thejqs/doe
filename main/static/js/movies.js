
$('.revealmovie').click(function(e) {
    // debugger
    e.preventDefault();
    e.stopPropagation();
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


$('.timeline').click(function(e) {
        $('.movie-details').fadeOut('fast')
});


$(document).ready(function(){
    $('[data-title="show-title"]').tooltip
});
