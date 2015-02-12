'use strict';

/**
 * @ngdoc directive
 * @name staticApp.directive:treeChart
 * @description
 * # treeChart
 */
angular.module('staticApp')
    .directive('treeChart', function () {
        return {
            template: '<div></div>',
            restrict: 'E',
            scope: {
                node: '='
            },
            link: function postLink(scope, element) {
                element.text('this is the treeChart directive');
            }
        };
    });
