  var app = angular.module('AppMudarte',['ngMaterial', 'ngMessages']);

  app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

/*sidebar open and close | modificacion= 02-02-2016*/

/*$(".menu-toggle").click(function(e) {
    e.preventDefault();

});*/
var cont = 0;
app.controller('ControlNavbar', function ($scope) {
    $scope.toggleSide = function () {
        sidebarBtn();
    };
});
app.controller('ControlSidebar', function ($scope) {
    $scope.toggleSide = function () {
       sidebarBtn();
    };
});

