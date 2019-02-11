import unittest
from server import replace_quotes, replace_hyphen_with_dash_in_text, \
    replace_hyphen_with_short_dash_in_phones, connect_numbers_and_words, clear_whitespaces, \
    connect_unions_and_words, beautify


class TestTextBeautifier(unittest.TestCase):
    def test_replace_quotes1(self):
        self.assertEqual(replace_quotes('"1234"'), '«1234»')

    def test_replace_quotes2(self):
        self.assertEqual(replace_quotes("'1234'"), '«1234»')

    def test_replace_quotes3(self):
        self.assertEqual(replace_quotes('"1234" 56 \'7\' 8'), '«1234» 56 «7» 8')

    def test_replace_hyphen_with_dash_in_text1(self):
        self.assertEqual(replace_hyphen_with_dash_in_text('Apple - is a fruit'),
                         'Apple — is a fruit')

    def test_replace_hyphen_with_dash_in_text2(self):
        self.assertEqual(replace_hyphen_with_dash_in_text('Apple -- is a fruit'),
                         'Apple — is a fruit')

    def test_replace_hyphen_with_dash_in_text3(self):
        self.assertEqual(replace_hyphen_with_dash_in_text('Apple- is a fruit'),
                         'Apple — is a fruit')

    def test_replace_hyphen_with_dash_in_text4(self):
        self.assertEqual(replace_hyphen_with_dash_in_text('Apple -is a fruit'),
                         'Apple — is a fruit')

    def test_replace_hyphen_with_short_dash_in_phones1(self):
        self.assertEqual(replace_hyphen_with_short_dash_in_phones('123-456-789'),
                         '123–456–789')

    def test_replace_hyphen_with_short_dash_in_phones2(self):
        self.assertEqual(replace_hyphen_with_short_dash_in_phones('123 456-789'),
                         '123 456–789')

    def test_connect_numbers_and_words1(self):
        self.assertEqual(connect_numbers_and_words('1 apple'), '1&nbsp;apple')

    def test_connect_numbers_and_words2(self):
        self.assertEqual(connect_numbers_and_words('23 maps'), '23&nbsp;maps')

    def test_connect_numbers_and_words3(self):
        self.assertEqual(connect_numbers_and_words('0 apples'), '0&nbsp;apples')

    def test_clear_whitespaces1(self):
        self.assertEqual(clear_whitespaces('I  am'), 'I am')

    def test_clear_whitespaces2(self):
        self.assertEqual(clear_whitespaces('We are   the heroes  '), 'We are the heroes ')

    def test_clear_whitespaces3(self):
        self.assertEqual(clear_whitespaces('I need\n\nYour  help'), 'I need\nYour help')

    def test_clear_whitespaces4(self):
        self.assertEqual(clear_whitespaces('I need\n \nYour  help'), 'I need\nYour help')

    def test_connect_unions_and_words1(self):
        self.assertEqual(connect_unions_and_words('the dog'), 'the dog')

    def test_connect_unions_and_words2(self):
        self.assertEqual(connect_unions_and_words('an apple'), 'an&nbsp;apple')

    def test_connect_unions_and_words3(self):
        self.assertEqual(connect_unions_and_words('an apple'), 'an&nbsp;apple')

    def test_connect_unions_and_words4(self):
        self.assertEqual(connect_unions_and_words('it is my dog'), 'it&nbsp;is&nbsp;my&nbsp;dog')

    def test_custom_beautify_case1(self):
        self.assertEqual(beautify('<p class="item">Hi</p>'), '<p class="item">Hi</p>')

if __name__ == '__main__':
    unittest.main()
