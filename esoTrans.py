# -*- coding: utf-8 -*-
# Esolang compiler or something

# read the input file (extension is '.me')

import sys

filename = sys.argv[1]

f = open(filename + '.py', 'r', encoding='utf-8')

code = f.read()

# dictionary of words to be swapped

swap = {
            'gamming' : 'for',
            'economy' : 'while',
            'shitpost' : 'in',
            '@heretic' : 'if',
            'wtf' : 'else',
            'seOH' : 'elif',
            'whiny' : 'try',
            'shitbaby' : 'except',
            'clong' : 'break',
            'clobbong' : 'continue',
            'cirno' : 'input',
            'gebneralk' : 'class',
            'meme' : 'def',
            'jeff' : 'return',
            'sex' : '-',
            'yang' : '+', 
            'gec' : '%',
            'anim' : '==',
            ' boner ' : ' = ',
            ' unfunwaa ' : ' < ',
            ' funwaa ' : ' > ',
            'strikesy' : '<=',
            'tero' : '>=',
            'xon' : 'and',
            'detecotb' : 'or',
            'fuck' : 'is',
            'zenzi' : 'not',
            'hpock' : 'import',
            'tysob' : 'from',
            'blorgia' : 'as',
            'dick' : 'with',
            'server_for_anime' : 'True',
            'server_not_for_anime' : 'False',
            'Ele_' : 'None',
            'ban' : 'del',
            'shit' : 'print',
            'zœœp' : 'yield',
            'troll' : 'lambda',
            'ADL' : 'raise',
            'oil' : 'pass',
            'zoomer' : 'nonlocal', 
            'boomer' : 'global',
            'doge' : 'finally',
            'sus' : 'await',
            'amongus' : 'assert',
            'chungus' : 'async',
            'blacksheets' : 'dict',
            'thumbnail' : 'str',
            'xomc' : 'int',
            'dicde' : 'double',
            'soinenr' : 'float',
            'touhou' : 'chr',
            'osu' : 'map',
            'reimu' : 'set',
            'based' : 'max',
            'cringe' : 'min',
            '⑨' : 'range',
            'mips' : 'round',
            'vig' : 'sum',
            'privilege' : 'super',
            'dino' : 'tuple',
            'rshig' : 'zip',
            'racism' : 'type',
            'dong' : 'len',
            'balls' : 'list',
            'jeb' : 'open',
            'femboy' : 'join',
            'epyc' : 'file',
            'skeet' : 'split',
            'goof' : 'append',
            'cock' : 'run',
            'cumburger' : '[]',
            'eburger' : '\'\'',
            'shart' : 'message',
            'sprite' : 'event'
}

swap = dict(zip(swap.values(),swap.keys()))

new = code

for item in swap: new = new.replace(item, swap[item])

f.close()

# now we just have regular python code

with open(filename + '.me', 'w+', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n' + new)
