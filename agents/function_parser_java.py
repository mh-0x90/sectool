import javalang

def parse_functions(code):
    """
    Parse Java code to extract functions and their inputs.
    """
    functions = []
    try:
        tree = javalang.parse.parse(code)
        for _, node in tree.filter(javalang.tree.MethodDeclaration):
            func_name = node.name
            inputs = [param.name for param in node.parameters]
            functions.append({"name": func_name, "inputs": inputs})
    except javalang.parser.JavaSyntaxError as e:
        print(f"Error parsing Java code: {e}")
    return functions