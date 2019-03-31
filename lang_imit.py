# -*- coding: utf-8 -*-
"""
lang_imit.py
Kind of imitates a language given a sample from it
"""

import numpy.random as random
import string


class LanguageGenerator:
    """Imitate a language from a given sample

    >>> language_sample = 'A hat'
    >>> generator = LanguageGenerator(language_sample)
    >>> generator.to_string()
    {'a': {None: 1, 't': 1}, 'h': {'a': 1}, 't': {None: 1}}
    """

    class Character:
        def __init__(self):
            self.map = {}

        def add(self, char):
            self.map[char] = self.map[char]+1 if char in self.map else 1

        def get(self):
            return random.choice(list(self.map.keys()), p=list(normalize(self.map).values()))

        def to_string(self):
            return self.map

    def __init__(self, sample=None):
        self.start = self.Character()
        self.map = {}
        if sample:
            self.analyze(sample)

    def analyze(self, sample, separator=' '):
        """
        Analyze a sample of text
        >>> generator = LanguageGenerator()
        >>> generator.analyze('geek gals only')
        >>> generator.start.to_string()
        {'g': 2, 'o': 1}
        >>> generator = LanguageGenerator()
        >>> generator.analyze('go ag')
        >>> generator.to_string()
        {'g': {'o': 1, None: 1}, 'o': {None: 1}, 'a': {'g': 1}}
        """
        assert isinstance(sample, str), \
            f'Expected dict but got {type(sample)}'
        for word in sample.split(separator):
            self._analyze(word)

    def _analyze(self, word):
        """
        Analyze a word
        >>> generator = LanguageGenerator()
        >>> generator._analyze('abcab')
        >>> generator.start.to_string()
        {'a': 1}
        >>> generator.to_string()
        {'a': {'b': 2}, 'b': {'c': 1, None: 1}, 'c': {'a': 1}}
        """
        word = clean(word)
        for char in word:
            if char not in self.map:
                self.map[char] = self.Character()

        self.start.add(word[0])
        for i in range(len(word)):
            char = word[i]
            next_char = word[i+1] if i < len(word)-1 else None
            self.map[char].add(next_char)

    def generate_word(self):
        string = ''
        char = self.start.get()
        while char is not None:
            string += char
            char = self.map[char].get()
        return string

    def generate_sentence(self):
        string = ''
        for _ in range(5):
            string += self.generate_word() + ' '
        string = string[0].upper() + string[1:-1] + '.'
        return string

    def to_string(self):
        return {key: self.map[key].to_string() for key in self.map.keys()}


def normalize(dic):
    """
    Normalize dictionary values

    >>> normalize({'a': 1, 'b': 1})
    {'a': 0.5, 'b': 0.5}
    """
    assert isinstance(dic, dict), \
        f'Expected dict but got {type(dic)}'
    dic_sum = sum(dic.values())
    return {k: v/dic_sum for k, v in dic.items()}


def clean(s):
    """Convert to lowercase and remove characters 
    not in alphabet

    >>> clean('A!2bcD#EFg')
    'abcdefg'
    """
    assert isinstance(s, str), \
        f'Expected string but got {type(s)}'
    clean_string = ''
    for char in s.lower():
        if char in string.ascii_lowercase:
            clean_string += char
    return clean_string
