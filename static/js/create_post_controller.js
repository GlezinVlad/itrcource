(function () {
  'use strict';
angular.module('itrcourceApp').controller('CreatePostCtrl', function ($scope, $http, $timeout) {

    $scope.post = {
        title: '',
        description: '',
        tags: '',
        media_url: '',
        text: ''
    }

    $scope.create = function(){
    if(/^\s*$/.test(this.post.title)||/^\s*$/.test(this.post.description)||/^\s*$/.test(this.post.text)){
            $scope.message='Fill all fields';
            $timeout(function(){$scope.message='';}, 5000)
        }
        else
            $http.post(window.location.href, this.post).then(created, http_error);
    }

    function created(data, status, headers, config) {
        window.location.href = "/posts/" + data.data.id;
     }

    function http_error(data, status, headers, config) {
        $scope.message='error';
        $timeout(function(){$scope.message='';}, 5000)
     }


    $('.cloudinary-fileupload').bind('fileuploadstart', function (e) {
        $('.preview').html('Upload started...');
    });

    this.image_uploaded=function (e, data){
        $scope.post.media_url=data.result.url
         $('.preview').html('Upload done');
         $timeout(function(){$scope.message='';}, 500)
    }

    $('.cloudinary-fileupload').bind('cloudinarydone', this.image_uploaded);


    $http.get('/tags').then(tags_autocomplete, http_error);

    function tags_autocomplete(data, status, headers, config){
        var tags = data.data;
        jQuery("#tags")
            .bind( "keydown", function(event){
              if ( event.keyCode === $.ui.keyCode.TAB &&
              $(this).data("autocomplete").menu.active ){
                event.preventDefault();
              }
            })
            .autocomplete({
              minLength: 0,
              source: function(request, response){
                response( $.ui.autocomplete.filter(
                tags, extractLast(request.term)) );
              },
              focus: function(){
                return false;
              },
              select: function(event, ui){
                var terms = split(this.value);
                terms.pop();
                terms.push(ui.item.value);
                terms.push("");
                this.value = terms.join(", ");
                return false;
              }
            });
        }
        function split(val){
            return val.split( /,\s*/);
        }
        function extractLast(term){
          return split(term).pop();
        }
});
})();