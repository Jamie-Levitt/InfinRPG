from __future__ import annotations
import os, json
from enum import Enum

#region PATHS
dataSourcePath = os.path.realpath(__path__, 'SOURCES')
baseSourcePath = dataSourcePath + os.sep + 'BASE'
modSourcePath = dataSourcePath + os.sep + 'MODS'
#endregion

def loadClasses() -> list:
    classFile = DataLoader.loadJson('SOURCES' + os.sep + 'classes.json')
    classes = []
    for key, data in classFile.items(): classes.append([key, data])
    return classes

from CharacterLogic import Class
from ItemLogic import Item, Attribute

#region CLASS TYPES:
class ClassType(Enum):
    CLASS = Class
    ITEM = Item
    ATTRIBUTE = Attribute
#endregion

class DataLoader:
    def __init__(self):
        self.classes = []
        self.items = []
        self.attributes = []

        self.checkFileStructure()
        self.checkIgnore()
        self.checkBASE()
        self.loadBASE()
        self.loadMODS()
    
    def checkIgnore(self):
        try:
            ignorePATH = os.path.join(modSourcePath, 'ignore.json')
        except OSError:
            self.makeJSON(modSourcePath + os.sep + 'ignore.json')
            ignorePATH = os.path.join(modSourcePath, 'ignore.json')
        
        ignoreList = self.loadJSON(ignorePATH)['IGNORE_LIST']
        self.ignoreCODES = [ignoreList[i] for i in range(len(ignoreList) - 1)]

    def checkBASE(self):
        if os.path.isdir(baseSourcePath) is False:
            os.makedirs(baseSourcePath)
        if os.path.isfile(baseSourcePath + os.sep + 'classes.json') is False:
            self.makeJSON(baseSourcePath + os.sep + 'classes.json')
        if os.path.isfile(baseSourcePath + os.sep + 'items.json') is False:
            self.makeJSON(baseSourcePath + os.sep + 'items.json')
        if os.path.isfile(baseSourcePath + os.sep + 'attributes.json') is False:
            self.makeJSON(baseSourcePath + os.sep + 'attributes.json')
    
    def loadBASE(self):
        classesJSONDATA = self.loadJSON(os.path.join(baseSourcePath, 'classes.json'))
        for classDATA in classesJSONDATA:
            self.classes.append(self.compileJSONtoClass(classDATA))
        itemsJSONDATA = self.loadJSON(os.path.join(baseSourcePath, 'items.json'))
        for itemDATA in itemsJSONDATA:
            self.items.append(self.compileJSONtoItem(itemDATA))
        attributesJSONDATA = self.loadJSON(os.path.join(baseSourcePath, 'attributes.json'))
        for attributeDATA in attributesJSONDATA:
            self.attributes.append(self.compileJSONtoClass(attributeDATA))

    def loadMODS(self):
        for subdir, dirs, files in os.walk(modSourcePath):
            for filename in files:
                if filename.endswith('.json'):
                    fileJSONDATA = self.loadJSON(os.path.join(modSourcePath, filename))
                    for modTARGET, modDATA in fileJSONDATA:
                        if modTARGET in ClassType._member_names_:
                            classRef = self.compileJSONtoClass(ClassType[modTARGET], modDATA)
                            if type(modTARGET) is ClassType.CLASS:
                                self.appendClass(classRef)
                            elif type(modTARGET) is ClassType.ITEM:
                                self.appendItem(classRef)
                            elif type(modTARGET) is ClassType.ATTRIBUTE:
                                self.appendAttribute(classRef)

    #region STATIC METHODS
    @staticmethod
    def checkFileStructure():
        if os.path.isdir(baseSourcePath) is False:
            os.makedirs(baseSourcePath)
        if os.path.isdir(modSourcePath) is False:
            os.makedirs(modSourcePath)

    @staticmethod
    def makeJSON(filePath:str):
        with open(filePath, 'w') as file:
            json.dump({}, file)
        file.close()
    @staticmethod
    def loadJSON(filePath) -> dict:
        file = open(filePath)
        data = json.load(file)
        file.close()
        return data
    @staticmethod
    def compileJSONtoClass(classType:ClassType, jsonDATA:dict):
        return classType(jsonDATA)
    #endregion

    #region PROPERTIES
    @property
    def ignoreCODES(self) -> dict:
        return self.__ignoreCODES
    @ignoreCODES.setter
    def ignoreCodes(self, ignoreCODES:dict):
        self.__ignoreCODES = ignoreCODES

    @property
    def classes(self) -> list[type[Class]]:
        return self.__classes
    @classes.setter
    def classes(self, classes:list[type[Class]]):
        self.__classes = classes
    def appendClass(self, classDICT: Class | list[type[Class]]):
        self.__classes.append(classDICT)

    @property
    def items(self) -> list[type[Item]]:
        return self.__items
    @items.setter
    def items(self, items:list[type[Item]]):
        self.__items = items
    def appendItem(self, itemDICT: Item | list[type[Item]]):
        self.__items.append(itemDICT)

    @property
    def attributes(self) -> list[type[Attribute]]:
        return self.__attributes
    @attributes.setter
    def attributes(self, attributes:list[type[Attribute]]):
        self.__attributes = attributes
    def appendAttribute(self, attributeDICT: Attribute | list[type[Attribute]]):
        self.__attributes.append(attributeDICT)
    #endregion