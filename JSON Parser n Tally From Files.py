#opens files, given target folder
    #parses JSON output of SmarterScanner App for "name" of vulnerability field as well as times found across all files, close file
    #if already in python dictionary, adds ++
    #if not found, add name and start at 1

import os, json

VulnsNameAmount = {}
filePath = input("Enter filename: ").strip('\"')
assert os.path.isdir(filePath), "Filepath not found...copy from explorer path?"

for file in os.listdir(filePath): #opening file
    openedfile = open(os.path.join(filePath, file), 'r', encoding="utf8")
    convertedJSON2Python = json.load(openedfile)

    for primaryKey in convertedJSON2Python: #iterate through every key in the JSON --> python dictionary
        listofVulnName = [] #create a list to add the vulnerability names, created here to clear it everytime a new file is accessed
        for dictionary in convertedJSON2Python["issues"]: #issues' values are dictionaries themselves, so we reference the values of only the issues key where the "name" field is
            for key in dictionary.keys(): # for every key under issues
                if key == "name":
                    listofVulnName.append(dictionary[key]) #adds dictionary value to list of vulnerabilities
        listofVulnName = set(listofVulnName) #makes list items unique. needed so they are counted once per file
    
    openedfile.close()

    for vulnName in listofVulnName: #update list with keys as vuln names/list items, and values are how many times we've seen it across files
        if vulnName not in VulnsNameAmount:
            VulnsNameAmount.update({vulnName: 1})
        else: 
            VulnsNameAmount[vulnName] = VulnsNameAmount[vulnName] + 1

if __name__ == "__main__": 
    for key in VulnsNameAmount:
        print ("Vulnerability Found: " + key + "\n    Times Found: " + str(VulnsNameAmount[key]))