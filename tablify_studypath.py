
import json

# Open and read the JSON file
with open('data1.json', 'rb') as file:
    data = json.load(file)

# Print the data
#print(data)
    
LANG = "fi"

studyrights = data['opiskeluoikeudet']
scope= ""
scopeUnit = ""

for impl  in studyrights:

    for course in impl:
        #print(course) keys of json

        if course == 'suoritukset' :

            occ = impl['suoritukset']

            for detail in occ:
            
                #print("D:", detail)
            

                coursename=detail['osasuoritukset'][0]['osasuoritukset'][0]['koulutusmoduuli']['nimi'][LANG].split(", ")[0]


                #'fi': 'Avoimen yliopiston opinnot, Avoimen yliopiston opinnot' <- split drops the other one.
                loc =  detail['koulutusmoduuli']['nimi'][LANG].split(", ")[0]
                org = detail['toimipiste']['nimi'][LANG]

                passedCourse = detail['osasuoritukset'][0]['arviointi'][0]['hyväksytty']
                passedValue = detail['osasuoritukset'][0]['arviointi'][0]['arvosana']['nimi'][LANG]

                scope  = detail['osasuoritukset'][0]['koulutusmoduuli']['laajuus']['arvo']
                scopeUnit =  detail['osasuoritukset'][0]['koulutusmoduuli']['laajuus']['yksikkö']['lyhytNimi'][LANG]

                #yyyy-mmm-DD
                dateapprv = detail['osasuoritukset'][0]['arviointi'][0]['päivä']

                #print(passedCourse, passedValue)
                if passedCourse :
                    passed = 'hyväksytty'
                else:
                    passed = 'hylätty'

                print("{4};{5};{0};{1};{2};{3};{6} ({7})".format(loc, coursename,scope, scopeUnit, dateapprv, org,passed,passedValue))
                





