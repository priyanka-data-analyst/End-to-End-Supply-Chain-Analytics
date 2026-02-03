📦 Global Supply Chain Risk & Performance Dashboard

End-to-End Data Engineering & Business Intelligence Solution

📌 Project Overview

In a globalized economy, supply chain visibility is the difference between profit and loss. This project addresses the "Black Box" problem in logistics by creating a centralized data warehouse in Snowflake and an executive-level diagnostic dashboard in Power BI.

By analyzing 180,000+ transaction records from the DataCo Smart Supply Chain dataset, I identified critical failure points in premium shipping tiers and geographical regions where late deliveries were significantly impacting service level agreements (SLAs).

🏢 Business Problem Statement

The organization lacked a "Single Source of Truth" for logistics performance. Management could not identify:
Which shipping modes were consistently failing to meet promised delivery dates.
Which global regions represented the highest risk for customer dissatisfaction.
The correlation between aggressive delivery scheduling and actual delay risk.

🛠️ Tech Stack & Data Architecture

1. Data Warehousing (Snowflake)
Infrastructure: Deployed an X-SMALL virtual warehouse to optimize cost-to-performance ratio.
ETL Process: * Designed a robust schema (SUPPLY_CHAIN_DB.RAW_DATA) to handle multi-dimensional logistics data.
Resolved data integrity issues during ingestion, specifically handling ISO-8859-1 encoding for international region names.
Data Modeling: Utilized SQL to transform raw transaction logs into an analytical table (DATACO_CLEANED_TABLE) optimized for BI consumption.
2. Business Intelligence (Power BI)
Connectivity: Established a secure connection to Snowflake using Import Mode to ensure high-speed interactivity for end-users.
DAX & Analytics: Developed custom measures to calculate Late Delivery Rates and Service Level Compliance.

📊 Dashboard Key Performance Indicators (KPIs)

I developed an 8-point visualization suite to provide a 360-degree view of operations:
Risk by Shipping Mode: Uncovered that First Class and Second Class shipments actually carried higher delay risks than Standard Class.
Global Heat Map: Visualized geographical bottlenecks, pinpointing high-delay zones in Southeast Asia and South America.

Scheduled vs. Actual Scatter Plot: Proved that orders scheduled for "1-2 Day" delivery had a failure rate 3x higher than those with a 4-day window.
Customer Segment Donut: Identified that Corporate clients were experiencing the same delay rates as individual consumers, indicating a lack of B2B prioritization.
Top 10 High-Risk Countries: A focused bar chart highlighting the specific nations where the carrier network is most fragile.

💡 Strategic Business Recommendations

Based on the data, I proposed the following actions:
Carrier Renegotiation: Investigate the First Class carrier contract, as the premium price paid is not translating to premium performance.
Lead-Time Padding: Automatically add a 1-day buffer to delivery estimates for the top 5 high-risk countries identified in the dashboard.
Segment Prioritization: Implement a "Priority Lane" for Corporate Segment orders to protect high-value contracts from supply chain volatility.

🚀 Deployment Instructions

👉Prerequisites

A Snowflake Account (Trial or Enterprise).
Power BI Desktop.
Execution Steps
Snowflake Setup: Execute the setup_tables.sql script to build the database environment.
Data Ingestion: Use the Snowflake Web UI to load the cleaned_supply_chain_data.csv using the DATACO_CSV_FORMAT (Skip Header = 1).

👉BI Connection:
Open Supply_Chain_Analytics_Dashboard.pbix.

Navigate to Transform Data > Data Source Settings.
Change the Server URL to your specific Snowflake Account URL.
Enter your credentials and refresh.

📝 Author & Project Credit

Developer: Priyanka Deshpande
Data Source: DataCo Smart Supply Chain Dataset.
Project Goal: Portfolio demonstration of Data Engineering and Business Intelligence expertise.
