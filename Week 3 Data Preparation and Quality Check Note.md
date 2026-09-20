# **Week 3 Data Preparation and Quality Check Note**

**Study Area:** Owerri North LGA, Imo State, Nigeria

## **Coordinate Reference System**

The datasets were reprojected to **WGS 84 / UTM Zone 32N (EPSG:32632)**. This projected CRS was selected because it is appropriate for the study area and provides coordinates in metres, making it suitable for spatial analysis and distance and area measurements.

## **Data Reprojected**

* Owerri North LGA boundary  
* Hospital facilities

## **Data Clipped**

The hospital facilities layer was clipped using the Owerri North LGA boundary. This retained only hospital facilities located within the study area.

## **Quality Checks**

1. **CRS Check**  
   Both datasets were checked to confirm that they use the same CRS: WGS 84 / UTM Zone 32N (EPSG:32632). No CRS mismatch was found after reprojection.  
2. **Geometry Check**  
   The geometries were checked for invalid features. No significant geometry errors were identified.  
3. **Study Area and Extent Check**  
   The hospital facilities were checked against the Owerri North LGA boundary to confirm that the clipped features fall within the study area.  
4. **Attribute and Data Check**  
   The attribute tables were checked to confirm that the expected fields and facility records were retained after reprojection and clipping. No major data loss or unexpected changes were observed.  
5. **Duplicate and Location Check**  
   The hospital facility records and locations were reviewed for obvious duplicate or misplaced features. No significant issues were identified.

## **Problems Found and Actions Taken**

No major data quality problems were identified during the checks. The datasets were reprojected successfully, and the hospital facilities were clipped to the Owerri North study area. Any minor issues identified during visual inspection were flagged rather than altering the original source data.

## **Analysis-Ready File**

The processed datasets were saved as an analysis-ready GeoPackage containing the Owerri North LGA boundary and clipped hospital facilities.

**File:** `hospital_facilities_in_owerri_north.gpkg`

