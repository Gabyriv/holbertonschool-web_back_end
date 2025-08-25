-- 8. Index my names
-- Create an index on the first character of `names.name`
-- This speeds up queries like: SELECT ... FROM names WHERE name LIKE 'a%';

CREATE INDEX idx_name_first ON names (name(1));
