import os
import json

def collect_data(src_dir, tests_dir):
    data = []

    # Function to read test files and strip the specific phrase from the input
    def get_test_functions(test_file_path):
        with open(test_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        functions = []
        current_function = []
        inside_function = False
        
        for line in lines:
            if line.strip().startswith('def '):
                if current_function:
                    functions.append(''.join(current_function))
                    current_function = []
                inside_function = True
            if inside_function:
                current_function.append(line)
        
        if current_function:
            functions.append(''.join(current_function))
        
        return functions

    # Process the source and test directories
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Processing source file: {file_path}")
                # Assuming integration test functions are collected from tests_dir
                for test_file in os.listdir(tests_dir):
                    test_file_path = os.path.join(tests_dir, test_file)
                    if test_file.endswith('.py'):
                        print(f"Found test file: {test_file_path}")
                        test_functions = get_test_functions(test_file_path)
                        for func in test_functions:
                            # Create the instruction and strip the unwanted phrase
                            instruction = "Write an integration test for the following code:"
                            input_code = func  # The code from the test function
                            output_code = func  # Placeholder: you may want to refine this
                            data.append({"instruction": instruction, "input": input_code, "output": output_code})

    # Save to JSON file
    output_file = 'dataset.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Collected {len(data)} entries with instruction, input, and output. Saved to {output_file}.")

def main():
    src_dir = 'src/oscar/apps'
    tests_dir = 'tests/integration'
    collect_data(src_dir, tests_dir)

if __name__ == '__main__':
    main()
