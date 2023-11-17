let app = angular.module('myApp', []);

function titleCase(str) {
    str = str.toLowerCase();
    return str.replace(/(^|\s)\S/g, function(t) { return t.toUpperCase() });
}

app.controller('APIController', function ($scope, $window, $http, $q) {
    /* Initialize variables */
    $scope.savedPoems = JSON.parse(localStorage.getItem("savedPoems"));
    if(Object.keys($scope.savedPoems).length != 0) {
        $scope.showSavedPoems = true;
    }

    console.log($scope.savedPoems);    
    $scope.poemGenerated = false;
    $scope.loading = false;
    $scope.poemLoaded = false;
    $scope.poemTitle = "";
    $scope.poemText = "";
    $scope.word1 = "";
    $scope.word2 = "";
    $scope.storageMessage = "";

    console.log("Saved poems: ")
    console.log($scope.savedPoems);

    /* Generates poem via API request and displays to screen. */
    $scope.getResults = function () {
        $scope.loading = true;
        var requestParams = "/generate-poem?word-1=".concat($scope.word1, "&word-2=", $scope.word2);
        $http.post(requestParams).then(function (response) {
            if(response.data.length > 0) {
                // Display poem
                $scope.poemGenerated = true;
                $scope.poemLoaded = false;
                $scope.poemTitle = titleCase($scope.word1 + " and " + $scope.word2);
                $scope.poemText = response.data;
            } else {
                $scope.poemText = "Word(s) not in vocab. Try different words.";
            }   
            $scope.loading = false;         
        });
    };

    /* Enables TTS on currently displaying poem. */
    $scope.enableTTS = function () {
        let speechSynthesis = window.speechSynthesis;
        if ("speechSynthesis" in window) {
            let utterance = new SpeechSynthesisUtterance($scope.poemText);
            utterance.rate = 0.7;
            speechSynthesis.speak(utterance);
        } else {
            alert("TTS is not supported in this browser.")
        }
    };

    /* Adds a poem to local storage. */
    $scope.savePoem = function() {
        var poem = {title: $scope.poemTitle, text: $scope.poemText};
        var title = $scope.poemTitle;

        if($scope.savedPoems === null) {
            $scope.savedPoems = {[title] : poem};
        }
        else {
            if($scope.savedPoems[$scope.poemTitle] != null) {
                $scope.poemTitle += " 1";
            }
            $scope.savedPoems[$scope.poemTitle] = poem;            
        }
        localStorage.setItem("savedPoems", JSON.stringify($scope.savedPoems));
        $scope.storageMessage = "Poem saved.";
    }

    /* Loads a poem to local storage. */
    $scope.loadPoem = function() {
        $scope.poemLoaded = true;
        $scope.poemGenerated = false;
        $scope.poemTitle = $scope.poemToLoad;
        $scope.poemText = $scope.savedPoems[$scope.poemToLoad].text;
    }

    /* Removes a poem from local storage. */
    $scope.removePoem = function() {
        var poemToRemove = $scope.poemTitle;
        delete $scope.savedPoems[poemToRemove];
        localStorage.setItem("savedPoems", JSON.stringify($scope.savedPoems));
        $scope.storageMessage = "Poem removed.";
    }
}
);
