-- Call SafeDiv() with various paramaters
select SafeDiv(12,2), SafeDiv(2,12), SafeDiv(12,0), SafeDiv(0,12), SafeDiv(9, 89);
SELECT *, (a / b) AS 'a / b', SafeDiv(a, b) FROM numbers;
