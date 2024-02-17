class IconMappingDictionary(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_value(self, key):
        return self.get(key, "Key not found")

    def add_key_value(self, key, value):
        self[key] = value

    def display(self):
        for key, value in self.items():
            print("Just Mapped:" + key + " to " + value)
        print("Mapping Complete. End of program.")
