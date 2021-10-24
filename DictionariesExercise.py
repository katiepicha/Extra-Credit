from textblob import TextBlob
from pathlib import Path

John = TextBlob(Path("book of John text.txt").read_text())

words = ['Father', 'God', 'Christ', 'Spirit', 'life', 'man']

for w in words:
    print(w + ':', John.words.count(w))