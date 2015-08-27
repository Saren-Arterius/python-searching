#!/usr/bin/env python3
from os.path import join, realpath, dirname
from time import time

SCRIPT_PATH = dirname(realpath(__file__))
WORD_PATH = join(SCRIPT_PATH, "words.txt")

# Word list will be randomized each time
WORD_LIST = []
with open(WORD_PATH) as f:
    for line in f:
        line = line.strip()
        if line:
            WORD_LIST.append(line.lower())
WORD_LIST = set(WORD_LIST)


def df_search(from_word, to_word, visited=[]):
    visited.append(from_word)
    # print("DF visited", visited)
    for word in WORD_LIST - set(visited):
        if from_word[-1] != word[0]:
            continue
        if word == to_word:
            visited.append(word)
            return visited
        path = df_search(word, to_word, visited.copy())
        if path is None:
            continue
        return path


def bf_search(from_word, to_word, iterable=WORD_LIST):
    visited = []
    queue = [from_word]
    path = []
    discovered = {}
    while len(queue):
        search_word = queue.pop(0)
        if search_word not in path:
            path.append(search_word)
        discovered[search_word] = []
        for word in iterable:
            if search_word[-1] != word[0]:
                continue
            if word in visited:
                continue
            visited.append(word)
            queue.append(word)
            discovered[search_word].append(word)
            if word == to_word:
                path.append(to_word)
                return backtrace(path, discovered)


def backtrace(path, discovered):
    actual_path = [path[-1]]
    while actual_path[-1] != path[0]:
        unchanged = True
        for key, words in discovered.items():
            if actual_path[-1] in words:
                actual_path.append(key)
                unchanged = False
                break
        if unchanged:
            actual_path.append(path[0])
    actual_path.reverse()
    return actual_path


if __name__ == "__main__":
    print("Start time: ", time())
    # Depth first search does not guarantee finishing in reasonable time...
    print("DFS result", df_search("lol", "fuck"))
    print("End time of DFS: ", time())
    # Luckily, breadth first search does guarantee a shortest path.
    print("BFS result", bf_search("lol", "fuck"))
    print("End time of BFS: ", time())
