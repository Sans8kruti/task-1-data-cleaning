# Netflix Dataset Cleaning - Task 1

## Summary of Changes

- **Original rows/columns**: 8807 rows, 12 columns  
- **Final rows/columns after cleaning**: 8807 rows, 12 columns  
- Removed **duplicate rows**  
- Filled missing values:  
  - `director`, `cast`: Replaced with 'Not Available'  
  - `country`, `rating`, `duration`: Replaced with most frequent value  
  - `date_added`: Converted to `datetime`, missing values set to '2000-01-01'  
- Standardized text:
  - Lowercased values in `type`
  - Uppercased values in `rating`  
- Renamed all columns to lowercase, removed spaces (snake_case format)

## Files Included

- `netflix_cleaned.csv`: Cleaned dataset  
- `clean_netflix.py`: Python code used for cleaning  

This task was completed as part of a Data Analyst Internship assignment focused on data cleaning and preprocessing.
