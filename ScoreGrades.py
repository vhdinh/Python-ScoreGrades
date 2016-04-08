print "score and grades"
for i in range(1,11):
    score = input("enter your score:")
    if score <= 59:
    	print "score: %s; You failed :( " % score
    elif score > 59 and score < 70:
        print "score: %s; Your grade is D" % score
    elif score > 69 and score < 80:
        print "score: %s; Your grade is C" % score
    elif score > 79 and score <90:
        print "score: %s; Your grade is B" % score
    elif score > 89 and score <= 100:
        print "score: %s; Your grade is A" % score

print "End of the program. Bye!"