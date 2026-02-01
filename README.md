# Ethiopia Financial Inclusion Forecasting System (2025–2027)

## 📌 Project Overview

This repository contains the end-to-end forecasting system developed for **Selam Analytics**. The project supports a consortium including the **National Bank of Ethiopia (NBE)**, **Mobile Money Operators (MMOs)**, and **Development Finance Institutions (DFIs)** to track and predict the trajectory of financial inclusion in Ethiopia.

### The Business Case

Ethiopia is currently navigating a radical digital financial transformation. While infrastructure and mobile money usage (Telebirr/M-Pesa) are growing exponentially, the 2024 Global Findex indicates that account ownership is lagging behind national targets. This system provides data-driven forecasts to help stakeholders decide on policy interventions and infrastructure investments for the 2025–2027 period.

---

## 🏗️ Technical Methodology

### 1. Unified Data Schema

To handle the sparse nature of financial inclusion data, we implemented a unified relational schema:

* **Observations:** Verified historical data points (e.g., Findex surveys).
* **Events:** Qualitative milestones (e.g., M-Pesa launch, Digital ID rollout).
* **Impact Links:** Defined relationships and estimated weights between events and indicators.
* **Targets:** Official goals from the National Financial Inclusion Strategy (NFIS-II).

### 2. Data Enrichment

The primary dataset was enriched with high-frequency proxy indicators to bridge the gaps between major surveys:

* **Infrastructure:** 4G/5G population coverage and mobile penetration rates.
* **Market Growth:** Registered user counts and transaction volumes from Telebirr and M-Pesa.
* **Regulatory Milestones:** Tracking the rollout of the *Fayda* Digital ID system.

---

## 📊 Key Insights from Exploratory Data Analysis (EDA)

* **The Access-Usage Divergence:** While account ownership (*Access*) grew by only 3 percentage points between 2021 and 2024, digital transaction volume (*Usage*) grew by over 100%. This indicates that existing users are becoming more active, but onboarding new users remains a challenge.
* **The P2P/ATM Crossover:** In late 2024, Peer-to-Peer (P2P) digital transfers officially surpassed physical ATM withdrawals in volume, signaling a shift toward a "digital circulation" economy.
* **Infrastructure as a Lead Indicator:** Analysis shows that 4G coverage expansion typically precedes account ownership growth by 12–18 months.
* **Target Gap:** Current trends suggest Ethiopia may miss its 70% account ownership target by 2025 unless the *Fayda* ID rollout significantly reduces onboarding friction.
* **Gender Gap Persistence:** Despite the rise of mobile money, the 20-point gender gap in financial access has remained largely unchanged since 2017.

---

## 🚀 Project Roadmap

### Phase 1: Event Impact Modeling (Current)

* Building an association matrix to quantify how specific policy changes (e.g., FX liberalization) correlate with inclusion metrics.
* Validating historical "Impact Links" against known data inflections.

### Phase 2: 2025–2027 Forecasting

* Generating three-year forecasts for **Access** (Ownership Rate) and **Usage** (Digital Payment Rate).
* Performing scenario analysis: *Baseline*, *Optimistic* (ID-driven acceleration), and *Conservative*.

### Phase 3: Dashboard Development

* Deploying an interactive Streamlit dashboard.
* Integrating "What-if" scenario sliders for policy-makers to test the impact of future regulatory decisions.

---

## 📂 Repository Structure

```bash
├── data/
│   ├── raw/                # Unified data and reference codes
│   └── processed/          # Cleaned and enriched datasets
├── notebooks/
│   ├── 01_data_enrichment.ipynb   # Task 1: Schema building
│   └── 02_eda_visualizations.ipynb # Task 2: Trend analysis
├── src/                    # Python modules for impact modeling
├── dashboard/              # Streamlit application files
└── reports/                # Project documentation and interim reports

```

---

## ⚙️ Installation & Usage

1. **Clone the Repo:** `git clone https://github.com/Nebiyou-x/ethiopia-fi-forecast.git`
2. **Install Requirements:** `pip install -r requirements.txt`
3. **Run Analysis:** Execute the Jupyter notebooks in the `notebooks/` directory to reproduce EDA findings.
4. **Launch Dashboard:** `streamlit run dashboard/app.py`
