import random

verbs = ['Leverage','Sync','Target','Gimify']
adjectives = ['A/B Tested','Freemium','Hyperlocal','Siloed']
nouns = ['Early Adopter','Low-hanging','pipeline']

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)
