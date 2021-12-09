$(document).ready(function () {
    console.log(URL)

    $("#add_task").submit(function (event) {
        event.preventDefault()

        $.ajax({
            type: "POST",
            dataType: "json",
            url: URL,
            data: {
                "title": $("#title").val(),
                "category": $("#category").val(),
                "priority": $("#priority").val(),
                "deadLine": $("#deadLine").val(),
                "description": $("#description").val(),
                'csrfmiddlewaretoken':CSRF_TOKEN,
            },
            success: function (data) {
                console.log(data)
            },
            fail: function (a) {
                alert("fail!!!")
            }
        });
    });
});