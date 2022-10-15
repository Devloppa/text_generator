from nltk.tokenize import regexp_tokenize
from nltk import bigrams
from nltk.util import ngrams


class MyCorpus:

    def __init__(self, ngram=None):
        self.file_name = input()
        self.file = None
        self.file_str = ""
        self.tokens = []
        self.unique_tokens = None
        self.bigrams = None
        self.ngram = ngram

        self.get_file_object()
        self.file_to_string()
        self.regexp_tokenize()
        self.get_unique_tokens()
        self.create_nltk_ngram()
        self.print_bigrams_stats()
        self.interact_with_bigrams()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_file()

    def close_file(self):
        self.file.close()

    def get_file_object(self):
        try:
            self.file = open(self.file_name, "r", encoding="utf-8")
        except FileNotFoundError:
            print("FileNotFound Error. Please input an existing file")

    def file_to_string(self):
        self.file_str = self.file.read()
        self.file.close()
        self.get_file_object()

    def regexp_tokenize(self):
        self.tokens = regexp_tokenize(self.file_str, r"[^\s]+")

    def print_stats(self):
        print("Corpus statistics")
        print(f"All tokens: {len(self.tokens)}")
        print(f"Unique tokens: {len(self.unique_tokens)}")

    def print_bigrams_stats(self):
        print(f"{len(self.bigrams)}")

    def get_unique_tokens(self):
        self.unique_tokens = set(self.tokens)

    def interact_with_corpus(self):
        try:
            user_input = input()
            if user_input == "exit":
                return
            int_user_input = int(user_input)
            print(self.tokens[int_user_input])
            self.interact_with_corpus()
        except ValueError:
            print("Value Error. Please input an integer.")
            self.interact_with_corpus()
        except TypeError:
            print("Type Error. Please input an integer.")
            self.interact_with_corpus()
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus")
            self.interact_with_corpus()

    def create_bigrams(self):
        self.bigrams = [self.tokens[i:i+2] for i in range(len(self.tokens) - 1)]

    def create_nltk_bigrams(self):
        self.bigrams = tuple(bigrams(self.tokens))

    def create_nltk_ngram(self):
        self.bigrams = list(ngrams(self.tokens, self.ngram))
    
    def print_bigram(self, num):
        print(f"Head: {self.bigrams[num][0]} Tail: {self.bigrams[num][1]}")

    def interact_with_bigrams(self):
        try:
            user_input = input()
            if user_input == "exit":
                return
            user_input = int(user_input)
            self.print_bigram(user_input)
            self.interact_with_bigrams()
        except ValueError:
            print("Value Error. Please input an integer.")
            self.interact_with_bigrams()
        except TypeError:
            print("Type Error. Please input an integer.")
            self.interact_with_bigrams()
        except IndexError:
            print("Index Error. Please input a value that is not greater than the number of all bigrams.")
            self.interact_with_bigrams()


app = MyCorpus(ngram=2)
