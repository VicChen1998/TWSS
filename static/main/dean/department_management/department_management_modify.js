$(document).ready(function () {

    toCenter();

    $('.blur_area').css('filter', 'blur(10px)');

    $('.add_cross').click(function () {
        $('.blur_area').css('filter', 'none');
        $('.add_popup').hide();
    });

    $('.add_cancel').click(function () {
        $('.blur_area').css('filter', 'none');
        $('.add_popup').hide();
    });

    $('.add_submit').click(function () {
        var form = $('#department_management_add_form');
        form.ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('连接服务器失败');
            }
        });
    });


});