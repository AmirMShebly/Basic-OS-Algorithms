import time
import copy


FILE_TYPES = {
    "doc": "Word Document",
    "txt": "Text Document",
    "py": "Python script"

}


class File:
    def __init__(self, name, size, file_type):
        self.name = name
        self.size = size
        self.file_type = file_type
        self.created_at = time.time()
        self.modified_at = self.created_at
        self.owner = "user"
        self.permissions = "rw-rw-r--"

    def get_file_type(self):
        return FILE_TYPES.get(self.file_type, "Unknown")

    def set_permissions(self, permissions):
        self.permissions = permissions

    def set_owner(self, owner):
        self.owner = owner

    def get_metadata(self):
        return {
            "Name": self.name,
            "Size": f"{self.size}KB",
            "Type": self.get_file_type(),
            "Created At": time.ctime(self.created_at),
            "Modified At": time.ctime(self.modified_at),
            "Owner": self.owner,
            "Permissions": self.permissions
        }


class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = {}

    def add_file(self, file):
        if file.name not in self.contents:
            self.contents[file.name] = file
            print(f"File '{file.name}' added to directory '{self.name}'.")
        else:
            print(f"File '{file.name}' already exists in directory '{self.name}'.")

    def add_directory(self, directory):
        if directory.name not in self.contents:
            self.contents[directory.name] = directory
            print(f"Directory '{directory.name}' added to directory '{self.name}'.")
        else:
            print(f"Directory '{directory.name}' already exists in directory '{self.name}'.")

    def search_file(self, filename):
        found = False
        if filename in self.contents and isinstance(self.contents[filename], File):
            print(f"File '{filename}' found in directory '{self.name}'.")
            found = True
        else:
            for item in self.contents.values():
                if isinstance(item, Directory):
                    if item.search_file(filename):
                        found = True

        return found

    def search_file_recursive(self, filename):
        found = self.search_file(filename)
        if not found:
            print(f"File '{filename}' not found")

    def delete_file(self, filename):
        if filename in self.contents and isinstance(self.contents[filename], File):
            del self.contents[filename]
            print(f"File '{filename}' deleted from directory '{self.name}'.")
        else:
            print(f"File '{filename}' not found in directory '{self.name}'.")

    def move_file(self, filename, destination_directory):
        if filename in self.contents and isinstance(self.contents[filename], File):
            file = self.contents[filename]
            del self.contents[filename]
            destination_directory.add_file(copy.deepcopy(file))
            print(f"File '{filename}' moved from '{self.name}' to '{destination_directory.name}'.")
        else:
            print(f"File '{filename}' not found in directory '{self.name}'.")

    def rename_file(self, old_name, new_name):
        if old_name in self.contents and isinstance(self.contents[old_name], File):
            file = self.contents[old_name]
            del self.contents[old_name]
            file.name = new_name
            self.add_file(file)
            print(f"File '{old_name}' renamed to '{new_name}' in directory '{self.name}'.")
        else:
            print(f"File '{old_name}' not found in directory '{self.name}'.")

    def copy_file(self, filename, destination_directory):
        if filename in self.contents and isinstance(self.contents[filename], File):
            file = self.contents[filename]
            destination_directory.add_file(copy.deepcopy(file))
            print(f"File '{filename}' copied from '{self.name}' to '{destination_directory.name}'.")
        else:
            print(f"File '{filename}' not found in directory '{self.name}'.")

    def list_contents(self, depth=0, sort_by="name"):
        indent = "  " * depth
        print(f"{indent}Contents of directory '{self.name}', sorted by {sort_by}:")

        if sort_by == "name":
            sorted_files = sorted(self.contents.values(),
                                  key=lambda x: getattr(x, "name", 0) if isinstance(x, File) else 0)
        elif sort_by == "size":
            sorted_files = sorted(self.contents.values(),
                                  key=lambda x: getattr(x, "size", 0) if isinstance(x, File) else 0)
        elif sort_by == "modified":
            sorted_files = sorted(self.contents.values(),
                                  key=lambda x: getattr(x, "modified_at", 0) if isinstance(x, File) else 0)
        else:
            sorted_files = list(self.contents.values())

        for item in sorted_files:
            if isinstance(item, File):
                print(
                    f"{indent}- File: {item.name}, Size: {item.size}KB, Type: {item.get_file_type()},"
                    f" Modified At: {time.ctime(getattr(item, 'modified_at', 0))}")
            elif isinstance(item, Directory):
                item.list_contents(depth + 1, sort_by)


root = Directory("Root")
docs = Directory("Documents")
code = Directory("Code")

resume = File("resume.doc", 150, "doc")
essay = File("essay.txt", 80, "txt")
script = File("script.py", 120, "py")

docs.add_file(resume)
docs.add_file(essay)
code.add_file(script)

root.add_directory(docs)
root.add_directory(code)

print("\n---- Sorting the existing files ----")
root.list_contents(sort_by="name")
root.list_contents(sort_by="size")
root.list_contents(sort_by="modified")

print("\n---- Additional features ----")
docs.rename_file("essay.txt", "new_essay.txt")
docs.delete_file("nonexistent_file.txt")
code.move_file("script.py", docs)
docs.copy_file("new_essay.txt", code)

print("\n---- Searching ----")
root.search_file_recursive("script.py")
root.search_file_recursive("nonexistent_file.txt")

print("\n---- File Metadata ----")
print(resume.get_metadata())
print(essay.get_metadata())
print(script.get_metadata())

