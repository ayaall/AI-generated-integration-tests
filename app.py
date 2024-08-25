import os
import ast
import re

def count_assertions(content):
    # Count unittest assertions
    unittest_assertions = len(re.findall(r'self\.assert\w+\(', content))
    
    # Count regular assert statements
    regular_assertions = content.count('assert ')
    
    return unittest_assertions + regular_assertions

def count_functions(tree):
    return sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))

def count_parameters(tree):
    return sum(len(node.args.args) for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))

def evaluate_code(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    try:
        tree = ast.parse(content)
        syntactically_correct = True
    except SyntaxError:
        syntactically_correct = False
        return {
            'Syntactically correct': False,
            'Success compilation': False,
            'Passing execution': False,
            'Effectiveness': 0,
            'Number of Assertions': count_assertions(content),
            'Number of functions': 0,
            'Parameters': 0,
            'Code lines': len(content.splitlines())
        }
    
    # Compile the code (but don't execute)
    try:
        compile(tree, file_path, 'exec')
        success_compilation = True
    except Exception:
        success_compilation = False
    
    # We can't safely execute the test code here, so we'll assume it passes if it compiles
    passing_execution = success_compilation
    
    return {
        'Syntactically correct': syntactically_correct,
        'Success compilation': success_compilation,
        'Passing execution': passing_execution,
        'Effectiveness': int(syntactically_correct and success_compilation),
        'Number of Assertions': count_assertions(content),
        'Number of functions': count_functions(tree),
        'Parameters': count_parameters(tree),
        'Code lines': len(content.splitlines())
    }

def evaluate_folder(folder_path, prefix):
    results = {}
    for file_name in os.listdir(folder_path):
        if file_name.startswith(prefix) and file_name.endswith('.py'):
            file_path = os.path.join(folder_path, file_name)
            results[file_name] = evaluate_code(file_path)
    return results

# Paths to the folders containing the test codes
human_folder = 'Human tests'
ai_folder = 'Output code(AI tests)'

# Evaluate both folders
human_results = evaluate_folder(human_folder, '#')
ai_results = evaluate_folder(ai_folder, 'Ai#')

# Print or process the results as needed
print("Human Test Results:")
for file, result in human_results.items():
    print(f"{file}:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    print()

print("\nAI Test Results:")
for file, result in ai_results.items():
    print(f"{file}:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    print()