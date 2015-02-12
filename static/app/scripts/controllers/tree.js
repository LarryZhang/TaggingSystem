'use strict';

/**
 * @ngdoc function
 * @name staticApp.controller:TreeCtrl
 * @description
 * # TreeCtrl
 * Controller of the staticApp
 */
angular.module('staticApp')
    .controller('TreeCtrl', function ($scope, $filter, tagRest,alertService) {
        $scope.rootTags = [];
        $scope.tagList = [];
        $scope.selectedTag = {};
        $scope.tagTreeControl = {};
        $scope.parentIdSelectOptions = [];
        $scope.selectTag = function (branch) {

            $scope.selectedTag = tagRest.get({_id: branch._id['$oid']});
            console.log($scope.selectedTag);


        };
        $scope.createNew = function () {
            $scope.selectedTag = {};

        };
        $scope.submit = function () {
            tagRest.save($scope.selectedTag, function () {
                $scope.tagTreeControl;
            },alertService.httpErrorHandler);
            render();
        };
        function render() {
            var tags = tagRest.query({}, function () {

                $scope.rootTags = tags;
                function addToTagList(tag) {
                    if (!tag.children) {

                    } else {
                        angular.forEach(tag.children, addToTagList);
                    }
                    //$scope.tagList[tag._id['$oid']]=tag;

                    $scope.tagList.push(tag);
                };
                $scope.tagList = [];
                angular.forEach(tags, addToTagList);
                console.log($scope.tagList);
            });
        }


        render();
    });
