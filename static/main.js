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

app.controller('APIController', function ($scope, $window, $http, $q) {
    $scope.showTTSButton = false;
    $scope.poemText = "";
    $scope.word1 = "";
    $scope.word2 = "";

    /* Generates poem via API request and displays to screen. */
    $scope.getResults = function () {
        $scope.poem = "Clicked poem value";
        console.log("Sending API Request...");
        var requestParams = "/generate-poem?word-1=".concat($scope.word1, "&word-2=", $scope.word2);
        $http.post(requestParams).then(function (response) {
            // Display poem
            $scope.showTTSButton = true;
            $scope.poemText = response.data;
        });
    };

    /* Enables TTS on currently displaying poem. */
    $scope.enableTTS = function () {
        let speechSynthesis = window.speechSynthesis;
        if ("speechSynthesis" in window) {
            let utterance = new SpeechSynthesisUtterance($scope.poemText);
            speechSynthesis.speak(utterance);
        } else {
            alert("TTS is not supported in this browser.")
        }
    };

}
);
