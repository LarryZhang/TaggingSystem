'use strict';

/**
 * @ngdoc service
 * @name staticApp.itemRest
 * @description
 * # itemRest
 * Factory in the staticApp.
 */
angular.module('staticApp')
    .factory('itemRest', function ($resource) {
        // Service logic
        // ...

        var meaningOfLife = 42;


        return $resource('/api/item/:_id');

    });
