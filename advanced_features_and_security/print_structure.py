import os

def print_tree(startpath, indent=''):
    for item in os.listdir(startpath):
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print(f"{indent}📁 {item}/")
            print_tree(path, indent + '    ')
        else:
            print(f"{indent}📄 {item}")

print_tree('.')
