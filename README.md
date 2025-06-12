# vGFit-1.0
Fitting Soil Water Retention Curve using the van Genuchten Model

README: Soil Water Retention Curve Fitting (van Genuchten Model)
=================================================================================

This script fits soil water retention data to the van Genuchten model using pressure head and volumetric water content data from an Excel file.

--------------------------------------------------------------------------------
1. How to Use
--------------------------------------------------------------------------------

1. Open the script in Spyder or any Python IDE.
2. Modify the file path in the line:
       file_path = 'your_excel_file.xlsx'
3. Run the script. It will:
   - Fit the van Genuchten model to your data.
   - Perform linear regression between measured and fitted water content.
   - Save the results to a new Excel file in the same directory.
   - Display two plots:
       • van Genuchten fit (θ vs. h) with R².
       • Correlation plot with regression equation and R².

--------------------------------------------------------------------------------
2. Input File Format (Excel)
--------------------------------------------------------------------------------

The Excel file must contain at least one sheet named "Sheet1", with:
- Column A: Pressure head (h) in cm (positive values).
- Column B: Measured water content (θ).

Example:
    |   A   |    B    |
    |-------|---------|
    |  10   |  0.320  |
    |  30   |  0.295  |
    | 100   |  0.250  |
    | 300   |  0.195  |
    | 1000  |  0.130  |

--------------------------------------------------------------------------------
3. Output
--------------------------------------------------------------------------------

A new Excel file will be saved with:
- Sheet 'Fitted Data': original and fitted θ values.
- Sheet 'Parameters': estimated van Genuchten parameters and regression statistics.

Plots displayed:
1. θ vs h (VG fit) with R² only.
2. Measured θ vs Fitted θ with regression equation and R².

--------------------------------------------------------------------------------
4. Requirements
--------------------------------------------------------------------------------

Install required Python libraries using:

pip install pandas numpy scipy scikit-learn matplotlib openpyxl

--------------------------------------------------------------------------------
5. Notes
--------------------------------------------------------------------------------

- Ensure your Excel data has no missing values.
- The pressure head values must be numeric and positive.
- This version uses a hardcoded file path instead of a GUI file dialog.

--------------------------------------------------------------------------------
Author: S. KANZARI
Date: 2025


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15651610.svg)](https://doi.org/10.5281/zenodo.15651610)

--------------------------------------------------------------------------------
