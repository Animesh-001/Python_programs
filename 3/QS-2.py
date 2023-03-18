'''Problem Statement: The goal is to tokenize the following
5 sentences into words, excluding the stop words. Input:
sentences = ["a new world record was set", "in the holy city of ayodhya",
"on the eve of diwali on tuesday", "with over three lakh diya or earthen lamps",
"lit up simultaneously on the banks of the sarayu river"]
stopwords=['for', 'a', 'of', 'the', 'and', 'to', 'in','on','with']'''


sentences = ["a new world record was set", "in the holy city of ayodhya",
"on the eve of diwali on tuesday", "with over three lakh diya or earthen lamps",
"lit up simultaneously on the banks of the sarayu river"]
stopwords=['for', 'a', 'of', 'the', 'and', 'to', 'in','on','with']
results = []
for i in sentences:
    sentence_tokens = []
    for j in i.split():
        if j not in stopwords:
            sentence_tokens.append(j)
    results.append(sentence_tokens)
print(results)

#list compehension
print([[word for word in sentence.split()
        if word not in stopwords]for sentence in sentences])
