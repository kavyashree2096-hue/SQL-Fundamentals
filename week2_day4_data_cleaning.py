"""
Week 2 - Day 4: Data Cleaning
Sunrise Healthcare Client Project
Place the CSV files in ./data/ before running.
"""

from pathlib import Path
import pandas as pd
import numpy as np

DATA = Path("data")
DATA.mkdir(exist_ok=True)

FILES = {
    "appointments": DATA / "da_healthcare_appointments.csv",
    "satisfaction": DATA / "sunrise_patient_satisfaction.csv",
    "resources": DATA / "sunrise_resource_utilisation.csv",
}

def load_csv(path):
    if not path.exists():
        print(f"WARNING: File not found: {path}")
        return pd.DataFrame()
    df = pd.read_csv(path)
    print(f"\nLoaded {path.name}: {df.shape}")
    print(df.head())
    return df

def standardise_columns(df):
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return df

def clean_strings(df):
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("string").str.strip()
        df[col] = df[col].replace({
            "": pd.NA, "nan": pd.NA, "None": pd.NA,
            "N/A": pd.NA, "NA": pd.NA, "null": pd.NA,
            "unknown": pd.NA
        })
    return df

def clean_duplicates(df):
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"Removed duplicates: {before - len(df)}")
    return df

def convert_dates(df):
    df = df.copy()
    date_keywords = ["date", "time", "timestamp", "scheduled", "appointment"]
    for col in df.columns:
        if any(k in col for k in date_keywords):
            converted = pd.to_datetime(df[col], errors="coerce")
            # Convert only when a useful proportion is parseable.
            if converted.notna().mean() >= 0.50:
                df[col] = converted
    return df

def impute_numeric(df):
    df = df.copy()
    for col in df.select_dtypes(include=np.number).columns:
        if df[col].isna().any():
            median = df[col].median()
            df[col] = df[col].fillna(median)
    return df

def impute_categorical(df):
    df = df.copy()
    for col in df.select_dtypes(include=["object", "string", "category"]).columns:
        if df[col].isna().any():
            mode = df[col].mode(dropna=True)
            if not mode.empty:
                df[col] = df[col].fillna(mode.iloc[0])
            else:
                df[col] = df[col].fillna("Unknown")
    return df

def cap_outliers_iqr(df):
    """
    Caps numeric outliers using the IQR rule instead of deleting rows.
    This preserves the appointment/resource records.
    """
    df = df.copy()
    log = []
    for col in df.select_dtypes(include=np.number).columns:
        s = df[col].dropna()
        if len(s) < 4:
            continue
        q1, q3 = s.quantile([0.25, 0.75])
        iqr = q3 - q1
        if iqr == 0:
            continue
        lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        n = ((df[col] < lo) | (df[col] > hi)).sum()
        if n:
            df[col] = df[col].clip(lo, hi)
            log.append((col, int(n), float(lo), float(hi)))
    print("IQR outlier capping:")
    for item in log:
        print(item)
    return df

def cleaning_report(df, name):
    report = pd.DataFrame({
        "column": df.columns,
        "dtype": [str(df[c].dtype) for c in df.columns],
        "missing_count": [int(df[c].isna().sum()) for c in df.columns],
        "missing_percent": [round(df[c].isna().mean()*100, 2) for c in df.columns],
        "unique_values": [int(df[c].nunique(dropna=True)) for c in df.columns],
    })
    report.to_csv(DATA / f"{name}_data_quality_log.csv", index=False)
    print(f"\n{name} data quality report:")
    print(report.to_string(index=False))

def clean_dataset(df, name):
    if df.empty:
        return df
    df = standardise_columns(df)
    df = clean_strings(df)
    cleaning_report(df, name + "_before")
    df = clean_duplicates(df)
    df = convert_dates(df)
    df = impute_numeric(df)
    df = impute_categorical(df)
    df = cap_outliers_iqr(df)
    cleaning_report(df, name + "_after")
    out = DATA / f"cleaned_{name}.csv"
    df.to_csv(out, index=False)
    print(f"Saved: {out}")
    return df

if __name__ == "__main__":
    appointments = clean_dataset(load_csv(FILES["appointments"]), "appointments")
    satisfaction = clean_dataset(load_csv(FILES["satisfaction"]), "satisfaction")
    resources = clean_dataset(load_csv(FILES["resources"]), "resources")
    print("\nWeek 2 Day 4 cleaning completed.")
