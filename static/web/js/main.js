;
(function ($) {
    "use strict";

    $(document).ready(function () {

        /**-----------------------------
         *  Navbar fix
         * ---------------------------*/
        $(document).on('click', '.navbar-area .navbar-nav li.menu-item-has-children>a', function (e) {
            e.preventDefault();
        })

        // Mobile Menu
        $(window).resize(function () {
            var click = false;
            var $hasMenu = $('.menu-item-has-children');
            if (window.innerWidth < 991) {
                $($hasMenu).on('click', function (e) {
                    var current = $(this).find(".sub-menu").first();
                    current.toggleClass('active');
                    e.stopPropagation();

                });
                $('.menu-item-has-children > a').on('click', function (e) {
                    if (!$(this).is('.clicked')) {
                        e.preventDefault();
                        $(this).addClass('clicked');
                    }
                });

            }
        });

        /*--------------------
            wow js init
        ---------------------*/
        new WOW().init();

        /*-------------------------
            magnific popup activation
        -------------------------*/
        $('.video-play-btn,.video-popup,.small-vide-play-btn').magnificPopup({
            type: 'video'
        });
        $('.image-popup').magnificPopup({
            type: 'image'
        });
        /*------------------
            back to top
        ------------------*/
        $(document).on('click', '.back-to-top', function () {
            $("html,body").animate({
                scrollTop: 0
            }, 2000);
        });
        /*------------------------------
            counter section activation
        -------------------------------*/
        var counternumber = $('.count-num');
        counternumber.counterUp({
            delay: 20,
            time: 3000
        });
        /*---------------------------
                    Mobile Cross Menu
        -----------------------------*/
        $(document).on('click', '.cross-menu', function (e) {
            e.preventDefault();
            $(this).toggleClass("change");
        })


        /*-------------------------------
            case study filter 
        ---------------------------------*/
        var $caseStudyThreeContainer = $('.case-studies-masonry');
        if ($caseStudyThreeContainer.length > 0) {
            $('.case-studies-masonry').imagesLoaded(function () {
                var caseMasonry = $caseStudyThreeContainer.isotope({
                    itemSelector: '.masonry-item', // use a separate class for itemSelector, other than .col-
                    masonry: {
                        gutter: 0
                    }
                });
                $(document).on('click', '.case-studies-menu li', function () {
                    var filterValue = $(this).attr('data-filter');
                    caseMasonry.isotope({
                        filter: filterValue
                    });
                });
            });
            $(document).on('click', '.case-studies-menu li', function () {
                $(this).siblings().removeClass('active');
                $(this).addClass('active');
            });
        }
        /*-------------------------------
            Portfolio filter 
        ---------------------------------*/
        var $caseContainer = $('.recent-case-filter-02');
        if ($caseContainer.length > 0) {
            $('.recent-case-filter-02').imagesLoaded(function () {
                var festivarMasonry = $caseContainer.isotope({
                    itemSelector: '.case-masonry', // use a separate class for itemSelector, other than .col-
                    masonry: {
                        gutter: 0
                    }
                });
                $(document).on('click', '.recent-case-filter-menu li', function () {
                    var filterValue = $(this).attr('data-filter');
                    festivarMasonry.isotope({
                        filter: filterValue
                    });
                });
            });
            $(document).on('click', '.recent-case-filter-menu li', function () {
                $(this).siblings().removeClass('active');
                $(this).addClass('active');
            });
        }

        /*---------------------------
            Testimonial carousel
        ---------------------------*/
        var $TestimonialCarousel = $('.testimonial-carousel');
        if ($TestimonialCarousel.length > 0) {
            $TestimonialCarousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: true,
                nav: true,
                navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
                animateOut: 'fadeOut',
                animateIn: 'fadeIn',
                responsive: {
                    0: {
                        items: 1
                    },
                    599: {
                        items: 2
                    }
                }
            });
        }



        var $service_carousel = $('.service-carousel');
        if ($service_carousel.length > 0) {
            $service_carousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: true,
                nav: false,
                navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
                animateOut: 'fadeOut',
                animateIn: 'fadeIn',
                responsive: {
                    0: {
                        items: 1
                    },
                    599: {
                        items: 2
                    }
                }
            });
        }


        /*---------------------------
            BLog Grid carousel
        ---------------------------*/
        var $TestimonialCarousel = $('.blog-grid-carousel');
        if ($TestimonialCarousel.length > 0) {
            $TestimonialCarousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: true,
                nav: true,
                navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
                animateOut: 'fadeOut',
                animateIn: 'fadeIn',
                responsive: {
                    0: {
                        items: 1
                    },
                    460: {
                        items: 1
                    },
                    599: {
                        items: 1
                    },
                    768: {
                        items: 2
                    },
                    960: {
                        items: 2
                    },
                    1200: {
                        items: 3
                    },
                    1920: {
                        items: 3
                    }
                }
            });
        }

        /*---------------------------
            header carousel
        ---------------------------*/
        var $headerCarousel = $('.header-slider');
        if ($headerCarousel.length > 0) {
            $headerCarousel.owlCarousel({
                loop: true,
                autoplay: true, //true if you want enable autoplay
                autoPlayTimeout: 1000,
                margin: 30,
                dots: true,
                nav: true,
                navText: ['<i class="fas fa-chevron-left"></i>', '<i class="fas fa-chevron-right"></i>'],
                animateOut: 'fadeOut',
                animateIn: 'fadeIn',
                responsive: {
                    0: {
                        items: 1,
                        nav: false,
                    },
                    460: {
                        items: 1,
                        nav: false,
                    },
                    599: {
                        items: 1
                    },
                    768: {
                        items: 1
                    },
                    960: {
                        items: 1
                    },
                    1200: {
                        items: 1
                    },
                    1920: {
                        items: 1
                    }
                }
            });
        }
        // Clinet - active
        $('.client-active-area').owlCarousel({
            loop: true,
            items: 5,
            nav: true,
            margin: 30,
            dots: false,
            navText: ['<span data-icon="&#x23;"></span>', '<span data-icon="&#x24;"></span>'],
            responsive: {
                0: {
                    items: 2
                },
                600: {
                    items: 3
                },
                992: {
                    items: 4
                },
                1200: {
                    items: 5
                }
            }
        })
        /*----------------------
        Search Popup
    -----------------------*/
        var bodyOvrelay = $('#body-overlay');
        var searchPopup = $('#search-popup');

        $(document).on('click', '#body-overlay', function (e) {
            e.preventDefault();
            bodyOvrelay.removeClass('active');
            searchPopup.removeClass('active');
        });
        $(document).on('click', '.border-none', function (e) {
            e.preventDefault();
            bodyOvrelay.removeClass('active');
            searchPopup.removeClass('active');
        });
        $(document).on('click', '#search', function (e) {
            e.preventDefault();
            searchPopup.addClass('active');
            bodyOvrelay.addClass('active');
        });


    });


    //define variable for store last scrolltop
    var lastScrollTop = '';

    $(window).on('scroll', function () {

        //back to top show/hide
        var ScrollTop = $('.back-to-top');
        if ($(window).scrollTop() > 1000) {
            ScrollTop.fadeIn(1000);
        } else {
            ScrollTop.fadeOut(1000);
        }

        /*--------------------------
         sticky menu activation
        -------------------------*/
        if ($(window).scrollTop() >= 1) {
            $('.nav-custom').addClass('nav-custom-fixed');
        } else {
            $('.nav-custom').removeClass('nav-custom-fixed');
        }

        //back to top show/hide
        var ScrollTop = $('.back-to-top');
        if ($(window).scrollTop() > 1000) {
            ScrollTop.fadeIn(1000);
        } else {
            ScrollTop.fadeOut(1000);
        }

    });


    $(window).on('load', function () {

        /*-----------------
            preloader
        ------------------*/
        var preLoder = $("#preloader");
        preLoder.fadeOut(1000);

        /*-----------------
            back to top
        ------------------*/
        var backtoTop = $('.back-to-top')
        backtoTop.fadeOut();

        /*---------------------
            Cancel Preloader
        ----------------------*/
        $(document).on('click', '.cancel-preloader a', function (e) {
            e.preventDefault();
            $("#preloader").fadeOut(2000);
        });
    });


})(jQuery);


