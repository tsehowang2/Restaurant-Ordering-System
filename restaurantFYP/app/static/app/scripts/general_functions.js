function check_bill(token) {
    const g_interval = setInterval(function () {
        $.ajax({
            type: 'POST',
            url: '/force_logout',
            data: {
                csrfmiddlewaretoken: token,
            },
            success: function (data) {
                if (data == 'false') {
                    window.location.href = '/logout';
                }
            }
        });
    }, 5000);

}