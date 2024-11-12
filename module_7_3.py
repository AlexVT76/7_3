class WordsFinder:
    def __init__(self,*args):
        self.file_name=[]
        for i in args:
            self.file_name.append(i)
    def get_all_words(self):
        all_words = {}
        for i in self.file_name:
            word_str=[]
            with open(i,encoding='utf8') as file:
                marks=[',', '.', '=', '!', '?', ';', ':', ' - ']
                for line in file:
                    for x in line:
                        if x in marks:
                            line=line.replace(x,' ')
                    line= line.lower().split()
                    for elem in line:
                         word_str.append(elem)
                all_words [i] = word_str
        return  all_words
    def find (self,word):
        word=word.lower()
        dict_result={}
        for i,words in  self.get_all_words().items():
            if word in words:
                dict_result [i] = words.index(word)+1
        return dict_result
    def count(self,word):
        word = word.lower()
        dict_result = {}
        for i,words in  self.get_all_words().items():
            if word in words:
                dict_result[i] = words.count(word)
        return  dict_result












finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
