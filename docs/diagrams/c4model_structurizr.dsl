workspace "Tax API" "API que oferece serviços relacionados à tributação de impostos"

    !identifiers hierarchical

    model {
        u = person "User"
        ts = softwareSystem "Tax System" {
            api = container "Tax API"
            db = container "Tax API DB" {
                tags "Database"
            }
        }

        u -> ts.api "Calcula e consulta impostos" "HTTPS"
        ts.api -> ts.db "Lê de e escreve para"
    }

    views {
        systemContext ts "ContextDiagram" {
            include *
            autolayout lr
        }

        container ts "ContainerDiagram" {
            include *
            autolayout lr
        }

        styles {
            element "Element" {
                color white
            }
            element "Person" {
                background #116611
                shape person
            }
            element "Software System" {
                background #2D882D
            }
            element "Container" {
                background #55aa55
            }
            element "Database" {
                shape cylinder
            }
        }
    }

}