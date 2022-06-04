from dis import dis
import os
import random
import re
import sys
from pomegranate import *

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(ranks)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    probability_distribution = dict()
    random_page_probability = round((1 - damping_factor) / len(corpus), 4)

    if len(corpus[page]) == 0:
        random_page_probability = 1 / len(corpus)
        for entry in corpus:
            probability_distribution[entry] = random_page_probability
    else:
        link_page_probability = round(damping_factor / len(corpus[page]), 4)
        for entry in corpus:
            if entry in corpus[page]:
                probability_distribution[entry] = round(link_page_probability + random_page_probability, 4)
            else:
                probability_distribution[entry] = random_page_probability
    return probability_distribution

# TODO fix for corpus1 and corpus2
def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    sample_pagerank_count = dict()
    for page in corpus:
        sample_pagerank_count[page] = 0

    starting_page_random_index = random.randint(0, len(corpus) - 1)
    starting_page = list(corpus)[starting_page_random_index]
    probability_distribution = transition_model(corpus, starting_page, damping_factor)

    for i in range(n):
       discreteDistribution = DiscreteDistribution(probability_distribution)
       next_page = discreteDistribution.sample(1)[0]
       sample_pagerank_count[next_page] += 1
       probability_distribution = transition_model(corpus, next_page, damping_factor)
       
    sample_pagerank = {key: value / n for key, value in sample_pagerank_count.items()}
    return sample_pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    iterate_pagerank = dict()
    page_count = len(corpus)
    for page in corpus:
        iterate_pagerank[page] = 1 / page_count
    
    # PR(p) = 1 - d / N + d Ei PR(i) / NumLinks(i)

    for corpus_page in corpus:
        # get pages that link to a page
        linked_pages =  [page for page, pages in corpus.items() if corpus_page in pages]
        # linked_pages =  [page for page, pages in corpus.items() if list(corpus.keys())[3] in pages]

        print(linked_pages)

        sigma_sum = 0
        for page in linked_pages:
            sigma_sum += (iterate_pagerank[page] / len(linked_pages))

        prob_page = ((1 - damping_factor) / page_count) + (damping_factor * sigma_sum)
        iterate_pagerank[corpus_page] = prob_page
    

    return iterate_pagerank


if __name__ == "__main__":
    main()
