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
    $scope.obj= {test: false};

    // Generate poem via API Request
    $scope.getResults = function () {
        $scope.poem = "Clicked poem value";
        console.log("Sending API Request...");
        $http.post('/generate-poem?word-1=w1&word-2=w2').then(function (response) {
            // var responseData = response.data;
            // $scope.poem.text = response.data;
            document.getElementById("poem-text").innerHTML = response.data;
            // $scope.showTTSButton = true;
            $scope.obj.test = true;
            console.log($scope.obj.test);
        });
    };

    // Enable TTS
    $scope.enableTTS = function () {
        let speechSynthesis = window.speechSynthesis;
        if ("speechSynthesis" in window) {
            let utterance = new SpeechSynthesisUtterance("Toby"); // TODO
            speechSynthesis.speak(utterance);
            utterance.text = "I'm so close"; // TODO
            speechSynthesis.speak(utterance);
        } else {
            alert("TTS is not supported in this browser.")
        }
    };
}
);
