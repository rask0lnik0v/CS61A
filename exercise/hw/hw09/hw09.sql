CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size
  FROM dogs, sizes
  WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT c.name
  FROM parents AS a,
       dogs AS b,
       dogs AS c
  WHERE c.name = a.child
        AND b.name = a.parent	
  ORDER BY b.height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings_of_same_size AS
  SELECT a.name AS name_a, b.name AS name_b, a.size 
  FROM size_of_dogs AS a,
       size_of_dogs AS b,
       parents AS c,
       parents AS d
  WHERE a.name < b.name
        AND a.size = b.size
	AND c.parent = d.parent
	AND c.child = a.name
	AND d.child = b.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || name_a || " plus " || name_b || " have the same size: " || size
  FROM siblings_of_same_size;

