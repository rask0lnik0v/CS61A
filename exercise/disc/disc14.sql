select quarter from scoring
		group by quarter
		having sum(points) > 10;

select b.team, sum(a.points) as total_score from scoring as a, players as b
		where a.player = b.name
		group by b.team;

		