#Adds ORCID IDs to the authors csv file
df = pd.read_csv("/DSKG_CreatorPerson.csv")

with open("/Matches_ORCID.txt", "r") as inp_orcid:
    for line in inp_orcid:
        i = 0
        while i < len(df):
            person_uri = "http://dskg.org/entity/person/" + str(df["creatorPersonID"][i])
            if line.split("\t")[0] == person_uri:
                df["ORCID"][i] = str(line.split("\t")[1]).strip("\t").strip("\n").strip()
            i+=1
                  
df.to_csv("/DSKG_CreatorPerson.csv") 