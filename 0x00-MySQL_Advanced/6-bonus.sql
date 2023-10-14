-- Creates a stored procedure that adds a new correction for a student:
-- AddBonus(user_id, project_name, score).
-- NOTES: Assume `user_id` is linked to an existing user in `users`,
--        create `projects.project_name` if not found in the table
DELIMITER // ;
DROP PROCEDURE IF EXISTS AddBonus//
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
-- Create given project if it does not exist
IF NOT EXISTS(SELECT * FROM projects WHERE name = project_name) THEN
    INSERT INTO projects (name)
    VALUES(project_name);
END IF;
-- Add new correction
INSERT INTO corrections (user_id, project_id, score)
VALUES(user_id, 
       (SELECT id FROM projects WHERE name = project_name),
       score);
END//
DELIMITER ; //
