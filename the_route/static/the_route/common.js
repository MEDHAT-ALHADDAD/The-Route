;
(function ($) {
    "use strict";
    
    $( ".datepicker" ).datepicker();
    /*========
     * Location Map
     */
    
    
    
    
    $('#dl-menu').dlmenu();


    $('.nav-tabs a').on('click', function () {
        $($(this).attr('href')).parent().children(".tab-pane").removeClass("active");

        $($(this).attr('href')).addClass('active');
    });
    var loginform = $(".login_form");
    var userlogin = $(".user_login");
    var userregister = $(".user_register");
// Plugin options and our code
    loginform.leanModal({
        top: 50,
        overlay: 0.6,
        closeButton: ".modal_close"
    });
// Calling Login Form


    // Calling Login Form
    loginform.on('click', function () {
        userregister.hide();
        userlogin.show();
        return false;
    });

    // Calling Register Form
    $(".register_form").on('click', function () {
        userlogin.hide();
        userregister.show();
        $(".header_title").text('Register');
        return false;
    });


    /*==================================
     Social Information add new row
     */
    $(".social-information").on('click','.trash', function () {

         $(this).closest('.form-group').remove();
        return false;
    });

    $(".add-row").on('click', function () {

        var markup = '<div class="form-group row"><div class="col-5"><select class="form-control border-top-0 border-left-0 border-right-0 rounded-0" id="inlineFormCustomSelect"><option value="1">Twitter</option><option value="2">Facebook</option><option value="3">Pinterest</option><option value="3">Tumblr</option></select></div><div class="col-6"><input class="form-control border-top-0 border-left-0 border-right-0 rounded-0" placeholder="Enter url..." type="text" value="" id="example-text-input"></div><div class="col-1"><a href="#" class="btn btn-primary trash"><i class="fa fa-trash  lis-f-14"></i></a></div></div>';
        $(".social-information").append(markup);
        return false;
    });
  $(".add-date").on('click', function () {

        var markup = '<div class="form-group row"> <div class="col-12 col-md-4"> <input type="text" class="form-control border-top-0 border-left-0 border-right-0 rounded-0 datepicker" placeholder="Date" > </div><div class="col-12 col-md-4"> <select class="form-control border-top-0 border-left-0 border-right-0 rounded-0" id="inlineFormCustomSelect"> <option value="1">10:00 am</option> <option value="1">11:00 am</option> <option value="1">12:00 am</option> <option value="1">1:00 pm</option> <option value="1">2:00 pm</option> <option value="1">3:00 pm</option> <option value="1">4:00 pm</option> <option value="1">5:00 pm</option> <option value="1">6:00 pm</option> </select> </div><div class="col-12 col-md-4"> <select class="form-control border-top-0 border-left-0 border-right-0 rounded-0" id="inlineFormCustomSelect"> <option value="1">10:00 am</option> <option value="1">11:00 am</option> <option value="1">12:00 am</option> <option value="1">1:00 pm</option> <option value="1">2:00 pm</option> <option value="1">3:00 pm</option> <option value="1">4:00 pm</option> <option value="1">5:00 pm</option> <option value="1">6:00 pm</option> </select> </div></div>';
        $(".event-information").append(markup);
        return false;
    });
     $(".event-information").on('click','.datepicker', function () {

           $( this ).datepicker();
        return false;
    });
    /*==============================================================
     Countdown
     =============================================================*/
    function getTimeRemaining(endtime) {
        var t = Date.parse(endtime) - Date.parse(new Date());
        var seconds = Math.floor((t / 1000) % 60);
        var minutes = Math.floor((t / 1000 / 60) % 60);
        var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
        var days = Math.floor(t / (1000 * 60 * 60 * 24));
        return {
            'total': t,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        };
    }

    function initializeClock(id, endtime) {
        var clock = document.getElementById(id);
        var daysSpan = clock.querySelector('.days');
        var hoursSpan = clock.querySelector('.hours');
        var minutesSpan = clock.querySelector('.minutes');
        var secondsSpan = clock.querySelector('.seconds');

        function updateClock() {
            var t = getTimeRemaining(endtime);

            daysSpan.innerHTML = t.days;
            hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
            minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
            secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

            if (t.total <= 0) {
                clearInterval(timeinterval);
            }
        }

        updateClock();
        var timeinterval = setInterval(updateClock, 1000);
    }

    var deadline = new Date(Date.parse(new Date()) + 28 * 11 * 28 * 60 * 1000);
    if ($('#clockdiv').length) {
        initializeClock('clockdiv', deadline);
    }


    /*==============================================================
     Background Image Maker
     =============================================================*/

    $('.background-image-maker').each(function () {
        var imgURL = $(this).next('.holder-image').find('img').attr('src');
        $(this).css('background-image', 'url(' + imgURL + ')');
    });


    /*==============================================================
     Animates
     =============================================================*/
    new WOW().init();

    /*==============================================================
     Slick Procuct Slider 1
     =============================================================*/
    $('.center').slick({
        centerMode: true,
        centerPadding: '150px',
        slidesToShow: 3,
        arrows: true,
        autoplay: false,
        responsive: [
            {
                breakpoint: 1199,
                settings: {
                    arrows: true,
                    centerMode: true,
                    centerPadding: '150px',
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 767,
                settings: {
                    arrows: true,
                    centerMode: true,
                    centerPadding: '0px',
                    slidesToShow: 1
                }
            }
        ]
    });

    /*==============================================================
     Slick Procuct Slider 2
     =============================================================*/
    $('.center2').slick({
        centerMode: true,
        centerPadding: '150px',
        slidesToShow: 3,
        arrows: false,
        autoplay: true,
        responsive: [
            {
                breakpoint: 1199,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '150px',
                    slidesToShow: 1
                }
            },
            {
                breakpoint: 767,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '0px',
                    slidesToShow: 1
                }
            }
        ]
    });

    /*==============================================================
     Slick Procuct Slider 3
     =============================================================*/
    $('.center3').slick({
        centerMode: true,
        centerPadding: '0px',
        slidesToShow: 3,
        arrows: false,
        autoplay: true,
        responsive: [
            {
                breakpoint: 1199,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '0px',
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 767,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '0px',
                    slidesToShow: 1
                }
            }
        ]
    });




    var $container = $('.portfolio-box2');
    $container.imagesLoaded(function () {
        $container.masonry({
            columnWidth: '.post',
            itemSelector: '.post'
        });
    });

    //Reinitialize masonry inside each panel after the relative tab link is clicked - 
    $('a[data-toggle=tab]').each(function () {
        var $this = $(this);
        $this.on('shown.bs.tab', function () {
            $container.masonry({
                columnWidth: '.post',
                itemSelector: '.post'
            });
        }); //end shown
    });  //end each


    /*==============================================================
     Testimonial Slider
     =============================================================*/

    $("#testimonial").owlCarousel({
        items: 1,
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [979, 1],
        itemsTablet: [768, 1],
        pagination: false,
        navigation: false,
        autoPlay: true
    });


    /*==============================================================
     Back To Top
     =============================================================*/


    $('.scrollup').on('click', function () {
        $("html, body").animate({
            scrollTop: 0
        }, 600);
        return false;
    });




    /*==============================================================
     flexslider Blog Page Item
     =============================================================*/
    $(window).on('load', function () {
        $('.portfolio-box').masonry({
            // options
            itemSelector: '.post'
        });

        $('#carousel').flexslider({
            animation: "slide",
            controlNav: false,
            animationLoop: false,
            slideshow: false,
            itemWidth: 200,
            itemMargin: 20,
            asNavFor: '#slider'
        });

        $('#slider').flexslider({
            animation: "slide",
            controlNav: false,
            animationLoop: false,
            slideshow: false,
            sync: "#carousel",
            start: function (slider) {
                $('body').removeClass('loading');
            }
        });
    });
    /*==============================================================
     Image Lightbox Gallery
     =============================================================*/
    $(document).on('click', '[data-toggle="lightbox"]', function (event) {
        event.preventDefault();
        $(this).ekkoLightbox();
    });
    /*==============================================================
     Range Slider 1
     =============================================================*/
// Without JQuery
    var mySlider = $("#ex6").bootstrapSlider();

    $('#ex6').slider().on('slide', function (value) {
        $("#ex6SliderVal").html($('#ex6').val());
    });
    /*==============================================================
     Range Slider 2
     =============================================================*/

// Without JQuery
    var mySlider = $("#ex7").bootstrapSlider();
    $('#ex7').slider().on('slide', function () {
        $("#ex7SliderVal").html($('#ex7').val());
    });

    /*==============================================================
     Range Slider 1
     =============================================================*/
// Without JQuery
    var mySlider = $("#ex8").bootstrapSlider();

    $('#ex8').slider().on('slide', function (value) {
        $("#ex8SliderVal").html($('#ex8').val());
    });

    /*==============================================================
     Header Fixed Scroll
     =============================================================*/
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }

        var fixheader = $("#header-fix");
        var spmenu = $("#cbp-spmenu-s1");
        var scroll = $(window).scrollTop();
        if (scroll >= 80) {
            fixheader.addClass("nav-affix");
            spmenu.addClass("nav-affix");
        } else {
            fixheader.removeClass("nav-affix");
            spmenu.removeClass("nav-affix");
        }
    });




})(jQuery);



