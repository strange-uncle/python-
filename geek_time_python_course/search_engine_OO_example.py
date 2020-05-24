from abc import abstractmethod

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

if __name__ == '__main__':
    search_worker = SearchEngine()
    main(search_worker)

