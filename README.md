

Converts the studypath https://opintopolku.fi  json to a simpler text list/table.



End result a row with:

* Date of approval of course (YYYY-MM-DD);
* Organization(Uni/School); 
* Open university info/Faculty
* course name/type; 
* number of ECTS and name of study units
* passed status (grade)


```

Course_Name   Grade  Study_Units  Date        University
Acme Course   HYV    1.00         2021-08-19  University of Acme
```


### TODO

- chk translations 
- test with the "real" file with lots of data.
- is there enough data to get pass grade in style 4/5 ? -> constants?
- yo side comes as unknowns
