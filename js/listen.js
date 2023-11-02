if ("webkitSpeechRecognition" in window) {
    console.log("Performing speech recognition");
    var speechRecognition = new speechRecognition();
    speechRecognition.continuous = true;
    speechRecognition.interimResults = true;

    document.querySelector("start-listen-button").onclick = () => {
        speechRecognition.start();
    };

    document.querySelector("stop-listen-button").onclick = () => {
        speechRecognition.stop();
    };

    let spokenWords = "";
    speechRecognition.onresult = (event) => {
        let wordsInProgress = "";

        for(let i = event.resultIndex; i < event.results.length; i++){
            if (event.results[i].isFinal){
                spokenWords += event.results[i][0].transcript;
            } else {
                wordsInProgress += event.results[i][0].transcript;
            }
        }

        document.querySelector("#heard-text").innerHTML = spokenWords;
        document.querySelector("#heard-in-progress-text").innerHTML = spokenWords;
    };

} else {
    console.log("Speech recognition not available.");
}