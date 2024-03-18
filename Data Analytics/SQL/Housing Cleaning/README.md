# Housing Data Cleaning SQL
Data cleaning project using SQL. The SQL script cleans and prepares housing data, demonstrating proficiency in data manipulation and database management.

This SQL project involves the meticulous cleaning of housing data and is influenced by the instructive YouTube tutorial series by [AlexTheAnalyst](https://www.youtube.com/watch?v=8rO7ztF4NtU&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF&index=20). The project uses the Nashville Housing dataset shared by [AlexTheAnalyst](https://github.com/AlexTheAnalyst/PortfolioProjects/blob/main/Nashville%20Housing%20Data%20for%20Data%20Cleaning.xlsx).

# SQL Scripts

## 1. Standardize Date Format

SELECT SaleDate, CONVERT(Date, SaleDate)

FROM Housing.dbo.DataCleaning;

UPDATE Housing.dbo.DataCleaning

SET SaleDate = CONVERT(Date, SaleDate);

## 2. Populate Property Address Data

-- Find Missing Property Addresses

SELECT *

FROM Housing.dbo.DataCleaning

WHERE PropertyAddress IS NULL

ORDER BY ParcelID;

-- Update Missing Property Addresses
UPDATE inspect

SET propertyAddress = ISNULL(inspect.PropertyAddress, change.PropertyAddress)

FROM Housing.dbo.DataCleaning inspect 

JOIN Housing.dbo.DataCleaning change
	ON inspect.Parcelid = change.Parcelid
	AND inspect.[UniqueId] <> change.[UniqueId]
 
WHERE inspect.PropertyAddress IS NULL;

## 3. Break Out Address into Individual Columns

ALTER TABLE Housing.dbo.DataCleaning

ADD PropertySplitAddress NVARCHAR(255);

UPDATE Housing.dbo.DataCleaning

SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) - 1);

ALTER TABLE Housing.dbo.DataCleaning

ADD PropertySplitCity NVARCHAR(255);

UPDATE Housing.dbo.DataCleaning

SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress));

## 4. Split Owner Address into Components

ALTER TABLE Housing.dbo.DataCleaning

ADD OwnerSplitAddress NVARCHAR(255);

UPDATE Housing.dbo.DataCleaning

SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3);

ALTER TABLE Housing.dbo.DataCleaning

ADD OwnerSplitCity NVARCHAR(255);

UPDATE Housing.dbo.DataCleaning

SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2);

ALTER TABLE Housing.dbo.DataCleaning

ADD OwnerSplitState NVARCHAR(255);

UPDATE Housing.dbo.DataCleaning

SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1);

## 5. Change Y and N to Yes and No in "Sold as Vacant" Field

UPDATE Housing.dbo.DataCleaning

SET SoldAsVacant = CASE
	WHEN SoldAsVacant = 'N' THEN 'No'
	WHEN SoldAsVacant = 'Y' THEN 'Yes'
	ELSE SoldAsVacant
	END;
 
## 6. Remove Duplicates Based on Certain Columns
WITH RowNumCTE AS (
	SELECT *,
		ROW_NUMBER() OVER (
			PARTITION BY ParcelID, PropertyAddress, SalePrice, SaleDate, LegalReference
			ORDER BY UniqueID
		) AS row_num
	FROM Housing.dbo.DataCleaning
)

DELETE

FROM RowNumCTE

WHERE Row_num > 1;

## 7. Delete Unused Columns

ALTER TABLE Housing.dbo.DataCleaning
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate;
