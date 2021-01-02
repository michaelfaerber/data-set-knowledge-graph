#Assigns URIs to the resources
#For entities that are not authors, it is assumed that entities with the same String are in fact the same entity. 

import pandas as pd


df = pd.read_csv("/Beta_Version_DSKG_NoIDs.csv")

foafPersonID = 10000
foafOrganizationID = 20000
foafAgentID = 30000
vcardKindID = 40000

df["creatorPersonID"] = ""
df["creatorOrganizationID"] = ""
df["creatorAgentID"] = ""
df["publisherOrganizationID"] = ""
df["publisherAgentID"] = ""
df["contributorOrganizationID"] = ""
df["contributorAgentID"] = ""
df["contactPointID"] = ""

#Assigning IDs for entities of the class foaf:Person
i = 0
while i < len(df):
    authors_string = df['creatorPersonName'][i]
    authors = str(authors_string).split(", ")

    for author in authors:
        if str(author) != "nan":
            df["creatorPersonID"][i] = df["creatorPersonID"][i] + str(foafPersonID) + ", "
            foafPersonID += 1
    if str(df["creatorPersonID"][i]).endswith(", "):
        max_len = len(str(df["creatorPersonID"][i]))
        unwanted_cut_off = max_len - 2
        df["creatorPersonID"][i] = str(df["creatorPersonID"][i])[0:unwanted_cut_off]
    i += 1

    
#Assign IDs for entities of the class foaf:Organization
foafOrganization_dict = dict()

#creatorOrganization
i = 0
while i < len(df):
    creators_string = df['creatorOrganizationName'][i]
    creators = str(creators_string).split(", ")

    for creator in creators:
        if creator not in foafOrganization_dict:
            if str(creator) != "nan":
                foafOrganization_dict[creator] = str(foafOrganizationID)
                foafOrganizationID += 1
    i += 1
    
#publisherOrganization      
i = 0
while i < len(df):
    creators_string = df['publisherOrganizationName'][i]
    creators = str(creators_string).split(", ")

    for creator in creators:
        if creator not in foafOrganization_dict:
            if str(creator) != "nan":
                foafOrganization_dict[creator] = str(foafOrganizationID)
                foafOrganizationID += 1
    i += 1
#contributorOrganization
i = 0
while i < len(df):
    creators_string = df['contributorOrganizationName'][i]
    creators = str(creators_string).split(", ")

    for creator in creators:
        if creator not in foafOrganization_dict:
            if str(creator) != "nan":
                foafOrganization_dict[creator] = str(foafOrganizationID)
                foafOrganizationID += 1
    i += 1  
    
#Save the IDs in the csv-file    
    
i = 0
while i < len(df):
    creators_string = df['creatorOrganizationName'][i]
    creators = str(creators_string).split(", ")
    for creator in creators:
        if str(creator) != "nan":
            creator_id = foafOrganization_dict.get(creator)
            df["creatorOrganizationID"][i] = df["creatorOrganizationID"][i] + str(creator_id) + ", "
        
    ids = df["creatorOrganizationID"][i]
    if str(ids).endswith(", "):
        max_len = len(str(ids))
        unwanted_cut_off = max_len - 2
        ids = str(ids)[0:unwanted_cut_off]  
        df["creatorOrganizationID"][i] = ids
    i += 1
    
    
i = 0
while i < len(df):
    creators_string = df['publisherOrganizationName'][i]
    creators = str(creators_string).split(", ")
    for creator in creators:
        if str(creator) != "nan":
            creator_id = foafOrganization_dict.get(creator)
            df["publisherOrganizationID"][i] = df["publisherOrganizationID"][i] + str(creator_id) + ", "
        
    ids = df["publisherOrganizationID"][i]
    if str(ids).endswith(", "):
        max_len = len(str(ids))
        unwanted_cut_off = max_len - 2
        ids = str(ids)[0:unwanted_cut_off]  
        df["publisherOrganizationID"][i] = ids
    i += 1
    
i = 0
while i < len(df):
    creators_string = df['contributorOrganizationName'][i]
    creators = str(creators_string).split(", ")
    for creator in creators:
        if str(creator) != "nan":
            creator_id = foafOrganization_dict.get(creator)
            df["contributorOrganizationID"][i] = df["contributorOrganizationID"][i] + str(creator_id) + ", "
        
    ids = df["contributorOrganizationID"][i]
    if str(ids).endswith(", "):
        max_len = len(str(ids))
        unwanted_cut_off = max_len - 2
        ids = str(ids)[0:unwanted_cut_off]  
        df["contributorOrganizationID"][i] = ids
    i += 1 
    
    
    
