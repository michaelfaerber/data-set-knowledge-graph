#OpenAIRE - Classification of resources according to DCAT
#Classifies the metadata entries for creator, publisher and contributor
#classifies the entries of creator into the classes person (creatorPerson), organisation (creatorOrganization) and agent (creatorOther)
#classifies the entries of publisher into the classes organisation and agent
#classifies the entries of contributor into the classes organisation and agent

import spacy
nlp = spacy.load('en_core_web_sm')
import pandas as pd
df = pd.read_csv("/OpenAire_unclassified.csv")
df['creatorPerson'] = ""
df['creatorOrganization'] = ""
df['creatorOther'] = ""
df['publisherOrganization'] = ""
df['publisherOther'] = ""
df['contributorOrganization'] = ""
df['contributorOther'] = ""


i = 0
while i < len(df.index):
    cellvalue = df['creator'][i]
    cellvaluestr = str(cellvalue)
    doc = nlp(cellvaluestr)
    persons = ""
    organization = ""
    other = ""
    for X in doc.ents:
        if (X.label_ == "PERSON"): 
            persons = persons + X.text + ", "
                
        elif (X.label_ == "ORG"): 
            organization = organization + X.text + ", "
        else:
            other = other + X.text + ", "  
            
    if persons.endswith(", "):
        max_len = len(persons)
        unwanted_cut_off = max_len - 2
        persons = persons[0:unwanted_cut_off]
    if organization.endswith(", "):
        max_len = len(organization)
        unwanted_cut_off = max_len - 2
        organization = organization[0:unwanted_cut_off]
    if other.endswith(", "):
        max_len = len(other)
        unwanted_cut_off = max_len - 2
        other = other[0:unwanted_cut_off]
    
    df['creatorPerson'][i] = persons   
    df['creatorOrganization'][i] = organization
    df['creatorOther'][i] = other
    i += 1
    
i = 0
while i < len(df.index):
    cellvalue = df['publisher'][i]
    cellvaluestr = str(cellvalue)
    doc = nlp(cellvaluestr)
    organization = ""
    other = ""
    
    for X in doc.ents:
        if (X.label_ == "ORG"): 
            organization = organization + X.text + ", "
        else:  
            other = other + X.text + ", "     
            
    if organization.endswith(", "):
        max_len = len(organization)
        unwanted_cut_off = max_len - 2
        organization = organization[0:unwanted_cut_off]
    if other.endswith(", "):
        max_len = len(other)
        unwanted_cut_off = max_len - 2
        other = other[0:unwanted_cut_off]
        
    df['publisherOrganization'][i] = organization
    df['publisherOther'][i] = other
    
    if (cellvaluestr.lower() == "figshare"):
        df['publisherOther'][i] = cellvaluestr
    if (cellvaluestr.lower() == "zenodo"):
        df['publisherOther'][i] = cellvaluestr
        
    i += 1
    
i = 0
while i < len(df.index):
    cellvalue = df['contributor'][i]
    cellvaluestr = str(cellvalue)
    doc = nlp(cellvaluestr)
    organization = ""
    other = ""
    for X in doc.ents:
        if (X.label_ == "ORG"): 
            organization = organization + X.text + ", "
        else:  
            other = other + X.text + ", "     
    
    if organization.endswith(", "):
        max_len = len(organization)
        unwanted_cut_off = max_len - 2
        organization = organization[0:unwanted_cut_off]
    if other.endswith(", "):
        max_len = len(other)
        unwanted_cut_off = max_len - 2
        other = other[0:unwanted_cut_off]
        
    df['contributorOrganization'][i] = organization
    df['contributorOther'][i] = other
    i += 1
     
    

df.to_csv('/OpenAire_classified.csv', index=False)


#Wikidata - Classification of resources according to DCAT
#Classifies the metadata entries for author, authorString, publisher and contributor
#classifies the entries of author into the classes person (authorPerson), organisation (authorOrganization) and agent (authorOther)
#classifies the entries of authorString into the classes person (authorStringPerson), organisation (authorStringOrganization) and agent (authorStringOther)
#classifies the entries of publisher into the classes organisation and agent
#classifies the entries of contributor into the classes organisation and agent
import spacy
nlp = spacy.load('en_core_web_sm')
import pandas as pd
df = pd.read_csv("/Wikidata_unclassified.csv")

