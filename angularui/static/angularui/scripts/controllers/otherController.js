sportModule.controller('faqController', function ($scope, $http, $location) {

    $http.get(host + "api/faq/")
        .then(function (response) {
            $scope.faqs = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

});
