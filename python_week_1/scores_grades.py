def scores():
    for score in range (0,10):
        score = input()
        if (score > 100):
            print ("This is not a valid score")
        if (score<101 and score >89):
            print ("Your score is {} it is an A").format(score)
        if (score<90 and score >79):
            print ("Your score is {} it is an b").format(score)
        if (score<80 and score >69):
            print ("Your score is {} it is an c").format(score)
        if (score<70 and score >59):
            print ("Your score is {} it is an D").format(score)
        if (score<60):
            print ("Your score is {} it is an F").format(score)
    print ("This is the end of the program")
scores()
