# Semantic Similarity

This program draws from the data in the attached text files to statistically predict the synonym of a given word with a 70% accuracy. It accomplishes this in linear time.

This was written as part of a course project for ESC180 (Engineering Science, University of Toronto). 

## the main python program
The python program is available in this [file](https://github.com/elorie-bernard-lacroix/ESC180_Project3/blob/main/synonyms.py).

To calculate semantic similarity it first assigns a semantic descriptor vector, which will store the number of times a word was seen in the same sentence as other words. For example, given the following sentences
```
I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.
However, I know nothing at all about my disease, and do not know for certain what ails me.
```
the respective semantic descriptor vector for "man" would be
```
{"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}
```
and the respective semantic descriptor vector for "liver" would be
```
{"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}
```

To compare two semantic descriptor vectors, we used cosine similarity which is calculated as 

$sim(uv) = \frac{u \cdot v}{|u| \cdot |v|}$

For example, the cosine similarity between the vectors given above would be

$\frac{3 \cdot 1}{\sqrt{(3^2 + 3^2 + 2^2 + 1^2 + 1^2 + 1^2 + 1^2)(1^2 + 1^2 + 1^2 + 1^2 + 1^2)}} = 0.2631...$ 

## the text files
* [War and Peace, by Leo Tolstoy](https://github.com/elorie-bernard-lacroix/ESC180_Project3/blob/main/wp.txt)
* [Swann's Way, by Marcel Proust](https://github.com/elorie-bernard-lacroix/ESC180_Project3/blob/main/sw.txt)
