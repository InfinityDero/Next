import functools


def longest_name(file_path):
    with open(file_path, 'r') as f:
        print(functools.reduce(lambda x, y: x if len(x) > len(y) else y, f.readlines(), ''))


def file_length(file_path):
    with open(file_path, 'r') as f:
        print(functools.reduce(lambda x, y:x + len(y.strip()), f.readlines(), 0))

def shortest_names(file_path):
     with open("C:\\bis\\next\\names.txt", 'r') as f:
        l = f.readlines()
        l.sort(key=len)
        print("\n".join([short_name.strip() for short_name in l if len(short_name.strip()) <= len(l[0])]))


def create_file_of_names_lengths(file_path, path_of_new_file):
    with open(file_path, 'r') as f:
        with open(path_of_new_file, 'w') as f_lengths: 
            f_lengths.writelines('\n'.join([str(len(name.strip())) for name in f.readlines()]))


def main():
    longest_name("C:\\bis\\next\\names.txt")
    file_length("C:\\bis\\next\\names.txt")
    shortest_names("C:\\bis\\next\\names.txt")
    create_file_of_names_lengths("C:\\bis\\next\\names.txt", "C:\\bis\\next\\names_length.txt")


if __name__ == "__main__":
    main()