from pathlib import Path

from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast


code = Path('code.js').read_text()

parser = Parser()
tree = parser.parse(code)

for node in nodevisitor.visit(tree):
    pass

print(tree.to_ecma())
