"""
2. Create a script that should find the line that you provided to it in the provided directory.
2a. On single thread
"""

import glob
import time


def find_by_pattern(filename, pattern):
    container = []
    with open(filename) as file:
        for line in file:
            if pattern in line:
                container.append(line)
    return container


def find_all_files(directory_path, pattern):
    files = glob.glob(f'{directory_path}/*.py')
    container = []
    for file in files:
        result = find_by_pattern(file, pattern)
        container.append(result)
    return container


if __name__ == '__main__':
    start = time.time()
    first = find_all_files('.', pattern='ThreadPoolExecutor')
    second = find_all_files('.', pattern='ProcessPoolExecutor')
    third = find_all_files('.', pattern='get_session')
    fourth = find_all_files('.', pattern='result.text')
    print(f'Total time for search {time.time() - start}')
    all_search = [first, second, third, fourth]
    
    for search in all_search:
        for element in search:
            print(element)

