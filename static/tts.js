

function enableTTS(){
    let speechSynthesis = window.speechSynthesis;
    // Check if speech synthesis enabled in window
    if ("speechSynthesis" in window){
        let utterance = new SpeechSynthesisUtterance("Toby"); // TODO
        speechSynthesis.speak(utterance);
        utterance.text = "I'm so close"; // TODO
        speechSynthesis.speak(utterance);
    } else {
        alert("TTS is not supported in this browser.")
    }
    
    // TODO delete
    // function logVoices(){
    //     var voices = speechSynthesis.getVoices();
    //     // You can index into this list to get voices
    //     // change utterance.pitch, .volume, .rate
    //     voices.forEach(function (voice){
    //         console.log({
    //             name: voice.name,
    //             lang: voice.lang
    //         });
    //     })
    // }
}