questions = [
    [
        "The International Literacy Day is observed on", 
        ['Sep 8','Nov 28', 'May 2', 'Sep 22'],
        1,
        5000
    ],
    [
        "The International Literacy Day is observed on", 
        ['Sep 8','Nov 28', 'May 2', 'Sep 22'],
        1,
        5000
    ],
    [
        "The International Literacy Day is observed on", 
        ['Sep 8','Nov 28', 'May 2', 'Sep 22'],
        1,
        5000
    ],   
]

for i in range(0, len(questions)) :
    # Printing a question
    que = questions[i] # 1st block of question
    print("Question : ", que[0]) # question priented

    # Printing options
    print("The Options are : ")
    optn = que[1]
    for j in range(0, len(optn)):
        print(j + 1, ' ', optn[j])
    answer = int(input("Type the Option number : "))

    # Checking the ans is correct or not
    if(answer == que[2]):
        print("Correct Answer, you won ", que[3], " amount")
    else:
        print("Wrong answer")
        break

    print('\n \n')