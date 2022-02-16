import re

IRREGULAR_PLURALS = {
    'aircraft': 'aircraft',
    'alumna': 'alumnae',
    'alumnus': 'alumni',
    'analysis': 'analyses',
    'antenna': 'antennas',
    'antithesis': 'antitheses',
    'appendix': 'appendices',
    'axis': 'axes',
    'bacillus': 'bacilli',
    'bacterium': 'bacteria',
    'basis': 'bases',
    'bison': 'bison',
    'cactus': 'cacti',
    'chateau': 'chateaux',
    'child': 'children',
    'codex': 'codices',
    'corpus': 'corpora',
    'crisis': 'crises',
    'criterion': 'criteria',
    'curriculum': 'curricula',
    'datum': 'data',
    'deer': 'deer',
    'diagnosis': 'diagnoses',
    'die': 'dice',
    'dwarf': 'dwarves',

    'foot': 'feet',
    'goose': 'geese',
}
def pluralize(noun):
    ''' Make regular nouns plural. '''
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'

print(pluralize('bureau'))
