USE lwmsDB
GO

IF DB_NAME() <> N'lwmsDB' SET NOEXEC ON
GO

--
-- Create table [dbo].[UnitOfMeasure]
--
PRINT (N'Create table [dbo].[UnitOfMeasure]')
GO
CREATE TABLE dbo.UnitOfMeasure (
  Id bigint IDENTITY,
  abbreviation nvarchar(20) NOT NULL,
  description text NULL,
  CONSTRAINT PK_UnitOfMeasure_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create table [dbo].[Product]
--
PRINT (N'Create table [dbo].[Product]')
GO
CREATE TABLE dbo.Product (
  Id bigint IDENTITY,
  name nvarchar(max) NOT NULL,
  subtype tinyint NOT NULL DEFAULT (0),
  description text NULL,
  isDeleted bit NOT NULL DEFAULT (0),
  unitOfMeasureId bigint NULL,
  CONSTRAINT PK_Product_id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create foreign key [FK_Product_unitOfMeasureId] on table [dbo].[Product]
--
PRINT (N'Create foreign key [FK_Product_unitOfMeasureId] on table [dbo].[Product]')
GO
ALTER TABLE dbo.Product
  ADD CONSTRAINT FK_Product_unitOfMeasureId FOREIGN KEY (unitOfMeasureId) REFERENCES dbo.UnitOfMeasure (Id)
GO

--
-- Create table [dbo].[ProductFeatureApplicability]
--
PRINT (N'Create table [dbo].[ProductFeatureApplicability]')
GO
CREATE TABLE dbo.ProductFeatureApplicability (
  Id bigint IDENTITY,
  productId bigint NOT NULL,
  fromDate date NOT NULL DEFAULT (getdate()),
  truDate date NULL,
  CONSTRAINT PK_ProductFeatureApplicability_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
GO

--
-- Create foreign key [FK_ProductFeatureApplicability_productId] on table [dbo].[ProductFeatureApplicability]
--
PRINT (N'Create foreign key [FK_ProductFeatureApplicability_productId] on table [dbo].[ProductFeatureApplicability]')
GO
ALTER TABLE dbo.ProductFeatureApplicability
  ADD CONSTRAINT FK_ProductFeatureApplicability_productId FOREIGN KEY (productId) REFERENCES dbo.Product (Id)
GO

--
-- Create table [dbo].[ProductCategoryClassification]
--
PRINT (N'Create table [dbo].[ProductCategoryClassification]')
GO
CREATE TABLE dbo.ProductCategoryClassification (
  Id bigint IDENTITY,
  productId bigint NOT NULL,
  [primary] bit NOT NULL DEFAULT (0),
  fromDate date NOT NULL DEFAULT (getdate()),
  thruDate date NULL,
  description text NULL,
  CONSTRAINT PK_ProductCategoryClassification_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create foreign key [FK_ProductCategoryClassification_productId] on table [dbo].[ProductCategoryClassification]
--
PRINT (N'Create foreign key [FK_ProductCategoryClassification_productId] on table [dbo].[ProductCategoryClassification]')
GO
ALTER TABLE dbo.ProductCategoryClassification
  ADD CONSTRAINT FK_ProductCategoryClassification_productId FOREIGN KEY (productId) REFERENCES dbo.Product (Id)
GO

--
-- Create table [dbo].[ProductCategory]
--
PRINT (N'Create table [dbo].[ProductCategory]')
GO
CREATE TABLE dbo.ProductCategory (
  Id bigint IDENTITY,
  productCategoryClassificationId bigint NOT NULL,
  categorizationId tinyint NOT NULL DEFAULT (0),
  CONSTRAINT PK_ProductCategory_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
GO

--
-- Create foreign key [FK_ProductCategory_productCategoryClassificationId] on table [dbo].[ProductCategory]
--
PRINT (N'Create foreign key [FK_ProductCategory_productCategoryClassificationId] on table [dbo].[ProductCategory]')
GO
ALTER TABLE dbo.ProductCategory
  ADD CONSTRAINT FK_ProductCategory_productCategoryClassificationId FOREIGN KEY (productCategoryClassificationId) REFERENCES dbo.ProductCategoryClassification (Id)
GO

--
-- Create table [dbo].[ProductFeatureCategory]
--
PRINT (N'Create table [dbo].[ProductFeatureCategory]')
GO
CREATE TABLE dbo.ProductFeatureCategory (
  Id bigint IDENTITY,
  description text NOT NULL,
  CONSTRAINT PK_ProductFeatureCategory_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create table [dbo].[ProductFeature]
--
PRINT (N'Create table [dbo].[ProductFeature]')
GO
CREATE TABLE dbo.ProductFeature (
  Id bigint IDENTITY,
  productFeatureCategory bigint NOT NULL,
  productFeatureApplicability bigint NOT NULL,
  description text NULL,
  CONSTRAINT PK_ProductFeature_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create foreign key [FK_ProductFeature_productFeatureApplicability] on table [dbo].[ProductFeature]
--
PRINT (N'Create foreign key [FK_ProductFeature_productFeatureApplicability] on table [dbo].[ProductFeature]')
GO
ALTER TABLE dbo.ProductFeature
  ADD CONSTRAINT FK_ProductFeature_productFeatureApplicability FOREIGN KEY (productFeatureApplicability) REFERENCES dbo.ProductFeatureApplicability (Id)
GO

--
-- Create foreign key [FK_ProductFeature_productFeatureCategory] on table [dbo].[ProductFeature]
--
PRINT (N'Create foreign key [FK_ProductFeature_productFeatureCategory] on table [dbo].[ProductFeature]')
GO
ALTER TABLE dbo.ProductFeature
  ADD CONSTRAINT FK_ProductFeature_productFeatureCategory FOREIGN KEY (productFeatureCategory) REFERENCES dbo.ProductFeatureCategory (Id)
GO

--
-- Create table [dbo].[InventoryItemStatusType]
--
PRINT (N'Create table [dbo].[InventoryItemStatusType]')
GO
CREATE TABLE dbo.InventoryItemStatusType (
  Id bigint IDENTITY,
  name nvarchar(50) NOT NULL,
  isDeleted bit NOT NULL DEFAULT (0),
  CONSTRAINT PK_InventoryItemStatusType_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
GO

--
-- Create table [dbo].[IdentificationType]
--
PRINT (N'Create table [dbo].[IdentificationType]')
GO
CREATE TABLE dbo.IdentificationType (
  Id bigint IDENTITY,
  name nvarchar(25) NOT NULL,
  description text NULL,
  CONSTRAINT PK_IdentificationType_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create table [dbo].[GoodIdentification]
--
PRINT (N'Create table [dbo].[GoodIdentification]')
GO
CREATE TABLE dbo.GoodIdentification (
  id bigint IDENTITY,
  productId bigint NOT NULL,
  identificationTypeId bigint NOT NULL,
  value nvarchar(max) NOT NULL,
  CONSTRAINT PK_GoodIdentification_id PRIMARY KEY CLUSTERED (id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create foreign key [FK_GoodIdentification_identificationTypeId] on table [dbo].[GoodIdentification]
--
PRINT (N'Create foreign key [FK_GoodIdentification_identificationTypeId] on table [dbo].[GoodIdentification]')
GO
ALTER TABLE dbo.GoodIdentification
  ADD CONSTRAINT FK_GoodIdentification_identificationTypeId FOREIGN KEY (identificationTypeId) REFERENCES dbo.IdentificationType (Id)
GO

--
-- Create foreign key [FK_GoodIdentification_productId] on table [dbo].[GoodIdentification]
--
PRINT (N'Create foreign key [FK_GoodIdentification_productId] on table [dbo].[GoodIdentification]')
GO
ALTER TABLE dbo.GoodIdentification
  ADD CONSTRAINT FK_GoodIdentification_productId FOREIGN KEY (productId) REFERENCES dbo.Product (Id)
GO

--
-- Create table [dbo].[Facility]
--
PRINT (N'Create table [dbo].[Facility]')
GO
CREATE TABLE dbo.Facility (
  Id bigint IDENTITY,
  name nvarchar(100) NOT NULL,
  type tinyint NOT NULL DEFAULT (0),
  isDeleted bit NOT NULL DEFAULT (0),
  CONSTRAINT PK_Facility_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
GO

--
-- Create table [dbo].[Container]
--
PRINT (N'Create table [dbo].[Container]')
GO
CREATE TABLE dbo.Container (
  Id bigint IDENTITY,
  name nvarchar(100) NOT NULL,
  facilityId bigint NOT NULL,
  isDeleted bit NOT NULL DEFAULT (0),
  CONSTRAINT PK_Container_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
GO

--
-- Create foreign key [FK_Container_facilityId] on table [dbo].[Container]
--
PRINT (N'Create foreign key [FK_Container_facilityId] on table [dbo].[Container]')
GO
ALTER TABLE dbo.Container
  ADD CONSTRAINT FK_Container_facilityId FOREIGN KEY (facilityId) REFERENCES dbo.Facility (Id)
GO

--
-- Create table [dbo].[Party]
--
PRINT (N'Create table [dbo].[Party]')
GO
CREATE TABLE dbo.Party (
  Id bigint IDENTITY,
  typeId tinyint NULL,
  isDeleted bit NOT NULL DEFAULT (0),
  CONSTRAINT PK_Party_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
GO

--
-- Create table [dbo].[Person]
--
PRINT (N'Create table [dbo].[Person]')
GO
CREATE TABLE dbo.Person (
  Id bigint IDENTITY,
  partyId bigint NOT NULL,
  firstName nvarchar(50) NULL,
  lastName nvarchar(50) NULL,
  nationalCode nvarchar(10) NULL,
  isDeleted bit NOT NULL DEFAULT (0),
  CONSTRAINT PK_Person_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
GO

--
-- Create foreign key [FK_Person_partyId] on table [dbo].[Person]
--
PRINT (N'Create foreign key [FK_Person_partyId] on table [dbo].[Person]')
GO
ALTER TABLE dbo.Person
  ADD CONSTRAINT FK_Person_partyId FOREIGN KEY (partyId) REFERENCES dbo.Party (Id)
GO

--
-- Create table [dbo].[InventoryItem]
--
PRINT (N'Create table [dbo].[InventoryItem]')
GO
CREATE TABLE dbo.InventoryItem (
  Id bigint IDENTITY,
  facilityId bigint NOT NULL,
  isDeleted bit NOT NULL DEFAULT (0),
  partyId bigint NOT NULL,
  fromDate date NOT NULL DEFAULT (getdate()),
  CONSTRAINT PK_InventoryItem_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
GO

--
-- Create foreign key [FK_InventoryItem_facilityId] on table [dbo].[InventoryItem]
--
PRINT (N'Create foreign key [FK_InventoryItem_facilityId] on table [dbo].[InventoryItem]')
GO
ALTER TABLE dbo.InventoryItem
  ADD CONSTRAINT FK_InventoryItem_facilityId FOREIGN KEY (facilityId) REFERENCES dbo.Facility (Id)
GO

--
-- Create foreign key [FK_InventoryItem_partyId] on table [dbo].[InventoryItem]
--
PRINT (N'Create foreign key [FK_InventoryItem_partyId] on table [dbo].[InventoryItem]')
GO
ALTER TABLE dbo.InventoryItem
  ADD CONSTRAINT FK_InventoryItem_partyId FOREIGN KEY (partyId) REFERENCES dbo.Party (Id)
GO

--
-- Create table [dbo].[InventoryItemDetail]
--
PRINT (N'Create table [dbo].[InventoryItemDetail]')
GO
CREATE TABLE dbo.InventoryItemDetail (
  Id bigint IDENTITY,
  serialNumber nvarchar(max) NULL,
  quantity bigint NOT NULL,
  inventoryItemId bigint NOT NULL,
  containerId bigint NULL,
  productId bigint NOT NULL,
  inventoryItemStatusTypeId bigint NULL,
  CONSTRAINT PK_InventoryItemDetail_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create foreign key [FK_InventoryItemDetail_containerId] on table [dbo].[InventoryItemDetail]
--
PRINT (N'Create foreign key [FK_InventoryItemDetail_containerId] on table [dbo].[InventoryItemDetail]')
GO
ALTER TABLE dbo.InventoryItemDetail
  ADD CONSTRAINT FK_InventoryItemDetail_containerId FOREIGN KEY (containerId) REFERENCES dbo.Container (Id)
GO

--
-- Create foreign key [FK_InventoryItemDetail_inventoryItemId] on table [dbo].[InventoryItemDetail]
--
PRINT (N'Create foreign key [FK_InventoryItemDetail_inventoryItemId] on table [dbo].[InventoryItemDetail]')
GO
ALTER TABLE dbo.InventoryItemDetail
  ADD CONSTRAINT FK_InventoryItemDetail_inventoryItemId FOREIGN KEY (inventoryItemId) REFERENCES dbo.InventoryItem (Id)
GO

--
-- Create foreign key [FK_InventoryItemDetail_inventoryItemStatusTypeId] on table [dbo].[InventoryItemDetail]
--
PRINT (N'Create foreign key [FK_InventoryItemDetail_inventoryItemStatusTypeId] on table [dbo].[InventoryItemDetail]')
GO
ALTER TABLE dbo.InventoryItemDetail
  ADD CONSTRAINT FK_InventoryItemDetail_inventoryItemStatusTypeId FOREIGN KEY (inventoryItemStatusTypeId) REFERENCES dbo.InventoryItemStatusType (Id)
GO

--
-- Create foreign key [FK_InventoryItemDetail_productId] on table [dbo].[InventoryItemDetail]
--
PRINT (N'Create foreign key [FK_InventoryItemDetail_productId] on table [dbo].[InventoryItemDetail]')
GO
ALTER TABLE dbo.InventoryItemDetail
  ADD CONSTRAINT FK_InventoryItemDetail_productId FOREIGN KEY (productId) REFERENCES dbo.Product (Id)
GO

--
-- Create table [dbo].[Company]
--
PRINT (N'Create table [dbo].[Company]')
GO
CREATE TABLE dbo.Company (
  Id bigint IDENTITY,
  partyId bigint NOT NULL,
  title nvarchar(max) NOT NULL,
  nationalCode nvarchar(50) NULL,
  isDeleted bit NOT NULL DEFAULT (0),
  CONSTRAINT PK_Company_Id PRIMARY KEY CLUSTERED (Id)
)
ON [PRIMARY]
TEXTIMAGE_ON [PRIMARY]
GO

--
-- Create foreign key [FK_Company_partyId] on table [dbo].[Company]
--
PRINT (N'Create foreign key [FK_Company_partyId] on table [dbo].[Company]')
GO
ALTER TABLE dbo.Company
  ADD CONSTRAINT FK_Company_partyId FOREIGN KEY (partyId) REFERENCES dbo.Party (Id)
GO