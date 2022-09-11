select Name from records where Supervisor = 'Oliver Warbucks';

select * from records where Supervisor = Name;

select Name from records where Salary > 50000 order by Name;

select Day, Time from records as a, meetings as b 
		where a.Supervisor = 'Oliver Warbucks' and 
			  b.Division = a.Division;


select a.Name, b.Name from records as a, records as b, meetings as c, meetings as d
		where a.Name < b.Name and
			  a.Division = c.Division and
			  b.Division = d.Division and
			  c.Day = d.Day and
			  c.Time = d.Time;		

select a.Name from records as a, records as b
		where a.Supervisor = b.Name and
			  b.Division != a.Division; 

select sum(Salary) as sum, Supervisor from records
		group by Supervisor;

select b.Day from records as a, meetings as b
		where a.Division = b.Division
		group by Day
		having count(*) < 5;

select Division from records
		group by Division
		having count(*) > 1 and
			   sum(Salary) < 100000;

create table num_taught as
	select Professor as professor, Course as course, count(*) as times
	from courses
	group by Professor, Course;


select a.professor, b.professor, a.course from num_taught as a, num_taught as b
		where a.professor < b.professor and
			  a.course = b.course and
			  a.times = b.times;

select a.Professor, b.Professor from courses as a, courses as b
		where a.Semester = b.Semester and
			  a.Course = b.Course and
			  a.Professor < b.Professor
		group by a.Course, b.Professor
		having count(*) > 1;

		