
 // $( window ).scroll(function(){
 // 	$('.navbar').sticky();
 // });


// $('.navbar').sticky({topSpacing:0}); 

// $('.navbar').on('sticky-start', function() { 
// 	$( this ).css("transition", "1s");
// });

// $(window).resize (function() { 
// 	$( '.navbar' ).css("transition", "0s");
// 	; });



var selector = '.nav li';

$(selector).on('click', function(){
    $(selector).removeClass('active');
    $(this).addClass('active');
});

var options = {
    offset: 350,
    classes: {
        clone:   'banner--clone',
        stick:   'banner--stick',
        unstick: 'banner--unstick'
    }
};

// Initialise with options
var banner = new Headhesive('.banner', options);

/**
 * Need to use the JS version, rather than the data-* attributes.
 */
$('.navbar-toggle').on('click', function () {
    $('.collapse').collapse('toggle');
});

$('.covervid-video').coverVid(1920, 1080);

// $('#carousel-example-generic').carousel();


