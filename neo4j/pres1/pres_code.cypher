//CREATE

CREATE  (st :Student) RETURN st

CREATE (st :Student{name:’HarryPotter’, age:17, grade:11} ) RETURN st

CREATE  ( st :Student {name : 'Sherlock Holmes', age:18,grade:12})-[:Friends]->(st2:Student {name : 'MickeyMouse', age:15, grade:9})
RETURN st, st2

CREATE (st :Student {name : 'Batman', age:17,grade:11}) -[:a_member_of { role : 'member' } ]-> (cl:Club{name:'Martial Arts Club'})
RETURN st, cl

//MATCH

MATCH (n) RETURN  n 

MATCH (st :Student) WHERE st.age = 17 RETURN st
|
MATCH (st{age:17}) RETURN st

MATCH(cl: Club) RETURN cl 

 
MATCH (st:Student)
WITH st ORDER BY st.age DESC LIMIT 2
RETURN st.name, st.age  

MATCH(st1:Student) -[re:A_MEMBER_OF{role:'President'}]->(cl:Club) RETURN st1,  cl

//MATCH(st1:Student) -[{role:'President'}]->(cl:Club) RETURN st1,  cl

//DELETE

match(st:Student {name :'Harry Potter'})
delete st 


MATCH(st:Student {name :'HarryPotter'})-[r:LIKES_SUBJECT]->(:Subject) 
DELETE r

MATCH (st:Student {name: "Harry Potter"})-[r:A_MEMBER_OF{role: 'President'}]-> ()
DELETE r

MATCH (st:Student {name: "Harry Potter"})-[r:Friends]-> ()
DELETE r

MATCH(st:Student {name :'HarryPotter'})
DELETE st

MATCH(st:Student) 
WHERE st.grade <> 11 
DETACH DELETE st

//SET

MATCH(st:Student {name :'Batman' } ) 
SET st.grade = 12
RETURN st

MATCH(st:Student{name:'Spongebob'})-[r:A_MEMBER_OF]->(cl:Club)
SET r.role = 'member'
RETURN st, cl

//MERGE

MERGE (st:Student {name: "Spongebob"})
RETURN st

MERGE (st:Student {name: "Harry Potter"})
RETURN st

//FOREACH

MATCH (s:Student)  
FOREACH (student IN [s] |
  SET student.age = student.age + 1
)



MATCH (s:Student)
WHERE s.grade < 12
FOREACH (student IN [s] |
  SET student.grade = student.age + 1
)

//AGREGATE

MATCH (s:Student)
RETURN COUNT(s) AS total_students

MATCH (s:Student)
RETURN SUM(s.age) AS total_age

MATCH (s:Student)
RETURN AVG(s.age) AS average_age

MATCH (s:Student)
RETURN MIN(s.age) AS youngest_age

MATCH (s:Student)
RETURN COUNT(DISTINCT s.age) AS unique_ages

MATCH (s:Student)
RETURN COLLECT(s.name) AS student_names
