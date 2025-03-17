CREATE
(Spongebob:Student {name: "Spongebob", age: 16, grade: 11}),
(HarryPotter:Student {name: "Harry Potter", age: 17, grade: 11}),
(SherlockHolmes:Student {name: "Sherlock Holmes", age: 18, grade: 12}),
(MickeyMouse:Student {name: "Mickey Mouse", age: 15, grade: 9}),
(Batman:Student {name: "Batman", age: 17, grade: 11}),

(Math:Subject {name: "Math"}),
(DADA:Subject {name: "Defense Against the Dark Arts"}),
(ForensicScience:Subject {name: "Forensic Science"}),
(Music:Subject {name: "Music"}),
(Physics:Subject {name: "Physics"}),

(CookingClub:Club {name: "Cooking Club"}),
(QuidditchClub:Club {name: "Quidditch Club"}),
(MysteryClub:Club {name: "Mystery Club"}),
(MartialArtsClub:Club {name: "Martial Arts Club"}),

(Spongebob)-[:LIKES_SUBJECT]->(Math),
(HarryPotter)-[:LIKES_SUBJECT]->(DADA),
(SherlockHolmes)-[:LIKES_SUBJECT]->(ForensicScience),
(MickeyMouse)-[:LIKES_SUBJECT]->(Music),
(Batman)-[:LIKES_SUBJECT]->(Physics),

(Spongebob)-[:A_MEMBER_OF {role: "President"}]->(CookingClub),
(HarryPotter)-[:A_MEMBER_OF {role: "President"}]->(QuidditchClub),
(SherlockHolmes)-[:A_MEMBER_OF {role: "President"}]->(MysteryClub),
(MickeyMouse)-[:A_MEMBER_OF {role: "member"}]->(CookingClub),
(Batman)-[:A_MEMBER_OF {role: "member"}]->(MartialArtsClub),

(Spongebob)-[:FRIENDS]->(HarryPotter),
(Spongebob)-[:FRIENDS]->(SherlockHolmes),
(Spongebob)-[:FRIENDS]->(MickeyMouse),
(Spongebob)-[:FRIENDS]->(Batman),
(HarryPotter)-[:FRIENDS]->(SherlockHolmes),
(HarryPotter)-[:FRIENDS]->(MickeyMouse),
(HarryPotter)-[:FRIENDS]->(Batman),
(SherlockHolmes)-[:FRIENDS]->(MickeyMouse),
(SherlockHolmes)-[:FRIENDS]->(Batman),
(MickeyMouse)-[:FRIENDS]->(Batman);



