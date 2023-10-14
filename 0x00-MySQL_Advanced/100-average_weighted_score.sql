-- Creates a stored procedure that computes and stores the average weighted
-- score for a student: ComputeAverageWeightedScoreForUser(user_id)
DELIMITER // ;
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser//
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    -- Calculate average weighted score
    DECLARE averageWeightedScore FLOAT;
    SELECT (SUM(scores) / SUM(weights)) INTO averageWeightedScore
    FROM (SELECT (score * weight) AS scores, weight AS weights
          FROM (SELECT score,
                    (SELECT weight
                     FROM projects
                     WHERE id = project_id) AS weight
                FROM corrections
                WHERE corrections.user_id = user_id) AS weights) AS avrg;

    -- Store the calculated average
    UPDATE users
    SET average_score = averageWeightedScore
    WHERE id = user_id;
END//
DELIMITER ; //
