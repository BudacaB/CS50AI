import math
import os
import string

import nltk
import sys

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = {}
    for filename in os.listdir(directory):
        file_text = open(os.path.join(directory, filename), 'r')
        files[filename] = file_text.read()
        file_text.close()
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    processed_document = [
        word for word in
        nltk.word_tokenize(document.lower())
        if word not in string.punctuation and word not in nltk.corpus.stopwords.words("english")
    ]
    return processed_document


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs_dict = {}
    number_of_docs = len(documents.keys())
    for doc, words in documents.items():
        seen = set()
        for word in words:
            if word not in seen:
                if word in idfs_dict:
                    idfs_dict[word] = idfs_dict[word] + 1
                    seen.add(word)
                elif word not in idfs_dict:
                    idfs_dict[word] = 1
                    seen.add(word)
    for word, appearances in idfs_dict.items():
        idfs_dict[word] = math.log(number_of_docs / appearances)
    return idfs_dict


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    file_ranks_dict = {}
    file_ranks_list = []
    for doc, words in files.items():
        file_ranks_dict[doc] = 0
        for term in query:
            word_count = len(list(filter(lambda word: word == term, words)))
            if word_count > 0:
                file_ranks_dict[doc] += word_count * idfs[term]
    ranks_list = list(file_ranks_dict.items())
    ranks_list.sort(key=lambda x: x[1], reverse=True)
    for pair in ranks_list:
        file_ranks_list.append(pair[0])
    return file_ranks_list[0:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sentence_ranks_dict = {}
    sentence_ranks_list = []
    for sentence, words in sentences.items():
        sentence_ranks_dict[sentence] = 0
        for term in query:
            if term in words:
                sentence_ranks_dict[sentence] += idfs[term]
    ranks_list = list(sentence_ranks_dict.items())
    ranks_list.sort(key=lambda x: x[1], reverse=True)
    reduced_ranks_list = ranks_list[0:(n + 1)]
    # matching word measure comparison and adjustment
    for index, elem in enumerate(reduced_ranks_list):
        query_term_density = 0
        query_term_density_next = 0
        if index + 1 < len(reduced_ranks_list) and elem[1] == reduced_ranks_list[index + 1][1]:
            sentence_length = len(sentences[elem[0]])
            for word in sentences[elem[0]]:
                if word in query:
                    query_term_density += 1
            query_term_density = query_term_density / sentence_length
            sentence_length_next = len(sentences[reduced_ranks_list[index + 1][0]])
            for word in sentences[reduced_ranks_list[index + 1][0]]:
                if word in query:
                    query_term_density_next += 1
            query_term_density_next = query_term_density_next / sentence_length_next
        if query_term_density < query_term_density_next:
            temp_sentence = elem
            reduced_ranks_list[index] = reduced_ranks_list[index + 1]
            reduced_ranks_list[index + 1] = temp_sentence
    for pair in reduced_ranks_list:
        sentence_ranks_list.append(pair[0])
    return sentence_ranks_list[0:n]


if __name__ == "__main__":
    main()
