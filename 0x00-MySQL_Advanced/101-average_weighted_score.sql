-- Creates a stored procedure that computes and stores the average weighted
-- score for a student: ComputeAverageWeightedScoreForUser(user_id)
DELIMITER // ;
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers//
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare variables and cursor
    DECLARE user_id INT;
    DECLARE averageWeightedScore FLOAT;
    DECLARE break BOOLEAN DEFAULT FALSE;
    -- DECLARE cursor_users CURSOR FOR SELECT id,data FROM users;
    DECLARE cursor_users CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET break = TRUE;

    -- Activate cursor and iterate through each id in users
    OPEN cursor_users;
    users_loop: LOOP
        FETCH cursor_users into user_id;
        -- Check iterator/cursor is not null before proceeding
        IF break THEN
            LEAVE users_loop;
        END IF;

        -- Calculate average weighted score
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
    END LOOP;
END//
DELIMITER ; //
