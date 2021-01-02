#Make final OpenAIRE-csv for transformation into RDF
import pandas as pd
df = pd.read_csv("/OpenAire.csv")
df_dskg = pd.read_csv("/Beta_Version_DSKG_IDs.csv", converters={"contactPointID":str})

df["creatorPersonID"] = ""
df["creatorOrganizationID"] = ""
df["creatorAgentID"] = ""
df["publisherOrganizationID"] = ""
df["publisherAgentID"] = ""
df["contributorOrganizationID"] = ""
df["contributorAgentID"] = ""
df["contactPointID"] = ""

i = 0
while i < len(df):
    df["creatorPersonID"][i] = df_dskg["creatorPersonID"][i]
    df["creatorOrganizationID"][i] = df_dskg["creatorOrganizationID"][i]
    df["creatorAgentID"][i] = df_dskg["creatorAgentID"][i]
    df["publisherOrganizationID"][i] = df_dskg["publisherOrganizationID"][i]
    df["publisherAgentID"][i] = df_dskg["publisherAgentID"][i]
    df["contributorOrganizationID"][i] = df_dskg["contributorOrganizationID"][i]
    df["contributorAgentID"][i] = df_dskg["contributorAgentID"][i]
    df["contactPointID"][i] = df_dskg["contactPointID"][i]
    i += 1
    
df.to_csv("/OpenAire_Dataset_Transformation.csv")


#Make final Wikidata-csv for transformation into RDF
df = pd.read_csv("/Wikidata.csv")
df_dskg = pd.read_csv("/Beta_Version_DSKG_IDs.csv", converters={"contactPointID":str})

df["creatorPersonID"] = ""
df["creatorOrganizationID"] = ""
df["creatorAgentID"] = ""
df["publisherOrganizationID"] = ""
df["publisherAgentID"] = ""
df["contributorOrganizationID"] = ""
df["contributorAgentID"] = ""
df["contactPointID"] = ""

i = 0
while i < len(df):
    df["creatorPersonID"][i] = df_dskg["creatorPersonID"][i + 450]
    df["creatorOrganizationID"][i] = df_dskg["creatorOrganizationID"][i + 450]
    df["creatorAgentID"][i] = df_dskg["creatorAgentID"][i + 450]
    df["publisherOrganizationID"][i] = df_dskg["publisherOrganizationID"][i + 450]
    df["publisherAgentID"][i] = df_dskg["publisherAgentID"][i + 450]
    df["contributorOrganizationID"][i] = df_dskg["contributorOrganizationID"][i + 450]
    df["contributorAgentID"][i] = df_dskg["contributorAgentID"][i + 450]
    df["contactPointID"][i] = df_dskg["contactPointID"][i + 450]
    i += 1
    
df.to_csv("/Wikidata_Dataset_Transformation.csv.csv")

#Make final CreatorPerson-csv for transformation into RDF
df = pd.read_csv("/Beta_Version_DSKG_IDs.csv")


new_dict = {}


i = 0
while i < len(df):
    creator_ids = df["creatorPersonID"][i]
    creator_ids_split = str(creator_ids).split(", ")
    creator_names = df["creatorPersonName"][i]
    creator_names_split = str(creator_names).split(", ") 
    
    for cid, cn in zip(creator_ids_split, creator_names_split):
        if str(cid) != "nan" and str(cn) != "nan":
            new_dict[cid] = cn
        
    i += 1
    
df_creator_person = pd.DataFrame(index=range(0,len(new_dict)))
df_creator_person["creatorPersonID"] = ""
df_creator_person["creatorPersonName"] = ""
df_creator_person["ORCID"] = ""
    

counter = 0
for key in new_dict:
    df_creator_person["creatorPersonID"][counter] = key
    df_creator_person["creatorPersonName"][counter] = new_dict[key]
    counter += 1

    
df_creator_person.to_csv("/DSKG_CreatorPerson_Transformation.csv")

#Creator_Organization
df = pd.read_csv("/Beta_Version_DSKG_IDs.csv")

new_dict = {}
i = 0
while i < len(df):
    creator_ids = df["creatorOrganizationID"][i]
    creator_ids_split = str(creator_ids).split(", ")
    creator_names = df["creatorOrganizationName"][i]
    creator_names_split = str(creator_names).split(", ") 
    
    for cid, cn in zip(creator_ids_split, creator_names_split):
        if str(cid) != "nan" and str(cn) != "nan":
            new_dict[cid] = cn
        
    i += 1

df_creator_person = pd.DataFrame(index=range(0,len(new_dict)))
df_creator_person["creatorOrganizationID"] = ""
df_creator_person["creatorOrganizationName"] = ""

counter = 0
for key in new_dict:
    df_creator_person["creatorOrganizationID"][counter] = key
    df_creator_person["creatorOrganizationName"][counter] = new_dict[key]
    counter += 1
    
df_creator_person.to_csv("/DSKG_CreatorOrganization_Transformation.csv")

#Creator_Agent
df = pd.read_csv("/Beta_Version_DSKG_IDs.csv")

new_dict = {}
i = 0
while i < len(df):
    creator_ids = df["creatorAgentID"][i]
    creator_ids_split = str(creator_ids).split(", ")
    creator_names = df["creatorAgentName"][i]
    creator_names_split = str(creator_names).split(", ") 
    
    for cid, cn in zip(creator_ids_split, creator_names_split):
        if str(cid) != "nan" and str(cn) != "nan":
            new_dict[cid] = cn
        
    i += 1

