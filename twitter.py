import sentiment_mod as s

a=str(input("Enter the Tweet for Analysis : "))
print(s.sentiment(a)[0])

# Examples
# print(s.sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
# print(s.sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))