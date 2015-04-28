def twodigit(number):
    '''Converts a number under 10 into a string representing it two digits long'''
    string = str(number)
    if len(string) == 1:
        string = "0"+string
    return string

def splitURL(url):
    '''Splits a companies house download URL into it's component parts'''
    urlstem = url[0:38]
    print(urlstem)
    filestem = url[38:54]
    print(filestem)
    year = int(url[55:59])
    print(year)
    month = int(url[60:62])
    print(month)
    day = int(url[63:65])
    print(day)
    part = int(url[70])
    print(part)
    total = int(url[72])
    print(total)
    return urlstem, filestem, year, month, day, part, total

def nameCrawl(urlstem, filestem, year, month, day, part, total, finalyear):
    '''Will go through all file names until the final year is reached'''
    while year >= finalyear:
        part += 1
        if part > total:
            part = 1
            month -= 1
        if month <= 0:
            month = 12
            year -= 1
        combined = urlstem+filestem
        combined += "-"+str(year)+"-"+twodigit(month)+"-"+str(day)+"-part"+str(part)+"_"+str(total)+".zip"
        print(combined)

    
    #http://download.companieshouse.gov.uk/BasicCompanyData-2013-04-01-part1_3.zip

tup = splitURL("http://download.companieshouse.gov.uk/BasicCompanyData-2013-04-01-part1_3.zip")

nameCrawl(tup[0], tup[1],tup[2],tup[3],tup[4],tup[5],tup[6],2000)


        
        
    
