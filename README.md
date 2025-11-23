

## **Chicago Crime Data Pipeline (2024–2025) — Final Project**

This project builds an end-to-end data pipeline that collects Chicago crime data, loads it into Snowflake, transforms it with dbt, and visualizes insights using Tableau. The analysis covers crime activity in Chicago from **October 2024 to October 2025**.

---

# **1. Project Overview**

The goal of this project is to design a complete workflow for data ingestion, transformation, and visualization using industry tools. The final output is an interactive Tableau dashboard showing:

* **Monthly crime trends**
* **Citywide crime hotspots (heatmap)**
* **Filterable crime types and districts**

---

# **2. Pipeline Architecture**

```
Chicago Crime API  
        ↓
Python ETL Script (extract_crime_LEMMING.py)
        ↓
Snowflake (MLDS430.final_LEMMING)
        ↓
dbt Transformations (stg + fct models)
        ↓
Tableau Dashboard (trend line + heatmap)
```

---

# **3. Data Extraction (Python)**

The Python script queries Chicago’s open data API with pagination and loads the full year of data into Snowflake using key-pair authentication.

The extraction script is here:
**`extract_crime_LEMMING.py`**

The script performs:

* 12-month API pull (2024-10-01 → 2025-10-01)
* Pagination through 50k-row limits
* Column selection and cleaning
* Writing to Snowflake using `write_pandas`

---

# **4. Snowflake Storage**

`final_LEMMING_QUERY.sql` is the queries run in snowflake.
It is used to create the schema final_LEMMING and creating the raw_crime_LEMMING table.

All tables are stored in the **MLDS430.final_LEMMING** schema:

* `raw_crime_LEMMING` → raw API data
* `stg_crime_LEMMING` → cleaned staging table
* `fct_crime_summary_LEMMING` → monthly aggregated crime summary

Snowflake connection is configured using private-key authentication in my `profiles.yml`:



---

# **5. dbt Transformations**

The dbt project performs two main transformations:

### **Staging Model (`stg_crime_LEMMING.sql`)**

* Standardizes columns
* Converts timestamps
* Derives `month` field for temporal grouping



---

### **Fact Model (`fct_crime_summary_LEMMING.sql`)**

* Aggregates crimes by month, district, and primary type
* Computes crime counts and arrest rate



---

### **dbt Tests (`schema.yml`)**

* Ensures key fields are non-null
* Validates transformation integrity



---

# **6. Tableau Visualization**

The Tableau dashboard includes:

### **1. Crime Trend by Month (Line Chart)**

Shows how total crime fluctuates month-to-month.

### **2. Heatmap of Chicago**

Highlights spatial crime density across neighborhoods.

### **3. Interactive Filters**

* Primary Type
* District
* Month / Year

Filters apply across all visualizations.

---

# **7. How to Run the Project**

### **1. Run ETL Script**

```bash
python extract_crime_LEMMING.py
```

### **2. Run dbt**

```bash
cd chicago_crime_dbt_project
dbt debug
dbt run
dbt test
```

### **3. Connect Tableau to Snowflake**

Schema: `final_LEMMING`
Tables: `stg_crime_LEMMING`, `fct_crime_summary_LEMMING`

---

# **8. Dashboard Description (Included on Dashboard)**

**This dashboard shows crime patterns in Chicago from October 2024 to October 2025.
Use the filters to explore specific crime types, districts, or months.**

* The **line chart** displays monthly changes in crime volume.
* The **heatmap** highlights where crime is most concentrated across the city.
* Together, the visuals reveal both **when** and **where** crime is most active.

---

# **9. Repository Structure**

```
/
├── extract_crime_LEMMING.py
├── chicago_crime_dbt_project/
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── stg_crime_LEMMING.sql
│   │   ├── fct_crime_summary_LEMMING.sql
│   │   ├── schema.yml
│   └── profiles.yml (local only)
└── tableau/
    ├── chicago_crime_dashboard.twbx
```