// $('#form').submit(function(form_value){
//     var data=$(this).serializeArray();
//     $.ajax({
//         url:"/ajax/",
//         method:'POST',
//         data:{
//             csrfmiddlewaretoken: '{{ csrf_token }}',
//         },
//         // headers: {
//         //     "X-CSRFToken": "{{ csrf_token }}"
//         //     },
//         success: function(){  
//             swal("Successfully Submitted!", "Message successfully updated", "success")
//             $('#form').trigger("reset")
//         },
//         error: function() { 
//             swal("Error!", "Form validation error", "error") 
//         }       
//     })
//     return false
      
// })


$(document).ready(function (){
    // Declare Carousel jquery object
    var owl = $('.owl-carousel');
  
    // Carousel initialization
    owl.owlCarousel({
        loop:false,
        margin:0,
        navSpeed:500,
        nav:true,
        autoplay: true,
        rewind: true,
        responsive: {
            0: {
              items: 1
            },
        
            600: {
              items: 3
            },
        
            1024: {
              items: 4
            },
        
            1366: {
              items: 4
            }
          }
        });
  
    // add animate.css class(es) to the elements to be animated
    function setAnimation ( _elem, _InOut ) {
      // Store all animationend event name in a string.
      // cf animate.css documentation
      var animationEndEvent = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
  
      _elem.each ( function () {
        var $elem = $(this);
        var $animationType = 'animated ' + $elem.data( 'animation-' + _InOut );
  
        $elem.addClass($animationType).one(animationEndEvent, function () {
          $elem.removeClass($animationType); // remove animate.css Class at the end of the animations
        });
      });
    }
  
  // Fired before current slide change
    owl.on('change.owl.carousel', function(event) {
        var $currentItem = $('.owl-item', owl).eq(event.item.index);
        var $elemsToanim = $currentItem.find("[data-animation-out]");
        setAnimation ($elemsToanim, 'out');
    });
  
  // Fired after current slide has been changed
    var round = 0;
    owl.on('changed.owl.carousel', function(event) {
  
        var $currentItem = $('.owl-item', owl).eq(event.item.index);
        var $elemsToanim = $currentItem.find("[data-animation-in]");
      
        setAnimation ($elemsToanim, 'in');
    })
    
    owl.on('translated.owl.carousel', function(event) {
      console.log (event.item.index, event.page.count);
      
        if (event.item.index == (event.page.count - 1))  {
          if (round < 1) {
            round++
            console.log (round);
          } else {
            owl.trigger('stop.owl.autoplay');
            var owlData = owl.data('owl.carousel');
            owlData.settings.autoplay = false; //don't know if both are necessary
            owlData.options.autoplay = false;
            owl.trigger('refresh.owl.carousel');
          }
        }
    });
  
  });


//   $.ajax({
//     url: '//delete_admission_fee_record/',
//     method: 'POST',
//     headers: {
//     "X-CSRFToken": "{{ csrf_token }}"
//     },
//     data: {'id': object_id},
//     success: function(response) {
//         if (response.status == 1) {
//             Swal.fire(
//                 'Deleted!',
//                 'Your object has been deleted.',
//                 'success'
//             )
//             // Refresh the page after deleting the object
//             setTimeout(function() {
//                 location.reload();
//             }, 1000);
//         }}
//     })
  

