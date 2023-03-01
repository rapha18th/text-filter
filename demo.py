import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('averaged_perceptron_tagger')


text = 'Can I share your email address'
text2 = 'The email has been shared with all my friends'


# Classify the text as either past tense or questions
def classify_text(text):
      text = text.lower()
      #tokenize text
      words = word_tokenize(text)
      # Tag the words to identify parts of speech
      tagged_words = nltk.pos_tag(words)
      stemmer = PorterStemmer()
      stems = [stemmer.stem(word) for word in words]
      # Find words which are tagged as past tense (VBD), future tense (VB) or questions
      if 'share' in stems and 'email' in words:
            past_tense_words = [w for w, tag in tagged_words if tag == 'VBD' or tag == 'VBN']
            future_tense_words = [w for w, tag in tagged_words if tag == 'VB']
            # Find question via the (MD) tag
            questions = [w for w, tag in tagged_words if tag == 'MD']
            if len(past_tense_words) > len(future_tense_words):
                  label = "Student has shared"
            elif len(questions) > 0:
                  label = "Student wants to know if can share"
            else:
                  label = "Unlabeled"
            return label

      else:
          label = "The sentence does not contain both the stem share and the word email"
          return label

# Print the label
print(classify_text(text))
print(classify_text(text2))

