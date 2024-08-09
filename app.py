import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from heapq import nlargest

nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

def calculate_word_frequencies(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    frequencies = {}
    for word in words:
        if word not in stop_words:
            frequencies[word] = frequencies.get(word, 0) + 1
    max_frequency = max(frequencies.values())
    for word in frequencies.keys():
        frequencies[word] /= max_frequency
    return frequencies

def score_sentences(sentences, word_frequencies):
    sentence_scores = {}
    for sentence in sentences:
        word_count = len(word_tokenize(sentence))
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]
        sentence_scores[sentence] /= word_count
    return sentence_scores

def summarize_text(text, n=3):
    cleaned_text = clean_text(text)
    sentences = sent_tokenize(text)
    word_frequencies = calculate_word_frequencies(cleaned_text)
    sentence_scores = score_sentences(sentences, word_frequencies)
    summarized_sentences = nlargest(n, sentence_scores, key=sentence_scores.get)
    return ' '.join(summarized_sentences)

if __name__ == "__main__":
    f = open(sample.txt, 'r')
    sample_text = f.read()
    summary = summarize_text(sample_text, n=2)
    print("Original Text:\n", sample_text)
    print("\nSummarized Text:\n", summary)
    f.close()
