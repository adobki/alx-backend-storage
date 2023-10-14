-- Creates a function SafeDiv(a, b) that
-- divides a by b or returns 0 if b == 0
DELIMITER // ;
DROP FUNCTION IF EXISTS SafeDiv//
CREATE FUNCTION SafeDiv(a INT, b INT)
    RETURNS FLOAT
    NO SQL
    BEGIN
        IF b = 0 THEN
            RETURN 0;
        END IF;

        RETURN a / b;
    END//
DELIMITER ; //
