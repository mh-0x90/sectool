# agents/function_parser.py
import ast

def parse_functions(code):
    tree = ast.parse(code)
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            inputs = [arg.arg for arg in node.args.args]
            functions.append({"name": func_name, "inputs": inputs})
    return functions

