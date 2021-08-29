# ARAB-ACQUIS

> Copyright © 2017-2018 New York University Abu Dhabi
>
> Computational Approaches to Modeling Language (CAMeL) Lab

## About

We present ARAB-ACQUIS, a large publicly available dataset for evaluating
machine translation between 22 European languages and Arabic. ARAB-ACQUIS
consists of over 12,000 sentence from the
[JRC-ACQUIS](https://ec.europa.eu/jrc/en/language-technologies/jrc-acquis)
(Acquis Communautaire) corpus* [1,2] translated twice by professional
translators, once from English and once from French, and totaling over 600,000
words.

The corpus follows previous data splits in the literature for tuning,
development, and test [3].

_* Originally published in the official languages of the European Union in the
Official Journal of the European Union by the Office for Official Publications
of the European Communities. Responsibility for the translation into Arabic from
the original English and French editions lies entirely with New York University
Abu Dhabi._

## Directory Structure

* **JRC-ACQUIS/** This directory contains the original JRC-ACQUIS data in the 22
  European languages of which we translated the French and English documents.

* **Arabic-Translations/** This directory contains our translations from French and
  English into Arabic. Note that *dev* and *tune* files in this directory map to
  *devtest* and *dev* respectively in the **JRC-ACQUIS** directory.

## Statistics

Below are some statistics for the JRC-ACQUIS English (JRC En) and French
(JRC Fr) data we translated to Arabic (ARAB En and Arab Fr respectively).

|           |         | **JRC En** | **JRC Fr** | **ARAB En** | **ARAB Fr** |
|:---------:|:-------:|:----------:|:----------:|:-----------:|:-----------:|
|           | *Lines* | *Words*    | *Words*    | *Words*     | *Words*     |
| **Tune**  | 4,107   | 108,405    |  112,984   | 107,271     | 113,942     |
| **Dev**   | 4,108   | 109,611    |  114,327   | 114,903     | 114,769     |
| **Test**  | 4,107   | 109,450    |  113,428   | 118,491     | 117,942     |
| **Total** | 12,322  |  327,466   |  340,739   | 340,665     | 346,679     |

## Citation

Please use the following citation when referencing this corpus:

> Habash, N., Zalmout, N., Taji, D., Hoang, H., & Alzate, M. (2017).
> A parallel corpus for evaluating machine translation between Arabic and
> European languages.
> In Proceedings of the 15th Conference of the European Chapter of the
> Association for Computational Linguistics, Valencia, Spain.

## Licenses

### ARAB-ACQUIS License

The ARAB-ACQUIS corpus is licensed under the the license attached in
 the download directory (LICENSE.txt).  Furthermore, we release the
 ARAB-ACQUIS corpus alongside the portions of the JRC-ACQUIS corpus
 following the JRC-ACQUIS usage condition below:

> The European Communities consider legislative and quasi-legislative documents
> published in the Official Journal of the European Union and related COM and
> SEC series as well as charters and treaties and ECJ case-law to be in the
> public domain. Prior written permission is thus not required for their
> reproduction/translation, and they may be reproduced/translated freely without
> restriction, including for the purpose of further non-commercial dissemination
> to final users, subject to the condition that appropriate acknowledgement is
> given to the European Communities and to the source, and provided that the
> additional guidelines set out below are respected.

### JRC-ACQUIS License

> The JRC-Acquis data is the exclusive property of the European Commission. The
> Commission cedes its non-exclusive rights free of charge and world-wide for
> the entire duration of the protection of those rights to the re-user, for all
> kinds of use which comply with the conditions laid down in the Commission
> Decision of 12 December 2011 on the re-use of Commission documents, published
> in Official Journal of the European Union L330 of 14 December 2011, pages 39
> to 42.

See [here](https://ec.europa.eu/jrc/en/language-technologies/jrc-acquis#Usage%20conditiosns%20/%20Licensing%20issues)
for more details.

## References

[1] [Steinberger Ralf, Mohamed Ebrahim, Alexandros Poulis,
Manuel Carrasco-Benitez, Patrick Schlüter, Marek Przybyszewski & Signe Gilbro
(2014). An overview of the European Union's highly multilingual parallel
corpora. Language Resources and Evaluation Journal (LRE).
DOI: 10.1007/s10579-014-9277-0.
](https://ec.europa.eu/jrc/sites/jrcsh/files/2014_08_LRE-Journal_JRC-Linguistic-Resources_Manuscript.pdf)

[2] [Steinberger Ralf,  Bruno Pouliquen, Anna Widiger, Camelia Ignat,
Tomaž Erjavec, Dan Tufis, Dániel Varga (2006). The JRC-Acquis: A multilingual
aligned parallel corpus with 20+ languages. Proceedings of the 5th International
Conference on Language Resources and Evaluation (LREC'2006).
Genoa, Italy, 24-26 May 2006.](https://web.archive.org/web/20160308090424/https://ec.europa.eu/jrc/en/publication/jrc-acquis-multilingual-aligned-parallel-corpus-20-languages-10725)

[3] [Philipp Koehn, Alexandra Birch, and Ralf Steinberger (2009). 462 Machine
Translation Systems for Europe. In Proceedings of the 12th Machine Translation
Summit (MT XII), pages 65–72, Ottawa, Canada.
](https://pdfs.semanticscholar.org/fb46/10eb197d0c1a0cca5e8f4926734083f3a89f.pdf)
