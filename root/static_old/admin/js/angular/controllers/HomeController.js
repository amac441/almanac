app.controller('HomeController', function ($scope, GlobalService) {

    $scope.globals = GlobalService;
    //options for modals
    $scope.opts = {
        backdropFade: true,
        dialogFade: true
    };

    $scope.toggleActive = function (s) {
        s.active = !s.active;
    };

});