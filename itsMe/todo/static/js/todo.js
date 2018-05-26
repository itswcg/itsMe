$(function () {
    $("main").on("mouseenter", "ul.list-group > li", function (event) {
        var li = $(this);
        $(li).children('.remove-todo').show();
    });


    $("main").on("mouseleave", 'ul.list-group > li', function (event) {
        var li = $(this);
        $(li).children('.remove-todo').hide();
    });

    $('ul.list-group').on('click', '.remove-todo', function () {
        var li = $(this).closest('li');
        var todo = $(li).attr('todo-id');
        $.ajax({
            url: '/todo/del/',
            data: {
                'todo-id': todo
            },
            type: 'get',
            cache: false,
            success: function (data) {
                $(li).fadeOut(400, function () {
                    $(li).remove();
                });

            }
        });
    });

});
