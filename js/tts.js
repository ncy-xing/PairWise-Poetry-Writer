let speechSynthesis = window.speechSynthesis;

function enableTTS(){
    // Check if speech synthesis enabled in window
    if ("speechSynthesis" in window){
        var utterance = new SpeechSynthesisUtterance("Toby"); // TODO
        speechSynthesis.speak(utterance);
        utterance.voice = 
        utterance.text = "I'm so close"; // TODO
        speechSynthesis.speak(utterance);
        logVoices();
    } else {
        alert("TTS is not supported in this browser.")
    }
    
    // TODO delete
    function logVoices(){
        var voices = speechSynthesis.getVoices();
        // You can index into this list to get voices
        // change utterance.pitch, .volume, .rate
        voices.forEach(function (voice){
            console.log({
                name: voice.name,
                lang: voice.lang
            });
        })
    }
}