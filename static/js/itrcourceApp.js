(function () {
  'use strict';
  angular
  .module('itrcourceApp', []);

angular
  .module('itrcourceApp')
  .run(run);

run.$inject = ['$http'];

function run($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}

})();