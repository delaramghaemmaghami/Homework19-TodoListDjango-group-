$(document).ready(function () {  //creates an API for add_task.html
    $("#add_task").submit(function (event) {  //add_task is the ID of form in add_task.html
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