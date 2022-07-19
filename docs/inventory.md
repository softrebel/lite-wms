## Inventory Overview
<div dir="rtl">
انبار

</div>

### Inventory Relations
| Type  | Symbol  |
|---|---|
|   Zero or One |  `|o--` |
|   Exactly One |  `||--` |
|   Zero or Many |  `}o--` |
|   One or Many |  `}|--` |



### Schema
	
```plantuml
@startuml
entity InventoryItem {
    * id : number <<generated>>
    --
    serial number : string
}
entity InventoryItemVariance {
    * id : number <<generated>>
    --
    * physical inventory date : date
    * quantity
    comment
}
entity Reason {
    * id : number <<generated>>
    --
    * comment
}
entity InventoryItemStatusType {
    * id : number <<generated>>
    --
    * name
}
entity Container {
    * id : number <<generated>>
    --
    * name
}
entity ContainerType {
    * id : number <<generated>>
    --
    * name
}
entity Facility {
    * id : number <<generated>>
    --
    * name
    * type (warehouse, plant)
}
entity Product {
    * id : number <<generated>>
    --
}



InventoryItemStatusType ||----|{ InventoryItem
InventoryItemVariance ||----|{ InventoryItem
Container ||----|{ InventoryItem
ContainerType ||----|{ Container
Facility ||----|{ InventoryItem
Facility ||----|{ Container
Product ||----|{ InventoryItem
Reason ||----|{ InventoryItemVariance
@enduml

```