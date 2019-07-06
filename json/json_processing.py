import json

sourceFile = open("end_work.json", "rU")

json_data = json.load(sourceFile)

print (json_data)