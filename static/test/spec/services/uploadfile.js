'use strict';

describe('Service: uploadFile', function () {

    // load the service's module
    beforeEach(module('staticApp'));

    // instantiate service
    var uploadFile;
    beforeEach(inject(function (_uploadFile_) {
        uploadFile = _uploadFile_;
    }));

    it('should do something', function () {
        expect(!!uploadFile).toBe(true);
    });

});
