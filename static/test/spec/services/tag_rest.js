'use strict';

describe('Service: tag_rest', function () {

    // load the service's module
    beforeEach(module('staticApp'));

    // instantiate service
    var tag;
    beforeEach(inject(function (_tag_) {
        tag = _tag_;
    }));

    it('should do something', function () {
        expect(!!tag).toBe(true);
    });

});
