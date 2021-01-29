##Add the results of linking to papers from the .txt files to the .csv files

import pandas as pd
df = pd.read_csv(".../OpenAire.csv") #and .../Wikidata.csv
df["MAGConnection"] = ""

#Add unique:
#Add results of matching for values that exist only once per metadata entry to csv file
with open(".../OpenAIRE_title_matches_filtered.txt", "r") as inp: #Do for all files which are listed in line 47
    for line in inp:
        i = 0
        a = line.split("\t")
        originalId = a[0]
        mag = a[3].strip("\n")
        while i < len(df.index):
            cellvalue = df['title'][i]
            csvoriginalId = str(cellvalue)
            if csvoriginalId == originalId:
                magcsv = df['MAGConnection'][i]
                magcsvSTR = str(magcsv)
                df.at[i, 'MAGConnection'] = magcsvSTR + str(mag) + ", "
            i += 1


#Add multi valued cells:
#Add results of matching for multi values which can exist more often per metadata entry to csv file 
#Values are separated with commas within a cell in the csv-file
with open(".../OpenAIRE_doi_matches.txt", "r") as inp: #Do for all files which are listed in line 48 & 49
    for line in inp:
        i = 0
        a = line.split("\t")
        originalValue = a[0]
        mag = a[3].strip("\n")
        while i < len(df.index):
            cellvalue = df['doi'][i]
            csvcellvalue_split = str(cellvalue).split(", ")
            for elem in csvcellvalue_split:
                csvcellvalue_split_strip = elem.strip()
                if csvcellvalue_split_strip == originalValue:
                    magcsv = df['MAGConnection'][i]
                    magcsvSTR = str(magcsv)
                    df.at[i, 'MAGConnection'] = magcsvSTR + str(mag) + ", "
            i += 1
        progress_counter += 1


#Do same "Add unique" for results of matching the value of: OpenAIRE_title and Wikidata_itemLabel
#Do same "Add multi valued cells" for results of matching the value of: OpenAIRE_originalId, OpenAIRE_doi, 
#Wikidata_AltLabel, Wikidata_officialwebsite, Wikidata_url, Wikidata_workURL

#Remove Duplikates
i = 0
while i < len(df):
    mag_split = str(df['MAGConnection'][i]).split(", ")
    lst = []
    for mag in mag_split:
        lst.append(mag)
    s = set(lst)
    new_mag = ""
    for mag in s:
        new_mag += mag + ", "
    df['MAGConnection'][i] = new_mag
    i += 1


#Remove ending commas 
i = 0
while i < len(df):
    if str(df['MAGConnection'][i]).endswith(", "):  
        max_len = len(str(df['MAGConnection'][i]))
        unwanted_cut_off = max_len - 2
        df['MAGConnection'][i] = str(df['MAGConnection'][i])[0:unwanted_cut_off]
    i += 1


        