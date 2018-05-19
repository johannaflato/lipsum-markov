import markovify

# markovify  # Get raw text as string.
with open("ALL.txt") as f:
    corpus = f.read()

# Build the model.
lipsum_model = markovify.Text(corpus)

n_sent = 9

chain = []

for i in range(n_sent):
    chain.append(lipsum_model.make_sentence())

print ' '.join(chain)
