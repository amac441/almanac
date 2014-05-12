
var app = angular.module("myApp",["ngRoute"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

//app.run(function ($http, $cookies) {
//    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
//})

app.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "../static/app/js/angular/views/home.html",
            controller: "HomeController",

        })


        .otherwise({
            redirectTo: '/'
        })
})


//// Declare app level module which depends on filters, and services
//angular.module('myApp', [
//  'ngRoute',
//  'myApp.filters',
//  'myApp.services',
//  'myApp.directives',
//  'myApp.controllers'
//]).
//config(['$routeProvider', function($routeProvider) {
//  $routeProvider.when('/view1', {templateUrl: 'partials/partial1.html', controller: 'MyCtrl1'});
//  $routeProvider.when('/view2', {templateUrl: 'partials/partial2.html', controller: 'MyCtrl2'});
//  $routeProvider.otherwise({redirectTo: '/view1'});
//}]);
