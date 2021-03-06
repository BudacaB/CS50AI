import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
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
    random_page_probability = (1 - damping_factor) / len(corpus)

    if len(corpus[page]) == 0:
        random_page_probability = 1 / len(corpus)
        for entry in corpus:
            probability_distribution[entry] = random_page_probability
    else:
        link_page_probability = damping_factor / len(corpus[page])
        for entry in corpus:
            if entry in corpus[page]:
                probability_distribution[entry] = link_page_probability + random_page_probability
            else:
                probability_distribution[entry] = random_page_probability
    return probability_distribution


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
       prob_dist_keys = list(probability_distribution.keys())
       prob_dist_values = list(probability_distribution.values())
       next_page = random.choices(population=prob_dist_keys, weights=prob_dist_values, k=1)[0]
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
    # PR(p) = 1 - d / N + d Ei PR(i) / NumLinks(i)

    iterate_pagerank = dict()
    page_count = len(corpus)
    for page in corpus:
        iterate_pagerank[page] = 1 / page_count
        
    unlinked_pages = []
    for corpus_page in corpus:
        if len(corpus[corpus_page]) == 0:
            unlinked_pages.append(corpus_page)
    
    i_pages_dict = dict()
    for corpus_page in corpus:
            i_pages = [page for page, pages in corpus.items() if corpus_page in pages]
            all_i_pages = i_pages + unlinked_pages
            i_pages_dict[corpus_page] = all_i_pages

    diff_tracker = 1
    ranks_sum = 0
    while diff_tracker >= 0.001 or not 1 != ranks_sum:
        ranks_sum = 0
        iterate_pagerank_temp = iterate_pagerank.copy()
        diff_tracker = 0
        for corpus_page in corpus:
            sigma_sum = 0
            for page in i_pages_dict[corpus_page]:
                numLinks = page_count if (len(corpus[page]) == 0) else len(corpus[page])
                sigma_sum += (iterate_pagerank[page] / numLinks)

            page_probability = ((1 - damping_factor) / page_count) + (damping_factor * sigma_sum)
            iterate_pagerank[corpus_page] = page_probability
            ranks_sum += page_probability
        for key, value in iterate_pagerank_temp.items():
            diff_tracker += abs(iterate_pagerank[key] - value)
        
    return iterate_pagerank


if __name__ == "__main__":
    main()