df["authorPerson"] = ""
df["authorOrganization"] = ""
df["authorOther"] = ""
df["authorStringPerson"] = ""
df["authorStringOrganization"] = ""
df["authorStringOther"] = ""
df["publisherOrganization"] = ""
df["publisherOther"] = ""
df['contributorOrganization'] = ""
df['contributorOther'] = ""

i = 0
while i < len(df.index):
    cellvalue = df['author'][i]
    cellvaluestr = str(cellvalue)
    doc = nlp(cellvaluestr)
    persons = ""
    organization = ""
    other = ""
    for X in doc.ents:
        if (X.label_ == "PERSON"): 
            persons = persons + X.text + ", "
                
        elif (X.label_ == "ORG"): 
            organization = organization + X.text + ", "
        else:
            other = other + X.text + ", "   
                    
    if persons.endswith(", "):
        max_len = len(persons)
        unwanted_cut_off = max_len - 2
        persons = persons[0:unwanted_cut_off]
    if organization.endswith(", "):
        max_len = len(organization)
        unwanted_cut_off = max_len - 2
        organization = organization[0:unwanted_cut_off]
    if other.endswith(", "):
        max_len = len(other)
        unwanted_cut_off = max_len - 2
        other = other[0:unwanted_cut_off]
        
    df.at[i, 'authorPerson'] = persons   
    df.at[i, 'authorOrganization'] = organization
    df.at[i, 'authorOther'] = other
    i += 1
    
    
i = 0
while i < len(df.index):
    cellvalue = df['authorString'][i]
    cellvaluestr = str(cellvalue)
    doc = nlp(cellvaluestr)
    persons = ""
    organization = ""
    other = ""
    for X in doc.ents:
        if (X.label_ == "PERSON"): 
            persons = persons + X.text + ", "
                
        elif (X.label_ == "ORG"): 
            organization = organization + X.text + ", "
        else:
            other = other + X.text + ", "  
            
    if persons.endswith(", "):
        max_len = len(persons)
        unwanted_cut_off = max_len - 2
        persons = persons[0:unwanted_cut_off]
    if organization.endswith(", "):
        max_len = len(organization)
        unwanted_cut_off = max_len - 2
        organization = organization[0:unwanted_cut_off]
    if other.endswith(", "):
        max_len = len(other)
        unwanted_cut_off = max_len - 2
        other = other[0:unwanted_cut_off]
        
    df.at[i, 'authorStringPerson'] = persons   
    df.at[i, 'authorStringOrganization'] = organization
    df.at[i, 'authorStringOther'] = other
    i += 1
    
    
i = 0
while i < len(df.index):
    cellvalue = df['publisher'][i]
    cellvaluestr = str(cellvalue)
    doc = nlp(cellvaluestr)
    organization = ""
    other = ""
    
    for X in doc.ents:
        if (X.label_ == "ORG"): 
            organization = organization + X.text + ", "
        else:  
            other = other + X.text + ", "     
            
    if organization.endswith(", "):
        max_len = len(organization)
        unwanted_cut_off = max_len - 2
        organization = organization[0:unwanted_cut_off]
    if other.endswith(", "):
        max_len = len(other)
        unwanted_cut_off = max_len - 2
        other = other[0:unwanted_cut_off]
        
    df.at[i, 'publisherOrganization'] = organization
    df.at[i, 'publisherOther'] = other  
    i += 1
    
i = 0
while i < len(df.index):
    cellvalue = df['contributor'][i]
    cellvaluestr = str(cellvalue)
    doc = nlp(cellvaluestr)
    organization = ""
    other = ""
    for X in doc.ents:
        if (X.label_ == "ORG"): 
            organization = organization + X.text + ", "
        else:  
            other = other + X.text + ", "     

    if organization.endswith(", "):
        max_len = len(organization)
        unwanted_cut_off = max_len - 2
        organization = organization[0:unwanted_cut_off]
    if other.endswith(", "):
        max_len = len(other)
        unwanted_cut_off = max_len - 2
        other = other[0:unwanted_cut_off]
        
    df.at[i, 'contributorOrganization'] = organization
    df.at[i, 'contributorOther'] = other
    i += 1
     
    

df.to_csv("/Wikidata_classified.csv")  
