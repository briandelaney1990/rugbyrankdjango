sportModule.controller('homeController', function ($scope, $http, $location) {

    $http.get(host + "api/home/rankings/")
        .then(function (response) {
            $scope.rankings = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/home/details/")
        .then(function (response) {
            $scope.details = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/home/matches/")
        .then(function (response) {
            $scope.matches = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get(host + "api/home/featured/")
        .then(function (response) {
            $scope.featured = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $scope.clickrank = function(id){
        console.log($location.path("teams/"  + id))
    };

    $scope.clickfeatured = function(id){
        console.log($location.path("teams/"  + id))
    };

});


sportModule.controller('navController', function ($scope, $http, $location) {

    $scope.menuItems = [
        {
            name: "Rankings",
            link: "/rankings",
            icon: "fa-list-ol"
        },
        {
            name: "Teams",
            link: "/teams",
            icon: "fa-users"
        },
        {
            name: "Countries",
            link: "/countries",
            icon: "fa-flag"
        },
        {
            name: "Tournaments",
            link: "/tournaments",
            icon: "fa-trophy"
        }
    ];

    $scope.setActive = function(menuItem) {
        $scope.activeMenu = menuItem;
        console.log($scope.activeMenu);
    };

});