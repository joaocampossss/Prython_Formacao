
"""
 tests = [
            ['last', 'lest', 'list', 'lost', 'lust'],
            ['beryl', 'jigsawed', 'oospheres', 'troweller', 'volcanizes'],
            ['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
             'blander', 'blastular', 'blawort', 'blender', 'blimbing',
             'blinder', 'blistered', 'blocks', 'blonde', 'blonder',
             'blotchier', 'blowlamp', 'blue', 'bluejays', 'blunder'],
        ]

        solutions = [
            [['last', 'lest', 'list', 'lost', 'lust']],
            [],
            [['blander', 'blender', 'blinder', 'blonder', 'blunder']]
        ]
"""

vowels = 'aeiou'
possivel_solução = []

def find_solutions(words):
    """Searches for solutions to the game returning a list of all solutions."""
    if not possivel_solução:
        possivel_solução.append(words)
    return []

# words_list = ['last', 'lest', 'list', 'lost', 'lust', 'cona']
words_list = ['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
             'blander', 'blastular', 'blawort', 'blender', 'blimbing',
             'blinder', 'blistered', 'blocks', 'blonde', 'blonder',
             'blotchier', 'blowlamp', 'blue', 'bluejays', 'blunder']

# char_sets = [set(word) for word in words_list]

# common_letters = list(set.intersection(*char_sets))
test=zip('last', 'lest')

for i in test:
    print(i)


print(test)
