## Pricing Overview
<div dir="rtl">
قیمت‌گذاری

</div>

### Pricing Relations
| Type  | Symbol  |
|---|---|
|   Zero or One |  `|o--` |
|   Exactly One |  `||--` |
|   Zero or Many |  `}o--` |
|   One or Many |  `}|--` |



### Schema
	
```plantuml
@startuml
entity PriceComponent {
    * id : number <<generated>>
    --
    * from date : date
    thru date : date
    price
    percent
    comment
    type: enum(base,discount)
}
entity Product {}
entity Company {}
entity PartyType {}

Product ||----|{ PriceComponent
Company ||----|{ PriceComponent
PartyType ||----|{ PriceComponent

@enduml

```


## Output


![ERD](../out/docs/pricing/pricing.png "Pricing ERD")