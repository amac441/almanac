var appController = years.controller('AppController', function ($scope, $rootScope, $location, GlobalService) {
    var failureCb = function (status) {
        console.log(status);
    };
    $scope.globals = GlobalService;

    $scope.initialize = function (is_authenticated) {
        $scope.globals.is_authenticated = is_authenticated;

    $scope.sidebar_click = function () {
        $scope.boolChangeClass = !$scope.boolChangeClass;
        $scope.$apply();
    }

    };
})