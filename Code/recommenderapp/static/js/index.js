$(document).ready(function () {

    $(window).on("load",function(){
        $(".loader-wrapper").fadeOut("slow");
    });

    $('#feedback').prop('disabled', true);
    // $('#success-alert').slideUp();

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
                const ulList = $('#selectedMovies');
                const spanElement = $('<span/>').attr("id", `close-${ui.item.value}`).addClass("close").text('\u00D7').click({
                    id:`${ui.item.value}`,ulList:ulList
                },removeElement)

                const li = $('<li/>').text(`${ui.item.value}`).attr('id',`${ui.item.value}`).append(spanElement).appendTo(ulList);
                $('#searchBox').val("");
                return false;
            },
            minLength: 2
        });
    });

    $("#predict").click( function(){
        const movie_list = []

        $('#selectedMovies li').each( function () {
            movie_list.push($(this).text());
        });

        const movies = {"movie_list": movie_list};

        $('#loader').show()

        $.ajax({
            type: "POST",
            url: "/predict",
            dataType: "json",
            contentType: "application/json;charset=UTF-8",
            traditional: "true",
            cache: false,
            data: JSON.stringify(movies),
            success: function (response) {
                const ulList = $('#predictedMovies');
                let x = 0;
                response['recommendations'].forEach(element => {
                    const diventry = $('<div/>').attr('id', 'div-entry');
                    const divStars = $('<div/>').addClass('stars')
                    const stars = $(`
                        <i class="fa-solid fa-star" id=${x}></i>
                        <i class="fa-solid fa-star" id=${x}></i>
                        <i class="fa-solid fa-star" id=${x}></i>
                        <i class="fa-solid fa-star" id=${x}></i>
                        <i class="fa-solid fa-star" id=${x}></i>
                    `);
                    for(let i = 0; i < stars.length; i += 2) {
                        stars[i].addEventListener('click', (e) => {
                            for(let j = 0; j < stars.length; j += 2) {
                                i >= j ? stars[j].classList.add('active') : stars[j].classList.remove('active')
                            }
                        });
                    }

                    const viewComments = $(`<input type="button" class="btn btn-outline-info" name="view-comments" id=${element} value="View Comments">`);

                    viewComments.click({movieName: element}, (eV) => window.location.href = "/comments/" + eV.data.movieName);

                    const fieldset = $('<fieldset/>', {id:x}).css("border",'0');
                    const li = $('<li/>').text(element);
                    divStars.append(stars);
                    diventry.append(li);
                    diventry.append(divStars);
                    diventry.append(viewComments);
                    fieldset.append(diventry);
                    ulList.append(fieldset);
                    x+=1;
                });
                
                // const li = $('<li/>').text()
                $('#feedback').prop('disabled', false)
                console.log("->", response['recommendations']);
                $('#loader').hide();
            },
            error: function (error) {
                console.log("ERROR ->" + error );
                $('#loader').hide();
            }
            
        });
    });

    $('#feedback').click(function(){
        const myForm = $('fieldset');
        const data = {};
        console.log(myForm, myForm.length)
        for(let i=0;i<myForm.length;i++){
            const input = $(`#${i}`).find('.active').length;
            console.log(input)
            // const input = $('#'+i).find('div').find('input:checked')[0] !== undefined ? $('#'+i).find('div').find('input:checked')[0].value : "Yet to be watched";
            const movieName = $('#'+i).find('div').find('li')[0].innerText;
            data[movieName]=input;
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
                // window.location.href="/success";
            },
            error: function (error) {
                console.log("ERROR ->" + error );
            }
        });
        $('#success-alert').show();
    });
});

const removeElement = (event) => {
    const id = event.data.id
    for (let i=0;i<event.data.ulList[0].children.length;i++) {
        if (event.data.ulList[0].children[i].id === id) {
            event.data.ulList[0].children[i].remove()
            event.data.ulList.splice(i, 1);
        }
    }
}