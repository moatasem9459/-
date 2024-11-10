print("      what it your gool\n\n")
goal_yes_or_no = input ("did you know your gool yes/no : ").lower()
if goal_yes_or_no != "yes" and goal_yes_or_no != "no" :
    print ("Choose yes or no only")
    input ("did you know your gool yes/no : ").lower()
if goal_yes_or_no == "yes" :
    print ("\n\nCongratulations, you know your goal\n\n")
else :
    print ("I don't know my projects at all haha")