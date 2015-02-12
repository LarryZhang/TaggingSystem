'use strict';

/**
 * @ngdoc filter
 * @name staticApp.filter:tagFilter
 * @function
 * @description
 * # tagFilter
 * Filter in the staticApp.
 */
angular.module('staticApp')
  .filter('tagFilter', function () {
     return function(items, selected) {
       console.log(selected);
       if(!selected){
         return items;
       }
       if(!items){
         return items;
       }
    var out = [];
    if(!angular.isArray(selected)){
      selected=[selected];
    }
    var exclude=[];
    function addToExclude(tag){
      if(tag.children){
        tag.children.forEach(addToExclude);
      }
      exclude.push(tag._id['$oid']);
    };
    selected.forEach(function(tag){

      addToExclude(tag);
       });
    console.log(exclude);
       items.forEach(function(item){
          if(exclude.indexOf(item._id['$oid'])==-1){
            out.push(item);
          }
       });
       console.log(out);
    return out;
  };
  });
