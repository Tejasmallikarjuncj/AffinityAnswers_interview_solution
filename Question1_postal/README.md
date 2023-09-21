###### Postal Address pincode correction solution

* BestDelivery Courier Company has an issue. Many parcels they get to deliver have the wrong PIN code and that leads to packages going to the wrong location and then someone figuring out manually that the PIN code is wrong from the other parts of the address. You are the programmer who has to fix this issue by writing a program that takes as input a free flowing address and checking if the PIN code indeed corresponds to the address mentioned. Use this free API http://www.postalpincode.in/Api-Details for the purpose of PIN code identification.
e.g. of correct addresses: "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050”,  
"2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050”, "374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050”,
e.g. of an incorrect addresses: "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095”,
“Colony, Bengaluru, Karnataka 560050”

####### I have Assume indain postal address will have this format
    * Recipient Information, such as Contact and Organization
    * House Number
    * Building Number or Name, or both
    * Sub-building Number or Name, or both
    * Main Street
    * Dependent Street
    * Locality 6
    * Locality 5
    * Locality 4
    * Locality 3
    * Locality 2
    * Locality 1 + Postal Code
    * Province (optional)
    * Country (optional)

####### My program's Algo is as follows
    * It parse the address and extarcts pincode locality subfield
    * Checks pincode with address using postal address with pincode
    * If it doesn't matches it find pincode using locality subfields using postal address with PostOffice

The solution is in pincodeverfy.py file

####### The test types are

* case1: If the address and pincode are correct like "2nd Phase, 374/B, 80 Feet Rd, State Bank Of Mysore Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore, Karnataka 560050"

* case2: if the address is correct and pincode is wrong like "2nd Phase, 374/B, 80 Feet Rd, State Bank Of Mysore Colony, Banashankari 3rd Stage, Srinivasa Nagar,  Bangalore, Karnataka 560045"

* case3: if the address and pincode are wrong like "Srinivasa Nagar,  Bangalore, Karnataka 560050"

###### For further study

I have collected addresses from collect swiggy delivery dataset form kaggle(Swiggy_50.csv) for using meachine to solve unstructured messy indian address, the address data is in address.csv , I exyracted data using Collection_address_Data.ipynb
