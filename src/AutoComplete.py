class AutoComplete:
    def __init__(self):
        pass

    def split_to_sentences(self, data):
        sentences = data.split('\n')
        sentences = [s.strip() for s in sentences]
        sentences = [s for s in sentences if len(s) > 0]
        return sentences

    def tokenize_sentences(self, sentences):
        tokenized_sentences = []
        for sentence in sentences:
            sentence = sentence.lower()
            words = sentence.split(' ')
            tokenized = []
            for index in range(len(words)):
                word = words[index]
                if len(word) == 0:
                    continue
                if word[-3:] == "...":
                    tokenized.append(word[:-3]), tokenized.append(word[-3:])
                elif word[-1] in list(".;?"):
                    tokenized.append(word[:-1]), tokenized.append(word[-1])
                    index += 1
                else:
                    tokenized.append(word)
            tokenized_sentences.append(tokenized)
        return tokenized_sentences