#Assign IDs for entities of the class foaf:Agent
       
#creatorAgent
foafAgent_dict = dict()
i = 0
while i < len(df):
    creators_string = df['creatorAgentName'][i]
    creators = str(creators_string).split(", ")

    for creator in creators:
        if creator not in foafAgent_dict:
            if str(creator) != "nan":
                foafAgent_dict[creator] = str(foafAgentID)
                foafAgentID += 1
    i += 1

#publisherAgent   
i = 0
while i < len(df):
    creators_string = df['publisherAgentName'][i]
    creators = str(creators_string).split(", ")

    for creator in creators:
        if creator not in foafAgent_dict:
            if str(creator) != "nan":
                foafAgent_dict[creator] = str(foafAgentID)
                foafAgentID += 1
    i += 1    
    
#contributorAgent
i = 0
while i < len(df):
    creators_string = df['contributorAgentName'][i]
    creators = str(creators_string).split(", ")

    for creator in creators:
        if creator not in foafAgent_dict:
            if str(creator) != "nan":
                foafAgent_dict[creator] = str(foafAgentID)
                foafAgentID += 1
    i += 1
#Save the IDs in the csv-file     
    
i = 0
while i < len(df):
    creators_string = df['creatorAgentName'][i]
    creators = str(creators_string).split(", ")
    for creator in creators:
        if str(creator) != "nan":
            creator_id = foafAgent_dict.get(creator)
            df["creatorAgentID"][i] = df["creatorAgentID"][i] + str(creator_id) + ", "
        
    ids = df["creatorAgentID"][i]
    if str(ids).endswith(", "):
        max_len = len(str(ids))
        unwanted_cut_off = max_len - 2
        ids = str(ids)[0:unwanted_cut_off]  
        df["creatorAgentID"][i] = ids
    i += 1
    
    
i = 0
while i < len(df):
    creators_string = df['publisherAgentName'][i]
    creators = str(creators_string).split(", ")
    for creator in creators:
        if str(creator) != "nan":
            creator_id = foafAgent_dict.get(creator)
            df["publisherAgentID"][i] = df["publisherAgentID"][i] + str(creator_id) + ", "
        
    ids = df["publisherAgentID"][i]
    if str(ids).endswith(", "):
        max_len = len(str(ids))
        unwanted_cut_off = max_len - 2
        ids = str(ids)[0:unwanted_cut_off]  
        df["publisherAgentID"][i] = ids
    i += 1  

    
    
i = 0
while i < len(df):
    creators_string = df['contributorAgentName'][i]
    creators = str(creators_string).split(", ")
    for creator in creators:
        if str(creator) != "nan":
            creator_id = foafAgent_dict.get(creator)
            df["contributorAgentID"][i] = df["contributorAgentID"][i] + str(creator_id) + ", "
        
    ids = df["contributorAgentID"][i]
    if str(ids).endswith(", "):
        max_len = len(str(ids))
        unwanted_cut_off = max_len - 2
        ids = str(ids)[0:unwanted_cut_off]  
        df["contributorAgentID"][i] = ids
    i += 1  
    
#Assign IDs for entities of the class vcard:Kind
#contactPoint   
new_dict = dict()
i = 0
while i < len(df):
    creator = df['contactPointName'][i]
    if creator not in new_dict:
        if str(creator) != "nan":
            new_dict[creator] = str(vcardKindID)
            vcardKindID += 1
    i += 1
    
i = 0
while i < len(df):
    creator = df['contactPointName'][i]
    if str(creator) != "nan":
        creator_id = new_dict.get(creator)
        df["contactPointID"][i] =str(creator_id)
    i += 1  
    
    
#Corrects the authors' URIs based on the results of author disambiguation
#Identical authors have identical ID



with open("/Users/davidlamprecht/Desktop/Abgabe_Final/Disambiguation_Neu/Ergebnisse_Disambiguation_Neu/all_positives.txt", "r") as inp:
    for line in inp:
        ids = line.split("\t")
        id_replace = ids[0]
        id_keep = ids[1].strip()
        i = 0
        while i < len(df):
            author_ids = df["creatorPersonID"][i]
            new_author_ids = df["creatorPersonID"][i]
            author_ids_split = str(author_ids).split(", ")
            for aid in author_ids_split: 
                if str(aid) == str(id_replace):
                    new_author_ids = new_author_ids.replace(aid, id_keep)
                    
            df["creatorPersonID"][i] = new_author_ids
            i += 1


df.to_csv("/Beta_Version_DSKG_IDs.csv")

