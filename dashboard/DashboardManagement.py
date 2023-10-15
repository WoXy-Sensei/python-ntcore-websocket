class DashboardManagement:
    entries = {}

    @staticmethod
    def add_entry(entry):
        name = str(entry.getName().split('/')[-1])
        DashboardManagement.entries[name] = entry
        return entry

    @staticmethod
    def remove_entry(entry):
        DashboardManagement.entries.pop(entry.getName().split('/')[-1])
        return entry

    @staticmethod
    def get_entry(name):
        return DashboardManagement.entries[name]

    @staticmethod
    def get_entries():
        return DashboardManagement.entries

    @staticmethod
    def set_entry(entryName, value):
        entry = DashboardManagement.entries[entryName]
        entry.setInteger(value)
        print(entry.getValue())
        return entry
