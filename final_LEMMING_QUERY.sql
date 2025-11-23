CREATE SCHEMA IF NOT EXISTS MLDS430.final_LEMMING;

CREATE OR REPLACE TABLE MLDS430.final_LEMMING.raw_crime_LEMMING (
    id STRING,
    case_number STRING,
    date TIMESTAMP,
    primary_type STRING,
    description STRING,
    location_description STRING,
    arrest BOOLEAN,
    domestic BOOLEAN,
    district STRING,
    ward STRING,
    community_area STRING,
    latitude FLOAT,
    longitude FLOAT
);

//test if tables exist
SELECT * FROM MLDS430.final_LEMMING.stg_crime_LEMMING LIMIT 10;
SELECT * FROM MLDS430.final_LEMMING.fct_crime_summary_LEMMING LIMIT 10;

