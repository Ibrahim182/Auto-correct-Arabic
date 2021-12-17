class AutoCoreect:
    def __init__(self, words, alph):
        self.words = words
        self.alph = alph
        self.counts = {}
        self.probs = {}
    """
    @ function to make this process (delete , insert, replace, swap) letters
    and return list have all right words that could be right for sentence
    """
    def process(self,word):
        # take unique words of dictionary
        unique_words = set(self.words)
        # delete
        delete = []
        for i in range(len(word)):
            # here we use condition to sure that each word that we create is right and include in dictionary
            if (word[:i] + word[i+1:]) in unique_words:
                delete.append(word[:i] + word[i+1:])
                
        # insert
        insert = []
        for i in range(len(word)+1):
            for char in self.alph:
                if (word[:i]+char+word[i:]) in unique_words:
                    insert.append(word[:i]+char+word[i:])
                    
        # replace
        replace = []
        for i in range(len(word)):
            for char in self.alph:
                if (word.replace(word[i],char)) in unique_words:
                    replace.append(word.replace(word[i],char))
        
        # swap
        swap = []
        for i in range(len(word)-1):
            if (word[:i]+word[i+1]+word[i]+word[i+2:]) in unique_words:
                swap.append(word[:i]+word[i+1]+word[i]+word[i+2:])
        # return all list as one list
        return delete + insert + replace + swap
    """
    @ function to make process in all words that returned from process function
    if no words in list return false and if there take probability of each one to return the biggest one
    """
    def get_result(self,word):
        # I retype them again because the right word in first case is repeated in second and third ....
        self.counts = {}
        self.probs = {}
        res = self.process(word)
        # check if there are words or not
        if len(res) == 0:
            return False
        # take counts for each right word from our all_words
        for word in res:
            self.counts[word] = self.words.count(word)
        # take sum of all count of each word to use it in probability
        conts_words = sum(self.counts.values())
        # take probability of each word
        for word, count in self.counts.items():
            self.probs[word] = count/conts_words
        # sort the probablity of each words but make reverse T and take first one because it has the highest prod
        sorted_prob = sorted(self.probs.items(), key=lambda item: item[1],reverse = True)[0]
        # return word only 
        return sorted_prob[0]