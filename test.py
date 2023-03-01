import unittest
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = 'I just shared your address'
text2 = 'Can I share your email address'
text3 = 'The email has been shared with all my friends'
text4 = 'Might I share your email'


def classify_text(text):
      text = text.lower()
      words = word_tokenize(text)
      tagged_words = nltk.pos_tag(words)
      stemmer = PorterStemmer()
      stems = [stemmer.stem(word) for word in words]
      # Find words which are tagged as past tense (VBD), future tense (VB) or questions
      if 'share' in stems and 'email' in words:
            past_tense_words = [w for w, tag in tagged_words if tag == 'VBD' or tag == 'VBN']
            future_tense_words = [w for w, tag in tagged_words if tag == 'VB']
            questions = [w for w, tag in tagged_words if tag == 'MD' or tag == 'IN']
            #print(len(questions))
            if len(past_tense_words) > len(future_tense_words):
                  label = "Student has shared"
            elif len(questions) > 0:
                  label = "Student wants to know if can share"
            else:
                  label = "Unlabeled"
            return label

      else:
          label = 'The sentence does not contain the stem share and the word email'
          return label



class TestClassifyText(unittest.TestCase):
    def test_classify_text(self):
        # Test with past tense
        self.assertEqual(classify_text(
            text), "The sentence does not contain the stem share and the word email")
        # Test with future tense
        self.assertEqual(classify_text(text2),
                         "Student wants to know if can share")
        # Test with no tense
        self.assertEqual(classify_text(text3), "Student has shared")
        self.assertEqual(classify_text(text4),
                         "Student wants to know if can share")

if __name__ == "__main__":
    unittest.main()
