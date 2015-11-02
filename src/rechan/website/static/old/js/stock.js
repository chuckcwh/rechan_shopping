$(document).ready(function() {

    function show_stock (category){
        $.ajax({
            url: "../get_stock/" + category,
            type: "GET",
            dataType: "json",
            success: function(data){
                $('#stock_show').html("");
                for (i=0, j=data.length; i<j; i++) {
                    $('#stock_show').append("<tr>" +
                        "<th>" + data[i].name + "</th>" +
                        "<th>" + data[i].have + "</th>" +
                        "<th>" + data[i].discount + "</th>" +
                        "<th>" + "<a href='" + data[i].id + "'> more </a>" + "</th>" +
                        "</tr>");
                }
            }
        })
    }


    $('input[type="radio"]').click(function(){
        var choice = $(this).attr("value");
        show_stock(choice);
    });

});