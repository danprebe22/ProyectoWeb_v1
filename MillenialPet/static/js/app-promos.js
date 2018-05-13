
$(document).ready(function(){
	$('.modal').modal();
	$('.sidenav').sidenav();
	$('.tap-target').tapTarget();
	$('.parallax').parallax();
	$('.slider').slider();
	$('.carousel').carousel();
	
	 $('.carousel.carousel-slider').carousel({
    fullWidth: true
    
  });
	

});


function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

$(document).ready(function(){
    $('.collapsible').collapsible();
     $('.materialboxed').materialbox();
  });

