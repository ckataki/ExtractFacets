facets = ["price", "sound", "quality"]
from nltk.corpus import wordnet as wn
import re
import json

def wordSimilarity(facet_synsets, word_synsets):
    for facet_synset in facet_synsets:
        for word_synset in word_synsets:
            similarity = wn.wup_similarity(word_synset, facet_synset)
            if similarity == None:
                continue
            elif similarity > 0.8:
                return similarity
    return 0.0


def extractFacets(reviewText):
    lines = re.split(',|\.', reviewText)
    lines = list(filter(None, lines))

    output_dict = dict()

    for facet in facets:
        output_dict[facet] = ""
        facet_synsets = wn.synsets(facet)
        for line in lines:
            words = re.split('\W+', line)
            words = list(filter(None, words))
            similarity = 0.0
            for word in words:
                word_synsets = wn.synsets(word)
                similarity = wordSimilarity(facet_synsets, word_synsets)
                if  similarity != 0.0:
                    break
            if similarity != 0.0:
                output_dict[facet] = line

    output = json.dumps(output_dict)
    return output
