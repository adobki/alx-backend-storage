-- Lists all bands with 'Glam rock' as their style,
-- ranked by their longevity `lifespan`, then name
SELECT 
    band_name, COALESCE(split, 2022) - formed AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY lifespan DESC , band_name DESC;
