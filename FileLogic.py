from __future__ import annotations
import os, json, sys
from enum import Enum

srcDIR = os.path.realpath(sys.path[0]) #Temporary for testi
#region PATHS
dataSourcePath = os.path.join(srcDIR, 'SOURCES')
baseSourcePath = os.path.join(dataSourcePath, 'BASE')
modSourcePath = os.path.join(dataSourcePath, 'MODS')
#endregion

def loadClasses() -> list:
    classFile = DataLoader.loadJSON('SOURCES' + os.sep + 'BASE' + os.sep + 'classes.json')
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
        ignorePATH = os.path.join(modSourcePath, 'ignore.json')
        if os.path.isfile(ignorePATH) is False:
            self.makeJSON(ignorePATH, {'IGNORE_LIST': []})
        
        ignoreList = self.loadJSON(ignorePATH)['IGNORE_LIST']
        self.ignoreCODES = [ignoreList[i] for i in range(len(ignoreList) - 1)]

    def checkBASE(self):
        if os.path.isdir(baseSourcePath) is False:
            os.makedirs(baseSourcePath)
        if os.path.isfile(baseSourcePath + os.sep + 'classes.json') is False:
            self.makeJSON(baseSourcePath + os.sep + 'classes.json', {"WAR":{"Name": "Warrior", "Base Health": 5, "Stat": "Strength"}, "WIZ":{"Name": "Wizard", "Base Health": 3, "Stat": "Mana"}})
        if os.path.isfile(baseSourcePath + os.sep + 'items.json') is False:
            self.makeJSON(baseSourcePath + os.sep + 'items.json', {"SWORD":{"Name": "Sword", "Stat": "Strength", "Value": 2, "Rating": 1, "Min Level": 1}})
        if os.path.isfile(baseSourcePath + os.sep + 'attributes.json') is False:
            self.makeJSON(baseSourcePath + os.sep + 'attributes.json', {"PLACEHOLDER": "I'm a placeholder!"})
    
    def loadBASE(self):
        classesJSONDATA = self.loadJSON(os.path.join(baseSourcePath, 'classes.json'))
        for classKEY, classDATA in classesJSONDATA.items():
            if classKEY not in self.ignoreCODES:
                self.appendClass(self.compileJSONtoClass(ClassType.CLASS, [classKEY, classDATA]))
        itemsJSONDATA = self.loadJSON(os.path.join(baseSourcePath, 'items.json'))
        for itemKEY, itemDATA in itemsJSONDATA.items():
            if classKEY not in self.ignoreCODES:
                self.appendItem(self.compileJSONtoClass(ClassType.ITEM, [itemKEY, itemDATA]))
        attributesJSONDATA = self.loadJSON(os.path.join(baseSourcePath, 'attributes.json'))
        for attributeKey, attributeDATA in attributesJSONDATA.items():
            if classKEY not in self.ignoreCODES:
                self.appendAttribute(self.compileJSONtoClass(ClassType.ATTRIBUTE, [attributeKey, attributeDATA]))

    def loadMODS(self):
        for subdir, dirs, files in os.walk(modSourcePath):
            for filename in files:
                if filename.endswith('.json') and filename.endswith('ignore.json') is False:
                    fileJSONDATA = self.loadJSON(os.path.join(modSourcePath, filename))
                    for modTARGET, modDATA in fileJSONDATA.items():
                        if modTARGET in ClassType._member_names_ and modDATA['Code'] not in self.ignoreCODES:
                            classRef = self.compileJSONtoClass(ClassType[modTARGET], modDATA)
                            if type(modTARGET) is ClassType.CLASS:
                                self.appendClass(classRef)
                            elif type(modTARGET) is ClassType.ITEM:
                                self.appendItem(classRef)
                            elif type(modTARGET) is ClassType.ATTRIBUTE:
                                self.appendAttribute(classRef)

    def getItems(self) -> list[type[Item]]:
        return self.items

    #region STATIC METHODS
    @staticmethod
    def checkFileStructure():
        if os.path.isdir(baseSourcePath) is False:
            os.makedirs(baseSourcePath)
        if os.path.isdir(modSourcePath) is False:
            os.makedirs(modSourcePath)

    @staticmethod
    def makeJSON(filePath:str, baseDATA:dict):
        with open(filePath, 'w', encoding='utf-8') as f:
            json.dump(baseDATA, f, ensure_ascii=False, indent=4)
        f.close()
    @staticmethod
    def loadJSON(filePath) -> dict:
        file = open(filePath)
        data = json.load(file)
        file.close()
        return data
    @staticmethod
    def compileJSONtoClass(classType:ClassType, jsonDATA:dict):
        return classType.value(jsonDATA)
    #endregion

    #region PROPERTIES
    @property
    def ignoreCODES(self) -> dict:
        return self.__ignoreCODES
    @ignoreCODES.setter
    def ignoreCODES(self, ignoreCODES:list):
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