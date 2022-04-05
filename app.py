from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio-details.html')
def show__profile_details():
    return render_template('portfolio-details.html')
        
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
