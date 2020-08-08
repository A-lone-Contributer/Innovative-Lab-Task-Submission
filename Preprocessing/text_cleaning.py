import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('stopwords')

stop = set(stopwords.words('english'))  #set of stopwords in english
sno = nltk.stem.SnowballStemmer('english')  # creating instance of Snowball Stemmer

# function to clean the word of any html-tags
def cleaned_html(sentence):
    
    # compile search string to avoid cache lookup
    cleanr = re.compile('<.*?>')
    
    # replace those occurences with blank spaces
    cleaned_text = re.sub(cleanr, ' ', sentence)
    return cleaned_text

def clean_punc(sentence):
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    return cleaned
