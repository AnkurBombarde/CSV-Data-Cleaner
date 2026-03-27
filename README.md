# 🧹 CSV Data Cleaner

A beginner-friendly web application for uploading, analyzing, and cleaning CSV datasets using Python, Pandas, and Streamlit.

---

## ⚡ Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Access at http://localhost:8501
```

---

## 🎯 Features

- ** Upload & Inspect**: Load CSV files with validation and preview
- ** Data Analysis**: Detect missing values, duplicates, whitespace issues, and data types
- ** Data Cleaning**: Remove duplicates, handle missing values, clean text, rename/remove columns, convert data types
- ** Before/After Comparison**: Track improvements and generate cleaning reports
- ** Export**: Download cleaned data as CSV

---

## 📖 How to Use

1. **Upload**: Go to " Upload & Inspect" and select your CSV file
2. **Analyze**: Click "Generate Analysis Report" to identify data quality issues
3. **Clean**: In " Clean Data", apply operations (remove duplicates, fill missing values, clean text, etc.)
4. **Export**: Download your cleaned data from "📊 Summary & Export"

---

## 🛠️ Architecture

### Modules

| Module | Purpose |
|--------|---------|
| `data_loader.py` | Load CSV files, extract metadata, generate previews |
| `data_analyzer.py` | Detect missing values, duplicates, whitespace issues, analyze data types |
| `data_cleaner.py` | Apply cleaning operations (missing values, duplicates, text cleaning, type conversion) |
| `app.py` | Streamlit UI and orchestration |

### Core Functions

**DataLoader:**
- `load_csv(file)` - Load with validation
- `get_dataset_info(df)` - Extract statistics
- `get_preview(df, rows)` - Get data preview

**DataAnalyzer:**
- `analyze_missing_values(df)` - Identify missing data
- `analyze_duplicates(df)` - Detect duplicates
- `analyze_data_types(df)` - Categorize column types
- `analyze_whitespace_issues(df)` - Find spacing issues
- `generate_full_report(df)` - Comprehensive report

**DataCleaner:**
- `handle_missing_values(df, strategy)` - Apply missing value strategy
- `remove_duplicates(df)` - Remove duplicate rows
- `clean_text(df, columns, operations)` - Apply text transformations
- `remove_columns(df, columns)` - Delete columns
- `rename_columns(df, rename_dict)` - Rename columns
- `change_data_type(df, column, type)` - Convert data types
- `export_to_csv(df, filename)` - Export cleaned data

---

## ❓ FAQ

| Question | Answer |
|----------|--------|
| Will my original file be modified? | No! The app works on a copy. Original is always preserved. |
| Can I undo changes? | Yes, reload the file to start fresh. |
| What file formats are supported? | CSV only (convert Excel/TSV to CSV first). |
| Is my data sent to a server? | No! Everything runs locally on your computer. |
| Can I clean large files? | Yes, depends on your available RAM. |

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| CSV parsing error | Verify file is properly formatted (UTF-8 encoding, consistent columns) |
| App won't open in browser | Manually navigate to `http://localhost:8501` |
| Memory error with large files | Try smaller files or check available RAM |
| Missing values not filling | Ensure correct data type for the strategy (mean/median need numeric columns) |

---

## 🔧 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.28.1+ | Web UI framework |
| pandas | 2.1.3+ | Data manipulation |
| numpy | 1.24.3+ | Numerical operations |
| openpyxl | 3.1.2+ | Excel support |

---

## 💡 Tips

1. **Always analyze first** before applying cleaning operations
2. **Apply operations one at a time** to identify issues easily
3. **Keep the cleaning report** for reproducibility
4. **Test cleaned data** before using in analysis/models

---

## 🎓 Learning Outcomes

- Data quality assessment techniques
- Common data cleaning patterns
- Pandas fundamentals
- Python data science workflow
- Building interactive apps with Streamlit

---



## 🆘 Support

1. Check Streamlit docs: https://docs.streamlit.io
2. Verify CSV file format
3. Ensure all dependencies are installed
