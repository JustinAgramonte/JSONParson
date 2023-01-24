#opens files, performs actions, given target folder
    #opens each file and then parses JSON for "name" field and times found across all files
    #if already in json, adds ++
    #if not found, add name & severity and start at 1
    #close file, hopefully moves to next

import os
import json

VulnsAmount = {}

for file in os.listdir(r"C:\Users\Justi\Downloads\JSON Reports"):
    filenamefull = os.path.join(r"C:\Users\Justi\Downloads\JSON Reports", file)
    openedfile = open(filenamefull, 'r', encoding="utf8")
    ConvertedJSON2Python = json.load(openedfile)
    for k in ConvertedJSON2Python: 
        for dictionary in ConvertedJSON2Python["issues"]:
            for key in dictionary.keys():
                if key == "name":
                    add2Vuln = dictionary["name"]
                    if dictionary["name"] in VulnsAmount.keys():
                        VulnsAmount[add2Vuln] += 1
                    else:
                        VulnsAmount.update({add2Vuln: 1})

    print (VulnsAmount, "\n \n \n ", filenamefull)

    openedfile.close()             

#print (VulnsAmount)

    
"""if __name__ == "__main__":
  tabularize()"""
