    # Grab the title 
    # guntitle = dataset['children'][0]['data']['title']
    cleantitle = []
    for i in c:
        cleantitle.append(unidecode(gtitles.lower()))

    return(cleantitle)


        '''
    for data in dataset:
        for key in data:
            if 'data' in key:
                gtitles.append(dataset.get("data"))

    return gtitles
    '''

        i = []
    for num in gtitles:
        if num['data']:
            while count < 1:
                i.append(num[count])
                count += 1
    return i


        #count the gun news title 
    target = 'gun'
    count = 0
    gtitle = []
    x = 0
    while x < 24:
        if target in title:
            gtitle.append(title[x])
            count += 1
            x += 1

    return gtitle    
    
        if lowtitle.find('gun','shot'):
            count+= 1
            lowtile.append(f"The news related to gun is {count}")



    for s in lowtitle:    
        if 'gun' in s:
            count+=1
        
    lowtitle.append(count)