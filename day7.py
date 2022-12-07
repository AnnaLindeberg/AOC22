# Day 7 of Advent of Code 2022: No Space Left On Device
# https://adventofcode.com/2022/day/7


def readDir(handle):
    file_tree = {}
    for line in handle:
        line = line.strip().split()
        if line[0] == '$' and line[1] == 'cd':
            if line[2] == '..':
                return file_tree
            else:
                file_tree[line[2]] = readDir(handle)
        elif line[0] == 'dir' or line[0] == '$':
            # no need to do anything for directories and ls-commands
            continue
        else:
            # found a file
            file_tree[line[1]] = int(line[0])
    return file_tree

def dirSizes(file_system):
    size_storer = {}

    def rec(file_sys):
        size = 0
        for dir, data in file_sys.items():
            if isinstance(data, dict):
                nested_size = rec(data)
                size += nested_size
                if dir not in size_storer:
                    size_storer[dir] = [nested_size]
                else:
                    size_storer[dir].append(nested_size)
            else:
                size += data
        return size

    rec(file_system)
    return size_storer

def printFileSystem(fs, indent = 0):
    for dir, data in fs.items():
        if isinstance(data, dict):
            print('\t'*indent, f"- {dir} (dir)")
            printFileSystem(data, indent + 1)
        else:
            print('\t'*indent,f"- {dir} (file, size={data})")


with open("input7.txt") as file:
    file_sys = readDir(file)

directorySizes = dirSizes(file_sys)

# for task 1
tot = 0

# for task 2
maxSpace = 70000000
spaceNeeded = 30000000
spaceNow = maxSpace - directorySizes['/'][0]
# looking for smallest directory size k such that spaceNow + k >= spaceNeeded
k = spaceNeeded # overkill initialization


for dir, sizes in directorySizes.items():
    for size in sizes:
        # task 1
        if size <= 100000:
            tot += size
        # task 2
        if spaceNow + size >= spaceNeeded and k > size:
            k = size


print(f"Task 1 {tot}\nTask 2 {k}")


