# https://www.programiz.com/python-programming/precedence-associativity

add_combinations = [
    ('INT', 'INT','INT'),
    ('FLOAT', 'FLOAT','FLOAT'),
    ('INT', 'FLOAT','FLOAT'),
    ('STRING', 'STRING','STRING'),
    ('LIST', 'LIST','LIST'),
    ('TUPLE', 'TUPLE','TUPLE'),
]

subtract_combinations = [
    ('INT', 'INT','INT'),
    ('FLOAT', 'FLOAT','FLOAT'),
    ('INT', 'FLOAT','FLOAT'),
    ('SET', 'SET','SET'),
]

multiply_combinations = [
    ('INT', 'INT','INT'),
    ('FLOAT', 'FLOAT','FLOAT'),
    ('INT', 'FLOAT','FLOAT'),
    ('STRING', 'INT','STRING'),
    ('LIST', 'INT','LIST'),
    ('TUPLE', 'INT','TUPLE'),
    ('INT', 'BOOL','INT'),
]

divide_combinations = [
    ('INT', 'INT','FLOAT'),
    ('FLOAT', 'FLOAT','FLOAT'),
    ('INT', 'FLOAT','FLOAT'),
    ('INT', 'BOOL','FLOAT'),
]

mod_combinations = [
    ('INT', 'INT','INT'),
    ('FLOAT', 'FLOAT','FLOAT'),
    ('INT', 'FLOAT','FLOAT'),
    ('INT', 'BOOL', 'INT'),
]

exp_combinations = [
    ('INT', 'INT','INT'),
    ('FLOAT', 'FLOAT','FLOAT'),
    ('INT', 'FLOAT','FLOAT'),
    ('INT', 'BOOL', 'INT'),
]

xor_combinations = [
    ('INT', 'INT','INT'),
    ('INT', 'BOOL', 'INT'),
]

floor_divide_combinations = [
    ('INT', 'INT','INT'),
    ('FLOAT', 'FLOAT','FLOAT'),
    ('INT', 'FLOAT','FLOAT'),
    ('FLOAT', 'BOOL', 'FLOAT'),
]

left_shift_combinations = [
    ('INT', 'INT','INT'),
]
right_shift_combinations = [
    ('INT', 'INT','INT'),
]
and_combinations = [
    ('INT', 'INT','INT'),
    ('INT', 'BOOL', 'INT'),
]
or_combinations = [
    ('INT', 'INT','INT'),
    ('INT', 'BOOL', 'INT'),
]

comparison_combinations = [
    ('INT', 'INT','BOOL'),
    ('FLOAT', 'FLOAT','BOOL'),
    ('INT', 'FLOAT','BOOL'),
    ('STRING', 'STRING','BOOL'),
    ('LIST', 'LIST','BOOL'),
    ('TUPLE', 'TUPLE','BOOL'),
    ('SET', 'SET','BOOL'),
]

data_types = ['INT', 'FLOAT', 'STRING', 'LIS', 'TUPLE', 'SET', 'NONE', 'BOOL', 'DICT']
any_combinations = [(x, y) for i, x in enumerate(data_types) for y in data_types[i:]]

combinations = {
    "or":any_combinations,
    "and":any_combinations,
    "<":comparison_combinations,
    ">":comparison_combinations,
    "<=":comparison_combinations,
    ">=":comparison_combinations,
    "|":or_combinations,
    "^":xor_combinations,
    "&":and_combinations,
    "+":add_combinations,
    "-":subtract_combinations,
    "*":multiply_combinations,
    "/":divide_combinations,
    "%":mod_combinations,
    "**":exp_combinations,
    "//":floor_divide_combinations,
    "<<":left_shift_combinations,
    ">>":right_shift_combinations,
    "==":any_combinations,
    "!=":any_combinations,

}