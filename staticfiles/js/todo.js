$(function () {
    $("main").on("mouseenter", 'ul.list-group > li', function (event) {
        var li = $(this);
        $(li).children('.remove-todo').show();
    });

    $("main").on("mouseleave", 'ul.list-group > li', function (event) {
        var li = $(this);
        $(li).children('.list-group-item').children('.remove-todo').hide();
    });
});
