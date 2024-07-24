import os, json

def loadJson(filePath) -> dict:
    file = open(filePath)
    data = json.load(file)
    file.close()
    return data

def loadClasses() -> list:
    classFile = loadJson('SOURCES' + os.sep + 'classes.json')
    classes = []
    for key, data in classFile.items(): classes.append([key, data])
    return classes