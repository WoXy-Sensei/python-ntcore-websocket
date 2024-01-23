import json

class Entry:
    def __init__(self,entryName,entryValue,entryType) -> None:
        self.entryName = entryName
        self.entryValue = entryValue
        self.entryType = entryType

    def getEntryName(self):
        return self.entryName

    def getEntryValue(self):
        return self.entryValue

    def getEntryType(self): 
        return self.entryType

    def getByObject(self):
        return {
            "name" : self.entryName,
            "value" : self.entryValue,
            "type" : self.entryType
        }

    def getByJson(self):
        return json.dumps(self.getByObject())