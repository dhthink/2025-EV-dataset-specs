-- SHOW Catalogs;
-- USE Catalog workspace;
-- show schemas ;
-- CREATE SCHEMA IF NOT EXISTS silver;

-- SHOW SCHEMAS;
-- use SCHEMA silver;

CREATE or REPLACE TABLE ev_specs_2025 AS
select 
    brand, model, segment,car_body_type, seats, 
    ROUND(acceleration_0_100_s * 0.621371,3) as zero_to_60_sec,
    ROUND(top_speed_kmh / 1.609, 3)  as top_speed_mph,
    battery_capacity_kwh,number_of_cells,
    ROUND(torque_nm * 0.73756, 2) as torque_ft_lbs,
    ROUND(efficiency_wh_per_km * 1.609334,2) AS range_miles,
     ROUND(1000 / (efficiency_wh_per_km * 1.609344), 3) AS miles_per_kwh

 from read_files(
      '/Volumes/workspace/onedrive/ev_data/ev_2025_raw_csv',
      format => 'csv',
      header => true 
 ) ;  