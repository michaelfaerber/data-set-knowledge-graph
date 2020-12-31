import pandas as pd
import requests
import xml.etree.ElementTree as et 
import urllib
import json
from xml.etree.ElementTree import XML, SubElement, Element, tostring
from unidecode import unidecode

def normalize_name(name):
    normalized_name = unidecode(name)
    normalized_name = str.lower(normalized_name)
    return normalized_name

def compare_name(author1, author2):
    names1 = set(author1.split(" "))
    names2 = set(author2.split(" "))
    return len(names1.intersection(names2))

def remove_unwanted(string):
    if string.endswith("; "):
        max_len = len(string)
        unwanted_cut_off = max_len - 2
        string = string[0:unwanted_cut_off]
    return string


df = pd.read_csv("/DSKG_Author_Profiles.csv")


with open("/ORCID_AuthorProfiles_Comparison.txt", "w") as outp_orcid:
    with open("/DSKG_AuthorProfiles_Comparison.txt", "w") as outp_dskg:
        i = 0
        while i < len(df): 
            author_id = df["creator"][i]
            author_name = df["creatorName"][i]
            author_name_original = df["creatorName"][i]
            #Only consider names that consist of at least two Terms
            try:
                author_name_split = author_name.split(' ')
            except:
                i += 1
                continue

            #Queries author names via API
            querie = ("https://pub.orcid.org/v3.0/search/?q=text:{0}&start=0&rows=25".format(author_name))
            r = requests.get(querie)
            root = et.fromstring(r.content)

            #Checks every entity that is returned by the API
            for child in root.iter('{http://www.orcid.org/ns/common}path'):
                orcid_id = child.text
                querie_2 = ("https://pub.orcid.org/v3.0/{0}/personal-details".format(orcid_id))
                r_2 = requests.get(querie_2)
                root_2 = et.fromstring(r_2.content)

                fullname_orcid = ""

                for child in root_2.iter('{http://www.orcid.org/ns/personal-details}given-names'):
                    fullname_orcid += child.text + " "
                for child in root_2.iter('{http://www.orcid.org/ns/personal-details}family-name'):
                    fullname_orcid += child.text + " "

                if fullname_orcid.endswith(" "):
                    max_len = len(fullname_orcid)
                    unwanted_cut_off = max_len - 1
                    fullname_orcid = fullname_orcid[0:unwanted_cut_off]

                author_name = normalize_name(author_name)
                fullname_orcid = normalize_name(fullname_orcid)
                if compare_name(author_name, fullname_orcid) >= 2:  
                    try:              
                        querie_3 = "https://pub.orcid.org/v3.0/{0}/record".format(orcid_id) 
                        r_3 = requests.get(querie_3)
                        root_3 = et.fromstring(r_3.content)
                        works = "" 
                        for child in root_3.iter('{http://www.orcid.org/ns/work}work-summary'):
                            works += child.attrib["put-code"] + ","
                        
                        max_len = len(works)
                        unwanted_cut_off = max_len - 1
                        works = works[0:unwanted_cut_off]

                        querie_4 = "https://pub.orcid.org/v3.0/{0}/works/{1}".format(orcid_id, works) 
                        r_4 = requests.get(querie_4)
                        rootr_4 = et.fromstring(r_4.content)
                    
                        orcid_titles = ""
                        orcid_sources = ""
                        orcid_coAuthors = ""

                        for child in rootr_4.iter('{http://www.orcid.org/ns/common}title'):
                            orcid_titles += child.text + "; "
                        for child in rootr_4.iter('{http://www.orcid.org/ns/common}external-id-value'):
                            orcid_sources += child.text + "; "
                        for child in rootr_4.iter('{http://www.orcid.org/ns/work}credit-name'):
                            orcid_coAuthors += child.text + "; "

                        orcid_titles = remove_unwanted(orcid_titles)
                        orcid_sources = remove_unwanted(orcid_sources)
                        orcid_coAuthors = remove_unwanted(orcid_coAuthors)
                 
                        orcid_titles = orcid_titles.replace("\t", "").replace("\n", "").strip()
                        orcid_sources = orcid_sources.replace("\t", "").replace("\n", "").strip()
                        orcid_coAuthors = orcid_coAuthors.replace("\t", "").replace("\n", "").strip()
                    
                        coAuthors_dskg = str(df["coAuthors"][i]).replace(author_name_original+", ", "").replace(", "+author_name_original, "").replace(author_name_original, "")
                       
                        outp_dskg.write(str(df["creator"][i]) + "\t" + str(df["creatorName"][i]) + "\t" + str(df["title"][i]) + ", " + str(df["alternative"][i]) + "\t" + str(coAuthors_dskg) + "\t" + str(df["landingPage"][i]) + ", " + str(df["identifier"][i]) + "\n")
                        outp_orcid.write(str(df["creator"][i]) + "\t" + orcid_id + "\t" + orcid_titles + "\t" + orcid_sources + "\t" + orcid_coAuthors + "\n")

                    except:
                        print("Exception for the API query")
                    
            i += 1
            print(i)