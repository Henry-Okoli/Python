import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Similarity between "cat" and "monkey": The result obtained by comparing "cat" and "monkey" 
# indicates a relatively low similarity score. This makes sense because although both are animals, 
# they belong to different species and have distinct characteristics.

# Similarity between "banana" and "monkey": The result obtained by comparing "banana" and "monkey" 
# indicates a relatively higher similarity score. This can be attributed to the common association of 
# monkeys with bananas, as monkeys are often depicted as eating or interacting with bananas.

# Similarity between "banana" and "cat": The result obtained by comparing "banana" and "cat" 
# indicates a very low similarity score. This aligns with the fact that these words have different 
# meanings and are not semantically related


# Load the 'en_core_web_sm' model
nlp_sm = spacy.load('en_core_web_sm')
word1_sm = nlp_sm("cat")
word2_sm = nlp_sm("monkey")
word3_sm = nlp_sm("banana")

# Load the 'en_core_web_md' model
nlp_md = spacy.load('en_core_web_md')
word1_md = nlp_md("cat")
word2_md = nlp_md("monkey")
word3_md = nlp_md("banana")

# Calculate similarity scores using 'en_core_web_sm' model
similarity_sm = word1_sm.similarity(word2_sm)
print("Similarity between 'cat' and 'monkey' (en_core_web_sm):", similarity_sm)

similarity_sm = word3_sm.similarity(word2_sm)
print("Similarity between 'banana' and 'monkey' (en_core_web_sm):", similarity_sm)

similarity_sm = word3_sm.similarity(word1_sm)
print("Similarity between 'banana' and 'cat' (en_core_web_sm):", similarity_sm)

print()

# Calculate similarity scores using 'en_core_web_md' model
similarity_md = word1_md.similarity(word2_md)
print("Similarity between 'cat' and 'monkey' (en_core_web_md):", similarity_md)

similarity_md = word3_md.similarity(word2_md)
print("Similarity between 'banana' and 'monkey' (en_core_web_md):", similarity_md)

similarity_md = word3_md.similarity(word1_md)
print("Similarity between 'banana' and 'cat' (en_core_web_md):", similarity_md)
