def calling_file (data_):
    #For calling the data and creating the lists
    rank=[]
    points=[]
    competitors=[]
    scores=[]
    exercise1=[]
    exercise2=[]
    exercise3=[]
    exercise4=[]
    final_list=[]

    for page in data_:
        for key, value in page.items():
            if key=='leaderboardRows':
                final_list.append(value)
            
    for data in final_list:
        for info in data:
            for key, value in info.items():
                if key=='overallRank':
                    rank.append(value)
                elif key=='overallScore':
                    points.append(value)
                elif key== 'entrant':
                    competitors.append(value)
                elif type(value)==list:
                    scores.append(value)

    for item in scores:
        if len(item)==4:
            exercise1.append(item[0])
            exercise2.append(item[1])
            exercise3.append(item[2])
            exercise4.append(item[3])
        elif len(item)<4:
            exercise1.append(item[0])
            exercise2.append(item[1])
            exercise3.append(item[2])

        
    return   rank, points, competitors, exercise1, exercise2, exercise3, exercise4
