

import pandas as pd
import numpy as np
from typing import Dict, List


class DataAnalyzer:
    
    @staticmethod
    def analyze_missing_values(df: pd.DataFrame) -> Dict:
        if df is None or df.empty:
            return {}
        
        missing_dict = {}
        
        for col in df.columns:
            missing_count = df[col].isnull().sum()
            missing_percent = (missing_count / len(df)) * 100
            
            missing_dict[col] = {
                'count': missing_count,
                'percentage': round(missing_percent, 2),
                'has_missing': missing_count > 0
            }
        
        return missing_dict
    
    @staticmethod
    def analyze_duplicates(df: pd.DataFrame) -> Dict:
        if df is None or df.empty:
            return {}
        
        total_duplicates = df.duplicated().sum()
        duplicate_percent = (total_duplicates / len(df)) * 100
        
        # Find complete duplicates (all columns match)
        complete_duplicates = df.duplicated(keep=False).sum()
        
        return {
            'total_duplicates': total_duplicates,
            'percentage': round(duplicate_percent, 2),
            'complete_duplicates': complete_duplicates,
            'has_duplicates': total_duplicates > 0
        }
    
    @staticmethod
    def analyze_data_types(df: pd.DataFrame) -> Dict:
        if df is None or df.empty:
            return {}
        
        type_summary = {}
        
        for col in df.columns:
            dtype = str(df[col].dtype)
            non_null_count = df[col].notna().sum()
            
            type_summary[col] = {
                'dtype': dtype,
                'non_null': non_null_count,
                'is_numeric': pd.api.types.is_numeric_dtype(df[col]),
                'is_string': pd.api.types.is_string_dtype(df[col])
            }
        
        return type_summary
    
    @staticmethod
    def analyze_whitespace_issues(df: pd.DataFrame) -> Dict:
        if df is None or df.empty:
            return {}
        
        whitespace_dict = {}
        
        for col in df.columns:
            if pd.api.types.is_string_dtype(df[col]) or df[col].dtype == 'object':
                # Check for leading/trailing spaces
                has_spaces = df[col].astype(str).str.match(r'^\s+|\s+$', na=False).sum()
                
                if has_spaces > 0:
                    whitespace_dict[col] = {
                        'count': has_spaces,
                        'percentage': round((has_spaces / len(df)) * 100, 2)
                    }
        
        return whitespace_dict
    
    @staticmethod
    def get_numeric_summary(df: pd.DataFrame) -> Dict:
        if df is None or df.empty:
            return {}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        summary = {}
        for col in numeric_cols:
            summary[col] = {
                'mean': round(df[col].mean(), 2) if not df[col].isnull().all() else None,
                'median': round(df[col].median(), 2) if not df[col].isnull().all() else None,
                'std': round(df[col].std(), 2) if not df[col].isnull().all() else None,
                'min': round(df[col].min(), 2) if not df[col].isnull().all() else None,
                'max': round(df[col].max(), 2) if not df[col].isnull().all() else None
            }
        
        return summary
    
    @staticmethod
    def generate_full_report(df: pd.DataFrame) -> Dict:
        if df is None or df.empty:
            return {}
        
        return {
            'missing_values': DataAnalyzer.analyze_missing_values(df),
            'duplicates': DataAnalyzer.analyze_duplicates(df),
            'data_types': DataAnalyzer.analyze_data_types(df),
            'whitespace_issues': DataAnalyzer.analyze_whitespace_issues(df),
            'numeric_summary': DataAnalyzer.get_numeric_summary(df)
        }
