'use strict';

/**
 * @ngdoc function
 * @name staticApp.controller:TagCtrl
 * @description
 * # TagCtrl
 * Controller of the staticApp
 */
angular.module('staticApp')
    .controller('TagCtrl', function ($scope, tagRest) {
        $scope.selectedTag = null;

        $scope.selectTag = function (e) {
            console.log(e);
            $scope.selectedTag = e;
        };
        function render() {
            var tags = tagRest.query({}, function () {

                $scope.rootTags = tags;
                var allTag = {};
                for (var t in tags) {
                    console.log(t._id);
                    allTag[t._id] = t;
                }
            }, {});
        }

        render();
    });
