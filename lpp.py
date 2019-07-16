import sys, os, re

# check for Python version [3.x required]
if sys.version < 3:
    print('This script is designed for Python 3.x.\nExiting...')
    sys.exit(0)

# check validity of path provided as argument
def check_validity(path: str) -> bool:
    # append current directory path if
    if not path.startswith('/'):
        path = os.path.dirname(os.path.realpath(__file__)) + '/' + path
    pattern = re.compile(r'(/\w+)+')
    if pattern.match(path) and os.direxists(path):
        return True
    return False


