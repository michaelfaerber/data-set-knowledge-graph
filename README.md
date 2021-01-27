# Dataset Knowledge Graph (DSKG)

## Abstract
We present an approach for constructing an RDF knowledge graph for Datasets. To build the knowledge graph, we use datasets registered in OpenAIRE and Wikidata.
We identify all publications out of 146 million scientific publications which contain mentions of datasets, and establish links between the dataset and publication representations in the Microsoft Academic Knowledge Graph. As the author names of datasets can be ambiguous, we develop and evaluate a method for author name disambiguation and enrich the knowledge graph with links to ORCID. Overall, our knowledge graph contains 2,208 datasets with associated properties, as well as 813,551 links to scientific publications. It can be used for a variety of scenarios, facilitating advanced dataset search systems and new ways of measuring and awarding the provisioning of datasets.
The constructed dataset knowledge graph (DSKG) is publicly available at [http://dskg.org](http://dskg.org).

## Knowledge Graph Construction:

We use the following database with metadata about datasets for the creation of the DSKG: 
1. We consider a subset of the OpenAIRE Research Graph dump which contains metadata about datasets. The used dump is created with this code: [https://github.com/michaelfaerber/OpenAIRE](https://github.com/michaelfaerber/OpenAIRE).
2. Wikidata: Sparql querie, endpoit & relevante Klassen Liste. 

### Identify publications from the MAKG which contain mentions of datasets:

### Transform tabular metadata to RDF and assign URIs for entities:
  1. Modify metadata entries according to DCTA (e.g. byteSize). Classification of metadata entities.
  2. Create csv-beta version of the DSKG where the properties are mapped to DCAT but no URIs for the resources are assigned yet (Beta_Version_DSKG_NoIDs.csv)
  3. Perform authors disambiguation
  4. Name the resources with unique URIs
  5. Create a CSV file with the metadata entries and URIs for each class of entities. 
  6. Load csv-files into GraphDB and transform the table data into RDF using SPARQl CONSTRUCT and SPARQl INSERT queries.
  
### Authore Diambiguation:
 1. Calculate the LDA vectors for the data sets (with the LDA model)
 2. Create a txt-file that contains all the necessary information for the author disambiguation.
 3. Perform the Diambiguation
  
## Linking the authors of the DSKG to ORCID:
  1. Create the authors profiles from the knowledge graph using a SAPRQL query. 
  2. SPARQL query via the MAKG SPARQL endpoint to get the title of the linked papers.
  3. Query of author names via ORCID API
  4. Perform Python-Script that compares author profiles 
  5. Add ORCID-ID to author csv file
  6. Add the ORCID-IDs to the knowledge graph in GraphDB using SPARQL CONSTRUCT and SPARQL INSERT.

 
  

