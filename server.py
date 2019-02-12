from flask import Flask, request, render_template
from typograph import beautify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    input_text = request.form['text'] or '' if request.method == 'POST' else ''
    beautified_text = beautify(input_text)

    return render_template('form.html', input_text=input_text, beautified_text=beautified_text)


if __name__ == '__main__':
    app.run()
