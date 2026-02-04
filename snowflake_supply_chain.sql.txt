-- SUPPLY CHAIN ANALYTICS PROJECT
-- Database Setup & Table Creation

-- 1. Setup the Architecture
-- We use the same Warehouse, but a new Database for clear separation
USE WAREHOUSE HOSPITAL_WH; -- (Or COMPUT_WH, whichever you use)
CREATE DATABASE IF NOT EXISTS SUPPLY_CHAIN_DB;
CREATE SCHEMA IF NOT EXISTS SUPPLY_CHAIN_DB.LOGISTICS_DATA;

-- 2. Create the Table
-- This matches the columns from the Dataco Smart Supply Chain dataset
CREATE OR REPLACE TABLE SUPPLY_CHAIN_DB.LOGISTICS_DATA.ORDERS (
    Order_Id INTEGER,
    Order_Date VARCHAR(50),      -- Loaded as text to prevent date format errors
    Shipping_Date VARCHAR(50),   -- Loaded as text
    Aging VARCHAR(50),           -- Delivery Status (Late/Advance)
    Days_For_Shipping_Real INTEGER,
    Days_For_Shipping_Scheduled INTEGER,
    Delivery_Status VARCHAR(100),
    Late_Delivery_Risk INTEGER,  -- 0 or 1
    Category_Name VARCHAR(100),
    Customer_City VARCHAR(100),
    Customer_Country VARCHAR(100),
    Customer_Segment VARCHAR(50),
    Department_Name VARCHAR(100),
    Market VARCHAR(50),
    Order_City VARCHAR(100),
    Order_Country VARCHAR(100),
    Order_Region VARCHAR(100),
    Order_State VARCHAR(100),
    Order_Status VARCHAR(50),
    Product_Name VARCHAR(255),
    Product_Price FLOAT,
    Order_Item_Quantity INTEGER,
    Sales FLOAT,
    Benefit_Per_Order FLOAT,
    Type VARCHAR(50),            -- Payment Type (Debit/Transfer)
    Shipping_Mode VARCHAR(50)    -- Standard Class/First Class
);

-- 3. Data Loading Log
-- Dataset: Dataco Smart Supply Chain for Big Data Analytics
-- Source: Kaggle
-- Load Method: Snowflake Web Interface (Upload)
-- File Format: CSV, Skip Header = 1, Encoding = ISO-8859-1