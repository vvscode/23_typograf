from flask import Flask, request, render_template

app = Flask(__name__)


def replace_quotes(text):
    # замена кавычек ' и " на « »
    return text


def replace_hyphen_with_dash_in_text(text):
    # в нужных местах заменить дефисы на тире
    return text


def replace_hyphen_with_short_dash_in_phones(text):
    # замена дефисов на короткое тире в номерах телефонов
    return text


def connect_numbers_and_words(text):
    # связывание чисел с последующими словами неразрывным пробелом
    return text

def clear_whitespaces(text):
    # удаление лишних пробелов и переносов строк
    return text

def connect_unions_and_words(text):
    # связывание союзов и любых слов из 1-2 символов с последующими словами
    return text


def beautify(text):
    if not text:
        return ''

    beautified_text = replace_quotes(text)
    beautified_text = replace_hyphen_with_dash_in_text(beautified_text)
    beautified_text = replace_hyphen_with_short_dash_in_phones(beautified_text)
    beautified_text = connect_numbers_and_words(beautified_text)
    beautified_text = clear_whitespaces(beautified_text)
    beautified_text = connect_unions_and_words(beautified_text)
    return beautified_text

@app.route('/', methods=['POST', 'GET'])
def form():
    input = request.form['text'] or '' if request.method == 'POST' else ''
    result = beautify(input)
    print({input, result})

    return render_template('form.html', input=input, result=result)


if __name__ == "__main__":
    app.run()
