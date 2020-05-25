from abc import abstractmethod
import re


class SearchEngineBase():
    def __init__(self):
        pass

    def add_file(self, file_url):
        with open(file_url, mode='r') as f:
            txt = f.read()
        self.process_file(file_url, txt)

    @abstractmethod
    def process_file(self, id, text):
        pass

    @abstractmethod
    def search_file(self, kw):
        pass

class SearchEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        self.__id_to_text = {}

    def process_file(self, id, text):
        self.__id_to_text[id] = text

    def search_file(self, kw):
        result = []
        for k, v in self.__id_to_text.items():
            if kw in v:
                result.append(k)
        return result


def main(search_engine:SearchEngine):
    for f in ['search_engine_OO_1.txt','search_engine_OO_2.txt','search_engine_OO_3.txt','search_engine_OO_4.txt','search_engine_OO_5.txt']:
        search_engine.add_file(f)

    while True:
        query = input('input keyword')
        results = search_engine.search_file(query)
        print(f'found {len(results)} results.')
        for i in results:
            print(i)


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    @staticmethod
    def parse_id_to_words(txt):
        text = re.sub(r'[^\w]', ' ', txt)
        text = text.lower()
        word_list = text.split(' ')
        word_list = filter(None, word_list)
        return set(word_list)

    def process_file(self, id, text):
        self.__id_to_words[id] = self.parse_id_to_words(text)

    @staticmethod
    def query_match(query, target):
        for i in query:
            if i not in target:
                return False
        return True

    def search_file(self, kw):
        query_words_list = self.parse_id_to_words(kw)
        results = []
        for k, v in self.__id_to_words.items():
            if self.query_match(query_words_list, v):
                results.append(k)
        return results


if __name__ == '__main__':
    # search_worker = SearchEngine()
    search_worker = BOWEngine()
    main(search_worker)








































