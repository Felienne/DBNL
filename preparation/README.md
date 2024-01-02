# Handleiding


## Benodigdheden
Om deze scripts te gebruiken heb je het Python 3 nodig met de volgende modules:

* Beautifulsoup
* ebooklib
* lxml
* SpaCy (met het model `nl_core_news_sm`.

## Instructies
Gebruik de scripts op de volgende manier, in deze volgorde:
1. `python index_dbnl.py` - Verzamel metadata van DBNL.
2. `python download_dbnl.py` - Download een selectie.
3. `python preprocess_text.py` - Selecteer relevante zinnen.
4. `jupyter notebook`, open `vragen.ipynb` en draai alle cellen.