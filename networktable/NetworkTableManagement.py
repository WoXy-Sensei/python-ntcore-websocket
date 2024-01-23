class NetworkTableManagement:
    entries = {}

    @staticmethod
    def add_entry(entry):
        name = str(entry.getName().split('/')[-1])
        NetworkTableManagement.entries[name] = entry
        return entry

    @staticmethod
    def remove_entry(entry):
        NetworkTableManagement.entries.pop(entry.getName().split('/')[-1])
        return entry

    @staticmethod
    def get_entry(name):
        return NetworkTableManagement.entries[name]

    @staticmethod
    def get_entries():
        return NetworkTableManagement.entries

    @staticmethod
    def set_entry(entryName, value):
        entry = NetworkTableManagement.entries[entryName]
        entry.setInteger(value)
        print(entry.getValue())
        return entry
