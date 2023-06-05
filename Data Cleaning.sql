select top (100) *
From Housing.dbo.DataCleaning

--standardize Date Format

Select SaleDate, CONVERT(Date,saleDate)
From Housing.dbo.DataCleaning

Update Housing.dbo.DataCleaning
SET SaleDate = CONVERT(Date,SaleDate)

-- Populate Property Adress data

select *
From Housing.dbo.DataCleaning
--Where PropertyAddress is null
ORDER by ParcelID

select inspect.ParcelID, inspect.PropertyAddress, change.ParcelID, change.PropertyAddress, ISNULL(inspect.PropertyAddress, change.PropertyAddress)
From Housing.dbo.DataCleaning inspect 
join Housing.dbo.DataCleaning change
	on inspect.Parcelid= change.Parcelid
	and inspect.[UniqueId] <> change.[UniqueId]
	where inspect.PropertyAddress is null 

	Update inspect
	SET propertyAddress = ISNULL(inspect.PropertyAddress, change.PropertyAddress)
	From Housing.dbo.DataCleaning inspect 
join Housing.dbo.DataCleaning change
	on inspect.Parcelid= change.Parcelid
	and inspect.[UniqueId] <> change.[UniqueId]

	-- Breaking out Adress into Individual Columns (address, City, State)

SELECT PropertyAddress
From Housing.dbo.DataCleaning

Select
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) as Address,
SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress)) as Address
From Housing.dbo.DataCleaning

ALTER TABLE Housing.dbo.DataCleaning
Add PropertySplitAddress Nvarchar(255)

Update Housing.dbo.DataCleaning
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)

ALTER TABLE Housing.dbo.DataCleaning
Add PropertySplitCity Nvarchar(255)

Update Housing.dbo.DataCleaning
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress))



Select OwnerAddress
From Housing.dbo.DataCleaning



Select
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)
,PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)
,PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
From Housing.dbo.DataCleaning

ALTER TABLE Housing.dbo.DataCleaning
Add OwnerSplitAddress Nvarchar(255)

Update Housing.dbo.DataCleaning
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)


ALTER TABLE Housing.dbo.DataCleaning
Add OwnerSplitCity Nvarchar(255)

Update Housing.dbo.DataCleaning
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)

 
ALTER TABLE Housing.dbo.DataCleaning
Add OwnerSplitState Nvarchar(255)

Update Housing.dbo.DataCleaning
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)


-- Change 1 and 0 to Yes and No In "Sold as vacant" field

Select Distinct(SoldAsVacant), COUNT(SoldAsVacant)
From Housing.dbo.DataCleaning
Group by SoldAsVacant
Order by 2



Select SoldAsVacant
, CASE When SoldAsVacant = 'N' Then 'No'
	When SoldAsVacant = 'Y' Then 'Yes'
	Else SoldAsVacant
	END as SoldAsVacant
From Housing.dbo.DataCleaning


Update Housing.dbo.DataCleaning
SET SoldAsVacant = CASE When SoldAsVacant = 'N' Then 'No'
	When SoldAsVacant = 'Y' Then 'Yes'
	Else SoldAsVacant
	END
From Housing.dbo.DataCleaning



--Remove Duplicates

with RowNumCTE AS(
Select*,
	ROW_NUMBER() Over(
	Partition By ParcelID,
				PropertyAddress,
				SalePrice,
				SaleDate,
				LegalReference
				Order By UniqueID
					) row_num

From Housing.dbo.DataCleaning
--ORDER by ParcelID
)
--Delete
Select*
From RowNumCTE
where Row_num > 1
--Order by PropertyAddress


--Delete unused Columns

Select *
From Housing.dbo.DataCleaning

Alter Table Housing.dbo.DataCleaning
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, Saledate