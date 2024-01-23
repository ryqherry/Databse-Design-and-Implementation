
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10608239&assignment_repo_type=AssignmentRepo)
# Exam 1

Update the solution contents of this file according to [the instructions](instructions/instructions.md).

## Solutions

The following sections contain a report on the solutions to each of the required components of this exam.

### Data munging

The code in the Python program, [solution.py](solution.py), contains the solutions to the **data munging** part of this exam.

### Spreadsheet analysis

The spreadsheet file, [wifi.xslx](data/wifi.xslx), contains the solutions to the **spreadsheet analysis** part of this exam. In addition, the formulas used in that spreadsheet are indicated below:

1. Total number of free Wi-Fi hotspots in NYC

```
=COUNTIF(C:C,"Free")
```

2. Number of free Wi-Fi hotspots in each of the 5 boroughs of NYC.

```
=COUNTIFS(C:C,"Free",R:R,AE7)
=COUNTIFS(C:C,"Free",R:R,AE8)
=COUNTIFS(C:C,"Free",R:R,AE9)
=COUNTIFS(C:C,"Free",R:R,AE10)
=COUNTIFS(C:C,"Free",R:R,AE11)
```

3. Number of free Wi-Fi hotspots provided by the LinkNYC - Citybridge in each of the zip codes of Manhattan.

```
=COUNTIFS(C:C,"Free",D:D,"LinkNYC - Citybridge",V:V,AE25)
```

4. The percent of all hotspots in Manhattan that are provided by LinkNYC - Citybridge.

```
=COUNTIFS(R:R,"Manhattan",D:D,"LinkNYC - Citybridge")/COUNTIF(R:R,"Manhattan")*100
```

### SQL queries

This section shows the SQL queries that you determined solved each of the given problems.

1. Write two SQL commands to create two tables named `hotspots` and `populations`.

```sql
CREATE TABLE hotspots (
    id INTEGER PRIMARY KEY,
    borough_id INTEGER,
    type TEXT,
    provider TEXT,
    name TEXT,
    location TEXT,
    latitude REAL,
    longitude REAL,
    x REAL,
    y REAL,
    location_t TEXT,
    remarks TEXT,
    city TEXT,
    ssid TEXT,
    source_id TEXT,
    activated TEXT,
    borocode INTEGER,
    borough_name TEXT,
    nta_code TEXT,
    nta TEXT,
    council_district INTEGER,
    postcode INTEGER,
    boro_cd INTEGER,
    census_tract INTEGER,
    bctcb2010 INTEGER,
    bin INTEGER,
    bbl INTEGER,
    doitt_id INTEGER,
    lat_lng TEXT
);
```

```sql
CREATE TABLE populations (
    borough TEXT,
    year INTEGER,
    fips_county_code INTEGER,
    nta_code TEXT,
    nta TEXT,
    population INTEGER,
    PRIMARY KEY (nta_code, year)
);
```

2. Import the data in the `wifi.csv` and `neighborhood_populations.csv` CSV files into these two tables.

```sql
.mode csv
.import C:/Users/Herry/Desktop/DDI/updated-exam1-ryqherry/data/wifi.csv hotspots --skip 1
```

```sql
.import C:/Users/Herry/Desktop/DDI/updated-exam1-ryqherry/data/neighborhood_populations.csv populations --skip 1
```

3. Display the five zip codes with the most Wi-Fi hotspots and the number of Wi-Fi-hotspots in each in descending order of the number of Wi-Fi-hotspots.

```sql
select postcode, count(id) from hotspots group by postcode order by count(id) desc limit 5;
```

4. Display a list of the name, location, and zip code for all of the free Wi-Fi locations provided by `ALTICEUSA` in Bronx, in descending order of zip code.

```sql
select name, location, postcode from hotspots where type = "Free" and provider = "ALTICEUSA" and borough_name = "Bronx" order by postcode desc;
```

5. Display the names of each of the boroughs of NYC, and the number of free Wi-Fi hotspots in each.

```sql
select borough_name, count(id) from hotspots where type = "Free" group by borough_name;
```

6. Display the number of wifi hotspots in Bay Ridge, Brooklyn along with the population of Bay Ridge, Brooklyn.

```sql
select count(hotspots.id), populations.population from hotspots inner join populations on hotspots.nta_code=populations.nta_code and populations.year = 2010 where hotspots.nta_code = "BK31";
```

7. Display the number of **Free** wifi hotspots in each of the 5 NYC boroughs, along with the population of each borough.

```sql
select count(hotspots.id), populations.population from hotspots inner join populations on hotspots.nta_code=populations.nta_code and populations.year = 2010 where hotspots.type = "Free" group by hotspots.borough_name;
```

8. Display the names of each of the neighborhoods in which there exist Wi-Fi hotspots, but for which we do not have population data.

```sql
select hotspots.nta from hotspots left join populations on hotspots.nta_code=populations.nta_code where populations.nta_code IS NULL;
```

9. Write an additional SQL query of your choice using Sqlite with this table; then describe the results

This query identifies all of the Wi-Fi-hotspots in the zip codes near NYU along with their names and locations.

```sql
select hotspots.ssid, hotspots.location from hotspots where type = "Free" and postcode in (10003, 10011, 10012);
```

### Normalization and Entity-relationship diagramming

This section contains responses to the questions on normalization and entity-relationship diagramming.

1. Is the data in `wifi.csv` in fourth normal form?

```
No, the data in `wifi.csv` is not in fourth normal form.
```

2. Explain why or why not the `wifi.csv` data meets 4NF.

```
Because `nta` is fact of `nta_code` and `borough_name` is fact of `nta_code` as well. Thus, a non-key field is a fact of another non-key field, then the data does not meet 4NF.
```

3. Is the data in `neighborhood_populations.csv` in fourth normal form?

```
No, the data in `neighborhood_populations.csv` is not in fourth normal form.
```

4. Explain why or why not the `neighborhood_populations.csv` data meets 4NF.

```
Because `borough` and `nta` are facts of `nta_code` only, and not facts of `year`. Thus, non-key fields are a fact of only part of the primary key, then the data does not meet 4NF.
```

5. Use [draw.io](https://draw.io) to draw an Entity-Relationship Diagram showing a 4NF-compliant form of this data, including primary key field(s), relationship(s), and cardinality.

![Placeholder E-R Diagram](./images/placeholder-er-diagram.svg)
