from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/recommendations')
def recommendations():
    return render_template('recommendations.html')

@app.route('/gosts')
def gosts():
    return render_template('gosts.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
