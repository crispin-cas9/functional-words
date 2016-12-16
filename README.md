# Functional Words Analysis
Using the distance between "functional words" (conjunctions, pronouns, prepositions, articles, etc) in a text to analyze authors' styles — namely, Shakespeare and Marlowe.

Requirements to run heatmap code: seaborn, matplotlib, pandas (should all be available through pip install)

# Credits

A replication of a method used by these people: http://www.seas.upenn.edu/~aribeiro/preprints/2015_segarra_etal_a.pdf

More information: http://newatlas.com/algorithm-shakespeare-coauthor-marlowe/46130/

Functional words list: https://fling.seas.upenn.edu/~maeisen/wiki/functionwords.txt

Seaborn code is from here: http://seaborn.pydata.org/examples/network_correlations.html

Shakespeare play texts: http://shakespeare.mit.edu/

# Process

Using the description from the researchers who originally tried to solve this problem, I essentially created my own algorithm. First, it makes a dictionary of the indices of “functional words” within a text. Then, a dictionary within a dictionary: every functional word is associated with every other functional word, with the value being the average distances between these two words when they both  appear in the same sentence. Using this data structure, I was able to create a heatmap (using seaborn) of which words are what distance away from each other. Currently, I have code that can compare two plays, and make a heatmap of the differences between the plays. However, none of the heatmaps are particularly different from one another. My next step would be to find a way to visualize the data that better emphasizes the differences between the plays—and thereby the differences between their authors.
