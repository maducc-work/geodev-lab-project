import csv  

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        values = []
        for row in rows:
            raw = row[column].strip()
            if raw == "":
                continue
            values.append(float(raw))
        return {"smallest": min(values), "largest": max(values), "count": len(values)}



result = inspect_column("wards.csv", "area_km2")
print(result)
