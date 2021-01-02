#Matches the metadata entries of the size property to the DCAT vocabulary.
#Converts all specified sizes into bytes

import re
import pandas as pd
df = pd.read_csv("/OpenAire.csv")

df['byteSize'] = ""

print (len(df.index))
i = 0
while i < len(df.index):
    byteSize = 0
    cellvalue = df['size'][i]
    cellvalueSplit = cellvalue.split(" ")
    if len(cellvalueSplit) >= 1:
        cellvalueNumber = cellvalueSplit[0]
    if len(cellvalueSplit) >= 2:
        cellvalueUnit = cellvalueSplit[1].lower()

    num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]?$")
    isnumber = re.match(num_format, cellvalueNumber)
    if (isnumber and (len(cellvalueSplit) >= 2)):
        if (cellvalueUnit == "bytes"):
            byteSize = float(cellvalueNumber)
        elif (cellvalueUnit == "kb"):
            byteSize = float(cellvalueNumber) * 1000     
        elif (cellvalueUnit == "mb"):
            byteSize = float(cellvalueNumber) * 1000000 
        elif (cellvalueUnit == "gb"):
            byteSize = float(cellvalueNumber) * 1000000000        
        elif (cellvalueUnit == "tb"):
            byteSize = float(cellvalueNumber) * 1000000000000
        elif (cellvalueUnit == "kbytes"):
            byteSize = float(cellvalueNumber) * 1000 
        elif (cellvalueUnit == "mbytes"):
            byteSize = float(cellvalueNumber) * 1000000 
        elif (cellvalueUnit == "gbytes"):
            byteSize = float(cellvalueNumber) * 1000000000 
        elif (cellvalueUnit == "tbytes"):
            byteSize = float(cellvalueNumber) * 1000000000000
        else:
            byteSize = 0
    if (byteSize != 0):
        byteSizestr = str(byteSize)
        df['byteSize'][i] = byteSizestr
    i += 1

    

df.to_csv('/OpenAire_final.csv', index=False)  