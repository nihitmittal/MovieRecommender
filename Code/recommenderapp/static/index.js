$(document).ready(function () {

    $(function () {
        $("#searchBox").autocomplete({
            source: function (request, response) {
                $.ajax({
                    type: "POST",
                    url: "http://localhost:5000/search",
                    dataType: "json",
                    cache: false,
                    data: {
                        q: request.term
                    },
                    success: function (data) {
                        //alert(data);
                        // console.log(data);
                        response(data);
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        console.log(textStatus + " " + errorThrown);
                    }
                });
            },
            select: function (event, ui) {
                var ulList = $('#selectedMovies');
                var li = $('<li/>').text(ui.item.value).appendTo(ulList);
                $('#searchBox').val("");
                return false;
            },
            minLength: 2
        });
    });

    $("#predict").click( function(){
        var movie_list = []

        $('#selectedMovies li').each( function () {
            movie_list.push($(this).text());
        });

        var movies = {"movie_list": movie_list};

        $.ajax({
            type: "POST",
            url: "/predict",
            dataType: "json",
            contentType: "application/json;charset=UTF-8",
            traditional: "true",
            cache: false,
            data: JSON.stringify(movies),
            success: function (response) {
                var ulList = $('#predictedMovies');
                var i = 0;
                response['recommendations'].forEach(element => {
                    var diventry = $('<div/>');
                    var fieldset = $('<fieldset/>', {id:i}).css("border",'0');
                    var li = $('<li/>').text(element);
                    var radios = $("<label class='radio-inline'><input type='radio' name="+i+" value=1>Dislike</label> \
                    <label class='radio-inline'><input type='radio' name="+i+" value=2>Yet to watch</label> \
                    <label class='radio-inline'><input type='radio' name="+i+" value=3>Like</label><br/><br/>");
                    diventry.append(li);
                    diventry.append(radios);
                    fieldset.append(diventry);
                    ulList.append(fieldset);
                    i+=1;
                });

                // var li = $('<li/>').text()
                console.log("->", response['recommendations']);
            },
            error: function (error) {
                console.log("ERROR ->" + error );
            }
        });
    });

    $('#feedback').click(function(){
        var myForm = $('fieldset');
        var data = {};
        var labels = {
            1: 'Dislike',
            2: 'Yet to watch',
            3: 'Like'
        };
        for(var i=0;i<myForm.length;i++){
            var input = $('#'+i).find('div').find('input:checked')[0].value;
            var movieName = $('#'+i).find('div').find('li')[0].innerText;
            data[movieName]=labels[input];
        }
        console.log(data);

        $.ajax({
            type: "POST",
            url: "/feedback",
            dataType: "json",
            contentType: "application/json;charset=UTF-8",
            traditional: "true",
            cache: false,
            data: JSON.stringify(data),
            success: function (response) {
                // console.log("->", response);
                // $("#dataCollected").css("display", "block");
                window.location.href="/success";
            },
            error: function (error) {
                console.log("ERROR ->" + error );
            }
        });

    });


});

console.log("Hello World!!!")
