$(function() {
    $( "#create_task_dialog" ).dialog({
        autoOpen: false,

    });

    $( "#create_task" ).click(function() {
        $( "#create_task_dialog" ).dialog( "open" );
        return false;
    });

    $('.slider')._TMS({
        show:0,
        pauseOnHover:true,
        prevBu:false,
        nextBu:false,
        playBu:false,
        duration:800,
        preset:'fade',
        pagination:true,
        pagNums:false,
        slideshow:7000,
        numStatus:false,
        banners:'fade',
        waitBannerAnimation:false,
        progressBar:false
    })

});