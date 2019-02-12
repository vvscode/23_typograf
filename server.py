from flask import Flask, request, render_template
from typograph import beautify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    input_text = request.form['text'] or '' if request.method == 'POST' else ''
    result = beautify(input_text)

    return render_template('form.html', input=input_text, result=result)


if __name__ == '__main__':
    app.run()
