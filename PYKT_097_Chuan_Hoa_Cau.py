import sys
import re

class cau:
    def __init__(self, words, punct):
        self.words = words
        self.punct = punct
        
    def out(self):
        kq = " ".join(self.words)
        kq = kq.capitalize()
        return kq + self.punct

data = sys.stdin.read()
tokens = re.split(r'([.!?\n])', data)

kq = []
current_words = []

for t in tokens:
    if t in '.!?\n':
        if current_words:
            punct = t if t != '\n' else '.'
            kq.append(cau(current_words, punct))
            current_words = []
    else:
        current_words.extend(t.split())

if current_words:
    kq.append(cau(current_words, '.'))

for i in kq:
    print(i.out())