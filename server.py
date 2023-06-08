from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo/')
def dojo():
    return 'dojo'

@app.route('/say/<string:name>/')
def hi_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:phrase>')
def repeat_phrase_by_int(phrase, num):
    return f"{phrase * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.