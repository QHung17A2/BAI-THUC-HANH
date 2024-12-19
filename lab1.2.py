import json
class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    def read_json(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)
    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name: {user['name']}, Age: {user['age']}, Address: {user['address']}")
# Sử dụng lớp JSONReader
path = 'd:\\python\\python\\minhtu-45-dhkl17a2-23174600106\\bai_tap_thuc_hanh\\lab1\\users.json'
reader = JSONReader(path)
reader.read_json()
reader.display_data()

