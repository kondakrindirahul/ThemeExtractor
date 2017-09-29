# ThemeExtractor
* The ThemeExtractor.py finds the theme or main topic of a sentence.   
* It does so by extracting the subject phrases as well as object phrases from the sentence.  
* A dependency parser is used for this purpose. 
* The dependency parser finds the dependencies among the various words present in a sentence. 
* The dependencies are mapped based on a predefined set of Dependency condition preferences.  
* The Dependency parsers are pretrained using TreeBanks. TreeBank is a parsed text corpus that annotates syntactic or semantic sentence structure. 
* In most cases, the treebanks are built manually by constructing a dependency tree for each sentence in the corpus.  
* The Dependency parser parses our sentence by making use of the predefined rules and knowledge obtained during the pretraining of parser.  
* The dependency parser is provided by spaCy which is an industrial strength Natural Language Processing toolkit that has faster implementation than the NLTK.  
* There are different parsers which provide the dependency parsing feature such as <br>
(i)  CMU's TurboParser      
(ii) Stanford Dependency Parser      
(iii)NLTK's Projective Dependency Parser etc.
