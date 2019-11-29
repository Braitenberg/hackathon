from flask import Flask, render_template, request
from mail.mail import Mail
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendmail')
def sendmail():
   txt = request.args.get('mail') 
   mail.mail(txt)
   return "done" 
if __name__ == "__main__":
    app.run(debug=True)
