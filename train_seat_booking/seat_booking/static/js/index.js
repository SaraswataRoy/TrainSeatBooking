$(document).ready(function ()
{
    sessionStorage.clear();
    sessionStorage.setItem("available_seats", "1-D, 1-E, 1-F, 1-G, 2-C, 2-D, 2-E, 2-F, 2-G, 3-E, 3-F, 3-G, 4-B, 4-C, 4-D, 4-E, 4-F, 4-G, 5-A, 5-B, 5-C, 5-D, 5-E, 5-F, 5-G, 6-A, 6-B, 6-C, 6-D, 6-E, 6-F, 6-G, 7-A, 7-B, 7-C, 7-D, 7-E, 7-F, 7-G, 8-A, 8-B, 8-C");
    sessionStorage.setItem("booked_seats", "1-A, 1-B, 1-C, 2-A, 2-B, 3-A, 3-B, 3-C, 3-D, 4-A");
    $(".New_books").hide();
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    targetURL = encodeURI(window.location.href + '/book_seats')
    document.getElementById("available_data").innerHTML = sessionStorage.getItem('available_seats')
    document.getElementById("already_booked").innerHTML = sessionStorage.getItem('booked_seats')
    $('#book').click(function(){
        session_data = {
            'seats': document.getElementById("seats").value,
            'available_seats': sessionStorage.getItem('available_seats'),
            'booked_seats': sessionStorage.getItem('booked_seats'),
        }

        console.dir(seats)
        $.ajax({
            url: targetURL,
            type: 'POST',
            data: session_data, 
        })
        .done(function(data){
            sessionStorage.setItem('available_seats', data.available_seats)
            document.getElementById("available_data").innerHTML = data.available_seats
            document.getElementById("already_booked").innerHTML = sessionStorage.getItem('booked_seats')
            document.getElementById("newly_booked").innerHTML = data.booked_seats
            $(".New_books").show();
            sessionStorage.setItem('booked_seats', sessionStorage.getItem('booked_seats')+', '+data.booked_seats)
        })
    })
})