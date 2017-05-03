"use strict";

($ => {
    const $navbar  = $('.navbar');
    const $menuBtn = $('#menuButton');

    function toggleNavbar() {
        $(this).toggleClass('is-active');
        $navbar.slideToggle();
    }

    $menuBtn.on('click', toggleNavbar);

})(jQuery)
