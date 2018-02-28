from __future__ import absolute_import
from __future__ import print_function
__author__ = 'a_medelyan'
import rake

# EXAMPLE: Extracting single words from a French text

# French stopwords
stoppath = "H:/xampp/htdocs/RAKE-BengaliKeywordExtraction/stopword.txt"

# 1. initialize RAKE by providing a path to a stopwords file and setting phrase length in words to 1
rake_object = rake.Rake(stoppath, 5, 1, 4)

# 2. run on RAKE on a given text
sample_file = open("H:/xampp/htdocs/RAKE-BengaliKeywordExtraction/bdtext.txt", 'r', encoding="utf8")
text = sample_file.read()
keywords = rake_object.run(text)

# 3. print results
for k in keywords:
    print(k[0])
