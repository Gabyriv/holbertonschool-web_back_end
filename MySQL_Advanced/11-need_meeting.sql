-- 11. Need meeting view
-- Create view need_meeting listing students with score < 80 AND (no last_meeting OR last_meeting older than 1 month)

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (
    last_meeting IS NULL
    OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
  );
