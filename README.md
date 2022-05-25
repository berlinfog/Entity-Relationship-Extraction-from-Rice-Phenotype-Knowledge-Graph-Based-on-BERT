# Entity Relationship Extraction from Rice Phenotype Knowledge Graph Based on BERT

 Transactions of the Chinese Society for Agricultural Machinery Journal Articles
1 is the python scrapy code and dataset
2 is the bert relation extract model and Neo4j database
3 is the ask-answer model from Baidu AnyQ(ANswer Your Questions)  project
4 is the python code consisting of Django,Sqlite

Essay abstract:

Abstract: Rice phenotype has an important guiding role in rice research by analyzing genetic information of various phenotype data. Knowledge graph technology has been widely used in knowledge storage and search engines by structurally describing the information, concepts, entities and relationships in data. As a key task in the knowledge graph, the relation extraction task can extract the connection between two entity words in the text. Within this research, rice phenotypic data was collected from the National Rice Data Center, and the data were preprocessed and annotates. The rice phenotype relationship was proposed based on the plant ontology, then method of bidirectional encoder representation from transformers is applied for classifying
relation between rice genomics, environment, and phenotype data based on plant ontology. Then the word vector, position vector and sentence vector were extracted in the relation dataset, and rice phenotype relation extraction model was realized based on BERT. Finally, the results of BERT model was compared with the convolutional neural network and the piecewise convolutional network model. In the comparison of the three relationship extraction models, BERT achieved the best performance, and reached an accuracy of 95.10% and F1 value of 95.85%. Deep learning methods were used to improve the performance of relation extraction of knowledge graphs, and provide technical support for the efficient construction of a rice phenotype knowledge graph system
