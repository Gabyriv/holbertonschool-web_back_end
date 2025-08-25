-- 9. Index name and score
-- Create a composite index on the first character of `names.name` and on `score`
-- Optimizes queries like: SELECT ... FROM names WHERE name LIKE 'a%' AND score < 80;

CREATE INDEX idx_name_first_score ON names (name(1), score);
