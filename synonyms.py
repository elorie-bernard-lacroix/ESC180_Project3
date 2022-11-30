'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2022.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Return the consine similarity between the sparse vectors 
    vec1 and vec2, stored as dictionaries.'''
    dot_prod = 0
    vec1_sum = 0
    vec2_sum = 0
    for w in vec1:
        vec1_sum += vec1[w]**2
        if w in vec1 and w in vec2:
            dot_prod += vec1[w]*vec2[w]
    for w in vec2:
        vec2_sum += vec2[w]**2
    return dot_prod/(vec1_sum**0.5 * vec2_sum**0.5)


def build_semantic_descriptors(sentences):
    word_dictionary = {}

    for sentence in sentences:
        cur_sentence_words = []
        for w in sentence:
            for x in cur_sentence_words:
                if x == w:
                    continue
                if w not in word_dictionary:
                    word_dictionary[w] = {x: 1}
                elif x not in word_dictionary[w]:
                    word_dictionary[w][x] = 1
                else:
                    word_dictionary[w][x] += 1
            cur_sentence_words.append(w)
            for x in cur_sentence_words:
                if x == w:
                    continue
                if x not in word_dictionary:
                    word_dictionary[x] = {w: 1}
                    word_dictionary[x][w] = 1
                elif w not in word_dictionary[x]:
                    word_dictionary[x][w] = 1
                else:
                    word_dictionary[x][w] += 1
    return word_dictionary

def build_semantic_descriptors_from_files(filenames):
    pass



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

if __name__ == "__main__":
#    print(build_semantic_descriptors([["i", "am", "a", "sick", "man"], ["i", "am", "a", "sick", "man"]]))
    print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))