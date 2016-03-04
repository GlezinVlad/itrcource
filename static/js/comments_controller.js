(function () {
  'use strict';
angular.module('itrcourceApp').controller('CommentsCtrl', function ($scope, $http, $timeout, $interval) {

    var arr = window.location.href.split('/');
    var post_id = arr[arr.length-1]
    
    $http.get('/user_status').then(set_user);
    function set_user(data, status, headers, config) { $scope.user = data.data; }
    
    $interval(get_comments, 10000);

    function get_comments() {
         $http.get('/api/posts/comments/' + post_id).then(set_comments, http_error);
    }
    get_comments();
    $scope.comments = []

    function set_comments(data, status, headers, config) {
        $scope.comments=data.data;
        for (var index in $scope.comments){
            $scope.comments[index].time_published=$scope.comments[index].time_published.replace(/[TZ]/g,' ')
        }
     }

    function http_error(data, status, headers, config) {
        //alert(data.data);
     }

    $scope.post_comment = function(){
    if(!/^\s*$/.test(this.comment_text))
        $http.post('/api/posts/comments/' + post_id, {'text': this.comment_text }).then(commented, http_error);
    }

    function commented(data, status, headers, config) {
        $scope.comment_text = ''
        get_comments();
     }

    $scope.delete_comment = function(id){
        $http.delete('/api/comments/'+id).then(deleted, http_error);
    }

    function deleted(data, status, headers, config) {
        get_comments();
    }

});
})();