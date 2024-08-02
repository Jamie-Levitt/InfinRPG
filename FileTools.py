from __future__ import annotations

import os, sys, json
from enum import Enum

from CharacterLogic import Class
from ItemLogic import Item
from Attributes import Attribute

srcDIR = os.path.realpath(sys.path[0]) #Temporary for testi
#region PATHS
dataSourcePath = os.path.join(srcDIR, 'SOURCES')
baseSourcePath = os.path.join(dataSourcePath, 'BASE')
modSourcePath = os.path.join(dataSourcePath, 'MODS')
#endregion

def makeJSON(filePath:str, baseDATA:dict):
    with open(filePath, 'w', encoding='utf-8') as f:
        json.dump(baseDATA, f, ensure_ascii=False, indent=4)
    f.close()

def ensureFolder(folderPath:str):
    if os.path.isdir(folderPath) is False:
        os.makedirs(folderPath)

def ensureJSONFile(filePath:str, baseDATA:dict):
    if os.path.isfile(filePath) is False:
        makeJSON(filePath, baseDATA)

def loadJSON(filePath) -> dict:
    file = open(filePath)
    data = json.load(file)
    file.close()
    return data

class ClassType(Enum):
    CLASS = Class
    ITEM = Item
    ATTRIBUTE = Attribute

def compileJSONtoClass(classType:ClassType, jsonDATA:dict):
    return classType.value(jsonDATA)