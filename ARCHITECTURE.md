# Project Configuration & Architecture

## 📋 Project Overview

**CSV Data Cleaner** is a modular, beginner-friendly data cleaning application.

### Architecture

```
┌─────────────────────────────────────────────────┐
│         Streamlit Web Interface (app.py)        │
│                                                 │
│  📤 Upload  │  🔍 Analyze  │  🧽 Clean  │ 📊 Export
└─────────────────────────────────────────────────┘
          │              │              │
          ↓              ↓              ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ DataLoader   │  │ DataAnalyzer │  │ DataCleaner  │
│              │  │              │  │              │
│ • load_csv   │  │ • missing    │  │ • handle_mv  │
│ • get_info   │  │ • duplicates │  │ • remove_dup │
│ • preview    │  │ • types      │  │ • clean_text │
│              │  │ • whitespace │  │ • remove_col │
│              │  │ • stats      │  │ • rename_col │
│              │  │ • report     │  │ • change_type│
│              │  │              │  │ • export     │
└──────────────┘  └──────────────┘  └──────────────┘
          │              │              │
          └──────────────┴──────────────┘
                   ↓
              Pandas DataFrames
```

## 🔧 Module Design

### 1. **data_loader.py** - File I/O & Preview
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

---

### 2. **data_analyzer.py** - Data Quality Assessment
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

---

### 3. **data_cleaner.py** - Data Transformation
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

---

### 4. **app.py** - UI Controller & Orchestrator
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

## 📊 Data Flow

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

## 🔄 State Management

The application uses Streamlit's `session_state` to maintain:

```python
st.session_state.original_df      # Original loaded data
st.session_state.cleaned_df       # Current working copy
st.session_state.analysis_report  # Cached analysis results
```

**Why?** Preserves data across page refreshes and user interactions.

## 🎨 UI Design Principles

1. **Navigation**: Sidebar with clear section labels
2. **Feedback**: Success/warning messages for all actions
3. **Metrics**: Visual cards for key statistics
4. **Previews**: Show data at each step
5. **Clarity**: Plain language, minimal jargon

## 🛡️ Error Handling Strategy

### File Loading Errors
```python
try:
    df = pd.read_csv(file)
except pd.errors.ParserError:
    show_error("CSV parsing failed")
except Exception as e:
    show_error(f"Load error: {e}")
```

### Data Type Conversion
```python
try:
    converted = pd.to_numeric(value, errors='coerce')
except:
    handle_gracefully()
```

### Missing Values
```python
if columns_have_missing:
    warn_user()
```

## 📈 Performance Considerations

- **Loaded Data**: Stored in session state (minimal memory for typical CSVs)
- **Operations**: Applied to copies to preserve originals
- **Large Files**: Pandas handles efficiently for typical datasets
- **Optimization**: Avoid unnecessary DataFrame copies

## 🔐 Data Privacy

✅ **Local Processing**: All data stays on user's computer
✅ **No Upload**: Never sent to external servers
✅ **Session-Based**: Data cleared when browser closes
✅ **No Logging**: Processing not logged externally

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.28.1 | Web UI framework |
| pandas | 2.1.3 | Data manipulation |
| numpy | 1.24.3 | Numerical operations |
| openpyxl | 3.1.2 | Excel support |

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

## 🔮 Future Enhancement Ideas

1. **Data Visualization**: Charts for missingness patterns
2. **Statistics**: Outlier detection
3. **Format Support**: Excel, JSON, SQL databases
4. **Advanced Cleaning**: Regex patterns, fuzzy matching
5. **Machine Learning**: Imputation with algorithms
6. **API**: REST API for automation
7. **Scheduling**: Batch processing
8. **Collaboration**: Share cleaning workflows

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

## 📚 Code Quality

- **Docstrings**: All functions documented with Args/Returns
- **Type Hints**: Clear parameter and return types
- **Error Messages**: User-friendly, actionable
- **Modular Design**: Single responsibility per module
- **DRY Principle**: Reusable utility functions

## 🎓 Learning Value

Users learn:
- ✅ Data quality assessment
- ✅ Pandas data manipulation
- ✅ Python best practices
- ✅ Web application design
- ✅ Data cleaning workflows

Developers learn:
- ✅ Modular architecture
- ✅ Separation of concerns
- ✅ Error handling patterns
- ✅ Streamlit best practices
- ✅ Data science pipeline design
