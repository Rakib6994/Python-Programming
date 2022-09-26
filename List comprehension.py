languages=["Bengali","English","Hindi","French","Spanish"]
x=[len(language) for language in languages]
print(x)
mul=[x for x in range(0,500) if x%3 == 0]
print(mul)
print(list(reversed(languages)))