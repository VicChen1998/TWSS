$(document).ready(function () {

    $('tr:even').addClass('even');

    $('.audit_reject').hover(
        function () {
            $(this).children().show();
        },
        function () {
            $(this).children().hide();
        }
    );

    $('.add_button').click(function () {
        MyAjax_Get('getpage', 'workload_input_theory_course_add', null, '.theory_course_add_content')
    });

    $('.theory_course_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_theory_course_add', id, '.theory_course_add_content')

    });

    $('.theory_course_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var location = $('#location_year').val() + ',' + $('#location_semester').val();
        if (confirm("确认删除？"))
            MyAjax_Get('/upload', 'theory_course_delete', id, null, location);
    });

    $('.search_button').click(function () {
        $('#theory_course_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error!');
            }
        })
    });

});