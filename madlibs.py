from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_random_word(word_type):
    words = {
        'noun': ['dog', 'car', 'house', 'tree', 'computer'],
        'verb': ['run', 'jump', 'swim', 'drive', 'fly'],
        'adjective': ['happy', 'sad', 'quick', 'lazy', 'bright'],
        'adverb': ['quickly', 'silently', 'happily', 'sadly', 'brightly'],
        'place': ['park', 'beach', 'city', 'mountain', 'forest'],
        'exclamation': ['Wow', 'Yikes', 'Hooray', 'Oops', 'Eureka'],
    }
    return random.choice(words[word_type])

def create_story():

    story_template = (
        "{exclamation}! I can't believe I saw a {adjective} {noun} "
        "that could {verb} {adverb} in the {place}!"
    )

    story = story_template.format(
        exclamation=get_random_word('exclamation'),
        adjective=get_random_word('adjective'),
        noun=get_random_word('noun'),
        verb=get_random_word('verb'),
        adverb=get_random_word('adverb'),
        place=get_random_word('place'),
    )

    return story

@app.route('/')
def home():
    return create_story()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)