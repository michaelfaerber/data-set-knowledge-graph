#Preprocessing and clean-up of the csv-files of the OpenAIRE dataset
import pandas as pd
df = pd.read_csv(".../OpenAire.csv", keep_default_na=False)
df["openairedump"] = "https://zenodo.org/record/3516918#.X06cAi336MI"

#Removes interfering characters of the metadata entries 
i = 0
while i < len(df):
    df['description'][i] = str(df['description'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("<br>", "").replace("</br>", "").replace("<b>", "").replace("</b>", "").replace("#", "").replace("<div>", "").replace("</div>", "").replace('["', "").replace('"]', "").replace("</p>", "").replace("<p>", "").replace("</ul>", "").replace("<ul>", "").replace("</ol>", "").replace("<ol>", "").replace("</li>", "").replace("<li>", "")
    df['title'][i] = str(df['title'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "")
    df['originalId'][i] = str(df['originalId'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("', '", ", ")
    df['contributor'][i] = str(df['contributor'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("', '", ", ")
    df['format'][i] = str(df['format'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("', '", ", ")
    df['relevantdate'][i] = str(df['relevantdate'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("', '", ", ")
    df['subject'][i] = str(df['subject'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("', '", ", ")
    df['doi'][i] = str(df['doi'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("', '", ", ")
    i +=1
    
#Clean up Creator entries (remove comma)
i = 0
while i < len(df):
    df['creator'][i] = str(df['creator'][i]).replace("', '", "'; '")
    i += 1    
i = 0
while i < len(df):
    df['creator'][i] = str(df['creator'][i]).replace(",", "")
    i += 1
i = 0
while i < len(df):
    df['creator'][i] = str(df['creator'][i]).replace(";", ",")
    i += 1    

i = 0
while i < len(df):
    df['creator'][i] = str(df['creator'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("', '", ", ")
    i += 1
    
#Clean up Contact Person entries (remove comma)
i = 0
while i < len(df):
    df['contactperson'][i] = str(df['contactperson'][i]).replace("', '", "'; '")
    i += 1    
i = 0
while i < len(df):
    df['contactperson'][i] = str(df['contactperson'][i]).replace(",", "")
    i += 1
i = 0
while i < len(df):
    df['contactperson'][i] = str(df['contactperson'][i]).replace(";", ",")
    i += 1    

i = 0
while i < len(df):
    df['contactperson'][i] = str(df['contactperson'][i]).replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace("', '", ", ")
    i += 1

    
#Matches the metadata entries of the size property to the DCAT vocabulary.
#Converts all specified sizes into bytes.

import re

df["byteSize"] = ""

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
        byteSizestr = int(byteSize) 
        df.at[i, 'byteSize'] = int(byteSizestr)
    i += 1


df.to_csv(".../OpenAire_cleaned.csv")
