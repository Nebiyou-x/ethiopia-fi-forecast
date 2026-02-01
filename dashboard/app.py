import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# --- 1. Page Config ---
st.set_page_config(page_title="Ethiopia Financial Inclusion Dashboard", layout="wide")
st.title("🇪🇹 Ethiopia Financial Inclusion Monitor")
st.markdown("Tracking progress towards NFIS-II Targets (2025)")

# --- 2. Load Data (Using the enriched file from Task 1) ---
@st.cache_data
def load_data():
    try:
        # Load the file we created in Task 1
        df = pd.read_csv('reports/results/ethiopia_fi_enriched.csv')
        df['observation_date'] = pd.to_datetime(df['observation_date'])
        df['year'] = df['observation_date'].dt.year
        return df
    except:
        return pd.DataFrame() # Return empty if file not found

df = load_data()

if df.empty:
    st.error("Data file 'ethiopia_fi_enriched.csv' not found. Please run Task 1 first.")
    st.stop()

# --- 3. Sidebar Controls ---
st.sidebar.header("Analysis Settings")
indicators = df[df['record_type'] == 'observation']['indicator'].unique()
selected_indicator = st.sidebar.selectbox("Select Indicator", indicators, index=0)

# --- 4. Main Metric Display ---
st.subheader(f"Analysis: {selected_indicator}")

# Filter data
obs_data = df[(df['record_type'] == 'observation') & (df['indicator'] == selected_indicator)].sort_values('observation_date')
target_data = df[(df['record_type'] == 'target') & (df['indicator'] == selected_indicator)]

# KPIs
latest_val = obs_data.iloc[-1]['value_numeric'] if not obs_data.empty else 0
latest_year = obs_data.iloc[-1]['year'] if not obs_data.empty else 0
target_val = target_data.iloc[0]['value_numeric'] if not target_data.empty else None

col1, col2, col3 = st.columns(3)
col1.metric("Latest Observed Value", f"{latest_val}%" if "Rate" in selected_indicator else f"{latest_val:,.0f}", f"Year: {latest_year}")

if target_val:
    gap = latest_val - target_val
    col2.metric("Official Target (2025)", f"{target_val}%", delta=f"{gap:.1f} Gap")
else:
    col2.metric("Official Target", "Not Defined")

# --- 5. Interactive Charts ---
tab1, tab2 = st.tabs(["Historical Trend", "Forecast Model"])

with tab1:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=obs_data, x='observation_date', y='value_numeric', marker='o', ax=ax, label='Actual')
    
    # Overlay Target
    if target_val:
        target_date = target_data.iloc[0]['observation_date']
        ax.scatter([target_date], [target_val], color='red', s=100, label='Target', zorder=5)
    
    ax.set_title(f"Timeline: {selected_indicator}")
    plt.legend()
    st.pyplot(fig)

with tab2:
    st.write("Simple Linear Projection (2025-2027)")
    if len(obs_data) > 1:
        # Simple Forecast Logic
        X = obs_data[['year']]
        y = obs_data['value_numeric']
        model = LinearRegression()
        model.fit(X, y)
        
        future_years = np.array([[2025], [2026], [2027]])
        preds = model.predict(future_years)
        
        forecast_df = pd.DataFrame({'Year': [2025, 2026, 2027], 'Forecast': preds})
        st.table(forecast_df)
        
        # Plot Forecast
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        ax2.plot(obs_data['year'], obs_data['value_numeric'], marker='o', label='Historical')
        ax2.plot(forecast_df['Year'], forecast_df['Forecast'], linestyle='--', color='orange', marker='x', label='Forecast')
        ax2.set_title("Forecast Trajectory")
        ax2.legend()
        st.pyplot(fig2)
    else:
        st.warning("Insufficient data points for forecasting.")

# --- 6. Events Context ---
st.subheader("Key Contextual Events")
events = df[df['record_type'] == 'event'].sort_values('observation_date', ascending=False)
st.dataframe(events[['observation_date', 'indicator', 'category', 'source_name']].head(10))