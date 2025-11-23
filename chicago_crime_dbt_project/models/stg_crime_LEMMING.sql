{{ config(materialized='table') }}

SELECT
    id,
    case_number,
    date,   -- already a timestamp
    primary_type,
    description,
    location_description,
    arrest,
    domestic,
    district,
    ward,
    community_area,
    latitude,
    longitude,
    DATE_TRUNC('month', date) AS month
FROM {{ source('final_LEMMING', 'raw_crime_LEMMING') }}
WHERE latitude IS NOT NULL
  AND longitude IS NOT NULL
