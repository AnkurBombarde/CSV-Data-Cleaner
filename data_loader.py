import pandas as pd
import io
from typing import Tuple, Optional


class DataLoader:
    
    @staticmethod
    def load_csv(uploaded_file) -> Tuple[pd.DataFrame, bool, str]:
        try:
            if uploaded_file is None:
                return None, False, "No file uploaded"
            
            df = pd.read_csv(uploaded_file)
            
            if df.empty:
                return None, False, "CSV file is empty"
            
            return df, True, "File loaded successfully"
            
        except pd.errors.ParserError as e:
            return None, False, f"CSV parsing error: {str(e)}"
        except Exception as e:
            return None, False, f"Error loading file: {str(e)}"
    
    @staticmethod
    def get_dataset_info(df: pd.DataFrame) -> dict:
        if df is None or df.empty:
            return {}
        
        return {
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': list(df.columns),
            'data_types': df.dtypes.to_dict(),
            'memory_usage': df.memory_usage(deep=True).sum() / 1024**2  # MB
        }
    
    @staticmethod
    def get_preview(df: pd.DataFrame, rows: int = 10) -> pd.DataFrame:
        if df is None or df.empty:
            return pd.DataFrame()
        
        return df.head(rows)
