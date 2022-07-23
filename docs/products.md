## Product Overview
<div dir="rtl">
محصول شامل اجزای زیر است:

- ویژگی
- دسته بندی
- شناسه‌های هویتی
- واحد سنجش
</div>

### Product Relations
| Type  | Symbol  |
|---|---|
|   Zero or One |  `|o--` |
|   Exactly One |  `||--` |
|   Zero or Many |  `}o--` |
|   One or Many |  `}|--` |



### Schema
	
```plantuml
@startuml
entity Product {
    * id : number <<generated>>
    --
    * name : text
    * product subtype (Good, Service)
    description : text
}


entity ProductCategoryClassification {
    * id : number <<generated>>
    --
    * Primary : bool
    * from date : date
    * thru date : date
    description : text
}

entity ProductCategory {
    * id : number <<generated>>
    --
    * product categorization (usage,industry,materials)

}

entity ProductCategoryRollup {
    * id : number <<generated>>
    --
    * made up of : id
    * part of containing: id 
}



Product ||----|{ ProductCategoryClassification
ProductCategoryClassification ||----|{ ProductCategory
ProductCategory ||----|{ ProductCategoryRollup


entity GoodIdentification {
    * id : number <<generated>>
    --
    * id value : string
}
entity IdentificationType {
    * id : number <<generated>>
    --
    * name
    description : text
}

Product ||----|{ GoodIdentification
IdentificationType ||----|{ GoodIdentification




entity ProductFeature {
    * id : number <<generated>>
    --
    * description : text
}

entity ProductFeatureCategory {
    * id : number <<generated>>
    --
    * description : text
}
entity UnitOfMeasure {
    * id : number <<generated>>
    --
    * abbreviation : text
    * description : text
}
entity ProductFeatureApplicability {
    * id : number <<generated>>
    --
    * from date : date
    * thru date : date
}


Product ||----|{ ProductFeatureApplicability
ProductFeatureApplicability ||----|{ ProductFeature
ProductFeatureCategory ||----|{ ProductFeature
UnitOfMeasure ||----|{ Product

@enduml

```


## Output


![ERD](../out/docs/products/products.png "Products ERD")