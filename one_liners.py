import functools


def longest_name(file_path):
    with open(file_path, 'r') as f:
        print(functools.reduce(lambda x, y: x if len(x) > len(y) else y, f.readlines(), ''))


def main():
    longest_name("C:\\bis\\next\\names.txt")


if __name__ == "__main__":
    main()