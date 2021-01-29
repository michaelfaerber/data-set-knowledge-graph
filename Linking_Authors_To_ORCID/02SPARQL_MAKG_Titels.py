#Queries the titles of publications from the MAKG via the public SPARQL endpoint.
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
df = pd.read_csv("/DSKG_Author_Profiles.csv")
df["paper_title"] = ""

def sparql_PaperTitle(paper_uri):
    sparql = SPARQLWrapper("http://ma-graph.org/sparql")
    uri = "<{0}>".format(paper_uri)

    sparql.setQuery("\n"
                    "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>"
                    "PREFIX magc: <http://ma-graph.org/class/>"
                    "PREFIX dcterms: <http://purl.org/dc/terms/>"
                    "PREFIX foaf: <http://xmlns.com/foaf/0.1/>\n"
                    "PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>\n"
                    "SELECT distinct ?paperTitle   WHERE {\n"
                   +uri+" dcterms:title ?paperTitle"
                    "}\n"
                    "                   ")
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    title = ""
    for result in results["results"]["bindings"]:
        title += result["paperTitle"]["value"]
    return title
    
    
    

i = 0
while i < len(df):
    mag_uris = df["paper"][i]
    mag_uris_list = mag_uris.split(", ")
    for uri in mag_uris_list:
        title = sparql_PaperTitle(uri)
        if len(title) > 1:
            df["paper_title"][i] = df["paper_title"][i] + title + "; "
        
    max_len = len(str(df["paper_title"][i]))
    unwanted_cut_off = max_len - 2
    df["paper_title"][i] = str(df["paper_title"][i])[0:unwanted_cut_off]
        
    i += 1
    print(i)
    
df.to_csv("/DSKG_Author_Profiles_MAKGTitels") 
