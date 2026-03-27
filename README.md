# 🧹 CSV Data Cleaner

A beginner-friendly web application for uploading, analyzing, and cleaning CSV datasets. Built with Python, Pandas, and Streamlit.

**Upload, inspect, and clean your CSV files with ease.** This tool helps you identify and fix data quality issues like missing values, duplicates, and whitespace problems. Analyze your data, apply cleaning operations, and export the results—all in one place.

---

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

---

## 🎯 Features

### 1. 📤 File Upload & Inspection
- Upload CSV files with instant validation
- View dataset overview (rows, columns, memory usage)
- Display column names and data types
- Preview first 10 rows of data
- Automatic error handling for malformed files

### 2. 🔍 Data Quality Analysis
- **Missing Values Analysis**: Count and percentage of missing values per column
- **Duplicate Detection**: Identify complete duplicate rows
- **Data Type Summary**: Overview of all data types in the dataset
- **Whitespace Issues**: Detect columns with leading/trailing spaces
- **Numeric Statistics**: Mean, median, std, min, max for numeric columns
- **High-Risk Indicators**: Highlight columns with >50% missing data

### 3. 🧽 Data Cleaning
Multiple cleaning strategies:

#### Missing Values Handling
- Remove rows with missing values
- Fill with mean (numeric columns)
- Fill with median (numeric columns)
- Fill with mode (most frequent value)
- Fill with custom value

#### Duplicate Handling
- Remove complete duplicate rows
- Keep first occurrence

#### Text Cleaning
- Remove leading/trailing spaces
- Convert to lowercase
- Convert to uppercase
- Capitalize text

#### Column Operations
- Remove unwanted columns
- Rename columns
- Change data types (int, float, string, datetime)

### 4. 📊 Before vs After Summary
- Compare row and column counts
- Track missing value reductions
- Visualize data quality improvements
- Generate cleaning report

### 5. 📥 Export
- Download cleaned data as CSV
- Generate cleaning summary report
- Maintain data integrity during export

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the project**
   ```bash
   cd "CSV Data cleaner"
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   ```

   **Activate virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Application

1. **Ensure you're in the project directory**
   ```bash
   cd "CSV Data cleaner"
   ```

2. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

3. **Access the application**
   - The app will automatically open in your default browser
   - URL: `http://localhost:8501`
   - If it doesn't open, manually navigate to the URL shown in terminal

---

## 📖 Getting Started

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

---

## 📚 How to Use

### Step 1: Upload Your Data
1. Go to **📤 Upload & Inspect** section
2. Click "Choose a CSV file" or drag and drop
3. View the dataset overview and preview

### Step 2: Analyze Data Quality
1. Navigate to **🔍 Data Analysis**
2. Click "Generate Analysis Report"
3. Review:
   - Missing values distribution
   - Duplicate rows
   - Data types
   - Whitespace issues
   - Numeric statistics

### Step 3: Clean Your Data
1. Go to **🧽 Clean Data**
2. Select from available cleaning options:
   - Handle missing values
   - Remove duplicates
   - Clean text columns
   - Remove unnecessary columns
   - Rename columns
   - Convert data types
3. Click respective buttons to apply each operation
4. Preview changes in real-time

### Step 4: Review & Export
1. Navigate to **📊 Summary & Export**
2. Review before/after metrics
3. Download cleaned CSV file
4. Download cleaning report (optional)

### Common Operations

#### Remove Missing Values
```
1. "🧽 Clean Data" section
2. Expand "Handle Missing Values"
3. Select "Remove rows"
4. Click "Apply Missing Values Fix"
```

#### Remove Duplicates
```
1. "🧽 Clean Data" section
2. Expand "Remove Duplicates"
3. Click "Remove Duplicate Rows"
```

#### Clean Text (Remove Spaces)
```
1. "🧽 Clean Data" section
2. Expand "Clean Text Columns"
3. Select columns (e.g., Name)
4. Check "Remove leading/trailing spaces"
5. Click "Apply Text Cleaning"
```

#### Change Data Type
```
1. "🧽 Clean Data" section
2. Expand "Change Data Type"
3. Select column and target type
4. Click "Apply Type Conversion"
```

---

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

---


### Module Design

#### 1. **data_loader.py** - File I/O & Preview
**Responsibilities:**
- Load CSV files with error handling
- Extract dataset metadata
- Generate data previews
- Validate file integrity

**Key Functions:**
```python
DataLoader.load_csv(file)              # Load with validation
DataLoader.get_dataset_info(df)        # Get statistics
DataLoader.get_preview(df, rows)       # Get preview
```

**Error Handling:**
- CSV parsing errors
- Empty files
- File encoding issues

