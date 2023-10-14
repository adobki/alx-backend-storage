-- Creates a view `need_meeting` that lists all students with
-- score < 80 (strict) and no `last_meeting` or > 1 month
CREATE OR REPLACE VIEW need_meeting AS
    SELECT name FROM students
        WHERE score < 80
            AND (ISNULL(last_meeting)
            OR last_meeting < ADDDATE(CURDATE(), INTERVAL -(1) MONTH));
