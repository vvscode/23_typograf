import re
from flask import Flask, request, render_template

app = Flask(__name__)


def is_match_inside_tag(match: re.Match):
    original_string: str = match.string
    start = match.start(0)
    end = match.end(0)

    prev_open_tag = original_string.rfind('<', 0, start)
    prev_close_tag = original_string.rfind('>', 0, start)
    next_open_tag = original_string.find('<', end)
    next_close_tag = original_string.find('>', end)

    return prev_open_tag > prev_close_tag and next_open_tag > next_close_tag


def replace_quotes_helper(match: re.Match):
    if is_match_inside_tag(match):
        return match.group(0)
    return '«{}»'.format(match.group(1))


def replace_quotes(text):
    # replace ' / " to  « »
    processed_text = re.sub(r'"(.+?)"', replace_quotes_helper, text)
    processed_text = re.sub(r"'(.+?)'", replace_quotes_helper, processed_text)
    return processed_text


def replace_hyphen_with_dash_in_text(text):
    processed_text = re.sub(r'(\w) -+(\w)', r'\1 — \2', text)
    processed_text = re.sub(r'(\w)-+ (\w)', r'\1 — \2', processed_text)
    processed_text = re.sub(r'(\w) -+ (\w)', r'\1 — \2', processed_text)
    return processed_text


def replace_hyphen_with_short_dash_in_phones(text):
    processed_text = re.sub(r'(\d)-(\d)', r'\1–\2', text)
    return processed_text


def connect_numbers_and_words(text):
    processed_text = re.sub(r'(\d)\s+(\w)', r'\1&nbsp;\2', text)
    return processed_text


def clear_whitespaces(text):
    processed_text = re.sub(r'(\s)+', r'\1', text)
    return processed_text


def connect_unions_and_words_helper(match: re.Match):
    if len(match.group(1)) > 2:
        return match.group(0)

    if is_match_inside_tag(match):
        return match.group(0)

    return '{}&nbsp;{}'.format(match.group(1), match.group(2))


def connect_unions_and_words(text):
    processed_text = re.sub(r'(\w+)\s+(\w)', connect_unions_and_words_helper, text)
    return processed_text


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
    
    return render_template('form.html', input=input, result=result)


if __name__ == '__main__':
    app.run()
