from nltk.tokenize import regexp_tokenize


class MyCorpus:

    def __init__(self):
        self.file_name = input()
        self.file = None
        self.file_str = ""
        self.tokens = []
        self.unique_tokens = None

        self.get_file_object()
        self.file_to_string()
        self.regexp_tokenize()
        self.get_unique_tokens()
        self.print_stats()
        self.interact_with_corpus()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_file()

    def regexp_tokenize(self):
        self.tokens = regexp_tokenize(self.file_str, r"[^\s]+")

    def close_file(self):
        self.file.close()

    def print_stats(self):
        print("Corpus statistics")
        print(f"All tokens: {len(self.tokens)}")
        print(f"Unique tokens: {len(self.unique_tokens)}")

    def file_to_string(self):
        self.file_str = self.file.read()
        self.get_file_object()

    def get_file_object(self):
        try:
            self.file = open(self.file_name, "r", encoding="utf-8")
        except FileNotFoundError:
            print("FileNotFound Error. Please input an existing file")

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


app = MyCorpus()
