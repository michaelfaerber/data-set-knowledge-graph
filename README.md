# dataset-knowledge-graph

#### Linking the authors to ORCID:
  1. Create the authors' profiles in the knowledge graph using a SAPRQL query. 
  2. SPARQL query via the MAKG SPARQL endpoint to get the title of the linked papers.
  3. Query of author names via ORCID API
  4. Perform Python-Script that compares authors' profiles 
  5. Add ORCID ID to author csv file


#### Knowledge Graph Construction:
  1. Modify metadata entries according to DCTA (e.g. byteSize). Classification of metadata entities.
  2. Create csv-beta version of the DSKG where the properties are mapped to DCAT but no URIs for the resources are assigned yet (Beta_Version_DSKG_NoIDs.csv)
  3. Perform authors disambiguation
  4. Name the resources with unique URIs
  5. Create a CSV file with the metadata entries and URIs for each class of entities. 
  6. Load csv-files into GraphDB and transform the table data into RDF using SPARQl CONSTRUCT and SPART INSERT queries-
  
  
 #### Authore Diambiguation
 1. Calculate the LDA vectors for the data sets (with the LDA model)
 2. Create a txt-file that contains all the necessary information for the author disambiguation.
 3. Perform the Diambiguation
