import re


def replace_quotes(text):
    # replace ' / " to  « »
    processed_text = re.sub(r'(?![^<]+>)("(.+?)")', r'«\2»', text)
    processed_text = re.sub(r"(?![^<]+>)('(.+?)')", r'«\2»', processed_text)
    return processed_text


def replace_hyphen_with_dash_in_text(text):
    processed_text = re.sub(r'(?![^<]+>)((\w) -+(\w))', r'\2 — \3', text)
    processed_text = re.sub(r'(?![^<]+>)((\w)-+ (\w))', r'\2 — \3', processed_text)
    processed_text = re.sub(r'(?![^<]+>)((\w) -+ (\w))', r'\2 — \3', processed_text)
    return processed_text


def replace_hyphen_with_short_dash_in_phones(text):
    processed_text = re.sub(r'(?![^<]+>)((\d)-(\d))', r'\2–\3', text)
    return processed_text


def connect_numbers_and_words(text):
    processed_text = re.sub(r'(?![^<]+>)((\d)\s+(\w))', r'\2&nbsp;\3', text)
    return processed_text


def clear_whitespaces(text):
    processed_text = re.sub(r'(?![^<]+>)((\s)+)', r'\2', text)
    return processed_text


def connect_unions_and_words(text):
    processed_text = re.sub(
        r'(?![^<]+>)((\b\w{1,2})\s+(\w))', r'\2&nbsp;\3', text)
    # to handle overlapping rexexps
    processed_text = re.sub(
        r'(?![^<]+>)((\b\w{1,2})\s+(\w))', r'\2&nbsp;\3', processed_text)
    return processed_text


def beautify(text):
    beautified_text = replace_quotes(text)
    beautified_text = replace_hyphen_with_dash_in_text(beautified_text)
    beautified_text = replace_hyphen_with_short_dash_in_phones(beautified_text)
    beautified_text = connect_numbers_and_words(beautified_text)
    beautified_text = clear_whitespaces(beautified_text)
    beautified_text = connect_unions_and_words(beautified_text)
    return beautified_text
