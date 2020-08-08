import gensim

# creating a list of list of sentences
i=0
list_of_sent=[]
for sent in final_data['Text'].values:
    filtered_Sentence = []
    sent = cleaned_html(sent)
    for w in sent.split():
        for cleaned_words in clean_punc(w).split():
            if cleaned_words.isalpha():
                filtered_Sentence.append(cleaned_words.lower())
            else:
                continue
    list_of_sent.append(filtered_Sentence)

# min_count = threshold for count needed for converting to a vector
# size = dimensionality of vector
# workers = number of cores to be used
w2v_model=gensim.models.Word2Vec(list_of_sent,min_count=5,size=50,workers=4)
