'use strict';

/**
 * @ngdoc overview
 * @name staticApp
 * @description
 * # staticApp
 *
 * Main module of the application.
 */
angular
    .module('staticApp', [
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'ngTouch',
        'angularBootstrapNavTree', 'angularFileUpload',
        'ui.select','ui.bootstrap'
    ])
    .config(function ($routeProvider) {
        $routeProvider
            .when('/', {
                redirectTo:'/tree',
                templateUrl: 'views/main.html',
                controller: 'MainCtrl'
            })

            .when('/tree', {
                templateUrl: 'views/tree.html',
                controller: 'TreeCtrl'
            })
            .when('/item', {
                templateUrl: 'views/item.html',
                controller: 'ItemCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    });
