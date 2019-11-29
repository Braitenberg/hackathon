

var recognition = new webkitSpeechRecognition();
recognition.continuous = true;

var output = document.getElementById('output');
recognition.onresult = function(event) {
  console.log("")
  output.textContent = event.results[0][0].transcript;
  sendmail(event.results[0][0].transcript)
};
function sendmail(txt) {
	var request = new XMLHttpRequest()
	console.log("here")
	request.open('GET', 'localhost/sendmail?mail=', true)
	request.send()
}
