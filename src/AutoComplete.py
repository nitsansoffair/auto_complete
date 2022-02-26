class AutoComplete:
    def __init__(self):
        pass

    def split_to_sentences(self, data):
        sentences = data.split('\n')
        sentences = [s.strip() for s in sentences]
        sentences = [s for s in sentences if len(s) > 0]
        return sentences