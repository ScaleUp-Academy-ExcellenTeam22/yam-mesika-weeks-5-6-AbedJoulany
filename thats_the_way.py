import os


def get_files():
    path = input("enter the file path: ")
    arr = []
    for file in os.listdir(path):
        if file.startswith("deep"):
            arr.append(file)
    return arr


if __name__ == '__main__':
    files = get_files()
    print(files)
