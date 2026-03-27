
import streamlit as st
import pandas as pd
from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from data_cleaner import DataCleaner

# Page configuration
st.set_page_config(
    page_title="CSV Data Cleaner",
    layout="wide",
)

st.markdown("""
    <style>
    .header-main {
        color: #1f77b4;
        margin-bottom: 30px;
        
    }

    /* Sticky, centered top navigation - Dark mode compatible */
    .st-key-top_nav {
        position: sticky;
        top: 0;
        z-index: 999;
        background: var(--background-color);
        backdrop-filter: blur(8px);
        padding: 1rem 0;
        border-bottom: 2px solid #1f77b4;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    @media (prefers-color-scheme: light) {
        .st-key-top_nav {
            background: rgba(255, 255, 255, 0.98);
        }
    }
    @media (prefers-color-scheme: dark) {
        .st-key-top_nav {
            background: rgba(20, 28, 36, 0.95);
        }
    }
    .st-key-top_nav h3 {
        text-align: center;
        margin: 0 0 0.5rem 0;
        color: #1f77b4;
        font-size: 1.1rem;
    }
    .st-key-top_nav [role="radiogroup"] {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
    }

    .metric-box {
        border: 2px solid #e0e0e0;
        padding: 15px;
        border-radius: 8px;
        background-color: #f8f9fa;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        padding: 10px;
        border-radius: 5px;
        color: #155724;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        padding: 10px;
        border-radius: 5px;
        color: #856404;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'original_df' not in st.session_state:
    st.session_state.original_df = None
if 'cleaned_df' not in st.session_state:
    st.session_state.cleaned_df = None
if 'analysis_report' not in st.session_state:
    st.session_state.analysis_report = None


def main():
    """Main application function"""

    # Header
    st.markdown("<h1 class='header-main'> CSV Data Cleaner</h1>", unsafe_allow_html=True)
    st.markdown("""
    **Upload, inspect, and clean your CSV files with ease.** This tool helps you identify and fix data quality issues like missing values, duplicates, and whitespace problems. 
    Analyze your data, apply cleaning operations, and export the results—all in one place.
    """)
    st.divider()

    with st.container(key="top_nav"):
        st.markdown("###  Navigation")
        page = st.radio(
            "Select a section:",
            [" Upload & Inspect", " Data Analysis", " Clean Data", " Summary & Export"],
            horizontal=True,
            label_visibility="collapsed"
        )

    st.divider()

    # ============================================
    # PAGE 1: UPLOAD & INSPECT
    # ============================================
    if page == " Upload & Inspect":
        st.header(" Upload & Inspect Your CSV File")
        st.markdown("Start by uploading your CSV file to begin the data cleaning process.")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            uploaded_file = st.file_uploader(
                "Choose a CSV file",
                type=['csv'],
                help="Select a CSV file to analyze and clean"
            )
        
        if uploaded_file is not None:
            # Load the file
            df, success, message = DataLoader.load_csv(uploaded_file)
            
            if success:
                st.session_state.original_df = df
                st.session_state.cleaned_df = df.copy()
                
                st.markdown("<div class='success-box'>✅ " + message + "</div>", unsafe_allow_html=True)
                
                # Get dataset info
                info = DataLoader.get_dataset_info(df)
                
                # Display key metrics
                st.subheader(" Dataset Overview")
                metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                
                with metric_col1:
                    st.metric("Total Rows", info['rows'])
                with metric_col2:
                    st.metric("Total Columns", info['columns'])
                with metric_col3:
                    st.metric("Memory Usage", f"{info['memory_usage']:.2f} MB")
                with metric_col4:
                    st.metric("Data Types", len(set(info['data_types'].values())))
                
                # Display column information
                st.subheader(" Column Information")
                col_info = pd.DataFrame({
                    'Column Name': list(info['data_types'].keys()),
                    'Data Type': [str(v) for v in info['data_types'].values()]
                })
                st.dataframe(col_info, use_container_width=True)
                
                # Display preview
                st.subheader("Data Preview (First 10 Rows)")
                preview = DataLoader.get_preview(df, rows=10)
                st.dataframe(preview, use_container_width=True)
                
            else:
                st.markdown("<div class='warning-box'>⚠️ " + message + "</div>", unsafe_allow_html=True)
        
        else:
            st.info("👆 Please upload a CSV file to get started!")
    
    # ============================================
    # PAGE 2: DATA ANALYSIS
    # ============================================
    elif page == " Data Analysis":
        st.header(" Data Quality Analysis")
        
        if st.session_state.original_df is None:
            st.warning("⚠️ Please upload a CSV file first from the 'Upload & Inspect' section.")
        else:
            df = st.session_state.original_df
            
            # Generate analysis report
            if st.button(" Generate Analysis Report", use_container_width=True):
                st.session_state.analysis_report = DataAnalyzer.generate_full_report(df)
            
            if st.session_state.analysis_report:
                report = st.session_state.analysis_report
                
                # Missing Values Analysis
                st.subheader("❌ Missing Values Analysis")
                missing_data = report['missing_values']
                
                if any(v['has_missing'] for v in missing_data.values()):
                    missing_df = pd.DataFrame({
                        'Column': list(missing_data.keys()),
                        'Missing Count': [v['count'] for v in missing_data.values()],
                        'Missing %': [v['percentage'] for v in missing_data.values()]
                    })
                    missing_df = missing_df[missing_df['Missing Count'] > 0]
                    st.dataframe(missing_df, use_container_width=True)
                    
                    # Highlight high-risk columns
                    high_missing = [col for col, v in missing_data.items() if v['percentage'] > 50]
                    if high_missing:
                        st.markdown(f"<div class='warning-box'>⚠️ High missing percentage: {', '.join(high_missing)}</div>", unsafe_allow_html=True)
                else:
                    st.success("✅ No missing values detected!")
                
                st.divider()
                
                # Duplicate Analysis
                st.subheader(" Duplicate Rows Analysis")
                dup_info = report['duplicates']
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Duplicates", dup_info['total_duplicates'])
                with col2:
                    st.metric("Duplicate %", f"{dup_info['percentage']:.2f}%")
                with col3:
                    if dup_info['has_duplicates']:
                        st.warning("⚠️ Duplicates Found")
                    else:
                        st.success("✅ No Duplicates")
                
                st.divider()
                
                # Data Type Analysis
                st.subheader(" Data Type Summary")
                dtype_info = report['data_types']
                type_count = {}
                for col, info in dtype_info.items():
                    dtype = info['dtype']
                    type_count[dtype] = type_count.get(dtype, 0) + 1
                
                type_df = pd.DataFrame({
                    'Data Type': list(type_count.keys()),
                    'Count': list(type_count.values())
                })
                st.dataframe(type_df, use_container_width=True)
                
                st.divider()
                
                # Whitespace Issues
                st.subheader(" Whitespace Issues")
                whitespace_issues = report['whitespace_issues']
                
                if whitespace_issues:
                    ws_df = pd.DataFrame({
                        'Column': list(whitespace_issues.keys()),
                        'Rows with Spaces': [v['count'] for v in whitespace_issues.values()],
                        'Percentage': [v['percentage'] for v in whitespace_issues.values()]
                    })
                    st.dataframe(ws_df, use_container_width=True)
                else:
                    st.success("✅ No whitespace issues detected!")
                
                st.divider()
                
                # Numeric Summary
                st.subheader(" Numeric Columns Summary")
                numeric_summary = report['numeric_summary']
                
                if numeric_summary:
                    numeric_df = pd.DataFrame(numeric_summary).T
                    st.dataframe(numeric_df, use_container_width=True)
                else:
                    st.info("No numeric columns found in the dataset.")
            
            else:
                st.info("👆 Click the button above to generate a data quality report!")
    
    # ============================================
    # PAGE 3: DATA CLEANING
    # ============================================
    elif page == " Clean Data":
        st.header(" Data Cleaning")
        
        if st.session_state.original_df is None:
            st.warning("⚠️ Please upload a CSV file first from the 'Upload & Inspect' section.")
        else:
            df = st.session_state.cleaned_df
            
            st.markdown("**Select cleaning options below and apply them to your data.**")
            st.divider()
            
            # Cleaning Options
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(" Cleaning Operations")
                
                # Missing Values Handling
                with st.expander("❌ Handle Missing Values", expanded=False):
                    strategy = st.radio(
                        "Select strategy:",
                        ["No action", "Remove rows", "Fill with Mean", "Fill with Median", "Fill with Mode", "Fill with Custom Value"],
                        key="missing_strategy"
                    )
                    
                    custom_value = None
                    if strategy == "Fill with Custom Value":
                        custom_value = st.text_input("Enter custom value:")
                    
                    if strategy != "No action" and st.button("Apply Missing Values Fix"):
                        if strategy == "Remove rows":
                            df = DataCleaner.handle_missing_values(df, 'remove')
                        elif strategy == "Fill with Mean":
                            df = DataCleaner.handle_missing_values(df, 'mean')
                        elif strategy == "Fill with Median":
                            df = DataCleaner.handle_missing_values(df, 'median')
                        elif strategy == "Fill with Mode":
                            df = DataCleaner.handle_missing_values(df, 'mode')
                        elif strategy == "Fill with Custom Value" and custom_value:
                            df = DataCleaner.handle_missing_values(df, 'custom', custom_value)
                        
                        st.session_state.cleaned_df = df
                        st.success("✅ Missing values handled!")
                
                # Duplicate Handling
                with st.expander("🔗 Remove Duplicates", expanded=False):
                    if st.button("Remove Duplicate Rows"):
                        df = DataCleaner.remove_duplicates(df)
                        st.session_state.cleaned_df = df
                        st.success("✅ Duplicates removed!")
                
                # Text Cleaning
                with st.expander(" Clean Text Columns", expanded=False):
                    text_cols = df.select_dtypes(include=['object']).columns.tolist()
                    
                    if text_cols:
                        selected_cols = st.multiselect("Select text columns:", text_cols)
                        
                        if selected_cols:
                            operations = {
                                'strip': st.checkbox("Remove leading/trailing spaces", value=True),
                                'lowercase': st.checkbox("Convert to lowercase"),
                                'uppercase': st.checkbox("Convert to uppercase"),
                                'capitalize': st.checkbox("Capitalize")
                            }
                            
                            if st.button("Apply Text Cleaning"):
                                df = DataCleaner.clean_text(df, selected_cols, operations)
                                st.session_state.cleaned_df = df
                                st.success("✅ Text cleaned!")
                    else:
                        st.info("No text columns found.")
            
            with col2:
                st.subheader(" Column Operations")
                
                # Remove Columns
                with st.expander(" Remove Columns", expanded=False):
                    cols_to_remove = st.multiselect("Select columns to remove:", df.columns)
                    
                    if cols_to_remove and st.button("Remove Selected Columns"):
                        df = DataCleaner.remove_columns(df, cols_to_remove)
                        st.session_state.cleaned_df = df
                        st.success("✅ Columns removed!")
                
                # Rename Columns
                with st.expander(" Rename Columns", expanded=False):
                    st.markdown("**Rename columns one by one:**")
                    
                    for col in df.columns:
                        new_name = st.text_input(f"Rename '{col}' to:", value=col, key=f"rename_{col}")
                        if new_name != col:
                            df = DataCleaner.rename_columns(df, {col: new_name})
                            st.session_state.cleaned_df = df
                
                # Change Data Type
                with st.expander(" Change Data Type", expanded=False):
                    col_to_convert = st.selectbox("Select column:", df.columns, key="convert_col")
                    new_type = st.selectbox("Convert to:", ["int", "float", "string", "datetime"])
                    
                    if st.button("Apply Type Conversion"):
                        df = DataCleaner.change_data_type(df, col_to_convert, new_type)
                        st.session_state.cleaned_df = df
                        st.success(f"✅ {col_to_convert} converted to {new_type}!")
            
            st.divider()
            
            # Preview cleaned data
            st.subheader(" Cleaned Data Preview")
            st.dataframe(st.session_state.cleaned_df, use_container_width=True)
    
    # ============================================
    # PAGE 4: SUMMARY & EXPORT
    # ============================================
    elif page == " Summary & Export":
        st.header(" Before vs After Summary")
        
        if st.session_state.original_df is None:
            st.warning("⚠️ Please upload a CSV file first.")
        else:
            original = st.session_state.original_df
            cleaned = st.session_state.cleaned_df
            
            # Summary metrics
            st.subheader(" Data Quality Improvements")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**Before Cleaning**")
                st.metric("Rows", len(original))
                st.metric("Columns", len(original.columns))
                missing_before = original.isnull().sum().sum()
                st.metric("Total Missing Values", missing_before)
            
            with col2:
                st.markdown("**After Cleaning**")
                st.metric("Rows", len(cleaned))
                st.metric("Columns", len(cleaned.columns))
                missing_after = cleaned.isnull().sum().sum()
                st.metric("Total Missing Values", missing_after)
            
            with col3:
                st.markdown("**Improvements**")
                rows_removed = len(original) - len(cleaned)
                st.metric("Rows Removed", rows_removed)
                missing_removed = missing_before - missing_after
                st.metric("Missing Values Fixed", missing_removed)
                
                if missing_removed > 0 or rows_removed > 0:
                    st.success("✅ Data cleaned successfully!")
            
            st.divider()
            
            # Detailed comparison
            st.subheader(" Detailed Changes")
            
            # Missing values before/after
            st.markdown("**Missing Values Comparison**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("*Before Cleaning*")
                missing_before_df = pd.DataFrame({
                    'Column': original.columns,
                    'Missing Count': original.isnull().sum(),
                    'Missing %': round((original.isnull().sum() / len(original)) * 100, 2)
                })
                st.dataframe(missing_before_df, use_container_width=True)
            
            with col2:
                st.markdown("*After Cleaning*")
                missing_after_df = pd.DataFrame({
                    'Column': cleaned.columns,
                    'Missing Count': cleaned.isnull().sum(),
                    'Missing %': round((cleaned.isnull().sum() / len(cleaned)) * 100, 2)
                })
                st.dataframe(missing_after_df, use_container_width=True)
            
            st.divider()
            
            # Export section
            st.subheader(" Export Cleaned Data")
            
            # Prepare filename
            filename = st.text_input("Set filename (without extension):", value="cleaned_data")
            
            if st.button(" Download Cleaned CSV", use_container_width=True):
                csv_data = cleaned.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label=" Download CSV",
                    data=csv_data,
                    file_name=f"{filename}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            
            # Option to download comparison report
            if st.button(" Generate Comparison Report", use_container_width=True):
                report = f"""
# Data Cleaning Report

## Summary
- **Original Rows:** {len(original)}
- **Cleaned Rows:** {len(cleaned)}
- **Rows Removed:** {len(original) - len(cleaned)}
- **Original Columns:** {len(original.columns)}
- **Cleaned Columns:** {len(cleaned.columns)}

## Missing Values
- **Before:** {missing_before}
- **After:** {missing_after}
- **Fixed:** {missing_removed}

## Data Quality Improvements
- Missing values fixed: {missing_removed}
- Duplicates potentially removed: {original.duplicated().sum()}
- Text cleaning applied: Yes
"""
                st.download_button(
                    label=" Download Report",
                    data=report,
                    file_name="cleaning_report.md",
                    mime="text/markdown",
                    use_container_width=True
                )


if __name__ == "__main__":
    main()
