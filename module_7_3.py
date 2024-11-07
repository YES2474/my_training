class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            all_words_list = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    for i in [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']:
                        line = line.replace(i, ' ')
                    line = line.lower().split(' ')
                    for word in line:
                        if word.__eq__(''):
                            continue
                        else:
                            all_words_list.append(word)

        all_words.update({file_name: all_words_list})
        return all_words

    def find(self, word):
        counter = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if i.lower().__eq__(word.lower()):
                    counter += 1
                    return {name: counter}
                else:
                    counter += 1

    def count(self, word):
        counter = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if i.lower().__eq__(word.lower()):
                    counter += 1
                else:
                    continue
        return {name: counter}


if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())  # Все слова
    print(finder.find('TEXT'))  # 3 слово по счёту
    print(finder.count('teXT'))  # 4 слова teXT в тексте всего