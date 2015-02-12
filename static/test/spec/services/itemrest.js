'use strict';

describe('Service: itemRest', function () {

    // load the service's module
    beforeEach(module('staticApp'));

    // instantiate service
    var itemRest;
    beforeEach(inject(function (_itemRest_) {
        itemRest = _itemRest_;
    }));

    it('should do something', function () {
        expect(!!itemRest).toBe(true);
    });

});
