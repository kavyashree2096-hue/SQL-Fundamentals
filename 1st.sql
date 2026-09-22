
USE RetailDemand;
GO
CREATE TABLE SellPrices (
    store_id VARCHAR(20),
    item_id VARCHAR(50),
    wm_yr_wk INT,
    sell_price FLOAT
);
GO
USE RetailDemand;
GO

BULK INSERT SellPrices
FROM 'C:\Users\kavya\OneDrive\Desktop\python\cleaned_sell_prices.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    TABLOCK
);
GO
SELECT TOP 10 *
FROM SellPrices;
SELECT COUNT(*) AS TotalRows
FROM SellPrices;
SELECT
    COUNT(*) AS TotalRows,
    COUNT(store_id) AS StoreIDs,
    COUNT(item_id) AS ItemIDs,
    COUNT(wm_yr_wk) AS Weeks,
    COUNT(sell_price) AS Prices
FROM SellPrices;
SELECT COUNT(*) AS TotalRows
FROM SellPrices;
USE RetailDemand;
GO

CREATE TABLE Calendar (
    date DATE,
    wm_yr_wk INT,
    weekday VARCHAR(20),
    wday INT,
    month INT,
    year INT,
    event_name_1 VARCHAR(100),
    event_type_1 VARCHAR(100),
    event_name_2 VARCHAR(100),
    event_type_2 VARCHAR(100),
    snap_CA INT,
    snap_TX INT,
    snap_WI INT
);
GO
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'calendar'
ORDER BY ORDINAL_POSITION;
SELECT TOP 10 *
FROM Calendar;
SELECT COUNT(*) AS TotalCalendarRows
FROM Calendar;
SELECT *
FROM Calendar
ORDER BY date;
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';
SELECT TOP 5 *
FROM Calendar;
select * from Calendar;
select top 10 * from SellPrices;
BULK INSERT Calendar
FROM "C:\Users\kavya\OneDrive\Desktop\python\calender_cleaned.csv"
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);
SELECT COUNT(*) FROM Calendar;
SELECT * FROM Calendar;
SELECT TOP 10 *
FROM Calendar;
SELECT COUNT(*) AS TotalRows,
       COUNT(DISTINCT store_id + '_' + item_id + '_' + CAST(wm_yr_wk AS VARCHAR) + '_' + CAST(sell_price AS VARCHAR)) AS UniqueRows
FROM Calendar;
SELECT TOP 10 *
FROM Calendar;