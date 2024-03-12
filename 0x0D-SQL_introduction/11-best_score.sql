-- Script to list all records with a score >= 10 ordered by score (top first)
-- List records with score >= 10 ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
