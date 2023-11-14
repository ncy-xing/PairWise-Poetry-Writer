let app = angular.module('myApp', []);

function titleCase(str) {
    str = str.toLowerCase();
    return str.replace(/(^|\s)\S/g, function(t) { return t.toUpperCase() });
}

app.controller('APIController', function ($scope, $window, $http, $q) {
    /* Initialize variables */
    $scope.savedPoems = JSON.parse(localStorage.getItem("savedPoems"));
    if($scope.savedPoems != null) {
        $scope.poemToLoad = "test";
        $scope.showSavedPoems = true;
    }
    $scope.poemGenerated = false;
    $scope.poemTitle = "";
    $scope.poemText = "";
    $scope.word1 = "";
    $scope.word2 = "";

    console.log("Saved poems: ")
    console.log($scope.savedPoems);

    /* Generates poem via API request and displays to screen. */
    $scope.getResults = function () {
        console.log("Sending API Request...");
        var requestParams = "/generate-poem?word-1=".concat($scope.word1, "&word-2=", $scope.word2);
        $http.post(requestParams).then(function (response) {
            // Display poem
            $scope.poemGenerated = true;
            $scope.poemTitle = titleCase($scope.word1 + " and " + $scope.word2);
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

    /* Adds a poem to local storage. */
    $scope.savePoem = function() {
        var poem = {title: $scope.poemTitle, text: $scope.poemText};
        if($scope.savedPoems === null) {
            $scope.savedPoems = {}
        }
        if($scope.savedPoems[$scope.poemTitle] != null) {
            $scope.poemTitle += " 1";
        }
        $scope.savedPoems[$scope.poemTitle] = poem;
        
        localStorage.setItem("savedPoems", JSON.stringify($scope.savedPoems));
        console.log("Save poem clicked");
    }

    $scope.loadPoem = function() {
        $scope.poemTitle = $scope.poemToLoad;
        $scope.poemText = $scope.savedPoems[$scope.poemToLoad].text;
    }
}
);
