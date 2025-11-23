{{ config(materialized='table') }}

SELECT
    month,
    primary_type,
    district,
    COUNT(*) AS crime_count,
    AVG(CASE WHEN arrest THEN 1 ELSE 0 END) AS arrest_rate
FROM {{ ref('stg_crime_LEMMING') }}
GROUP BY 1, 2, 3
ORDER BY 1, 2