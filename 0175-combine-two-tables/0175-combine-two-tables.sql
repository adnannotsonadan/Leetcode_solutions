# Write your MySQL query statement below
-- select Person.firstName, Person.lastName, Address.city ,Address.state 
-- FROM Person
-- LEFT JOIN Address
-- ON Person.personId = Address.personId;

select p.firstName,p.lastName,a.city,a.state
from Person as p 
left join Address as a on a.personId=p.personId