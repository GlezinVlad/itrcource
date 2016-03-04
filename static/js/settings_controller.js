(function () {
  'use strict';
angular.module('itrcourceApp').controller('SettingsCtrl', function ($scope, $http, $timeout) {


     $http.get('/userinfo').then(set_userinfo, http_error);

    $scope.languages=['English', 'Russian']
      function set_userinfo(data, status, headers, config) {
        $scope.info=data.data;
        $scope.info.date_of_birth= new Date(data.data.date_of_birth);
      }

      function http_error(data, status, headers, config) {
        $scope.message='done';
        $timeout(function(){$scope.message='';}, 5000)
      }

    $scope.save = function(){
        this.info.language=$('#language').val();
        this.info.theme=$('#theme').val();
        $http.put('/userinfo', this.info).then(saved, http_error);
    }

    function saved(data, status, headers, config) {
        $scope.message='done';
        $timeout(function(){$scope.message='';}, 5000)
      }



    $('.cloudinary-fileupload').bind('fileuploadstart', function (e) {
        $('.preview').html('Upload started...');
    });

    this.avatar_uploaded=function (e, data){
        $scope.info.avatar_url=data.result.url
         $('.preview').html('Upload done, press save to save changes');
         $timeout(function(){$scope.message='';}, 500)
    }

    $('.cloudinary-fileupload').bind('cloudinarydone', this.avatar_uploaded);

});
})();