## Product Overview


### Information Engineering Relations
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
    * description : text

}



Entity01 }|..|| Entity02
Entity03 }o..o| Entity04
Entity05 ||--o{ Entity06
Entity07 |o--|| Entity08
@enduml

```