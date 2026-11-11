import os
import re

def _getSearch():
    os.chdir("C:/Users/BTsubaki/scripts/vs_projects")
    askTarget = input("Enter a sentence/word to search : ")
    getTarget = re.compile(askTarget)
    _result = []
    _currentWD = os.getcwd()
    listDir = os.listdir()
    print(listDir)

    for file in range(len(listDir)):
        with open(listDir[file], "r", encoding = "utf-8") as currentFile:
            current = currentFile.read()
            _result += re.findall(getTarget, current)

    print(f"""
    {askTarget} appears {len(_result)} times
    """)
    _getSearch()

_getSearch()