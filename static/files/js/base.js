$(document).ready(function(){
    
    // 'a' tag
    $('a').mouseenter(function(){
        $(this).css({
            'box-shadow':'0px 0px 15px 1px #35474b',
            'border-radius': '5px'
        });
    });
    $('a').mouseleave(function(){
        $(this).css({'box-shadow':''});
    });

    // 'shadow' tag
    $('.shadow').mouseenter(function(){
        $(this).css({'box-shadow':'0px 0px 15px 1px #35474b'});
    });
    $('.shadow').mouseleave(function(){
        $(this).css({'box-shadow':'1px 1px 5px 0.5px #35474b'});
    });

    $('#menu').click(function(){
        $('#footer').fadeToggle(500);
    });
});