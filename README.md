# Dataset Knowledge Graph (DSKG)

## Abstract
We present an approach for constructing an RDF knowledge graph for Datasets. To build the knowledge graph, we use datasets registered in OpenAIRE and Wikidata.
We identify all publications out of 146 million scientific publications which contain mentions of datasets, and establish links between the dataset and publication representations in the [Microsoft Academic Knowledge Graph](http://ma-graph.org). As the author names of datasets can be ambiguous, we develop and evaluate a method for author name disambiguation and enrich the knowledge graph with links to [ORCID](https://orcid.org). Overall, our knowledge graph contains 2,208 datasets with associated properties, as well as 813,551 links to scientific publications. It can be used for a variety of scenarios, facilitating advanced dataset search systems and new ways of measuring and awarding the provisioning of datasets.
The constructed dataset knowledge graph (DSKG) is publicly available at [http://dskg.org](http://dskg.org).

## Knowledge Graph Construction:

We use the following database with metadata about datasets for the creation of the DSKG: 
1. OpenAIRE-Dataset: We consider a subset of the [OpenAIRE Research Graph dump](https://zenodo.org/record/3516918) which contains metadata about datasets. The used dump is created with this code: [https://github.com/michaelfaerber/OpenAIRE](https://github.com/michaelfaerber/OpenAIRE).
2. Wikidata-Dataset: We use instances of the classes of [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) which represent datasets. The instances of the [relevant classes](wikidata-dataset/SPARQL_wikidata_dataset.txt) and their properties can be accessed based on semantic queries via the publicly available [Wikidata SPARQL endpoint](https://query.wikidata.org).

### Identify publications from the MAG which contain mentions of datasets:
We use a string-based algorithm to detect mentions of datasets in papers. We use the files containing the paper abstracts and citation context of the MAG-dump for the matching. For dataset from OpenAIRE, we use the following metadata information to recognize dataset in the files: ``title``, ``originalId`` and ``doi``. For dataset from Wikidata, we use: ``itemLabel``, ``altLabel``, ``officialWebsite``, ``workURL`` and ``url``. [This](string-matching-MAKG-dumps/data) are the used files for the Matching.

1. The first step is to filter out the most frequently used English words for the match. The following Script calculates this not considered intersection: ``string-matching-MAKG-dumps/match_text_corpus.py``
2. For then run the script for the matching. MAG dumps are used as input and the output are text files with the matches found: ``string-matching-MAKG-dumps/string_based_matching_MAKG.py`` 
3. After that, the results are filtered using the created filter list to reduce false matches: ``string-matching-MAKG-dumps/filterwords_matching.py``
4. The following script inserts the found matches into these initial datasets (csv-files) of the OpenAIRE and Wikidata dataset: `string-matching-MAKG-dumps/MAKG_links_in_csv.py``


### Transform tabular metadata to RDF and assign URIs for entities:
We implemented the data transformation of the original metadata using SPARQL CONSTRUCT and SPARQL INSERT queries in [Ontotext's GraphDB graph database](https://graphdb.ontotext.com).

  1. Modify metadata entries according to DCTA (e.g. byteSize). Classification of metadata entities.
  2. Create csv-beta version of the DSKG where the properties are mapped to DCAT but no URIs for the resources are assigned yet (Beta_Version_DSKG_NoIDs.csv)
  3. FOS: input file: PaperFieldsOfStudy.txt from the MAG
  4. Perform author disambiguation
  5. Name the resources with unique URIs (use results from disambiguation)
  6. Create a CSV file with the metadata entries and URIs for each class of entities. 
  7. Load csv-files into a [GraphDB]((https://graphdb.ontotext.com) Repository and transform the table data into RDF using SPARQl CONSTRUCT(link) and SPARQl INSERT(link) queries.
  INSERT: SERVICE <ontorefine:9999999999999> the SPARQL endpoint
  
### Authore Diambiguation:
 1. Calculate the LDA vectors for the data sets (with the LDA model)
 2. Load all needed information for the disambiguation into the csv-file of the beta version of the DSKG
 3. Create a txt-file that contains all the necessary information for the author disambiguation.
 4. Perform the Diambiguation
  
## Linking the authors of the DSKG to ORCID:
  1. Create the authors profiles from the knowledge graph using a SAPRQL query. 
  2. SPARQL query via the MAKG SPARQL endpoint to get the title of the linked papers.
  3. Query of author names via ORCID API
  4. Perform Python-Script that compares author profiles 
  5. Add ORCID-ID to author csv file
  6. Add the ORCID-IDs to the knowledge graph in GraphDB using SPARQL CONSTRUCT and SPARQL INSERT.

 
  

