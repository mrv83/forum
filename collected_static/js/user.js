/**
 * Created with PyCharm.
 * User: Администратор
 * Date: 22.01.14
 * Time: 13:01
 * To change this template use File | Settings | File Templates.
 */

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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        var csrftoken = getCookie('csrftoken');
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



$(document).ready(function(){

    function changerowcount() {
        var h = document.documentElement.clientHeight
        var r = (h - 310 - (h - 310)%21)/21-1;
        $("#chat_messages").attr('rows', r);
    }

    $("#chat_messages").rowIndex[3].fo

    changerowcount();

    $( window ).resize(function(){
        changerowcount()
})



    $(".search_option").click(function () {
        $("#select_search").val(this.innerHTML);
    });

    function deleteSELECTEDusers(btn) {
        var new_button = document.createElement("button");
        new_button.setAttribute("class", "btn btn-default btn-sm users_select_button");
        new_button.innerHTML = btn.innerHTML;
        var p = document.createElement("p");
        p.appendChild(new_button);
        document.getElementById("all_people").appendChild(p);
        btn.remove();
        document.getElementById("all_people").refresh();
        $(".users_select_button").unbind();
        $(".users_select_button").bind("click", function () {
            deleteSELECTEDusers(this);
        });
    }

    function deleteSELECTusers(btn) {
        var new_button = document.createElement("button");
        new_button.setAttribute("class", "btn btn-default btn-sm selected_users_button");
        new_button.innerHTML = btn.innerHTML;
        var p = document.createElement("p");
        p.appendChild(new_button);
        document.getElementById("inv_people").appendChild(p);
        btn.remove();
        document.getElementById("all_people").refresh();
        $(".selected_users_button").unbind();
        $(".selected_users_button").bind("click", function () {
            deleteSELECTusers(this);
        });
    }

    $(".selected_users_button").click(function () {
        deleteSELECTEDusers(this);
    });

    $(".users_select_button").click(function () {
        deleteSELECTusers(this);
    });

    $('#chat_message_input').keypress(function(event) {
        if (event.which == 13) {
            event.preventDefault();
            var new_s = $('#chat_message_input').val();
            var s = $("#chat_messages").val();
            s.replace(/^\s*\n/gm);
            var d = new Date();
            var c = $("#current_channel").val();
            var posting = $.post("/chat/add/", {dt: d, st: new_s, cn: c },
            function(data) {
                var date = "["+d.getHours()+":"+ d.getMinutes()+":"+ d.getMinutes()+"] ";
                var username = $("#current_username").val();
                if (s != "") {
                    $("#chat_messages").val(s + "\n" + date+username+": "+new_s);
                }
                else $("#chat_messages").val(date+username+": "+new_s);
                $('#chat_message_input').val("");
            });
        }

    })

});