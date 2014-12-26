$(document).ready(function() {
    $('h3').click(function() {
        var id;

        id = $(this).attr('id');

        $('#code_' + id).toggleClass('hidden');
    });
});
