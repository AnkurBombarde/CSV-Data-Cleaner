"""
Data Cleaner Module
Handles data cleaning operations based on user selections
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any


class DataCleaner:
    """Performs data cleaning operations on dataframes"""
    
    @staticmethod
    def handle_missing_values(
        df: pd.DataFrame,
        strategy: str,
        fill_value: Any = None,
        columns: List[str] = None
    ) -> pd.DataFrame:
        """
        Handle missing values using specified strategy
        
        Args:
            df: Input dataframe
            strategy: 'remove', 'mean', 'median', 'mode', 'custom'
            fill_value: Value to fill (for 'custom' strategy)
            columns: Specific columns to apply strategy (None = all)
            
        Returns:
            Cleaned dataframe
        """
        df_copy = df.copy()
        
        if columns is None:
            columns = df_copy.columns[df_copy.isnull().any()].tolist()
        
        if strategy == 'remove':
            # Remove rows with missing values
            df_copy = df_copy.dropna(subset=columns)
            
        elif strategy == 'mean':
            # Fill numeric columns with mean
            for col in columns:
                if pd.api.types.is_numeric_dtype(df_copy[col]):
                    df_copy[col].fillna(df_copy[col].mean(), inplace=True)
                    
        elif strategy == 'median':
            # Fill numeric columns with median
            for col in columns:
                if pd.api.types.is_numeric_dtype(df_copy[col]):
                    df_copy[col].fillna(df_copy[col].median(), inplace=True)
                    
        elif strategy == 'mode':
            # Fill with mode (most frequent value)
            for col in columns:
                mode_val = df_copy[col].mode()
                if len(mode_val) > 0:
                    df_copy[col].fillna(mode_val[0], inplace=True)
                    
        elif strategy == 'custom':
            # Fill with custom value
            df_copy[columns] = df_copy[columns].fillna(fill_value)
        
        return df_copy
    
    @staticmethod
    def remove_duplicates(df: pd.DataFrame, subset: List[str] = None) -> pd.DataFrame:
        """
        Remove duplicate rows
        
        Args:
            df: Input dataframe
            subset: Columns to consider for duplicates (None = all)
            
        Returns:
            Dataframe with duplicates removed
        """
        if subset:
            return df.drop_duplicates(subset=subset, keep='first')
        return df.drop_duplicates(keep='first')
    
    @staticmethod
    def clean_text(
        df: pd.DataFrame,
        columns: List[str],
        operations: Dict[str, bool]
    ) -> pd.DataFrame:
        """
        Apply text cleaning operations
        
        Args:
            df: Input dataframe
            columns: Columns to clean
            operations: Dict with operations like {'lowercase': True, 'strip': True}
            
        Returns:
            Cleaned dataframe
        """
        df_copy = df.copy()
        
        for col in columns:
            if col not in df_copy.columns:
                continue
            
            # Convert to string for operations
            if operations.get('strip', False):
                df_copy[col] = df_copy[col].astype(str).str.strip()
            
            if operations.get('lowercase', False):
                df_copy[col] = df_copy[col].astype(str).str.lower()
            
            if operations.get('uppercase', False):
                df_copy[col] = df_copy[col].astype(str).str.upper()
            
            if operations.get('capitalize', False):
                df_copy[col] = df_copy[col].astype(str).str.capitalize()
        
        return df_copy
    
    @staticmethod
    def remove_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Remove specified columns
        
        Args:
            df: Input dataframe
            columns: Columns to remove
            
        Returns:
            Dataframe with columns removed
        """
        return df.drop(columns=columns, errors='ignore')
    
    @staticmethod
    def rename_columns(df: pd.DataFrame, rename_dict: Dict[str, str]) -> pd.DataFrame:
        """
        Rename columns
        
        Args:
            df: Input dataframe
            rename_dict: Dictionary of old_name: new_name
            
        Returns:
            Dataframe with renamed columns
        """
        return df.rename(columns=rename_dict)
    
    @staticmethod
    def change_data_type(
        df: pd.DataFrame,
        column: str,
        new_type: str
    ) -> pd.DataFrame:
        """
        Change data type of a column
        
        Args:
            df: Input dataframe
            column: Column to convert
            new_type: Target type ('int', 'float', 'string', 'datetime')
            
        Returns:
            Dataframe with converted column
        """
        df_copy = df.copy()
        
        try:
            if new_type == 'int':
                df_copy[column] = pd.to_numeric(df_copy[column], errors='coerce').astype('Int64')
            elif new_type == 'float':
                df_copy[column] = pd.to_numeric(df_copy[column], errors='coerce')
            elif new_type == 'string':
                df_copy[column] = df_copy[column].astype(str)
            elif new_type == 'datetime':
                df_copy[column] = pd.to_datetime(df_copy[column], errors='coerce')
        except Exception as e:
            print(f"Error converting {column} to {new_type}: {str(e)}")
        
        return df_copy
    
    @staticmethod
    def export_to_csv(df: pd.DataFrame, filename: str = 'cleaned_data.csv') -> bytes:
        """
        Export dataframe to CSV bytes
        
        Args:
            df: Input dataframe
            filename: Output filename
            
        Returns:
            CSV file as bytes
        """
        return df.to_csv(index=False).encode('utf-8')
