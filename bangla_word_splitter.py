import re
pattern = re.compile(u'[\u0980-\u09FF]+', re.UNICODE)
sample_file = open('H:/xampp/htdocs/RAKE-BengaliKeywordExtraction/bdtext.txt', 'r',encoding='utf8')
text = sample_file.read()
words = re.findall(pattern,text)
print(words, file=open("output1.txt", "a", encoding='utf8'))