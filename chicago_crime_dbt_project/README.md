
# **dbt: Chicago Crime Transformations (LEMMING)**

This dbt project contains the transformation logic for the Chicago Crime Pipeline. Raw crime data is ingested from the Chicago API and stored in **Snowflake (MLDS430.final_LEMMING)**. dbt models clean, standardize, and aggregate the data for downstream analytics.

---

# **Models Overview**

## **1. Staging Model — `stg_crime_LEMMING.sql`**

Purpose:

* Clean raw crime data
* Remove invalid latitude/longitude
* Convert timestamp field
* Extract `month` for trend analysis

Model source reference:


---

## **2. Fact Model — `fct_crime_summary_LEMMING.sql`**

Purpose:

* Aggregate crimes by month, type, and district
* Compute total crime count
* Calculate arrest rate

Model file:


---

## **3. Tests — `schema.yml`**

This file defines:

* Sources (raw crime table)
* Column-level tests
* Model validation rules



---

# **dbt Usage**

### **Build all models**

```bash
dbt run
```

### **Run tests**

```bash
dbt test
```

### **Debug Snowflake connection**

```bash
dbt debug
```

---

# **Project Structure**

```
models/
│
├── stg_crime_LEMMING.sql
├── fct_crime_summary_LEMMING.sql
├── schema.yml
│
dbt_project.yml
profiles.yml (local only)
```

---

# **Purpose of dbt Layer**

dbt ensures the pipeline is:

* Reproducible
* Documented
* Easily tested
* Transformations are version-controlled
* Modeling logic is separated from extraction and visualization


