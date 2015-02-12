'use strict';

/**
 * @ngdoc service
 * @name staticApp.alertService
 * @description
 * # alertService
 * Factory in the staticApp.
 */
angular.module('staticApp')
    .factory('alertService', function () {
        // Service logic
        // ...

        var alertService = {};

        // 创建一个全局的 alert 数组

        alertService.add = function (alerts, type, msg) {
            alerts.push({
                'type': type, 'msg': msg, 'close': function () {
                    alertService.closeAlert(this);
                }
            });
        };

        alertService.closeAlert = function (alerts, alert) {
            alertService.closeAlertIdx(alerts.indexOf(alert));
        };

        alertService.closeAlertIdx = function (alerts, index) {
            alerts.splice(index, 1);
        };
        alertService.httpErrorHandler = function (response) {
            //if(response.status==400){
            console.log(response.status);

            console.log(response.data);
            alert('error:'+response.data);
        };
            //}

            alertService.alert = function (type, msg) {

                alert(msg);
            };
            return alertService;
        }
        )