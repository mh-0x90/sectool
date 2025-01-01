# agents/orchestrator.py
from agents.function_parser_java import parse_functions
from agents.sql_vulnerability import find_sql_injections

def orchestrate_code_analysis(code):
    functions = parse_functions(code)
    vulnerabilities = find_sql_injections(code)
    
    return {
        "functions": functions,
        "vulnerabilities": vulnerabilities,
    }

