import sys

from isort import SortImports


if __name__ == '__main__':
    path = sys.argv[1]
    SortImports(path, check=True, show_diff=True)
