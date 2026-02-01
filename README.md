
# Ethiopia Financial Inclusion Forecasting System (2025–2027)

## 📌 Project Overview

As part of a strategic engagement by **Selam Analytics**, this project develops a forecasting system to track and predict Ethiopia’s digital financial transformation. Working for a consortium including **Development Finance Institutions (DFIs)**, **Mobile Money Operators (MMOs)**, and the **National Bank of Ethiopia (NBE)**, this system models the impact of policy and infrastructure milestones on national financial inclusion.

### The Business Case

Ethiopia is at a digital tipping point. Since 2021, **Telebirr** and **M-Pesa** have collectively onboarded over 64 million users. In late 2024, the nation achieved a historic milestone: **P2P digital transfers surpassed ATM cash withdrawals** for the first time. Despite this, the 2024 Global Findex reveals that account ownership stands at **49%**, only 3 percentage points higher than in 2021. This system forecasts whether Ethiopia will bridge the gap to its **70% NFIS-II target** by 2025.

---

## 🏗️ Unified Data Schema

The project utilizes a unified relational schema to harmonize sparse survey data with high-frequency market events.

| Record Type | Description |
| --- | --- |
| **Observation** | Measured values from Findex surveys, operator reports (Ethio Telecom/Safaricom), and infrastructure data.

 |
| **Event** | Qualitative milestones such as the **FX Liberalization**, **M-Pesa Launch**, or **Fayda ID Rollout**.

 |
| **Impact Link** | Modeled relationships between events and indicators (e.g., how Telebirr launch impacts P2P counts).

 |
| **Target** | Official policy goals, including the **NFIS-II Strategy**.

 |

---

## 📊 Key Insights (EDA Phase)

1. 
**Account Ownership Plateau:** Ownership grew from 22% in 2014 to 49% in 2024. However, the recent slowdown (+3pp between 2021-2024) suggests structural bottlenecks despite mobile money expansion.


2. 
**Usage Explosion:** P2P transaction counts grew by **158% YoY** in FY2024/25, reaching 128.3 million transactions.


3. 
**Infrastructure Leap:** 4G population coverage doubled from **37.5% (2023)** to **70.8% (2025)**.


4. 
**Persistent Gender Gap:** A **20 percentage point gap** in account ownership remains between men (56%) and women (36%) as of the latest primary disaggregated data.


5. 
**The Digital ID Catalyst:** **Fayda Digital ID** enrollment reached 15 million by mid-2025, serving as a critical leading indicator for future account growth.



---

## 🚀 Forecasting Methodology

The system employs an **Event-Augmented Trend Model** to project Access and Usage for 2025–2027.

* 
**Baseline:** Linear/Log trend based on 13 years of Findex points.


* 
**Event Impact Layer:** Adjusts trends based on the association matrix of national events (e.g., the 2025 M-Pesa EthSwitch integration).


* 
**Scenario Analysis:** Provides **Optimistic** (target-aligned), **Base**, and **Pessimistic** forecasts with 95% confidence intervals.



---

## 📂 Project Structure

```bash
ethiopia-fi-forecast/
├── data/
│   ├── raw/                # ethiopia_fi_unified_data.csv & reference_codes.csv
│   └── processed/          # Enriched and analysis-ready data
├── notebooks/              # Notebooks
├── src/                    # Core modeling logic
├── dashboard/
│   └── app.py              # Streamlit Interactive Dashboard
├── reports/                # Interim and Final Submission reports
└── requirements.txt        # Dependencies (Streamlit, Pandas, Scikit-Learn, Seaborn)

---

## 💻 Getting Started

### Prerequisites
* Python 3.9+
* Git

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ethiopia-fi-forecast.git
    cd ethiopia-fi-forecast
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Dashboard:**
    ```bash
    streamlit run dashboard/app.py
    ```

---

## 📝 Learning Outcomes & Skills
* **Working with Sparse Time Series:** Forecasting with limited historical data points.
* **Event Impact Estimation:** Using comparable country evidence (e.g., Kenya M-Pesa) to weight Ethiopian market shifts.
* **Policy Analysis:** Translating technical AI forecasts into actionable policy insights for the NBE.

---


```
