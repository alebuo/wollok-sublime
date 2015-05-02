import re

# regex = (
#     r'^(?P<file>.+?):(?P<line>\d+):(?P<col>\d+): '
#     r'(?P<error>ERROR) '
#     r'(?P<message>.+)'
# )

regex = (
    r'^(?P<file>.+?):(?P<line>\d+):(?P<col>\d+) '
    r'(?:((?P<error>ERROR)|(?P<warning>WARNING))) '
    r'(?P<message>.+)'
)

p = re.compile(regex)

m = p.match('Users/jfernandes/dev/data/repo/wollok/wollok-tests/src/wollok/classes/templateMethod-program.wlk:5:1 ERROR Wrong number of arguments. Should be ()')

print('file ' + m.group('file'))

print('line ' + m.group('line'))

print('col ' + m.group('col'))

print('error ' + m.group('error'))

print('Message ' + m.group('message'))