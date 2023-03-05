import timeit

class Graph:
    def __init__(self):
        self._word_dict = {}
        self._visited = set()

    def _add_word(self, word: str, synonyms: list[str]) -> None:
        # If word already exists, add the synonyms
        # Else add the word to the graph and initialize synonyms
        if word in self._word_dict:
            self._word_dict[word].update(synonyms)
        else:
            self._word_dict[word] = set(synonyms)

    def _find_all_synonyms(self, synonyms: list[str]) -> None:
        # Search graph for all synonyms of the word in the given synonyms list
        for syn in synonyms:
            if syn not in self._visited:
                self._visited.add(syn)
                synonyms.extend(self.get_synonyms(syn))
                self._find_all_synonyms(synonyms)

    def _add_transitive_synonyms(self, synonyms: list[str]) -> None:
        # Add synonyms using transitive rule
        self._find_all_synonyms(synonyms)
        for syn in self._visited:
            synonyms_to_syn = [x for x in self._visited if x != syn]
            
            self._add_word(syn, synonyms_to_syn)
        
        self._visited = set()

    def add_word(self, word: str, synonyms: list[str] = []) -> None:
        # Add a word and its synonyms
        synonyms.append(word)
        synonyms = [x.lower().strip() for x in synonyms]
        self._add_transitive_synonyms(synonyms)

    def get_synonyms(self, word: str) -> set[str]:
        # If the dict contains word return all synonyms for the given word
        # Else return an empty set
        word = word.lower().strip()
        if word in self._word_dict:
            return list(self._word_dict[word])
        else:
            return []
        
