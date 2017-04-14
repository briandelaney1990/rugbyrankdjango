sportModule.controller('countryController', function ($scope, $http, $routeParams, $location) {

    var countryId = String($routeParams.countryId);

    $http.get(host + "api/country/" + countryId + "/")
        .then(function (response) {
            $scope.country = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/country/" + countryId + "/teams/")
        .then(function (response) {
            $scope.teams = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/country/" + countryId + "/tournaments/")
        .then(function (response) {
            $scope.tournaments = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/country/" + countryId + "/information/")
        .then(function (response) {
            $scope.information = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

     $scope.clickrank = function(name){

        console.log($location.path("teams/"  + name))
    };

    $scope.clicktournament = function(id){
       console.log($location.path("tournaments/"  + id))
    };

});