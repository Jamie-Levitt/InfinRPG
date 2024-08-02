from __future__ import annotations
import os, sys
from FileTools import (baseSourcePath, dataSourcePath, modSourcePath, modSourcePath,
                       makeJSON, ensureJSONFile, ensureFolder, loadJSON, compileJSONtoClass,
                       ClassType)
from beartype import beartype
from DataTypes import RefCode

from CharacterLogic import Class
from ItemLogic import Item
from Attributes import Attribute

#region CLASS TYPES:
#endregion

class DataLoader:
    def __init__(self):
        self.classes = {}
        self.items = {}
        self.attributes = {}
    
    def checkIgnore(self):
        ignorePATH = os.path.join(modSourcePath, 'ignore.json')
        ensureJSONFile(ignorePATH, {'IGNORE_LIST': []})
        
        ignoreList = self.loadJSON(ignorePATH)['IGNORE_LIST']
        self.ignoreCODES = [ignoreList[i] for i in range(len(ignoreList) - 1)]

    def checkBASE(self):
        ensureFolder(baseSourcePath)
        ensureJSONFile(baseSourcePath + os.sep + 'classes.json', {"WAR":{"Name": "Warrior", "Base Health": 5, "Stat": "Strength"}, "WIZ":{"Name": "Wizard", "Base Health": 3, "Stat": "Mana"}})
        ensureJSONFile(baseSourcePath + os.sep + 'items.json', {"SWORD":{"Name": "Sword", "Stat": "Strength", "Value": 2, "Rating": 1, "Min Level": 1}, "STAFF":{"Name": "Staff", "Stat": "Mana", "Value": 2, "Rating": 1, "Min Level": 1}})
        ensureJSONFile(baseSourcePath + os.sep + 'attributes.json', {"CLASS": {"WAR": {"VIO": {"TARGET": "WAR", "NAME": "Violent", "RATING": 1, "EFFECTS": {"HEALTH": 1, "STR": 1}},"RUT": {"TARGET": "WAR", "NAME": "Ruthless", "RATING": 2, "EFFECTS": {"STR": 3}},"REK": {"TARGET": "WAR", "NAME": "Reckless", "RATING": 3, "EFFECTS": {"HEALTH": -1, "STR": 2}}},"WIZ": {"WIL": {"TARGET": "WIZ", "NAME": "Wild", "RATING": 1, "EFFECTS": {"MAN": 1}},"WIS": {"TARGET": "WIZ", "NAME": "Wise", "RATING": 2, "EFFECTS": {"MAN": 2}},"BOL": {"TARGET": "WIZ", "NAME": "Bold", "RATING": 3, "EFFECTS": {"HEALTH": -1, "MAN": 4}}}},"WEAPON": {"SWO": {"BLU": {"TARGET": "SWO", "NAME": "Blunt", "RATING": 1, "EFFECTS": {"STR": -1}},"SHA": {"TARGET": "SWO", "NAME": "Sharp", "RATING": 2, "EFFECTS": {"STR": 1}},"LEG": {"TARGET": "SWO", "NAME": "Legendary", "RATING": 3, "EFFECTS": {"STR": 3}}},"STA": {"BRI": {"TARGET": "STA", "NAME": "Brittle", "RATING": 1, "EFFECTS": {"MAN": -1}},"TUN": {"TARGET": "STA", "NAME": "Tuned", "RATING": 2, "EFFECTS": {"MAN": 1}},"MYT": {"TARGET": "STA", "NAME": "Mythical", "RATING": 3, "EFFECTS": {"MAN": 3}}}}})

    def loadData(self):
        self.loadBASE()
        self.loadMODS()
    
    def loadBASE(self):
        classesJSONDATA = loadJSON(os.path.join(baseSourcePath, 'classes.json'))
        self.compileJSONDATA(classesJSONDATA, ClassType.CLASS)
        itemsJSONDATA = loadJSON(os.path.join(baseSourcePath, 'items.json'))
        self.compileJSONDATA(itemsJSONDATA, ClassType.ITEM)
        attributesJSONDATA = loadJSON(os.path.join(baseSourcePath, 'attributes.json'))
        self.compileJSONDATA(attributesJSONDATA, ClassType.ATTRIBUTIO)

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

    def compileJSONDATA(self, jsonData:dict, outputClassType:ClassType):
        for (key, data) in jsonData.items():
            if key not in self.ignoreCODES:
                if outputClassType == ClassType.CLASS:
                    self.appendClass(self.compileJSONtoClass([key, ClassType.CLASS], [key, data]))
                elif outputClassType == ClassType.ITEM:
                    self.appendItem(self.compileJSONtoClass([key, ClassType.ITEM], [key, data]))
                if outputClassType == ClassType.ATTRIBUTE:
                    self.appendAttribute(self.compileJSONtoClass([key, ClassType.ATTRIBUTE], [key, data]))

    #region STATIC METHODS
    @staticmethod
    def checkFileStructure():
        if os.path.isdir(baseSourcePath) is False:
            os.makedirs(baseSourcePath)
        if os.path.isdir(modSourcePath) is False:
            os.makedirs(modSourcePath)
    #endregion

    #region PROPERTIES
    @property
    def ignoreCODES(self) -> dict:
        return self.__ignoreCODES
    @ignoreCODES.setter
    def ignoreCODES(self, ignoreCODES:list):
        self.__ignoreCODES = ignoreCODES

    @property
    def classes(self) -> list[Class]:
        return self.__classes
    @classes.setter
    def classes(self, classes:list[Class]):
        self.__classes = classes
    def appendClass(self, classDICT: list[RefCode, Class] | list[list[RefCode, Class]]):
        self.__classes.append(classDICT)

    @property
    def items(self) -> list[Item]:
        return self.__items
    @items.setter
    def items(self, items:list[Item]):
        self.__items = items
    def appendItem(self, itemDICT: list[RefCode, Item] | list[list[RefCode, Item]]):
        self.__items.append(itemDICT)

    @property
    def attributes(self) -> dict:
        return self.__attributes
    @attributes.setter
    def attributes(self, attributes:dict):
        self.__attributes = attributes
    @beartype
    def appendAttribute(self, attributeDICT: list[RefCode, Attribute] | list[list[RefCode, Attribute]]):
        if type(attributeDICT[0]) is list:
            for item in attributeDICT:
                self.__attributes[item[0]].append(item[1])
        else:
            self.__attributes[attributeDICT[0]].append(attributeDICT[1])
    #endregion