## Text Filter

### To Run Locally
`pip install nltk`
`python demo.py`

The premise of my solution is that the texts that Marry receives can be classified as past tense statements or questions.

`demo.py` includes the function called `classify_text `that takes a text as an argument and returns a label based on some criteria. The function does the following steps:

- Converts the text to lowercase
- Splits the text into words using `word_tokenize`
- Tags each word with its part of speech using `nltk.pos_tag`
- Stems each word using PorterStemmer
- Checks if the text contains both the stem ‘share’ and the word ‘email’
- If yes, counts how many words are tagged as past tense (VBD or VBN), future tense (VB) or questions (MD)
- If past tense words are more than future tense words, returns “Student has shared”
- If questions are present, returns “Student wants to know if can share”
Otherwise, returns “Unlabeled”
- If no, returns “The sentence does not contain both the stem share and the word email”

### Parts of Speech (POS) tags for used in the function
- *VBD*: verb, past tense
dipped pleaded swiped regummed soaked tidied convened halted registered
cushioned exacted snubbed strode aimed adopted belied figgered
speculated wore appreciated contemplated etc
- *VBN*: verb, past participle
multihulled dilapidated aerosolized chaired languished panelized used
experimented flourished imitated reunifed factored condensed sheared
unsettled primed dubbed desired etc
- *VB*: verb, base form
ask assemble assess assign assume atone attention avoid bake balkanize
bank begin behold believe bend benefit bevel beware bless boil bomb
boost brace break bring broil brush build etc
- *MD*: modal auxiliary
can cannot could couldn't dare may might must need ought shall should
shouldn't will would etc

#### Reference
https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
