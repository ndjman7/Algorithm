# Write your MySQL query statement below
UPDATE salary
SET sex = IF (sex = "m", "f", "m");

# UPDATE
# SET
#       SEX = CASE sex
#           WHEN "m" THEN "f"
#           ELSE "m"
#       END;
