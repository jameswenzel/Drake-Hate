import pickle
from nltk.tokenize import word_tokenize


class Classifier:
    def __init__(self, type='Naive Bayes'):
        assert type == 'Naive Bayes' or type == 'Max Ent'

        if type == 'Naive Bayes':
            self.type = type
            dir = 'naive_bayes'
        elif type == 'Max Ent':
            self.type = type
            dir = 'max_ent'

        with open(dir + '/analyzer.pk1', 'rb') as f:
            self.analyzer = pickle.load(f)

        with open(dir + '/classifier.pk1', 'rb') as f:
            self.classifier = pickle.load(f)

    def classify(self, tweet):
        tokens = word_tokenize(tweet)
        features = self.analyzer.apply_features(tokens)
        return self.classifier.classify(features[0])

    def prob_classify(self, tweet):
        tokens = word_tokenize(tweet)
        features = self.analyzer.apply_features(tokens)
        classified = self.classifier.prob_classify(features[0])
        probabilities = {}
        for outcome in ['positive', 'negative']:
            probabilities[outcome] = classified.prob(outcome)
        return probabilities

    def classify_eighty_percent(self, tweet):
        probability = self.prob_classify(tweet)
        if probability['negative'] >= 0.8:
            return 'negative'
        else:
            return 'positive'
