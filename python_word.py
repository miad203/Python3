import requests
import re
from html import escape

def html_to_text(url):
    response = requests.get(url)
    return response.text


def word_finder(text):
    word = re.findall(r'<label class="cursor_link">(.*?)<', text)
    for each_word in word:
        each_word = escape(each_word)
        print(each_word)


if __name__ == '__main__':
    print('Starting....')
    words = word_finder(html_to_text(
        'https://www.bdword.com/english-to-bengali-dictionary-learn-3000-plus-common-words'))
