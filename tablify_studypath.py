# -*- coding: utf-8 -*-
import json
import pandas as pd

# Load JSON data
with open('data2.json', 'rb') as file:
    data = json.load(file)

# Extract course information
courses = []
for opiskeluoikeus in data.get('opiskeluoikeudet', []):
    university_name = opiskeluoikeus.get('oppilaitos', {}).get('nimi', {}).get('en', 'Unknown University')
    for suoritus in opiskeluoikeus.get('suoritukset', []):
        # Handle osasuoritukset (submodules or individual courses)
        for osasuoritus in suoritus.get('osasuoritukset', []):
            course_name = osasuoritus.get('koulutusmoduuli', {}).get('nimi', {}).get('en', 'Unknown Course')
            university_name = osasuoritus.get('toimipiste', {}).get('nimi', {}).get('en', university_name)

            # Access the 'vahvistus' date safely
            #if 'vahvistus' in osasuoritus and osasuoritus['vahvistus'] is not None:
            #    vahvistus_date = osasuoritus['vahvistus'].get('päivä', 'No Date')
            #else:
            #    vahvistus_date = 'No Date'

            #print("Vahvistus", vahvistus_date)

            for arviointi in osasuoritus.get('arviointi', []):
                grade = arviointi.get('arvosana', {}).get('koodiarvo', 'No Grade')
                passed_date = arviointi.get('päivä', 'No Date')
                #passed_date = arviointi.get('p\u00E4iv\u00E4', 'No Date')

                laajuus = osasuoritus.get('koulutusmoduuli', {}).get('laajuus', {})
                study_units = laajuus.get('arvo', 1)  # Default to 1 if not present

                #print("passed_datee:",passed_date)
                # Add to courses list
                courses.append({
                    'Course_Name': course_name,
                    'Grade': grade,
                    'Study_Units': study_units,
                    'Date': passed_date,
                    'University': university_name
                })


df = pd.DataFrame(courses)


df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%Y-%m-%d')  # Ensure date format YYYY-MM-DD

df_sorted = df.sort_values(by='Date', ascending=False)


print(df_sorted)


df_sorted.to_csv('courses_sorted.csv', index=False)
