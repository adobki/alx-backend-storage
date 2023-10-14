-- Creates a stored procedure that computes and stores the average
-- score for a student: ComputeAverageScoreForUser(user_id)
DELIMITER // ;
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser//
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
    DECLARE total INT;
    DECLARE number_of_scores INT;
    SET total = (SELECT SUM(score) 
                 FROM corrections
                 WHERE corrections.user_id = user_id);
    SET number_of_scores = (SELECT COUNT(score)
                            FROM corrections
                            WHERE corrections.user_id = user_id);
    UPDATE users
    SET average_score = total / number_of_scores
    WHERE id = user_id;
END//
DELIMITER ; //
