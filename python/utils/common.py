import os.path

def read_token():
    with open(os.path.dirname(__file__) + "/../../TOKEN", 'r') as tok_file:
        TOKEN = tok_file.read()
        return TOKEN