df_creator_person = pd.DataFrame(index=range(0,len(new_dict)))
df_creator_person["creatorAgentID"] = ""
df_creator_person["creatorAgentName"] = ""

counter = 0
for key in new_dict:
    df_creator_person["creatorAgentID"][counter] = key
    df_creator_person["creatorAgentName"][counter] = new_dict[key]
    counter += 1
    
df_creator_person.to_csv("/DSKG_CreatorAgent_Transformation.csv")

#publisher_Organization
df = pd.read_csv("/Beta_Version_DSKG_IDs.csv")

new_dict = {}
i = 0
while i < len(df):
    creator_ids = df["publisherOrganizationID"][i]
    creator_ids_split = str(creator_ids).split(", ")
    creator_names = df["publisherOrganizationName"][i]
    creator_names_split = str(creator_names).split(", ") 
    
    for cid, cn in zip(creator_ids_split, creator_names_split):
        if str(cid) != "nan" and str(cn) != "nan":
            new_dict[cid] = cn
        
    i += 1

df_creator_person = pd.DataFrame(index=range(0,len(new_dict)))
df_creator_person["publisherOrganizationID"] = ""
df_creator_person["publisherOrganizationName"] = ""

counter = 0
for key in new_dict:
    df_creator_person["publisherOrganizationID"][counter] = key
    df_creator_person["publisherOrganizationName"][counter] = new_dict[key]
    counter += 1

df_creator_person.to_csv("/DSKG_PublisherOrganization_Transformation.csv")


#publisher_Agent
df = pd.read_csv("/Beta_Version_DSKG_IDs.csv")

new_dict = {}
i = 0
while i < len(df):
    creator_ids = df["publisherAgentID"][i]
    creator_ids_split = str(creator_ids).split(", ")
    creator_names = df["publisherAgentName"][i]
    creator_names_split = str(creator_names).split(", ") 
    
    for cid, cn in zip(creator_ids_split, creator_names_split):
        if str(cid) != "nan" and str(cn) != "nan":
            new_dict[cid] = cn
        
    i += 1

df_creator_person = pd.DataFrame(index=range(0,len(new_dict)))
df_creator_person["publisherAgentID"] = ""
df_creator_person["publisherAgentName"] = ""

counter = 0
for key in new_dict:
    df_creator_person["publisherAgentID"][counter] = key
    df_creator_person["publisherAgentName"][counter] = new_dict[key]
    counter += 1
    

df_creator_person.to_csv("/DSKG_PublisherAgent_Transformation.csv")


#contributor_Organization
df = pd.read_csv("/Beta_Version_DSKG_IDs.csv")

new_dict = {}
i = 0
while i < len(df):
    creator_ids = df["contributorOrganizationID"][i]
    creator_ids_split = str(creator_ids).split(", ")
    creator_names = df["contributorOrganizationName"][i]
    creator_names_split = str(creator_names).split(", ") 
    
    for cid, cn in zip(creator_ids_split, creator_names_split):
        if str(cid) != "nan" and str(cn) != "nan":
            new_dict[cid] = cn
        
    i += 1

df_creator_person = pd.DataFrame(index=range(0,len(new_dict)))
df_creator_person["contributorOrganizationID"] = ""
df_creator_person["contributorOrganizationName"] = ""

counter = 0
for key in new_dict:
    df_creator_person["contributorOrganizationID"][counter] = key
    df_creator_person["contributorOrganizationName"][counter] = new_dict[key]
    counter += 1
    
df_creator_person.to_csv("/DSKG_ContributorOrganization_Transformation.csv")


#contributor_Agent
import pandas as pd
df = pd.read_csv("/Beta_Version_DSKG_IDs.csv")

new_dict = {}
i = 0
while i < len(df):
    creator_ids = df["contributorAgentID"][i]
    creator_ids_split = str(creator_ids).split(", ")
    creator_names = df["contributorAgentName"][i]
    creator_names_split = str(creator_names).split(", ") 
    
    for cid, cn in zip(creator_ids_split, creator_names_split):
        if str(cid) != "nan" and str(cn) != "nan":
            new_dict[cid] = cn
        
    i += 1

df_creator_person = pd.DataFrame(index=range(0,len(new_dict)))
df_creator_person["contributorAgentID"] = ""
df_creator_person["contributorAgentName"] = ""

counter = 0
for key in new_dict:
    df_creator_person["contributorAgentID"][counter] = key
    df_creator_person["contributorAgentName"][counter] = new_dict[key]
    counter += 1
    
df_creator_person.to_csv("/DSKG_ContributorAgent_Transformation.csv")


#contactPoint
df = pd.read_csv("/Beta_Version_DSKG_IDs.csv", converters={"contactPointID":str})

new_dict = {}
i = 0
while i < len(df):
    creator_ids = df["contactPointID"][i]
    creator_names = df["contactPointName"][i]
    if str(creator_ids) != "nan" and str(creator_names) != "nan":
        new_dict[creator_ids] = creator_names
        
    i += 1

df_creator_person = pd.DataFrame(index=range(0,len(new_dict)))
df_creator_person["contactPointID"] = ""
df_creator_person["contactPoint"] = ""
df_creator_person["contactPointEmail"] = ""

counter = 0
for key in new_dict:
    df_creator_person["contactPointID"][counter] = key
    df_creator_person["contactPoint"][counter] = new_dict[key]
    counter += 1
    
df_creator_person.to_csv("DSKG_ContactPoint_Transformation.csv")