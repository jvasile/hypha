import $ from './globals';
import MobileMenu from './components/mobile-menu';
import Search from './components/search';
import MobileSearch from './components/mobile-search';

$(function () {
    $(MobileMenu.selector()).each((index, el) => {
        new MobileMenu($(el), $('.js-mobile-menu-close'), $('.header__menus--mobile'), $('.header__search'));
    });

    $(Search.selector()).each((index, el) => {
        new Search($(el), $('.header__search'));
    });

    $(MobileSearch.selector()).each((index, el) => {
        new MobileSearch($(el), $('.header__menus--mobile'), $('.header__search'), $('.js-search-toggle'));
    });
});
