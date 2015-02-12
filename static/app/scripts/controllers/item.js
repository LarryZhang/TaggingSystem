'use strict';

/**
 * @ngdoc function
 * @name staticApp.controller:ItemCtrl
 * @description
 * # ItemCtrl
 * Controller of the staticApp
 */
angular.module('staticApp')
    .controller('ItemCtrl', function ($scope, itemRest,tagRest, $upload,alertService) {
        $scope.allItems = [];
        //$scope.gridOptions = {
        //    enableRowSelection: true,
        //    multiSelect: false,
        //    enableRowHeaderSelection: false,
        //    //enableSorting: true,
        //    //enableFiltering: true,
        //    columnDefs: [
        //        {name:'id',field:'_id.$oid'},
        //        {name: 'Name', field: 'label'},
        //        {name: 'Description', field: 'description'}
        //        //{ name:'city', field: 'address.city'},
        //        // { name:'getZip', field: 'getZip()', enableCellEdit:false}
        //    ],
        //    //rowIdentity: function (row) {
        //    //    return row._id['$oid'];
        //    //},
        //    //getRowIdentity: function (row) {
        //    //    return row._id['$oid'];
        //    //},
        //    onRegisterApi: function (gridApi) {
        //        $scope.gridApi = gridApi;
        //    },
        //    data: [{label:1,description:2},{label:1,description:2}]
        //};c c c
        function render() {


            var allItems = itemRest.query({}, function () {
                $scope.allItems = allItems;
                console.log(allItems);
                //$scope.gridOptions.data = allItems;
            });
            var allTags=tagRest.query({},function(){
                 function addToTagList(tag) {
                    if (!tag.children) {

                    } else {
                        angular.forEach(tag.children, addToTagList);
                    }
                    //$scope.tagList[tag._id['$oid']]=tag;

                    $scope.tagList.push(tag);
                };
                $scope.tagList = [];
                angular.forEach(allTags, addToTagList);
                console.log($scope.tagList);
            });
        }

        $scope.selectItem = function (item) {
            $scope.selectedItem = item;
            if (!$scope.selectedItem.files) {
                $scope.selectedItem.files = [];
                $scope.selectedItem.tags = [];
            }
        };
        $scope.createNew = function () {
            $scope.selectedItem = {files: [], tags: []};
        };
        $scope.selectedItem = {files: [], tags: []};
        $scope.submit = function () {
            itemRest.save($scope.selectedItem,function(){
                console.log('succses');
            },alertService.httpErrorHandler
            );
            render();
        }
        $scope.deleteFile = function (file, index) {
            console.log(index);
            $scope.selectedItem.files.splice(index, 1);
        };
        render();
        $scope.$watch('files', function () {
            $scope.upload($scope.files);
        });
        $scope.deleteItem=function(){
            itemRest.delete({_id:$scope.selectedItem._id['$oid']});
            render();
        };
        $scope.upload = function (files) {
            if (files && files.length) {
                for (var i = 0; i < files.length; i++) {
                    var file = files[i];
                    $upload.upload({
                        url: '/api/uploads',

                        file: file
                    }).progress(function (evt) {
                        var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                        console.log('progress: ' + progressPercentage + '% ' +
                        evt.config.file.name);
                    }).success(function (data, status, headers, config) {
                        console.log('file ' + config.file.name + 'uploaded. Response: ' +
                        JSON.stringify(data));
                        angular.forEach(data, function (obj) {
                            $scope.selectedItem.files.push(obj);

                        });
                    });
                }
            }
        };
    });
