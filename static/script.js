var recognition = new webkitSpeechRecognition();
recognition.continuous = true;

var output = document.getElementById('output');
recognition.onresult = function(event) {
  output.textContent = event.results[0][0].transcript;
};