#### 2. **data_analyzer.py** - Data Quality Assessment
**Responsibilities:**
- Identify missing values
- Detect duplicates
- Analyze data types
- Find whitespace issues
- Calculate statistics
- Generate comprehensive reports

**Key Functions:**
```python
DataAnalyzer.analyze_missing_values(df)      # Missing data
DataAnalyzer.analyze_duplicates(df)          # Duplicate detection
DataAnalyzer.analyze_data_types(df)          # Type summary
DataAnalyzer.analyze_whitespace_issues(df)   # Whitespace check
DataAnalyzer.get_numeric_summary(df)         # Stats
DataAnalyzer.generate_full_report(df)        # Complete report
```

#### 3. **data_cleaner.py** - Data Transformation
**Responsibilities:**
- Handle missing values (multiple strategies)
- Remove duplicates
- Clean text data
- Manage columns (remove, rename)
- Convert data types
- Export cleaned data

**Key Functions:**
```python
DataCleaner.handle_missing_values(df, strategy, ...)
DataCleaner.remove_duplicates(df, subset)
DataCleaner.clean_text(df, columns, operations)
DataCleaner.remove_columns(df, columns)
DataCleaner.rename_columns(df, rename_dict)
DataCleaner.change_data_type(df, column, type)
DataCleaner.export_to_csv(df, filename)
```

#### 4. **app.py** - UI Controller & Orchestrator
**Responsibilities:**
- Provide Streamlit interface
- Manage session state
- Orchestrate module interactions
- Handle user interactions
- Display results

**Structure:**
```python
main()
├── Page 1: Upload & Inspect
│   ├── File uploader
│   ├── Error handling
│   ├── Dataset overview
│   ├── Column info
│   └── Data preview
├── Page 2: Data Analysis
│   ├── Analysis trigger
│   ├── Missing values report
│   ├── Duplicates report
│   ├── Data types summary
│   ├── Whitespace issues
│   └── Numeric stats
├── Page 3: Clean Data
│   ├── Missing values options
│   ├── Duplicate removal
│   ├── Text cleaning
│   ├── Column operations
│   └── Data preview
└── Page 4: Summary & Export
    ├── Before/After metrics
    ├── Detailed comparison
    └── Download options
```

### Data Flow

```
User Action
    ↓
Streamlit UI (app.py)
    ↓
Direction to Module
    ├─→ DataLoader (for file operations)
    ├─→ DataAnalyzer (for analysis)
    └─→ DataCleaner (for cleaning)
    ↓
Module processes DataFrame
    ↓
Results returned to UI
    ↓
Display in Streamlit
```

### State Management

The application uses Streamlit's `session_state` to maintain:

```python
st.session_state.original_df      # Original loaded data
st.session_state.cleaned_df       # Current working copy
st.session_state.analysis_report  # Cached analysis results
```

**Why?** Preserves data across page refreshes and user interactions.

### UI Design Principles

1. **Navigation**: Top navigation with clear section labels
2. **Feedback**: Success/warning messages for all actions
3. **Metrics**: Visual cards for key statistics
4. **Previews**: Show data at each step
5. **Clarity**: Plain language, minimal jargon

### Error Handling Strategy

**File Loading Errors**
```python
try:
    df = pd.read_csv(file)
except pd.errors.ParserError:
    show_error("CSV parsing failed")
except Exception as e:
    show_error(f"Load error: {e}")
```

**Data Type Conversion**
```python
try:
    converted = pd.to_numeric(value, errors='coerce')
except:
    handle_gracefully()
```

**Missing Values**
```python
if columns_have_missing:
    warn_user()
```

### Performance Considerations

- **Loaded Data**: Stored in session state (minimal memory for typical CSVs)
- **Operations**: Applied to copies to preserve originals
- **Large Files**: Pandas handles efficiently for typical datasets
- **Optimization**: Avoid unnecessary DataFrame copies

### Data Privacy

✅ **Local Processing**: All data stays on user's computer
✅ **No Upload**: Never sent to external servers
✅ **Session-Based**: Data cleared when browser closes
✅ **No Logging**: Processing not logged externally

---

## 🔧 Technical Details

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.28.1+ | Web UI framework |
| pandas | 2.1.3+ | Data manipulation |
| numpy | 1.24.3+ | Numerical operations |
| openpyxl | 3.1.2+ | Excel support |

### Module Descriptions

#### `data_loader.py`
- `DataLoader.load_csv()`: Load CSV files with error handling
- `DataLoader.get_dataset_info()`: Extract basic dataset statistics
- `DataLoader.get_preview()`: Get first N rows

