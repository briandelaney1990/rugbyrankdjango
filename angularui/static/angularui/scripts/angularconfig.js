var sportModule = angular.module('sportModule', ['ngRoute']);

var host = "http://localhost:8000/";

sportModule.config(['$routeProvider', '$locationProvider', '$httpProvider',
    function ($routeProvider, $locationProvider, $httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $locationProvider.html5Mode(true);
        $routeProvider
          .when('/rankings', {
            templateUrl: '/static/angularui/angulartemplates/rankings.html',
            controller: 'rankingsController'
        }).when('/teams/', {
            templateUrl: '/static/angularui/angulartemplates/teams.html',
            controller: 'teamsController'
        }).when('/teams/:teamId', {
            templateUrl: '/static/angularui/angulartemplates/team.html',
            controller: 'teamController'
        }).when('/tournaments', {
            templateUrl: '/static/angularui/angulartemplates/tournaments.html',
            controller: 'tournamentsController'
        }).when('/tournaments/:tournamentId', {
            templateUrl: '/static/angularui/angulartemplates/tournament.html',
            controller: 'tournamentController'
        }).when('/countries', {
            templateUrl: '/static/angularui/angulartemplates/countries.html',
            controller: 'countriesController'
        }).when('/countries/:countryId', {
            templateUrl: '/static/angularui/angulartemplates/country.html',
            controller: 'countryController'
        }).when('/', {
            templateUrl: '/static/angularui/angulartemplates/home.html',
            controller: 'homeController'
        }).when('/about',{
            templateUrl: '/static/angularui/angulartemplates/about.html'
        }).when('/faq',{
            templateUrl: '/static/angularui/angulartemplates/faq.html',
            controller: 'faqController'
        }).when('/contact',{
            templateUrl: '/static/angularui/angulartemplates/contact.html'
        }).otherwise({
            templateUrl: '/static/angularui/angulartemplates/error.html'
    });
    }
]);
















