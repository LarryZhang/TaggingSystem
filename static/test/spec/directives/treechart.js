'use strict';

describe('Directive: treeChart', function () {

    // load the directive's module
    beforeEach(module('staticApp'));

    var element,
        scope;

    beforeEach(inject(function ($rootScope) {
        scope = $rootScope.$new();
    }));

    it('should make hidden element visible', inject(function ($compile) {
        element = angular.element('<tree-chart></tree-chart>');
        element = $compile(element)(scope);
        expect(element.text()).toBe('this is the treeChart directive');
    }));
});
