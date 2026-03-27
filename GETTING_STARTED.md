# 🚀 Getting Started Guide - CSV Data Cleaner

A quick start guide to get up and running with the CSV Data Cleaner application in minutes!

## ⚡ Quick Start (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
streamlit run app.py
```

### 3. Open in Browser
- Application opens automatically at `http://localhost:8501`
- Or manually navigate to that URL

## 📖 First Steps

### Using Sample Data
1. In the **"📤 Upload & Inspect"** section
2. Click **"Choose a CSV file"**
3. Select **"sample_data.csv"** for testing
4. You should see:
   - Dataset overview with 10 rows
   - 7 columns with mixed data types
   - Some intentional data quality issues to practice cleaning

### What You'll See in Sample Data
- ✅ Complete records with all fields
- ❌ Missing values (Age, Salary, Performance_Score)
- ❌ Duplicate records (Alice Johnson appears twice)
- ❌ Extra spaces in names (Bob Williams, Henry Taylor)
- ❌ Inconsistent formatting (lowercase 'iris chen')

### Practice Cleaning Steps

**Step 1: Analyze Data Quality**
1. Go to **"🔍 Data Analysis"**
2. Click **"Generate Analysis Report"**
3. Notice:
   - Missing values per column
   - Duplicate row (Alice Johnson)
   - Whitespace issues
   - Data type distribution

**Step 2: Clean the Data**
1. Go to **"🧽 Clean Data"**
2. Apply these operations:
   - **Missing Values**: Choose "Fill with Mode" or "Remove rows"
   - **Duplicates**: Click "Remove Duplicate Rows"
   - **Text Cleaning**: Select Name and Department columns, enable "Strip" and "Capitalize"
   - **Data Types**: Convert Age and Salary to appropriate numeric types

**Step 3: Review Results**
1. Go to **"📊 Summary & Export"**
2. See improvements:
   - Fewer missing values
   - Duplicates removed
   - Consistent formatting
3. Download the cleaned data

## 🎯 Key Features at a Glance

| Feature | Location | Purpose |
|---------|----------|---------|
| Upload CSV | 📤 Upload & Inspect | Load and preview data |
| Analyze Quality | 🔍 Data Analysis | Identify data issues |
| Clean Data | 🧽 Clean Data | Apply cleaning operations |
| View Summary | 📊 Summary & Export | Compare before/after |
| Download | 📊 Summary & Export | Get cleaned CSV file |

## 💡 Common Operations

### Remove Missing Values
```
1. "🧽 Clean Data" section
2. Expand "Handle Missing Values"
3. Select "Remove rows"
4. Click "Apply Missing Values Fix"
```

### Remove Duplicates
```
1. "🧽 Clean Data" section
2. Expand "Remove Duplicates"
3. Click "Remove Duplicate Rows"
```

### Clean Text (Remove Spaces)
```
1. "🧽 Clean Data" section
2. Expand "Clean Text Columns"
3. Select columns (e.g., Name)
4. Check "Remove leading/trailing spaces"
5. Click "Apply Text Cleaning"
```

### Change Data Type
```
1. "🧽 Clean Data" section
2. Expand "Change Data Type"
3. Select column and target type
4. Click "Apply Type Conversion"
```

## 📊 Understanding the Analysis Report

### Missing Values Section
- **Missing Count**: Number of empty cells
- **Missing %**: Percentage of empty cells in that column
- **⚠️ Warning**: Columns with >50% missing are highlighted

### Duplicates Section
- **Total Duplicates**: Number of duplicate rows
- **Duplicate %**: Percentage of data that's duplicated
- ✅/⚠️ Indicator shows if duplicates exist

### Data Type Summary
- Shows count of each data type
- Helps identify unexpected types (e.g., Age as text)

### Whitespace Issues
- Columns with leading/trailing spaces
- Useful for data consistency

### Numeric Summary
- Statistics for numeric columns
- Mean, Median, Std Dev, Min, Max

## 🔄 Full Workflow Example

```
1. UPLOAD
   └─ Upload sample_data.csv

2. INSPECT
   └─ View: 10 rows, 7 columns
   └─ See: Missing values, duplicates, extra spaces

3. ANALYZE
   └─ Click "Generate Analysis Report"
   └─ Identify: 3 missing values, 1 duplicate, whitespace issues

4. CLEAN
   └─ Handle Missing Values → Remove rows
   └─ Remove Duplicates → Remove Duplicate Rows
   └─ Clean Text → Strip spaces, Capitalize

5. REVIEW
   └─ See improvements: 9 rows (1 removed), 0 duplicates
   └─ Missing values reduced from 3 to 0

6. EXPORT
   └─ Download cleaned CSV file
   └─ Use cleaned data for analysis
```

## ❓ FAQ

**Q: Will my original file be modified?**
A: No! The app creates a copy. Original is never changed.

**Q: Can I undo changes?**
A: Reload the file to start fresh with original data.

**Q: What file formats are supported?**
A: Currently CSV only. Other formats (Excel, TSV) can be converted to CSV first.

**Q: Is my data sent to any server?**
A: No! Everything runs locally on your computer. Your data stays with you.

**Q: Can I clean very large files?**
A: Depends on your computer's RAM. Try with smaller files first.

**Q: What if cleaning goes wrong?**
A: Upload the file again - original is always preserved!

## 🛠️ If Something Goes Wrong

### Application won't start
```bash
# Try restarting
streamlit run app.py

# Or restart the terminal and try again
```

### CSV not uploading
- Check file is actually .csv format
- Ensure it's not corrupted
- Try opening it in Excel/text editor to verify
- Look for encoding issues (should be UTF-8)

### Changes not applying
- Make sure you click the "Apply" button
- Check for error messages
- Verify column names are correct

### Need more help?
See **README.md** for detailed troubleshooting guide

## 🎓 Next Steps

Once you're comfortable with the sample data:
1. Try with your own CSV files
2. Explore all cleaning options
3. Experiment with different operations
4. Read the full **README.md** for advanced features

## 📚 File Organization

```
Your Project Folder/
├── app.py              ← Run this file
├── data_loader.py      ← Loading module
├── data_analyzer.py    ← Analysis module
├── data_cleaner.py     ← Cleaning module
├── sample_data.csv     ← Practice with this
├── requirements.txt    ← Dependencies
├── README.md           ← Full documentation
└── GETTING_STARTED.md  ← This file
```

## 🎉 You're Ready!

You now have everything to:
- ✅ Upload CSV files
- ✅ Analyze data quality
- ✅ Clean your data
- ✅ Export results

**Happy cleaning! 🧹**
