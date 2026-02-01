# Ethiopia Financial Inclusion Forecasting System

## Project Overview

This repository contains the implementation of a **financial inclusion forecasting system for Ethiopia**, developed as part of a data science engagement for **Selam Analytics**, a financial technology consulting firm specializing in emerging markets.

The project is commissioned by a consortium of stakeholders including:
- Development finance institutions (DFIs)
- Mobile money operators
- The National Bank of Ethiopia (NBE)

Ethiopia is undergoing a rapid digital financial transformation, driven by the expansion of mobile money services (Telebirr, M-Pesa), interoperability infrastructure (EthSwitch), and national digital public goods (Fayda ID). Despite these developments, progress in financial inclusion has slowed in recent years, raising critical policy and market questions.

This project aims to **analyze, explain, and forecast Ethiopia’s financial inclusion trajectory** using the World Bank Global Findex framework.

---

## Core Research Questions

1. What factors drive financial inclusion in Ethiopia?
2. How do policies, product launches, and infrastructure investments affect inclusion outcomes?
3. Why did account ownership growth slow between 2021 and 2024 despite rapid mobile money expansion?
4. How did financial inclusion change in 2025?
5. What are plausible forecasts for financial inclusion in 2026–2027?

---

## Financial Inclusion Framework

The project follows the **World Bank Global Findex definitions**, focusing on two core dimensions:

### 1. Access — Account Ownership
> Share of adults (15+) who report having an account at a financial institution or personally using a mobile money service in the past 12 months.

### 2. Usage — Digital Payments
> Share of adults who report making or receiving digital payments (mobile money, cards, internet payments) in the past 12 months.

These indicators are forecasted using sparse survey data enriched with higher-frequency proxy and infrastructure indicators.

---

## Dataset Design

### Unified Data Schema

All data is stored in a **single unified dataset**:

```

ethiopia_fi_unified_data.csv

```

Each row represents one of four record types, identified by the `record_type` field:

| record_type | Description |
|------------|-------------|
| `observation` | Measured values from surveys, regulators, operators |
| `event` | Policies, product launches, market entries, milestones |
| `impact_link` | Modeled relationships between events and indicators |
| `target` | Official policy goals (e.g. NFIS-II targets) |

This design avoids pre-assigning events to pillars, reducing bias and making causal assumptions explicit.

### Reference Codes

Valid categorical values and schema documentation are provided in:

```

reference_codes.csv

```

---

## Task 1: Data Exploration & Enrichment

### Objectives
- Understand the unified data schema
- Assess indicator coverage and data quality
- Review existing events and modeled impact relationships
- Identify data gaps
- Enrich the dataset with additional high-value observations, events, and impact links

### Key Activities
- Schema validation and record counts by type and pillar
- Temporal coverage analysis of indicators
- Review of event catalog and impact assumptions
- Addition of:
  - Infrastructure and usage proxy indicators
  - Missing policy or product launch events
  - Explicit impact links with direction, magnitude, and lag assumptions

All enrichment decisions are documented in:

```

docs/data_enrichment_log.md

```

---

## Task 2: Exploratory Data Analysis (EDA)

### Objectives
- Understand historical patterns in financial inclusion
- Identify drivers of Access and Usage
- Explain observed stagnation in account ownership growth
- Generate hypotheses for impact modeling and forecasting

### Analysis Components
- Account ownership trends (2011–2024)
- Growth rate decomposition between Findex waves
- Digital payment adoption patterns
- Mobile money registration vs active usage gap
- Infrastructure and enabler analysis (coverage, agent networks)
- Event timeline overlays
- Correlation analysis (with explicit caveats)

### Outputs
- Visualizations of Access and Usage trajectories
- Event-annotated time series
- Data quality and coverage assessment
- A documented set of key analytical insights

---

## Key Analytical Insights (Summary)

- Rapid mobile money expansion did not translate proportionally into new account ownership.
- Digital payment usage grew faster than access, driven largely by P2P transfers.
- Gender and rural inclusion gaps remain binding constraints.
- Infrastructure is necessary but insufficient without merchant ecosystems.
- Event impacts appear lagged, supporting intervention-based modeling approaches.

---

## Methodological Approach

- Sparse outcome modeling using Global Findex survey points
- Enrichment with higher-frequency proxy indicators
- Explicit modeling of event impacts via intervention variables
- Conservative treatment of causality and uncertainty
- Scenario-based forecasting with confidence bounds

---

## Tools & Technologies

- **Python** (pandas, numpy, statsmodels, scikit-learn)
- **Visualization** (matplotlib, seaborn, plotly)
- **Notebooks** (Jupyter / Colab)
- **Dashboard (planned)**: Streamlit or Dash

Dependencies are listed in `requirements.txt`.

---

## Limitations

- Global Findex data is only available every three years
- Some indicators rely on operator-reported aggregates
- Impact links represent modeled assumptions, not causal proof
- Forecasts are subject to policy, regulatory, and market uncertainty

These limitations are explicitly documented and incorporated into modeling choices.

---

## Future Work

- Intervention-augmented regression modeling
- Forecasts for 2025–2027 with uncertainty bands
- Interactive dashboard for policymakers
- Sensitivity analysis across policy and infrastructure scenarios

Just tell me 👍
