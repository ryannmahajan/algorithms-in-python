
class WordDictionary:
        
    def __init__(self, word=''):
        self.word = word
        self.char_assosciations = {}

        self.is_word = False        
    
    def addWord(self, word: str, next_char_index = 0) -> None:
        if self.word == word:
            self.is_word = True
            return

        char = word[next_char_index]
        self.create_assosciation_if_not_exist(word[0:next_char_index+1], char)

        self.char_assosciations[char].addWord(word, next_char_index + 1)

    def create_assosciation_if_not_exist(self, word_so_far, char):
        if char not in self.char_assosciations:
            word_node = WordDictionary(word_so_far)
            self.char_assosciations[char] = word_node

    def search(self, word: str) -> bool:
        node = self.find_node_for_word(word)
        return node is not None and node.is_word
    
    def find_node_for_word(self, word, next_char_index=0):
        if next_char_index==len(word):
            return self if (self.word[-1] == word[-1] or '.'==word[-1]) else None

        look_for_char = word[next_char_index]

        if look_for_char=='.':
            for child_node in self.char_assosciations.values():
                res = child_node.find_node_for_word(word, next_char_index+1)
                print(vars(res))
                if res is not None: return res
            return None
        elif look_for_char not in self.char_assosciations:
            return None
        else: 
            return self.char_assosciations[look_for_char].find_node_for_word(word, next_char_index+1)

    def startsWith(self, prefix: str) -> bool:
        node = self.find_node_for_word(prefix)
        return node is not None
        
