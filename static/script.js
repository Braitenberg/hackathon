var recognition = new webkitSpeechRecognition();
recognition.continuous = true;

var output = document.getElementById('output');
recognition.onresult = function(event) {
  output.textContent = event.results[0][0].transcript;
  sendmail(event.results[0][0].transcript)
};

function sendmail(txt) {
	var request = new XMLHttpRequest()
	request.open('GET', 'localhost/sendmail?mail=', true)
	request.send()
}
