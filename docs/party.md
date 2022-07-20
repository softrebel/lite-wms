## Pricing Overview
<div dir="rtl">
طرف حساب

</div>

### Party Relations
| Type  | Symbol  |
|---|---|
|   Zero or One |  `|o--` |
|   Exactly One |  `||--` |
|   Zero or Many |  `}o--` |
|   One or Many |  `}|--` |



### Schema
	
```plantuml
@startuml
entity Party {
    * id : number <<generated>>
    --
}
entity Person {
    * id : number <<generated>>
    --
    first name : str
    last name : str
    gender : enum(male,female)
    national code: str
    birth date : date
    description : text
}
entity Company {
    * id : number <<generated>>
    --
    * name : str
    description : text
}
entity PartyRole {
    * id : number <<generated>>
    --
    * from date : date
    thru date

}
entity RoleType {
    * id : number <<generated>>
    --
    * name : str
   
}
RoleType ||----|{ PartyRole
Party ||----|{ PartyRole
Party ||----|{ Company
Party ||----|{ Person
@enduml

```