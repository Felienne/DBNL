import json
from collections import defaultdict

import spacy
nlp = spacy.load("nl_core_news_sm")




def laad_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


def indexeer_vragen():
    data = laad_json("selected_sentences.json")
    resultaten = []
    woord_ervoor_man = []
    woord_ervoor_vrouw = []
    woord_ervoor_man_ADJ = []
    woord_ervoor_vrouw_ADJ = []

    j = 0
    for book, sents in data.items():
        j = j + 1
        print(f'item {j} uit {len(data.items())}')
        for sentence in sents:
            doc = nlp(sentence)
            for i in range(len(doc)):
                word = doc[i]
                if i > 0:
                    woord_ervoor = doc[i-1]
                if word.lower_ == 'vrouw':
                    woord_ervoor_vrouw.append(woord_ervoor)
                    if woord_ervoor.pos_ == 'ADJ':
                        woord_ervoor_vrouw_ADJ.append(woord_ervoor)
                if word.lower_ == 'man':
                    woord_ervoor_man.append(word)
                    if woord_ervoor.pos_ == 'ADJ':
                        woord_ervoor_man_ADJ.append(word)


    resultaten = [woord_ervoor_man, woord_ervoor_vrouw, woord_ervoor_man_ADJ, woord_ervoor_vrouw_ADJ]
    return resultaten

resultaten = indexeer_vragen()
print(resultaten)


# korte_vragen = index.copy()
# for key in index:
#     if len(key.split()) > 20:
#         del korte_vragen[key]
#
# with open("./resources/mannen.json", 'w') as f:
#     json.dump(korte_vragen, f, indent=4)
#
# with open("./resources/vrouwen.json", 'w') as f:
#     json.dump(korte_vragen, f, separators=(',', ':'))
#
# # Selecteer gebruikte ids.
# used_ids = set.union(*[set(l) for l in index.values()])
#
# # Laad DBNL-metadata.
# dbnl = laad_json("./resources/dbnl.json")
#
# # Maak dictionary
# dbnl_index = {entry['id']: entry for entry in dbnl if entry['id'] in used_ids}
#
# print(len(dbnl_index), "gebruikte boeken")
# print(len(dbnl) - len(dbnl_index), "items bespaard")
#
# data = dict(vragen=korte_vragen,
#             metadata=dbnl_index)
#
# with open("./resources/site_data.json", 'w') as f:
#     json.dump(data, f, separators=(',', ':'))