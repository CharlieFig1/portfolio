$('body').scrollspy({
    target: '.bs-docs-sidebar',
    offset: 40
});

$( ".clip" ).click(function() {
  $(this).addClass("selected");
});

var clipboard = new Clipboard('.btn');
    clipboard.on('success', function(e) {
      console.log(e);
      $('.selected').attr('title', 'Success!').tooltip('fixTitle').tooltip('show');
      $( ".clip" ).removeClass("selected");
    });
    clipboard.on('error', function(e) {
        console.log(e);
        $('.selected').attr('title', 'Press ⌘-C to Copy').tooltip('fixTitle').tooltip('show');
        $( ".clip" ).removeClass("selected");
    })

$( "#alert" ).click(function() {
  alert( "Handler for .click() called." );
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})


$( "#clickme" ).click(function() {
  $( "#book" ).slideDown( "slow", function() {
    // Animation complete.
  });
});
// end slide down


$(document).ready(function(){
$(".answer").hide(); 
$("h3.reveal").click(function(){
    $(this).toggleClass("active").next().slideToggle("fast");

});
 $("a[href='" + window.location.hash + "']").parent(".reveal").click();
});