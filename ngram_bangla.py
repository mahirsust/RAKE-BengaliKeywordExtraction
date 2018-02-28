from nltk import ngrams
sample_file = open('H:/xampp/htdocs/RAKE-BengaliKeywordExtraction/oneline_bangla.txt', 'r',encoding='utf8')
text = sample_file.read()
n = 3
sixgrams = ngrams(text.split(), n)
for grams in sixgrams:
  print(grams, file=open("output2.txt", "a", encoding='utf8'))