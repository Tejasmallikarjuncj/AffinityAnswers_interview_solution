import regex as re
import requests
import json

def parsePincode(address):
    """
    Extracts the pincode from the given address

    Args:
        address(str): It is the messy string address

    Return:
        pincode(str): It is str of digits if we find the pincode else empty string i.e ''
    """

    addr = address.split(',')

    #regex pattern for finding pincode
    pattern = r'[-\s]*?(\d{6})'
    pincode = ''

    #parsing sub fields in address to find pincode
    for subfield in addr:
        subfield = subfield.strip(' ')
        result = re.search(pattern, subfield)
        if(result == None):
            continue
        pincode = result.group(1)

    return pincode

def parseLocality(address):
    """
    Extract the locality from the given ADDRESS

    Args:
        address(str): It is the messy string address

    Return:
        locality: It is the list of locality order form highest to lowest ex. [Karanataka, Bengaluru, Banashankari III stage]
    """

    addr = address.split(',')

    #regex pattern for finding pincode
    pattern = r'([-\s]*?\d{6})'
    locality = []

    #parsing sub fields in address to find pincode
    for subfield in addr:
        subfield = subfield.strip(' ')
        subfield = re.sub(pattern, '',subfield)
        subfield = re.sub(r'\.','',subfield)
        if(len(subfield) == 0):
            continue
        locality.append(subfield)

    return locality


def postalAPI(url):
    """
    Sends https query to postal service api for pincode

    Args:
        url(str): It is the url to be searched

    Return:
       content(list of dictionary): It is details of post office form the json response from the query

    Raise:
        HTTPS request error
    """

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Access the content of the response
            content = response.json()
        else:
            raise Exception(f"HTTP request failed with status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred: {e}")

    if(content[0]["Status"] == "Success"):

        content = content[0]["PostOffice"]
        return content

    return None


def verifyPincode(pincode, locality):
    """
    It verifies the pincode for given address

    Args:
        pincodeResp : The extarcted pincode form address
        locality(list of str): It is list of locality from the address

    Return:
        match: It returns True if pinocde matchs the address else false

    """

    match = False

    if(pincode == ''):
        return match

    #making url geeting the response
    url = f"https://api.postalpincode.in/pincode/{pincode}"
    content = postalAPI(url)
    if(content == None):
        return match

    #parsing throught locailty to match the ,state,district,Name of postoffice
    for postAddr in content:

        if postAddr["District"].upper() in locality and postAddr["Name"].upper() in locality and postAddr["Name"] != postAddr["District"]:
            match = True

    return match

def findPincode(locality):
    """
    It finds the pincode by locality fields

    Args:
        locality(list of str): It is list of locality from the address

    Return:
        pinocde: It resturns if found else empty str i.e ''
    """

    #initializing pincode
    pincode = ''
    pinfoundFlg = False

    #iterating throught the loaclity fields
    for field in locality:

        #making url geeting the response
        url = f"https://api.postalpincode.in/postoffice/{field}"
        content = postalAPI(url)
        if(content == None):
            continue

        #matching field of locality
        for postAddr in content:
            if postAddr["District"].upper() in locality and postAddr["Name"].upper() in locality and postAddr["Name"] != postAddr["District"]:
                pincode = postAddr["Pincode"]
                pinfoundFlg = True
                break
        if pinfoundFlg:
            return pincode

    return pincode


#correcting the pin or address
def corAddr(address):
    """
    This function coorects pincode of the address given

    Args:
        address: It is the input address

    Return:
        correctAdr: It given corrected address
    """

    #initialzing
    correctAdr = ''

    #extarcting pincode and parseLocality
    pincode = parsePincode(address)
    locality = parseLocality(address)
    locality = list(map(str.upper, locality))

    #cleaning locality
    if(locality[-1] == 'INDIA'):
        locality = locality[:-1]

    #verfying pincode
    if(verifyPincode(pincode, locality)):
        correctAdr = ', '.join(locality) + ', '+pincode
        return correctAdr #if pincode matches the address and ending the same adress

    #getting pincode form locality
    newPincode = findPincode(locality)

    #It's wrong address
    if(newPincode == ''):
        return correctAdr

    #return coorected address
    correctAdr =  ', '.join(locality) + ', '+newPincode
    return correctAdr

if __name__ == '__main__':

    #case1:if the address and pincode are correct
    address = "2nd Phase, 374/B, 80 Feet Rd, State Bank Of Mysore Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore, Karnataka 560050"
    correctAdr = corAddr(address)
    print(f'The address is {address}\n The corrected addres is {correctAdr}')

    #case2: if the address is correct and pincode is wrong
    address2 =  "2nd Phase, 374/B, 80 Feet Rd, State Bank Of Mysore Colony, Banashankari 3rd Stage, Srinivasa Nagar,  Bangalore, Karnataka 560045"
    correctAdr = corAddr(address2)
    print(f'The address is {address2}\n The corrected addres is {correctAdr}')

    #case3: if the address and pincode are wrong
    address3 = "Srinivasa Nagar,  Bangalore, Karnataka 560050"
    correctAdr = corAddr(address3)
    print(f'The address is {address3}\n The corrected addres is {correctAdr}')
