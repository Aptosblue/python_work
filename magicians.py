magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!') #anything written inside the loop will apply to each item or in this case, magician, in this list
    print(f'I cannot wait to see your next trick, {magician.title()}.') #do not forget to indent lines after the loop starts, it can cause indentation error or logical errors

#indentation errors are caused by forgetting to indent code after a loop starts, a for statement expects indentation.
#it is possible to indent something that does not need to be indented as well, this will cause the same error
#logical errors have valid syntax, ie. the code works but does not produce the correct outcome.

print('Thank you everyone, that was a great magic show.') #This print function does not print with the loop for each "magician" because it is outside of the loop

#DO NOT forget the colon (I always forget the stupid colon)
#Forgetting the colon will result in a syntaxerror