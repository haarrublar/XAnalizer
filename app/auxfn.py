import emoji
import re
import nltk
nltk.download('stopwords')


def emojiMask(sentence):
    emoji_mask_sentence = emoji.replace_emoji(sentence,
                        replace=lambda chars,
                        data_dict: chars.encode('ascii', 'namereplace').decode())
    emoji_mask_sentence = re.sub(r"\\N\{(.+?)\}", r"\1", emoji_mask_sentence)
    return emoji_mask_sentence


def cleanSentence(sentence, stopwords=True):
    stopwords_vocabulary = nltk.corpus.stopwords.words('english')
    stopwords_pattern = r'\b(?:' + '\s*|'.join(map(re.escape, stopwords_vocabulary)) + r')\b' if stopwords else ''
    lower_sentence = sentence.lower()
    clean_sentence = re.sub(stopwords_pattern + r'|[^\w\s]', '', lower_sentence)
    return clean_sentence