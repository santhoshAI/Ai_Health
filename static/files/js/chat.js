// chat
$(document).ready(function(){

    // auto scrolling to Bottom.
    $('#box').animate({
        scrollTop: $('#box').get(0).scrollHeight
    }, 0);

    $("#chatinput").on("submit", function(event){
       
        var input = $("#input").val();
        var user = '<div class="user" ><div class="chatlogo">👤</div><div>'+input+'</div></div>'

        $("#box").append(user);
        $("#input").val("");
        $("#box").animate({
            scrollTop: $('#box').get(0).scrollHeight
        }, 1500);
        
        $.ajax({
            data:{
                msg: input,
            },
            type: "POST",
            url: "/get",
        }).done(function(Data){
            var bot = '<div class="bot"><div class="chatlogo">🤖</div><div>'+Data+'</div></div>'

            $("#box").append(bot);

            $("#box").animate({
                scrollTop: $('#box').get(0).scrollHeight
            }, 1500);
        })




        event.preventDefault();
    });

});