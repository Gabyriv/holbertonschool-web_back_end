-- 10. Safe division function
-- Create a SQL function SafeDiv(a INT, b INT) that returns a / b, or 0 if b == 0

DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
  -- Avoid division by zero; return 0 when b is 0
  IF b = 0 THEN
    RETURN 0;
  ELSE
    -- MySQL '/' does floating division; return type is FLOAT
    RETURN a / b;
  END IF;
END $$
DELIMITER ;