#### `data_analyzer.py`
- `DataAnalyzer.analyze_missing_values()`: Identify and quantify missing data
- `DataAnalyzer.analyze_duplicates()`: Detect duplicate rows
- `DataAnalyzer.analyze_data_types()`: Categorize column types
- `DataAnalyzer.analyze_whitespace_issues()`: Find columns with spacing issues
- `DataAnalyzer.get_numeric_summary()`: Calculate statistics for numeric columns
- `DataAnalyzer.generate_full_report()`: Comprehensive data quality report

#### `data_cleaner.py`
- `DataCleaner.handle_missing_values()`: Multiple strategies for missing data
- `DataCleaner.remove_duplicates()`: Remove duplicate rows
- `DataCleaner.clean_text()`: Apply text transformations
- `DataCleaner.remove_columns()`: Delete unwanted columns
- `DataCleaner.rename_columns()`: Rename columns
- `DataCleaner.change_data_type()`: Convert column types
- `DataCleaner.export_to_csv()`: Export cleaned data

---

## 💡 Tips & Best Practices

### Before Cleaning
1. **Always analyze first**: Review data quality report before applying changes
2. **Keep backups**: The application works on a copy; original is preserved
3. **Understand your data**: Know what missing values mean (errors vs intentional)

### During Cleaning
1. **Apply operations one at a time**: Makes it easier to identify issues
2. **Verify changes**: Preview data after each operation
3. **Be careful with duplicates**: Ensure duplicate detection logic matches your needs

### After Cleaning
1. **Review improvements**: Check before/after metrics
2. **Test the data**: Use cleaned data in analysis/models
3. **Document changes**: Keep the cleaning report for reproducibility

---

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

---

## 🐛 Troubleshooting

### Issue: "CSV parsing error"
**Solution**: Ensure your CSV file is properly formatted. Check:
- Correct delimiter (usually comma)
- Consistent number of columns
- Proper encoding (UTF-8 recommended)

### Issue: "Application not opening in browser"
**Solution**: Manually navigate to `http://localhost:8501` in your browser

### Issue: "Memory error with large files"
**Solution**: 
- Try loading a smaller subset first
- Check available RAM
- Consider splitting the CSV into smaller files

### Issue: "Missing values not filling correctly"
**Solution**: 
- Ensure column has appropriate data type for the strategy (mean/median need numeric)
- Check for "None", "N/A", or other null representations

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

---

## 🚀 Deployment Considerations

### Local Development
```bash
streamlit run app.py
```

### Production Deployment
```bash
# Streamlit Cloud
# Heroku
# Docker container
# AWS Lambda
```

---

## 🔮 Future Enhancement Ideas

1. **Data Visualization**: Charts for missingness patterns
2. **Statistics**: Outlier detection
3. **Format Support**: Excel, JSON, SQL databases
4. **Advanced Cleaning**: Regex patterns, fuzzy matching
5. **Machine Learning**: Imputation with algorithms
6. **API**: REST API for automation
7. **Scheduling**: Batch processing
8. **Collaboration**: Share cleaning workflows

---

## 🧪 Testing Suggestions

### Unit Tests (data_loader.py)
- Test CSV loading with various formats
- Test error handling for malformed files
- Test preview generation

### Unit Tests (data_analyzer.py)
- Test missing value detection
- Test duplicate identification
- Test whitespace detection

### Unit Tests (data_cleaner.py)
- Test each cleaning strategy
- Test data type conversions
- Test column operations

### Integration Tests
- Full workflow from upload to export
- State management
- Error recovery

---

## 📚 Code Quality

- **Docstrings**: All functions documented with Args/Returns
- **Type Hints**: Clear parameter and return types
- **Error Messages**: User-friendly, actionable
- **Modular Design**: Single responsibility per module
- **DRY Principle**: Reusable utility functions

---

## 🎓 Learning Outcomes

By using this application, you'll learn:
- ✅ Data quality assessment techniques
- ✅ Common data cleaning patterns
- ✅ Pandas fundamentals
- ✅ Python data science workflow
- ✅ Building interactive apps with Streamlit

Developers learn:
- ✅ Modular architecture
- ✅ Separation of concerns
- ✅ Error handling patterns
- ✅ Streamlit best practices
- ✅ Data science pipeline design

---

## 📊 Example Use Cases

1. **Student Grades Dataset**: Remove duplicates, fill missing grades with mode
2. **Sales Data**: Clean product names (lowercase), remove incomplete records
3. **Survey Responses**: Handle missing values, standardize text fields
4. **Financial Data**: Convert columns to numeric types, identify outliers
5. **Customer Database**: Remove duplicates, clean contact information

---

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest new features
- Improve documentation
- Add sample datasets

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review your CSV file format
3. Ensure all dependencies are installed
4. Check Streamlit documentation: https://docs.streamlit.io

---

## 🎉 Have Fun!

Happy data cleaning! This tool is designed to be intuitive and beginner-friendly. Don't be afraid to experiment with different cleaning options.
