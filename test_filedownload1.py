import urllib.request


try:
    url = "http://download.companieshouse.gov.uk/BasicCompanyData-2015-01-01-part1_6.zip"
    folder = "C:\\Users\\Jamie\\Downloads\\Companies House Data\\Automated"
    filename ="\\BasicCompanyData-2015-01-01-part1_6.zip"
    returned = urllib.request.urlretrieve(url,folder+filename)
    print(returned)
except urllib.error.HTTPError:
    print("File not found")



#Returns the location if correct e.g:
#'C:\\Users\\Jamie\\Downloads\\Companies House Data\\Automated\\BasicCompanyData-2015-01-01-part1_5.zip', <http.client.HTTPMessage object at 0x0000000003BC3588>)
