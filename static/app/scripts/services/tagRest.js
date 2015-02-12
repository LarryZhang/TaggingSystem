'use strict';

/**
 * @ngdoc service
 * @name staticApp.tag
 * @description
 * # tag_rest
 * Service in the staticApp.
 */
angular.module('staticApp')
    .factory('tagRest', function ($resource) {
        // AngularJS will instantiate a singleton by calling "new" on this function
        return $resource('/api/tag/:_id');
    });
