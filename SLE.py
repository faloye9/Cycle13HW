# establish operative variables
minword = 0
minword2 = 0
sentmax = 0
sentmax2 = 0
puncts = []
puncts2 = []

# set additional params
def moreparams():
    moreparamsset = False
    while (moreparamsset == False):
        set2 = int(input(
            "Please input the number for another parameter you want to change or choose number 4 to finish: (1) Minimum characters in word, (2) Maximum words in sentence, "
            "(3) Punctuation marking end of sentence. (4) You are finished setting parameters."))
        if set2 == 1:
            setminword2()
            moreparamsset = True
        elif set2 == 2:
            setsentmax2()
            moreparamsset = True
        elif set2 == 3:
            setpunct2()
            moreparamsset = True
        elif set2 == 4:
            print("OK, so your parameters are set.")
            moreparamsset = True


# set smallest word to be counted in sentence
def setminword():
    minwordset = False  # setminword finished when True
    while (minwordset == False):
        try:
            global minword
            minword = int(input(
                "What's the least amount of characters a counted word can have? 1-4."))
            if minword  < 4:
                print("OK, we'll only count words with",
                      minword, "characters or more")
                minwordset = True
                moreparams()
            else:
                print("I recommend that you only not "
                  "count words 4 characters or less. "
                      "Please re-enter an integer, 1-4.")
        except ValueError:
            print("Please enter an integer from 1-4.")

# set smallest word to be counted in sentence as
# additional parameter
def setminword2():
    minwordset2 = False  # setminword finished when True
    while (minwordset2 == False):
        try:
            global minword2
            minword2 = int(input(
                "What's the least amount of characters a counted word can have? 1-4."))
            if minword2 < 4:
                print("OK, we'll only count words with",
                      minword2, "characters or more")
                minwordset2 = True
                moreparams()
            else:
                print(
                    "I recommend that you only not "
                    "count words 4 characters or less. Please re-enter an integer, 1-4.")
        except ValueError:
            print(
                "Please enter an integer from 1-4.")

# set number of words in good sentence
def setsentmax():
    sentmaxset = False
    while (sentmaxset == False):
        try:
            global sentmax
            sentmax = int(input("What's the most "
                                    "words a good sentence should have? I recommend not going over 12 words."))
            print("OK, good sentences will have",
                  sentmax, "words or less.")
            sentmaxset = True
            moreparams()
        except ValueError:
            print("Please enter an integer.")

# set number of words in good sentence as additional parameter
def setsentmax2():
    sentmaxset2 = False
    while (sentmaxset2 == False):
        try:
            global sentmax2
            sentmax2 = int(input(
                "What's the most words a good sentence should have? I recommend not going over 12 words."))
            print("OK, good sentences will have",
                  sentmax2, "words or less.")
            sentmaxset2 = True
            moreparams()
        except ValueError:
            print("Please enter an integer.")

# set sentence enders
def setpunct():
    punctset = False
    while (punctset == False):
        punct = input(
            "Please enter any or all of these possible sentence enders, one after the other, no spaces or commas: .,!;?")
        # remove any spaces from string
        punct.replace(" ", "")
        # Turn string into list
        punct.split()
        global puncts
        puncts = punct
        # list of acceptable values
        accval = [".", ",", "!", ";", "?"]
        # limit punct to only values that are in accval
        if ([i for i in accval if i in puncts]):
            puncts = [i for i in accval if i in puncts]
            print("OK, we'll use these as 'sentence' "
                  "enders:", puncts)
            punctset = True
            moreparams()

# set sentence enders as additional parameters
def setpunct2():
    punctset2 = False
    while (punctset2 == False):
        punct2 = input(
            "Please enter any or all of these possible sentence enders, one after the other, no spaces or commas: .,!;?")
        # remove any spaces from string
        punct2.replace(" ", "")
        # Turn string into list
        punct2.split()
        global puncts2
        puncts2 = punct2
        # list of acceptable values
        accval2 = [".", ",", "!", ";", "?"]
        # limit punct2 to only values that are in accval
        if ([i for i in accval2 if i in puncts2]):
            puncts2 = [i for i in accval2 if
                     i in puncts2]
            print("OK, we'll use these as 'sentence' "
                  "enders:", puncts2)
            punctset2 = True
            moreparams()

def idenders(text, sentenders):
    ender = sentenders[0]
    for n in sentenders[1:]:
        text = text.replace(n, ender)
    return [i.strip() for i in text.split(ender)]

# prompt user to set parameters
print("Hi, writer! Welcome to the Sentence Length Evaluator. I am going to analyze the length of sentences in your report, to help you be a more efficient writer. (Anytime you need help, type 'Help')")
setparamfin = False	# first parameter set when true
while (setparamfin == False):
    set = int(input("Please input the number for any parameter you want to change: (1) Minimum characters in word, (2) Maximum words in sentence, (3) Punctuation marking end of sentence, (4) None; I will keep all defaults – 3, 10, . , ! ; ?"))
    # set smallest word to be counted in sentence
    if set == 1:
        setminword()
        setparamfin = True
    # set number of words in good sentence
    elif set == 2:
        setsentmax()
        setparamfin = True
    elif set == 3:
        setpunct()
        setparamfin = True
    elif set == 4:
        print("OK, so we’ll keep the defaults: We'll "
              "only count words with 3 characters or more, "
              "treat sentences with 10 words or more as "
              "bad, and use .,!;? as sentence enders.")
        setparamfin = True

# get report, params and break into list of sentences
x = input("Please provide the name of the .txt report (in the SLE folder) you want SLE to analyze.", )
rpt = open(x, "r")
rpt = rpt.read()
p1 = minword or minword2
p2 = sentmax or sentmax2
p3 = puncts or puncts2
sentences = idenders(rpt, p3)

# check length of words per sentence, then number of
# remaining words per sentence
sentences2 = []
for item in sentences:
    # turn each string into list, on spaces
    liofstr = item.split(" ")
    y = [s for s in liofstr if len(s) > p1]
    sentences2.append(y)

# get and print average
avg = []
for item in sentences2:
    num = len(item)
    avg.append(num)

avsentlen = (float(sum(avg))) / (max(len(avg), 1))
print ("The average sentence length in", x, "is",
       avsentlen, ".")

# get and print bad sentences
print("Here are the bad sentences:")
bad = [s for s in sentences2 if len(s) >p2]
for item in bad:
    print (" ".join(item))




