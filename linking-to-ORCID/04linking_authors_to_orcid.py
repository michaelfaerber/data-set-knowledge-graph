#Comparison of author profiles of authors from DSKG and ORCID 
import math
import re
from pyjarowinkler import distance
from collections import Counter
import pandas as pd
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

df = pd.read_csv("/DSKG_Author_Profiles_MAKGTitels")
WORD = re.compile(r"\w+")



def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def remove_stopWords(string):
    string_split = string.split(" ")
    output = ""
    for word in string_split:
        if word not in stop_words:
            output += word + " "
    output = output.strip()
    return output

def get_PaperTitles_for_ID(author_id):
    paper_titles_list = []
    i = 0
    while i < len(df):
        if df["creator"][i] == author_id:
            paper_titles = df["paper_title"][i]
            paper_titles_list = str(paper_titles).split("; ")
        i += 1
    return paper_titles_list
        
#Compare MAKG PaperTitle with ORCID-Work
def compare_PaperTitles(author_orcid, author_dskg):
    number_Matches = 0
    dskg_id = author_orcid.split("\t")[0].strip()
    dskg_id_papers = get_PaperTitles_for_ID(dskg_id)
    
    orcid_work_titles = author_orcid.split("\t")[2].strip().split("; ")
    
    for dskgPaper in dskg_id_papers:
        for orcidWork in orcid_work_titles:
            vector1 = text_to_vector(dskgPaper)
            vector2 = text_to_vector(orcidWork)
            cosine = get_cosine(vector1, vector2)
            if cosine > 0.75: #0.75
                number_Matches += 1
    return number_Matches
    

def compare_Titels(author_orcid, author_dskg):
    titels_orcid = remove_stopWords(author_orcid.split("\t")[2].strip().lower())
    titels_dskg = remove_stopWords(author_dskg.split("\t")[2].strip().lower())
    titels_dskg_clean = ""
    titels_orcid = set(titels_orcid.split("; "))
    titels_dskg = set(titels_dskg.split(", "))  
    if "nan" in titels_orcid:
        titels_orcid.remove("nan")
    if "nan" in titels_dskg:
        titels_dskg.remove("nan")
    return len(titels_orcid.intersection(titels_dskg))

def compare_author_initials(author1, author2):
    author1_initials = set()
    author2_initials = set()
    author1_names = author1.split(" ")
    author2_names = author2.split(" ")
    for name in author1_names:
        author1_initials.add(name[:1])
    for name in author2_names:
        author2_initials.add(name[:1])
    return len(author1_initials.intersection(author2_initials))
    

def compare_CoAutors(author_orcid, author_dskg):
    number_Matches = 0
    coAuthors_orcid = set(author_orcid.split("\t")[4].split("; "))
    coAuthors_dskg = set(author_dskg.split("\t")[3].split(", "))
    if "nan" in coAuthors_orcid:
        titels_orcid.remove("nan")
    if "nan" in coAuthors_dskg:
        titels_dskg.remove("nan")
 
    for author_dskg in coAuthors_dskg:
        for author_orcid in coAuthors_orcid:
            if author_dskg != "" and author_orcid != "":
                jaro_distance = distance.get_jaro_distance(str.lower(author_dskg), str.lower(author_orcid), winkler=True, scaling=0.1)
                vector1 = text_to_vector(author_dskg)
                vector2 = text_to_vector(author_orcid)
                cosine_sim = get_cosine(vector1, vector2)  
                if (jaro_distance > 0.9 and (compare_author_initials(author_dskg, author_orcid) >= 2)) or (cosine_sim > 0.98):              
                    number_Matches += 1
            
    return number_Matches
 
       
def compare_Sources(author_orcid, author_dskg):
    sources_orcid = set(author_orcid.split("\t")[3].split("; "))
    sources_dskg = set(author_dskg.split("\t")[4].strip("\n").split(", "))
    
    sources_normalized_orcid = set()
    sources_normalized_dskg = set()
    for source in sources_orcid:
        source = source.replace("https://doi.org/", "")
        sources_normalized_orcid.add(source)
    for source in sources_dskg:
        source = source.replace("https://doi.org/", "")
        sources_normalized_dskg.add(source)
    if len(sources_normalized_orcid) == 0 or len(sources_normalized_dskg) == 0:
        return 0
    else:
        return len(sources_normalized_orcid.intersection(sources_normalized_dskg))

counter_source = 0
    
def compare_Authors(author_orcid, author_dskg):
    score = 0
    
    if compare_Titels(author_orcid, author_dskg) == 1:
        score += 1
        outp_counter.write("Titel1" + "\n")
    elif compare_Titels(author_orcid, author_dskg) == 2:
        score += 2 
        outp_counter.write("Titel2" + "\n")
    elif compare_Titels(author_orcid, author_dskg) >= 2:
        score += 4
        outp_counter.write("Titel3" + "\n")
        
    if compare_CoAutors(author_orcid, author_dskg) == 1:
        score += 3 
        outp_counter.write("CoAuthor1" + "\n")
    if compare_CoAutors(author_orcid, author_dskg) >= 1:
        score += 4
        outp_counter.write("CoAuthor2" + "\n")

    if compare_Sources(author_orcid, author_dskg) >= 1:
        score += 4
        outp_counter.write("Source" + "\n")
      
        
    if compare_PaperTitles(author_orcid, author_dskg) >= 1:
        score += 4 
        outp_counter.write("MAKG" + "\n")

      
 
    return score
 


with open("/ORCID_AuthorProfiles_Comparison.txt", "r") as inp_orcid: 
    with open("/DSKG_AuthorProfiles_Comparison.txt", "r") as inp_dskg:    
        with open("/Matches_ORCID.txt", "w") as outp:
            for line_orcid, line_dskg in zip(inp_orcid, inp_dskg):
                if compare_Authors(line_orcid, line_dskg) > 3:
                    dskg_id = line_orcid.split("\t")[0]
                    orcid_id = line_orcid.split("\t")[1]
                    outp.write(dskg_id + "\t" + orcid_id + "\n")