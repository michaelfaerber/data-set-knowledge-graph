#Filter OpenAIRE titles
filter_title = ['Quality of Life', 'Experimental data', 'Energy Consumption', 'Image data', 'water pump', 'Figure 1', 'Data set', 'time series', 'Machine Learning',
'Linear regression', 'Type 2 Diabetes', 'Carbon Nanotubes', 'Oil and Gas', 'real estate', 'Figure 2', 'Available data', 'Human Resource', 
'Training Data', 'VoxEL', 'Figure 3', 'Thrombolysis', 'Raw data', 'phonons', 'Simulation result', 'Figure 4', 'Exchange Rates', 
'Research Paper', 'sample data', 'Stock Price', 'Natural language processing', 'Table 2', 'Social interactions', 'Tweets', 'Digital Media', 
'Figure 5', 'anomaly detection', 'Ebola', 'BASE DE DATOS', 'perovskites', 'Conjoint', 'Satellite Imagery', 
'Census data', 'World Population', 'All results', 'student performance', 'Experiment Data', 'Indoor Positioning', 
'Semantic similarity', 'climate data', 'Countries of the world', 'Supplementary data', 'Sales Data', 'Supplementary Information', 
'Robotic surgery', 'Cosmetic Products', 'News Articles', 'image files', 'Acoustic data', 'Food choices', 'Human Development Index', 
'Data sheet', 'Health Insurance Coverage', 'Appendix 1', 'Sedimentology', 'Eye Gaze', 'Network Intrusion Detection', 'Sample Images', 
'Site information', 'Supplementary Materials', 'Word2Vec', 'Song Lyrics', 'Wine Quality', 'test dataset', 'Original dataset', 
'Protein interaction networks', 'Proxy data', 'Data 2', 'Supplemental Information', 'CYBER CRIME', 'DDY', 'Cohort Data', 'Survival data.', 
'Truth table','FIFA World Cup', 'Feature Subset Selection', 'CUSTOMER CHURN', 'Liquid foam', 'Database 2', 'Field temperature', 'test video', 
'Full dataset', 'Database 7']

with open("/OpenAIRE_title_matches.txt", "r") as inp:
    with open("OpenAIRE_title_matches_filtered.txt", "w") as outp:
        tagged_lines = (line for line in inp if not any(line.startswith(tag) for tag in filter_title))
        for line in tagged_lines:
            outp.write(line)


#Filter Wikidata itemLabel
filter_title = ['Source', 'Atlas']

with open("/Wikidata_itemLabel_matches.txt", "r") as inp:
    with open("Wikidata_itemLabel_matches_filtered.txt", "w") as outp:
        tagged_lines = (line for line in inp if not any(line.startswith(tag) for tag in filter_title))
        for line in tagged_lines:
            outp.write(line)

#Filter Wikidata AltLabel
filter_title = ['deaths', 'The 10', 'April 30', 'October 31', 'event log', 'ontology matching', 
                'my school', 'Pandora']

with open("/Wikidata_altLabel_matches.txt", "r") as inp:
    with open("Wikidata_altLabel_matches_filtered.txt", "w") as outp:
        tagged_lines = (line for line in inp if not any(line.startswith(tag) for tag in filter_title))
        for line in tagged_lines:
            outp.write(line)