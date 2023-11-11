let app = angular.module('myApp', []);

app.directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function (scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;
            element.bind('change', function () {
                scope.$apply(function () {
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
    };
}]);

app.controller('APIController', function ($scope, $log, $http) {
    $scope.showTTS = false;

    $scope.getResults = function () {
        $scope.poem = "Clicked poem value";
        console.log("Sending API Request...");
        $http.post('/generate-poem?word-1=w1&word-2=w2').then(function (response) {
            var responseData = response.data;
            document.getElementById("poem-text").innerHTML = responseData;
        });
    };

}
);
