import os

logs_path = input("Enter the logs file path: ")
files_list = os.listdir(logs_path)
os.chdir(logs_path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())


def adding_to_list(file_path):
    with open(file_path, 'r') as f:
        event = f.read()

    return event

def adding_logs_to_list():
    event_list = []
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{logs_path}\{file}"
            read_text_file(file_path)

            event_list.append(adding_to_list(file_path))

    return event_list

def


print(adding_logs_to_list())