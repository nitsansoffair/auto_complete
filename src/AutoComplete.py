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
            tokenized, tokenized_words = [], []
            for index in range(len(words)):
                word = words[index]
                if len(word) == 0:
                    continue
                if word[-3:] == "...":
                    tokenized_words.append(word[:-3]), tokenized_words.append(word[-3:])
                elif word[-1] in list(".;?"):
                    tokenized_words.append(word[:-1]), tokenized_words.append(word[-1])
                    index += 1
                else:
                    tokenized_words.append(word)
            for word in tokenized_words:
                if word == '':
                    continue
                tokenized.append(word)
            tokenized_sentences.append(tokenized)
        return tokenized_sentences

    def get_tokenized_data(self, data):
        sentences = data.split('\n')
        reduced = []
        for sentence in sentences:
            if len(sentence) == 0 or sentence.isspace():
                continue
            reduced.append(sentence)
        tokenized_sentences = self.tokenize_sentences(reduced)
        return tokenized_sentences

    def count_words(self, tokenized_sentences):
        word_counts = {}
        for sentence in tokenized_sentences:
            for token in sentence:
                if token not in word_counts.keys():
                    word_counts[token] = 1
                else:
                    word_counts[token] += 1
        return word_counts

    def get_words_with_nplus_frequency(self, tokenized_sentences, count_threshold):
        closed_vocab = []
        word_counts = self.count_words(tokenized_sentences)
        for word, cnt in word_counts.items():
            if cnt >= count_threshold:
                closed_vocab.append(word)
        return closed_vocab

    def replace_oov_words_by_unk(self, tokenized_sentences, vocabulary, unknown_token="<unk>"):
        vocabulary = set(vocabulary)
        replaced_tokenized_sentences = []
        for sentence in tokenized_sentences:
            replaced_sentence = []
            for token in sentence:
                if token in vocabulary:
                    replaced_sentence.append(token)
                else:
                    replaced_sentence.append(unknown_token)
            replaced_tokenized_sentences.append(replaced_sentence)
        return replaced_tokenized_sentences