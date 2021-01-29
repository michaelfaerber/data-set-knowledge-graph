#Checks which record titles occur in the English Language Corpus
#Do this for the first 50.000 Words for OpenAIRE_title and Wikidata_Label
#Do this for the first 100.000 Words for  Wikidata_AltLabel
#Used Dataset for the English Language Corpus: English Word Frequency - https://www.kaggle.com/rtatman/english-word-frequency

    
with open(".../OpenAIRE_title.txt") as f:
    titles = f.readlines()
    
with open(".../EnglishLanguageCorpus_50k.txt") as v:
    elc = v.readlines()
    
with open(".../OpenAIRE_title_filtered.txt", "w") as outp:
    for linea in titles:
        for lineb in elc:
            if linea.lower() == lineb:
                outp.write(str(linea))