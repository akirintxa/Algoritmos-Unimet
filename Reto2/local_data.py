from country import *
from state import *
from measurement import *


countries = [
    {
        "location_name": "Argentina",
        "location_capital": "Buenos Aires",
        "population": 45000000,
        "area": 2780000,
        "currency": "Peso Argentino",
        "main_language": "Spanish"
    },
    {
        "location_name": "Bolivia",
        "location_capital": "Sucre / La Paz",
        "population": 11500000,
        "area": 1100000,
        "currency": "Boliviano",
        "main_language": "Spanish"
    },
    {
        "location_name": "Brazil",
        "location_capital": "Brasilia",
        "population": 213000000,
        "area": 8515767,
        "currency": "Real Brasileño",
        "main_language": "Portuguese"
    },
    {
        "location_name": "Canada",
        "location_capital": "Ottawa",
        "population": 38000000,
        "area": 9984670,
        "currency": "Dolar Canadiense",
        "main_language": "English"
    },
    {
        "location_name": "Chile",
        "location_capital": "Santiago",
        "population": 19000000,
        "area": 756096,
        "currency": "Peso Chileno",
        "main_language": "Spanish"
    },
    {
        "location_name": "Colombia",
        "location_capital": "Bogotá",
        "population": 50000000,
        "area": 1141748,
        "currency": "Peso Colombiano",
        "main_language": "Spanish"
    },
    {
        "location_name": "Mexico",
        "location_capital": "Ciudad de México",
        "population": 129000000,
        "area": 1964375,
        "currency": "Peso Mexicano",
        "main_language": "Spanish"
    },
    {
        "location_name": "Peru",
        "location_capital": "Lima",
        "population": 33000000,
        "area": 1285216,
        "currency": "Sol Peruano",
        "main_language": "Spanish"
    },
    {
        "location_name": "United States",
        "location_capital": "Washington D.C.",
        "population": 332000000,
        "area": 9833520,
        "currency": "Dolar",
        "main_language": "English"
    },
    {
        "location_name": "Venezuela",
        "location_capital": "Caracas",
        "population": 28000000,
        "area": 916445,
        "currency": "Bolívar Soberano",
        "main_language": "Spanish"
    }
]

states = [
    {
        "location_name": "Argentina",
        "location_states": [
            {
                "state_name": "Buenos Aires",
                "state_capital": "La Plata",
                "population": 17541141,
                "area": 307571
            },
            {
                "state_name": "CABA (Ciudad Autónoma de Buenos Aires)",
                "state_capital": "Buenos Aires",
                "population": 3075646,
                "area": 203
            },
            {
                "state_name": "Catamarca",
                "state_capital": "San Fernando del Valle de Catamarca",
                "population": 415438,
                "area": 102602
            },
            {
                "state_name": "Chaco",
                "state_capital": "Resistencia",
                "population": 1189446,
                "area": 99633
            },
            {
                "state_name": "Chubut",
                "state_capital": "Rawson",
                "population": 637913,
                "area": 224686
            },
            {
                "state_name": "Corrientes",
                "state_capital": "Corrientes",
                "population": 1135795,
                "area": 88199
            },
            {
                "state_name": "Córdoba",
                "state_capital": "Córdoba",
                "population": 3760450,
                "area": 165321
            },
            {
                "state_name": "Entre Ríos",
                "state_capital": "Paraná",
                "population": 1385961,
                "area": 78781
            },
            {
                "state_name": "Formosa",
                "state_capital": "Formosa",
                "population": 605193,
                "area": 72066
            },
            {
                "state_name": "Jujuy",
                "state_capital": "San Salvador de Jujuy",
                "population": 779212,
                "area": 53219
            },
            {
                "state_name": "La Pampa",
                "state_capital": "Santa Rosa",
                "population": 358428,
                "area": 143440
            },
            {
                "state_name": "La Rioja",
                "state_capital": "La Rioja",
                "population": 333642,
                "area": 89680
            },
            {
                "state_name": "Mendoza",
                "state_capital": "Mendoza",
                "population": 2142820,
                "area": 148827
            },
            {
                "state_name": "Misiones",
                "state_capital": "Posadas",
                "population": 1274996,
                "area": 29801
            },
            {
                "state_name": "Neuquén",
                "state_capital": "Neuquén",
                "population": 711774,
                "area": 94078
            },
            {
                "state_name": "Río Negro",
                "state_capital": "Viedma",
                "population": 747610,
                "area": 203013
            },
            {
                "state_name": "Salta",
                "state_capital": "Salta",
                "population": 1553279,
                "area": 155488
            },
            {
                "state_name": "San Juan",
                "state_capital": "San Juan",
                "population": 861737,
                "area": 89651
            },
            {
                "state_name": "San Luis",
                "state_capital": "San Luis",
                "population": 508328,
                "area": 76748
            },
            {
                "state_name": "Santa Cruz",
                "state_capital": "Río Gallegos",
                "population": 373468,
                "area": 243943
            },
            {
                "state_name": "Santa Fe",
                "state_capital": "Santa Fe",
                "population": 358428,
                "area": 133007
            },
            {
                "state_name": "Santiago del Estero",
                "state_capital": "Santiago del Estero",
                "population": 988245,
                "area": 136351
            },
            {
                "state_name": "Tierra del Fuego, Antártida e Islas del Atlántico Sur",
                "state_capital": "Ushuaia",
                "population": 173432,
                "area": 210587
            },
            {
                "state_name": "Tucumán",
                "state_capital": "San Miguel de Tucumán",
                "population": 1794471,
                "area": 22524
            }
        ]
    },
    {
        "location_name": "Bolivia",
        "location_states": [
            {
                "state_name": "Beni",
                "state_capital": "Trinidad",
                "population": 421626,
                "area": 213564
            },
            {
                "state_name": "Chuquisaca",
                "state_capital": "Sucre",
                "population": 660293,
                "area": 51125
            },
            {
                "state_name": "Cochabamba",
                "state_capital": "Cochabamba",
                "population": 2045741,
                "area": 55633
            },
            {
                "state_name": "La Paz",
                "state_capital": "La Paz",
                "population": 2890146,
                "area": 133985
            },
            {
                "state_name": "Oruro",
                "state_capital": "Oruro",
                "population": 494178,
                "area": 53430
            },
            {
                "state_name": "Pando",
                "state_capital": "Cobija",
                "population": 149432,
                "area": 63822
            },
            {
                "state_name": "Potosí",
                "state_capital": "Potosí",
                "population": 887590,
                "area": 118218
            },
            {
                "state_name": "Santa Cruz",
                "state_capital": "Santa Cruz de la Sierra",
                "population": 3333892,
                "area": 370621
            },
            {
                "state_name": "Tarija",
                "state_capital": "Tarija",
                "population": 613401,
                "area": 37623
            }
        ]
    },
    {
        "location_name": "Brazil",
        "location_states": [
            {
                "state_name": "Acre",
                "state_capital": "Rio Branco",
                "population": 894470,
                "area": 164123
            },
            {
                "state_name": "Alagoas",
                "state_capital": "Maceió",
                "population": 3351543,
                "area": 27843
            },
            {
                "state_name": "Amapá",
                "state_capital": "Macapá",
                "population": 861773,
                "area": 142828
            },
            {
                "state_name": "Amazonas",
                "state_capital": "Manaus",
                "population": 4207714,
                "area": 1559159
            },
            {
                "state_name": "Bahia",
                "state_capital": "Salvador",
                "population": 14930634,
                "area": 564733
            },
            {
                "state_name": "Ceará",
                "state_capital": "Fortaleza",
                "population": 9187103,
                "area": 148920
            },
            {
                "state_name": "Distrito Federal",
                "state_capital": "Brasília",
                "population": 3055149,
                "area": 5760
            },
            {
                "state_name": "Espírito Santo",
                "state_capital": "Vitória",
                "population": 4212408,
                "area": 46095
            },
            {
                "state_name": "Goiás",
                "state_capital": "Goiânia",
                "population": 7142074,
                "area": 340086
            },
            {
                "state_name": "Maranhão",
                "state_capital": "São Luís",
                "population": 7315088,
                "area": 331937
            },
            {
                "state_name": "Mato Grosso",
                "state_capital": "Cuiabá",
                "population": 3526220,
                "area": 903357
            },
            {
                "state_name": "Mato Grosso do Sul",
                "state_capital": "Campo Grande",
                "population": 2809394,
                "area": 357145
            },
            {
                "state_name": "Minas Gerais",
                "state_capital": "Belo Horizonte",
                "population": 212559417,
                "area": 586522
            },
            {
                "state_name": "Paraná",
                "state_capital": "Curitiba",
                "population": 11516840,
                "area": 199307
            },
            {
                "state_name": "Paraíba",
                "state_capital": "João Pessoa",
                "population": 4097843,
                "area": 56585
            },
            {
                "state_name": "Pará",
                "state_capital": "Belém",
                "population": 8690745,
                "area": 1247689
            },
            {
                "state_name": "Pernambuco",
                "state_capital": "Recife",
                "population": 9616621,
                "area": 98311
            },
            {
                "state_name": "Piauí",
                "state_capital": "Teresina",
                "population": 3281480,
                "area": 251577
            },
            {
                "state_name": "Rio Grande do Norte",
                "state_capital": "Natal",
                "population": 3534165,
                "area": 52811
            },
            {
                "state_name": "Rio Grande do Sul",
                "state_capital": "Porto Alegre",
                "population": 11422973,
                "area": 281748
            },
            {
                "state_name": "Rio de Janeiro",
                "state_capital": "Rio de Janeiro",
                "population": 17366189,
                "area": 43780
            },
            {
                "state_name": "Rondônia",
                "state_capital": "Porto Velho",
                "population": 1796460,
                "area": 237590
            },
            {
                "state_name": "Roraima",
                "state_capital": "Boa Vista",
                "population": 652713,
                "area": 224299
            },
            {
                "state_name": "Santa Catarina",
                "state_capital": "Florianópolis",
                "population": 7279639,
                "area": 95736
            },
            {
                "state_name": "Sergipe",
                "state_capital": "Aracaju",
                "population": 2318822,
                "area": 21915
            },
            {
                "state_name": "São Paulo",
                "state_capital": "São Paulo",
                "population": 46289333,
                "area": 248209
            },
            {
                "state_name": "Tocantins",
                "state_capital": "Palmas",
                "population": 1607375,
                "area": 277620
            }
        ]
    },
    {
        "location_name": "Canada",
        "location_states": [
            {
                "state_name": "Alberta",
                "state_capital": "Edmonton",
                "population": 4439430,
                "area": 661848
            },
            {
                "state_name": "British Columbia",
                "state_capital": "Victoria",
                "population": 5110917,
                "area": 944735
            },
            {
                "state_name": "Manitoba",
                "state_capital": "Winnipeg",
                "population": 1379584,
                "area": 647797
            },
            {
                "state_name": "New Brunswick",
                "state_capital": "Fredericton",
                "population": 781315,
                "area": 71450
            },
            {
                "state_name": "Newfoundland and Labrador",
                "state_capital": "St. John's",
                "population": 520437,
                "area": 373872
            },
            {
                "state_name": "Northwest Territories",
                "state_capital": "Yellowknife",
                "population": 44904,
                "area": 1183085
            },
            {
                "state_name": "Nova Scotia",
                "state_capital": "Halifax",
                "population": 979115,
                "area": 55184
            },
            {
                "state_name": "Nunavut",
                "state_capital": "Iqaluit",
                "population": 39285,
                "area": 1936113
            },
            {
                "state_name": "Ontario",
                "state_capital": "Toronto",
                "population": 14755234,
                "area": 1076395
            },
            {
                "state_name": "Prince Edward Island",
                "state_capital": "Charlottetown",
                "population": 159625,
                "area": 5660
            },
            {
                "state_name": "Quebec",
                "state_capital": "Quebec City",
                "population": 8575779,
                "area": 1542056
            },
            {
                "state_name": "Saskatchewan",
                "state_capital": "Regina",
                "population": 1181666,
                "area": 651036
            },
            {
                "state_name": "Yukon",
                "state_capital": "Whitehorse",
                "population": 42176,
                "area": 482443
            }
        ]
    },
    {
        "location_name": "Chile",
        "location_states": [
            {
                "state_name": "Antofagasta",
                "state_capital": "Antofagasta",
                "population": 607534,
                "area": 126049
            },
            {
                "state_name": "Araucanía",
                "state_capital": "Temuco",
                "population": 1014343,
                "area": 31974
            },
            {
                "state_name": "Arica y Parinacota",
                "state_capital": "Arica",
                "population": 252110,
                "area": 16873
            },
            {
                "state_name": "Atacama",
                "state_capital": "Copiapó",
                "population": 286168,
                "area": 75176
            },
            {
                "state_name": "Aysén del General Carlos Ibáñez del Campo",
                "state_capital": "Coyhaique",
                "population": 107297,
                "area": 108494
            },
            {
                "state_name": "Biobío",
                "state_capital": "Concepción",
                "population": 2186529,
                "area": 37195
            },
            {
                "state_name": "Coquimbo",
                "state_capital": "La Serena",
                "population": 790239,
                "area": 40579
            },
            {
                "state_name": "Libertador General Bernardo O'Higgins",
                "state_capital": "Rancagua",
                "population": 993978,
                "area": 16378
            },
            {
                "state_name": "Los Lagos",
                "state_capital": "Puerto Montt",
                "population": 842293,
                "area": 48583
            },
            {
                "state_name": "Los Ríos",
                "state_capital": "Valdivia",
                "population": 405835,
                "area": 18429
            },
            {
                "state_name": "Magallanes y de la Antártica Chilena",
                "state_capital": "Punta Arenas",
                "population": 177892,
                "area": 132291
            },
            {
                "state_name": "Maule",
                "state_capital": "Talca",
                "population": 1258360,
                "area": 30318
            },
            {
                "state_name": "Metropolitana de Santiago",
                "state_capital": "Santiago",
                "population": 7770073,
                "area": 15403
            },
            {
                "state_name": "Tarapacá",
                "state_capital": "Iquique",
                "population": 330558,
                "area": 42249
            },
            {
                "state_name": "Valparaíso",
                "state_capital": "Valparaíso",
                "population": 1903908,
                "area": 16203
            },
            {
                "state_name": "Ñuble",
                "state_capital": "Chillán",
                "population": 480609,
                "area": 13206
            }
        ]
    },
    {
        "location_name": "Colombia",
        "location_states": [
            {
                "state_name": "Amazonas",
                "state_capital": "Leticia",
                "population": 78812,
                "area": 109665
            },
            {
                "state_name": "Antioquia",
                "state_capital": "Medellín",
                "population": 6584490,
                "area": 63612
            },
            {
                "state_name": "Arauca",
                "state_capital": "Arauca",
                "population": 280109,
                "area": 23818
            },
            {
                "state_name": "Atlántico",
                "state_capital": "Barranquilla",
                "population": 2381788,
                "area": 30177
            },
            {
                "state_name": "Bolívar",
                "state_capital": "Cartagena",
                "population": 2257693,
                "area": 26197
            },
            {
                "state_name": "Boyacá",
                "state_capital": "Tunja",
                "population": 1258291,
                "area": 23099
            },
            {
                "state_name": "Caldas",
                "state_capital": "Manizales",
                "population": 1001416,
                "area": 7889
            },
            {
                "state_name": "Caquetá",
                "state_capital": "Florencia",
                "population": 512438,
                "area": 88965
            },
            {
                "state_name": "Casanare",
                "state_capital": "Yopal",
                "population": 408148,
                "area": 44648
            },
            {
                "state_name": "Cauca",
                "state_capital": "Popayán",
                "population": 1452992,
                "area": 29174
            },
            {
                "state_name": "Cesar",
                "state_capital": "Valledupar",
                "population": 1223095,
                "area": 22912
            },
            {
                "state_name": "Chocó",
                "state_capital": "Quibdó",
                "population": 530808,
                "area": 46202
            },
            {
                "state_name": "Cundinamarca",
                "state_capital": "Bogotá D.C.",
                "population": 8963984,
                "area": 24211
            },
            {
                "state_name": "Córdoba",
                "state_capital": "Montería",
                "population": 1843102,
                "area": 25020
            },
            {
                "state_name": "Guainía",
                "state_capital": "Puerto Inírida",
                "population": 43242,
                "area": 72304
            },
            {
                "state_name": "Guaviare",
                "state_capital": "San José del Guaviare",
                "population": 110939,
                "area": 53485
            },
            {
                "state_name": "Huila",
                "state_capital": "Neiva",
                "population": 1305822,
                "area": 19890
            },
            {
                "state_name": "La Guajira",
                "state_capital": "Riohacha",
                "population": 1024993,
                "area": 20849
            },
            {
                "state_name": "Magdalena",
                "state_capital": "Santa Marta",
                "population": 1361951,
                "area": 23812
            },
            {
                "state_name": "Meta",
                "state_capital": "Villavicencio",
                "population": 1099459,
                "area": 85635
            },
            {
                "state_name": "Nariño",
                "state_capital": "Pasto",
                "population": 1796268,
                "area": 33356
            },
            {
                "state_name": "Norte de Santander",
                "state_capital": "Cúcuta",
                "population": 1446631,
                "area": 21654
            },
            {
                "state_name": "Putumayo",
                "state_capital": "Mocoa",
                "population": 358140,
                "area": 24525
            },
            {
                "state_name": "Quindío",
                "state_capital": "Armenia",
                "population": 562011,
                "area": 18453
            },
            {
                "state_name": "Risaralda",
                "state_capital": "Pereira",
                "population": 1003939,
                "area": 4153
            },
            {
                "state_name": "San Andrés y Providencia",
                "state_capital": "San Andrés",
                "population": 84032,
                "area": 5258
            },
            {
                "state_name": "Santander",
                "state_capital": "Bucaramanga",
                "population": 2099185,
                "area": 30536
            },
            {
                "state_name": "Sucre",
                "state_capital": "Sincelejo",
                "population": 884522,
                "area": 10646
            },
            {
                "state_name": "Tolima",
                "state_capital": "Ibagué",
                "population": 1443361,
                "area": 23580
            },
            {
                "state_name": "Valle del Cauca",
                "state_capital": "Cali",
                "population": 5029196,
                "area": 22398
            },
            {
                "state_name": "Vaupés",
                "state_capital": "Mitú",
                "population": 46788,
                "area": 54126
            },
            {
                "state_name": "Vichada",
                "state_capital": "Puerto Carreño",
                "population": 79829,
                "area": 100242
            }
        ]
    },
    {
        "location_name": "Mexico",
        "location_states": [
            {
                "state_name": "Aguascalientes",
                "state_capital": "Aguascalientes",
                "population": 1434635,
                "area": 5616
            },
            {
                "state_name": "Baja California",
                "state_capital": "Mexicali",
                "population": 3769020,
                "area": 71450
            },
            {
                "state_name": "Baja California Sur",
                "state_capital": "La Paz",
                "population": 798447,
                "area": 73960
            },
            {
                "state_name": "Campeche",
                "state_capital": "San Francisco de Campeche",
                "population": 928363,
                "area": 57975
            },
            {
                "state_name": "Chiapas",
                "state_capital": "Tuxtla Gutiérrez",
                "population": 5543828,
                "area": 73978
            },
            {
                "state_name": "Chihuahua",
                "state_capital": "Chihuahua",
                "population": 3801487,
                "area": 247460
            },
            {
                "state_name": "Coahuila",
                "state_capital": "Saltillo",
                "population": 3146771,
                "area": 151571
            },
            {
                "state_name": "Colima",
                "state_capital": "Colima",
                "population": 731391,
                "area": 5450
            },
            {
                "state_name": "Durango",
                "state_capital": "Durango",
                "population": 1868996,
                "area": 123181
            },
            {
                "state_name": "Guanajuato",
                "state_capital": "Guanajuato",
                "population": 6228175,
                "area": 30608
            },
            {
                "state_name": "Guerrero",
                "state_capital": "Chilpancingo",
                "population": 3533251,
                "area": 63763
            },
            {
                "state_name": "Hidalgo",
                "state_capital": "Pachuca",
                "population": 3082841,
                "area": 20849
            },
            {
                "state_name": "Jalisco",
                "state_capital": "Guadalajara",
                "population": 8348151,
                "area": 78534
            },
            {
                "state_name": "Mexico City (Ciudad de México)",
                "state_capital": "Mexico City",
                "population": 9209944,
                "area": 1485
            },
            {
                "state_name": "Mexico State (Estado de México)",
                "state_capital": "Toluca",
                "population": 17427790,
                "area": 22233
            },
            {
                "state_name": "Michoacán",
                "state_capital": "Morelia",
                "population": 4825401,
                "area": 58595
            },
            {
                "state_name": "Morelos",
                "state_capital": "Cuernavaca",
                "population": 2044058,
                "area": 4898
            },
            {
                "state_name": "Nayarit",
                "state_capital": "Tepic",
                "population": 1380011,
                "area": 27842
            },
            {
                "state_name": "Nuevo León",
                "state_capital": "Monterrey",
                "population": 5610153,
                "area": 64282
            },
            {
                "state_name": "Oaxaca",
                "state_capital": "Oaxaca",
                "population": 4132148,
                "area": 93753
            },
            {
                "state_name": "Puebla",
                "state_capital": "Puebla",
                "population": 6583278,
                "area": 34255
            },
            {
                "state_name": "Querétaro",
                "state_capital": "Santiago de Querétaro",
                "population": 2279637,
                "area": 11647
            },
            {
                "state_name": "Quintana Roo",
                "state_capital": "Chetumal",
                "population": 1857985,
                "area": 44709
            },
            {
                "state_name": "San Luis Potosí",
                "state_capital": "San Luis Potosí",
                "population": 2822255,
                "area": 60981
            },
            {
                "state_name": "Sinaloa",
                "state_capital": "Culiacán",
                "population": 3156674,
                "area": 57336
            },
            {
                "state_name": "Sonora",
                "state_capital": "Hermosillo",
                "population": 3074745,
                "area": 179503
            },
            {
                "state_name": "Tabasco",
                "state_capital": "Villahermosa",
                "population": 2487167,
                "area": 24740
            },
            {
                "state_name": "Tamaulipas",
                "state_capital": "Ciudad Victoria",
                "population": 3650602,
                "area": 80902
            },
            {
                "state_name": "Tlaxcala",
                "state_capital": "Tlaxcala",
                "population": 1376086,
                "area": 3915
            },
            {
                "state_name": "Veracruz",
                "state_capital": "Xalapa",
                "population": 8112505,
                "area": 71241
            },
            {
                "state_name": "Yucatán",
                "state_capital": "Mérida",
                "population": 2320895,
                "area": 39633
            },
            {
                "state_name": "Zacatecas",
                "state_capital": "Zacatecas",
                "population": 1644822,
                "area": 75338
            }
        ]
    },
    {
        "location_name": "Peru",
        "location_states": [
            {
                "state_name": "Amazonas",
                "state_capital": "Chachapoyas",
                "population": 426806,
                "area": 39249
            },
            {
                "state_name": "Apurímac",
                "state_capital": "Abancay",
                "population": 430736,
                "area": 20723
            },
            {
                "state_name": "Arequipa",
                "state_capital": "Arequipa",
                "population": 1484898,
                "area": 63185
            },
            {
                "state_name": "Ayacucho",
                "state_capital": "Ayacucho",
                "population": 651556,
                "area": 43815
            },
            {
                "state_name": "Cajamarca",
                "state_capital": "Cajamarca",
                "population": 1446516,
                "area": 33324
            },
            {
                "state_name": "Callao",
                "state_capital": "Callao",
                "population": 994494,
                "area": 146
            },
            {
                "state_name": "Cusco",
                "state_capital": "Cusco",
                "population": 1385568,
                "area": 71348
            },
            {
                "state_name": "Huancavelica",
                "state_capital": "Huancavelica",
                "population": 454797,
                "area": 22125
            },
            {
                "state_name": "Huánuco",
                "state_capital": "Huánuco",
                "population": 811866,
                "area": 36888
            },
            {
                "state_name": "Ica",
                "state_capital": "Ica",
                "population": 830993,
                "area": 21375
            },
            {
                "state_name": "Junín",
                "state_capital": "Huancayo",
                "population": 1469536,
                "area": 44197
            },
            {
                "state_name": "La Libertad",
                "state_capital": "Trujillo",
                "population": 1943753,
                "area": 25390
            },
            {
                "state_name": "Lambayeque",
                "state_capital": "Chiclayo",
                "population": 1261567,
                "area": 14364
            },
            {
                "state_name": "Lima",
                "state_capital": "Lima",
                "population": 10099265,
                "area": 2672
            },
            {
                "state_name": "Loreto",
                "state_capital": "Iquitos",
                "population": 1001327,
                "area": 368852
            },
            {
                "state_name": "Madre de Dios",
                "state_capital": "Puerto Maldonado",
                "population": 173811,
                "area": 85338
            },
            {
                "state_name": "Moquegua",
                "state_capital": "Moquegua",
                "population": 196930,
                "area": 15476
            },
            {
                "state_name": "Pasco",
                "state_capital": "Cerro de Pasco",
                "population": 254065,
                "area": 25188
            },
            {
                "state_name": "Piura",
                "state_capital": "Piura",
                "population": 2015545,
                "area": 35856
            },
            {
                "state_name": "Puno",
                "state_capital": "Puno",
                "population": 1309575,
                "area": 71582
            },
            {
                "state_name": "San Martín",
                "state_capital": "Moyobamba",
                "population": 860957,
                "area": 51210
            },
            {
                "state_name": "Tacna",
                "state_capital": "Tacna",
                "population": 386292,
                "area": 16076
            },
            {
                "state_name": "Tumbes",
                "state_capital": "Tumbes",
                "population": 252508,
                "area": 4662
            },
            {
                "state_name": "Ucayali",
                "state_capital": "Pucallpa",
                "population": 520798,
                "area": 102411
            },
            {
                "state_name": "Áncash",
                "state_capital": "Huaraz",
                "population": 1145908,
                "area": 35917
            }
        ]
    },
    {
        "location_name": "United States",
        "location_states": [
            {
                "state_name": "Alabama",
                "state_capital": "Montgomery",
                "population": 5024279,
                "area": 135767
            },
            {
                "state_name": "Alaska",
                "state_capital": "Juneau",
                "population": 735720,
                "area": 1723337
            },
            {
                "state_name": "Arizona",
                "state_capital": "Phoenix",
                "population": 7151502,
                "area": 295234
            },
            {
                "state_name": "Arkansas",
                "state_capital": "Little Rock",
                "population": 3011524,
                "area": 137732
            },
            {
                "state_name": "California",
                "state_capital": "Sacramento",
                "population": 39538223,
                "area": 423968
            },
            {
                "state_name": "Colorado",
                "state_capital": "Denver",
                "population": 5773714,
                "area": 269601
            },
            {
                "state_name": "Connecticut",
                "state_capital": "Hartford",
                "population": 3605944,
                "area": 14357
            },
            {
                "state_name": "Delaware",
                "state_capital": "Dover",
                "population": 989948,
                "area": 6446
            },
            {
                "state_name": "Florida",
                "state_capital": "Tallahassee",
                "population": 21538187,
                "area": 170312
            },
            {
                "state_name": "Georgia",
                "state_capital": "Atlanta",
                "population": 10711908,
                "area": 153910
            },
            {
                "state_name": "Hawaii",
                "state_capital": "Honolulu",
                "population": 1455271,
                "area": 28314
            },
            {
                "state_name": "Idaho",
                "state_capital": "Boise",
                "population": 1839106,
                "area": 216443
            },
            {
                "state_name": "Illinois",
                "state_capital": "Springfield",
                "population": 12812508,
                "area": 149997
            },
            {
                "state_name": "Indiana",
                "state_capital": "Indianapolis",
                "population": 6785528,
                "area": 94327
            },
            {
                "state_name": "Iowa",
                "state_capital": "Des Moines",
                "population": 3190369,
                "area": 145746
            },
            {
                "state_name": "Kansas",
                "state_capital": "Topeka",
                "population": 2937880,
                "area": 213099
            },
            {
                "state_name": "Kentucky",
                "state_capital": "Frankfort",
                "population": 4505836,
                "area": 104656
            },
            {
                "state_name": "Louisiana",
                "state_capital": "Baton Rouge",
                "population": 4648794,
                "area": 135659
            },
            {
                "state_name": "Maine",
                "state_capital": "Augusta",
                "population": 1362359,
                "area": 91634
            },
            {
                "state_name": "Maryland",
                "state_capital": "Annapolis",
                "population": 6177224,
                "area": 32131
            },
            {
                "state_name": "Massachusetts",
                "state_capital": "Boston",
                "population": 7029917,
                "area": 27336
            },
            {
                "state_name": "Michigan",
                "state_capital": "Lansing",
                "population": 10077331,
                "area": 250487
            },
            {
                "state_name": "Minnesota",
                "state_capital": "St. Paul",
                "population": 5700671,
                "area": 225163
            },
            {
                "state_name": "Mississippi",
                "state_capital": "Jackson",
                "population": 2961279,
                "area": 125438
            },
            {
                "state_name": "Missouri",
                "state_capital": "Jefferson City",
                "population": 6154913,
                "area": 180540
            },
            {
                "state_name": "Montana",
                "state_capital": "Helena",
                "population": 1084259,
                "area": 380831
            },
            {
                "state_name": "Nebraska",
                "state_capital": "Lincoln",
                "population": 1961504,
                "area": 200330
            },
            {
                "state_name": "Nevada",
                "state_capital": "Carson City",
                "population": 3104614,
                "area": 286380
            },
            {
                "state_name": "New Hampshire",
                "state_capital": "Concord",
                "population": 1377529,
                "area": 24214
            },
            {
                "state_name": "New Jersey",
                "state_capital": "Trenton",
                "population": 9288994,
                "area": 22592
            },
            {
                "state_name": "New Mexico",
                "state_capital": "Santa Fe",
                "population": 2117522,
                "area": 314917
            },
            {
                "state_name": "New York",
                "state_capital": "Albany",
                "population": 20201249,
                "area": 141297
            },
            {
                "state_name": "North Carolina",
                "state_capital": "Raleigh",
                "population": 10439388,
                "area": 139391
            },
            {
                "state_name": "North Dakota",
                "state_capital": "Bismarck",
                "population": 779094,
                "area": 183107
            },
            {
                "state_name": "Ohio",
                "state_capital": "Columbus",
                "population": 11799448,
                "area": 116098
            },
            {
                "state_name": "Oklahoma",
                "state_capital": "Oklahoma City",
                "population": 3959353,
                "area": 181037
            },
            {
                "state_name": "Oregon",
                "state_capital": "Salem",
                "population": 4301089,
                "area": 254800
            },
            {
                "state_name": "Pennsylvania",
                "state_capital": "Harrisburg",
                "population": 12820878,
                "area": 119280
            },
            {
                "state_name": "Rhode Island",
                "state_capital": "Providence",
                "population": 1097379,
                "area": 4001
            },
            {
                "state_name": "South Carolina",
                "state_capital": "Columbia",
                "population": 5118425,
                "area": 82931
            },
            {
                "state_name": "South Dakota",
                "state_capital": "Pierre",
                "population": 886667,
                "area": 199730
            },
            {
                "state_name": "Tennessee",
                "state_capital": "Nashville",
                "population": 6910840,
                "area": 109153
            },
            {
                "state_name": "Texas",
                "state_capital": "Austin",
                "population": 29145505,
                "area": 695662
            },
            {
                "state_name": "Utah",
                "state_capital": "Salt Lake City",
                "population": 3271616,
                "area": 219882
            },
            {
                "state_name": "Vermont",
                "state_capital": "Montpelier",
                "population": 643077,
                "area": 24906
            },
            {
                "state_name": "Virginia",
                "state_capital": "Richmond",
                "population": 8626207,
                "area": 110787
            },
            {
                "state_name": "Washington",
                "state_capital": "Olympia",
                "population": 7693612,
                "area": 184661
            },
            {
                "state_name": "West Virginia",
                "state_capital": "Charleston",
                "population": 1792147,
                "area": 62755
            },
            {
                "state_name": "Wisconsin",
                "state_capital": "Madison",
                "population": 5893634,
                "area": 169634
            },
            {
                "state_name": "Wyoming",
                "state_capital": "Cheyenne",
                "population": 576851,
                "area": 253335
            }
        ]
    },
    {
        "location_name": "Venezuela",
        "location_states": [
            {
                "state_name": "Amazonas",
                "state_capital": "Puerto Ayacucho",
                "population": 173183,
                "area": 176899
            },
            {
                "state_name": "Anzoátegui",
                "state_capital": "Barcelona",
                "population": 1509895,
                "area": 43800
            },
            {
                "state_name": "Apure",
                "state_capital": "San Fernando de Apure",
                "population": 545723,
                "area": 76600
            },
            {
                "state_name": "Aragua",
                "state_capital": "Maracay",
                "population": 1943901,
                "area": 7012
            },
            {
                "state_name": "Barinas",
                "state_capital": "Barinas",
                "population": 916918,
                "area": 35384
            },
            {
                "state_name": "Bolívar",
                "state_capital": "Ciudad Bolívar",
                "population": 1507133,
                "area": 238000
            },
            {
                "state_name": "Carabobo",
                "state_capital": "Valencia",
                "population": 2503790,
                "area": 4480
            },
            {
                "state_name": "Cojedes",
                "state_capital": "San Carlos",
                "population": 323165,
                "area": 14985
            },
            {
                "state_name": "Delta Amacuro",
                "state_capital": "Tucupita",
                "population": 170477,
                "area": 40380
            },
            {
                "state_name": "Distrito Capital",
                "state_capital": "Caracas",
                "population": 2851377,
                "area": 433
            },
            {
                "state_name": "Falcón",
                "state_capital": "Coro",
                "population": 1015996,
                "area": 24800
            },
            {
                "state_name": "Guárico",
                "state_capital": "San Juan de Los Morros",
                "population": 903132,
                "area": 64931
            },
            {
                "state_name": "Lara",
                "state_capital": "Barquisimeto",
                "population": 1988405,
                "area": 19800
            },
            {
                "state_name": "Miranda",
                "state_capital": "Los Teques",
                "population": 3491765,
                "area": 7500
            },
            {
                "state_name": "Monagas",
                "state_capital": "Maturín",
                "population": 1038701,
                "area": 28800
            },
            {
                "state_name": "Mérida",
                "state_capital": "Mérida",
                "population": 974925,
                "area": 11200
            },
            {
                "state_name": "Nueva Esparta",
                "state_capital": "La Asunción",
                "population": 491610,
                "area": 1150
            },
            {
                "state_name": "Portuguesa",
                "state_capital": "Guanare",
                "population": 1104992,
                "area": 15520
            },
            {
                "state_name": "Sucre",
                "state_capital": "Cumaná",
                "population": 892076,
                "area": 11200
            },
            {
                "state_name": "Trujillo",
                "state_capital": "Trujillo",
                "population": 686367,
                "area": 7400
            },
            {
                "state_name": "Táchira",
                "state_capital": "San Cristóbal",
                "population": 1412900,
                "area": 11600
            },
            {
                "state_name": "Vargas",
                "state_capital": "La Guaira",
                "population": 399244,
                "area": 108
            },
            {
                "state_name": "Yaracuy",
                "state_capital": "San Felipe",
                "population": 700362,
                "area": 7100
            },
            {
                "state_name": "Zulia",
                "state_capital": "Maracaibo",
                "population": 4143595,
                "area": 63600
            }
        ]
    }
]

weather = [
    {"location_name": "Argentina", "location_measurements": [
        {"temperature": 25.2, "humidity": 0.50,
            "wind_speed": 9, "date": "2023/07/23"},
        {"temperature": 25.1, "humidity": 0.50,
            "wind_speed": 20, "date": "2023/07/17"},
        {"temperature": 26.6, "humidity": 0.59,
            "wind_speed": 16, "date": "2023/07/22"},
        {"temperature": 26.5, "humidity": 0.58,
            "wind_speed": 11, "date": "2023/07/18"},
        {"temperature": 26.9, "humidity": 0.47,
            "wind_speed": 12, "date": "2023/07/22"},
        {"temperature": 26.5, "humidity": 0.54,
            "wind_speed": 9, "date": "2023/07/20"},
        {"temperature": 26.0, "humidity": 0.53,
            "wind_speed": 14, "date": "2023/07/19"},
        {"temperature": 25.0, "humidity": 0.62,
            "wind_speed": 18, "date": "2023/07/23"},
        {"temperature": 26.5, "humidity": 0.51,
            "wind_speed": 9, "date": "2023/07/20"},
        {"temperature": 25.0, "humidity": 0.46,
            "wind_speed": 17, "date": "2023/07/22"},
        {"temperature": 25.2, "humidity": 0.51,
            "wind_speed": 16, "date": "2023/07/17"},
        {"temperature": 26.9, "humidity": 0.58,
            "wind_speed": 15, "date": "2023/07/21"},
        {"temperature": 25.6, "humidity": 0.57,
            "wind_speed": 8, "date": "2023/07/22"},
        {"temperature": 26.3, "humidity": 0.51,
            "wind_speed": 5, "date": "2023/07/23"},
        {"temperature": 25.2, "humidity": 0.52,
            "wind_speed": 8, "date": "2023/07/17"},
        {"temperature": 25.2, "humidity": 0.50,
            "wind_speed": 9, "date": "2023/07/21"},
        {"temperature": 26.7, "humidity": 0.63,
            "wind_speed": 10, "date": "2023/07/20"},
        {"temperature": 25.6, "humidity": 0.49,
            "wind_speed": 18, "date": "2023/07/19"},
        {"temperature": 26.2, "humidity": 0.50,
            "wind_speed": 19, "date": "2023/07/19"},
        {"temperature": 27.0, "humidity": 0.56,
            "wind_speed": 14, "date": "2023/07/23"},
        {"temperature": 25.7, "humidity": 0.60,
            "wind_speed": 18, "date": "2023/07/19"},
        {"temperature": 25.9, "humidity": 0.52,
            "wind_speed": 7, "date": "2023/07/19"},
        {"temperature": 25.1, "humidity": 0.64,
            "wind_speed": 10, "date": "2023/07/22"},
        {"temperature": 25.7, "humidity": 0.61,
            "wind_speed": 18, "date": "2023/07/19"},
        {"temperature": 26.4, "humidity": 0.65,
            "wind_speed": 20, "date": "2023/07/22"},
        {"temperature": 26.1, "humidity": 0.59,
            "wind_speed": 5, "date": "2023/07/21"},
        {"temperature": 26.4, "humidity": 0.61,
            "wind_speed": 12, "date": "2023/07/22"},
        {"temperature": 26.3, "humidity": 0.65,
            "wind_speed": 14, "date": "2023/07/22"},
        {"temperature": 26.3, "humidity": 0.61,
            "wind_speed": 15, "date": "2023/07/23"},
        {"temperature": 25.9, "humidity": 0.60,
            "wind_speed": 8, "date": "2023/07/22"}
    ]
    },
    {"location_name": "Bolivia", "location_measurements": [
        {"temperature": 27.0, "humidity": 0.51,
            "wind_speed": 7, "date": "2023/07/21"},
        {"temperature": 26.8, "humidity": 0.65,
            "wind_speed": 7, "date": "2023/07/21"},
        {"temperature": 25.9, "humidity": 0.47,
            "wind_speed": 14, "date": "2023/07/21"},
        {"temperature": 25.1, "humidity": 0.53,
            "wind_speed": 6, "date": "2023/07/19"},
        {"temperature": 27.0, "humidity": 0.52,
            "wind_speed": 8, "date": "2023/07/20"},
        {"temperature": 26.9, "humidity": 0.52,
            "wind_speed": 7, "date": "2023/07/18"},
        {"temperature": 25.1, "humidity": 0.46,
            "wind_speed": 16, "date": "2023/07/17"},
        {"temperature": 25.2, "humidity": 0.55,
            "wind_speed": 8, "date": "2023/07/23"},
        {"temperature": 26.8, "humidity": 0.45,
            "wind_speed": 8, "date": "2023/07/20"},
        {"temperature": 25.8, "humidity": 0.48,
            "wind_speed": 19, "date": "2023/07/21"},
        {"temperature": 26.9, "humidity": 0.57,
            "wind_speed": 20, "date": "2023/07/20"},
        {"temperature": 25.9, "humidity": 0.59,
            "wind_speed": 15, "date": "2023/07/22"},
        {"temperature": 26.9, "humidity": 0.57,
            "wind_speed": 13, "date": "2023/07/20"},
        {"temperature": 26.5, "humidity": 0.65,
            "wind_speed": 16, "date": "2023/07/21"},
        {"temperature": 26.2, "humidity": 0.61,
            "wind_speed": 12, "date": "2023/07/17"},
        {"temperature": 26.1, "humidity": 0.54,
            "wind_speed": 20, "date": "2023/07/22"},
        {"temperature": 26.0, "humidity": 0.57,
            "wind_speed": 5, "date": "2023/07/17"},
        {"temperature": 26.6, "humidity": 0.49,
            "wind_speed": 5, "date": "2023/07/23"},
        {"temperature": 26.7, "humidity": 0.57,
            "wind_speed": 16, "date": "2023/07/20"},
        {"temperature": 25.8, "humidity": 0.60,
            "wind_speed": 17, "date": "2023/07/18"},
        {"temperature": 26.8, "humidity": 0.56,
            "wind_speed": 19, "date": "2023/07/18"},
        {"temperature": 27.0, "humidity": 0.63,
            "wind_speed": 16, "date": "2023/07/23"},
        {"temperature": 26.2, "humidity": 0.47,
            "wind_speed": 13, "date": "2023/07/17"},
        {"temperature": 26.6, "humidity": 0.49,
            "wind_speed": 18, "date": "2023/07/19"},
        {"temperature": 26.2, "humidity": 0.55,
            "wind_speed": 14, "date": "2023/07/23"},
        {"temperature": 26.4, "humidity": 0.62,
            "wind_speed": 20, "date": "2023/07/23"},
        {"temperature": 26.3, "humidity": 0.63,
            "wind_speed": 13, "date": "2023/07/21"},
        {"temperature": 25.6, "humidity": 0.59,
            "wind_speed": 16, "date": "2023/07/23"},
        {"temperature": 26.5, "humidity": 0.59,
            "wind_speed": 11, "date": "2023/07/19"},
        {"temperature": 25.7, "humidity": 0.48,
            "wind_speed": 17, "date": "2023/07/18"}
    ]
    },
    {"location_name": "Brazil", "location_measurements": [
        {"temperature": 25.1, "humidity": 0.51,
            "wind_speed": 14, "date": "2023/07/23"},
        {"temperature": 26.5, "humidity": 0.52,
            "wind_speed": 6, "date": "2023/07/23"},
        {"temperature": 25.5, "humidity": 0.54,
            "wind_speed": 18, "date": "2023/07/19"},
        {"temperature": 26.8, "humidity": 0.54,
            "wind_speed": 13, "date": "2023/07/18"},
        {"temperature": 26.7, "humidity": 0.55,
            "wind_speed": 7, "date": "2023/07/19"},
        {"temperature": 26.4, "humidity": 0.52,
            "wind_speed": 6, "date": "2023/07/19"},
        {"temperature": 26.6, "humidity": 0.56,
            "wind_speed": 6, "date": "2023/07/22"},
        {"temperature": 25.6, "humidity": 0.46,
            "wind_speed": 13, "date": "2023/07/20"},
        {"temperature": 26.3, "humidity": 0.45,
            "wind_speed": 6, "date": "2023/07/20"},
        {"temperature": 25.2, "humidity": 0.57,
            "wind_speed": 7, "date": "2023/07/20"},
        {"temperature": 26.3, "humidity": 0.58,
            "wind_speed": 14, "date": "2023/07/23"},
        {"temperature": 26.9, "humidity": 0.63,
            "wind_speed": 8, "date": "2023/07/23"},
        {"temperature": 25.6, "humidity": 0.52,
            "wind_speed": 15, "date": "2023/07/21"},
        {"temperature": 26.0, "humidity": 0.54,
            "wind_speed": 14, "date": "2023/07/21"},
        {"temperature": 26.9, "humidity": 0.46,
            "wind_speed": 14, "date": "2023/07/20"},
        {"temperature": 25.6, "humidity": 0.59,
            "wind_speed": 13, "date": "2023/07/21"},
        {"temperature": 26.8, "humidity": 0.45,
            "wind_speed": 8, "date": "2023/07/18"},
        {"temperature": 26.2, "humidity": 0.46,
            "wind_speed": 6, "date": "2023/07/22"},
        {"temperature": 25.5, "humidity": 0.55,
            "wind_speed": 13, "date": "2023/07/23"},
        {"temperature": 26.3, "humidity": 0.65,
            "wind_speed": 20, "date": "2023/07/21"},
        {"temperature": 26.7, "humidity": 0.52,
            "wind_speed": 19, "date": "2023/07/21"},
        {"temperature": 25.5, "humidity": 0.49,
            "wind_speed": 17, "date": "2023/07/23"},
        {"temperature": 25.0, "humidity": 0.62,
            "wind_speed": 15, "date": "2023/07/18"},
        {"temperature": 26.1, "humidity": 0.50,
            "wind_speed": 15, "date": "2023/07/19"},
        {"temperature": 26.7, "humidity": 0.64,
            "wind_speed": 5, "date": "2023/07/18"},
        {"temperature": 26.8, "humidity": 0.54,
            "wind_speed": 9, "date": "2023/07/17"},
        {"temperature": 26.8, "humidity": 0.56,
            "wind_speed": 15, "date": "2023/07/20"},
        {"temperature": 25.1, "humidity": 0.64,
            "wind_speed": 8, "date": "2023/07/17"},
        {"temperature": 25.8, "humidity": 0.56,
            "wind_speed": 5, "date": "2023/07/20"},
        {"temperature": 25.8, "humidity": 0.50,
            "wind_speed": 17, "date": "2023/07/18"}
    ]
    },
    {"location_name": "Canada", "location_measurements": [
        {"temperature": 25.7, "humidity": 0.59,
            "wind_speed": 5, "date": "2023/07/19"},
        {"temperature": 25.1, "humidity": 0.50,
            "wind_speed": 12, "date": "2023/07/21"},
        {"temperature": 25.9, "humidity": 0.52,
            "wind_speed": 13, "date": "2023/07/22"},
        {"temperature": 25.6, "humidity": 0.49,
            "wind_speed": 11, "date": "2023/07/19"},
        {"temperature": 25.8, "humidity": 0.63,
            "wind_speed": 7, "date": "2023/07/18"},
        {"temperature": 26.2, "humidity": 0.49,
            "wind_speed": 19, "date": "2023/07/17"},
        {"temperature": 26.5, "humidity": 0.55,
            "wind_speed": 9, "date": "2023/07/17"},
        {"temperature": 25.6, "humidity": 0.57,
            "wind_speed": 9, "date": "2023/07/23"},
        {"temperature": 25.5, "humidity": 0.65,
            "wind_speed": 12, "date": "2023/07/21"},
        {"temperature": 25.8, "humidity": 0.51,
            "wind_speed": 7, "date": "2023/07/19"},
        {"temperature": 25.1, "humidity": 0.46,
            "wind_speed": 13, "date": "2023/07/19"},
        {"temperature": 26.9, "humidity": 0.61,
            "wind_speed": 18, "date": "2023/07/20"},
        {"temperature": 25.7, "humidity": 0.50,
            "wind_speed": 17, "date": "2023/07/22"},
        {"temperature": 26.4, "humidity": 0.55,
            "wind_speed": 8, "date": "2023/07/19"},
        {"temperature": 26.1, "humidity": 0.52,
            "wind_speed": 14, "date": "2023/07/20"},
        {"temperature": 26.5, "humidity": 0.61,
            "wind_speed": 20, "date": "2023/07/21"},
        {"temperature": 25.7, "humidity": 0.65,
            "wind_speed": 11, "date": "2023/07/18"},
        {"temperature": 27.0, "humidity": 0.65,
            "wind_speed": 16, "date": "2023/07/19"},
        {"temperature": 26.8, "humidity": 0.52,
            "wind_speed": 13, "date": "2023/07/21"},
        {"temperature": 25.4, "humidity": 0.61,
            "wind_speed": 6, "date": "2023/07/20"},
        {"temperature": 25.8, "humidity": 0.60,
            "wind_speed": 16, "date": "2023/07/19"},
        {"temperature": 25.7, "humidity": 0.64,
            "wind_speed": 16, "date": "2023/07/19"},
        {"temperature": 26.8, "humidity": 0.54,
            "wind_speed": 14, "date": "2023/07/18"},
        {"temperature": 25.2, "humidity": 0.46,
            "wind_speed": 10, "date": "2023/07/23"},
        {"temperature": 26.9, "humidity": 0.57,
            "wind_speed": 5, "date": "2023/07/20"},
        {"temperature": 26.2, "humidity": 0.62,
            "wind_speed": 8, "date": "2023/07/21"},
        {"temperature": 26.2, "humidity": 0.46,
            "wind_speed": 18, "date": "2023/07/21"},
        {"temperature": 25.5, "humidity": 0.52,
            "wind_speed": 14, "date": "2023/07/17"},
        {"temperature": 26.3, "humidity": 0.46,
            "wind_speed": 20, "date": "2023/07/17"},
        {"temperature": 25.9, "humidity": 0.58,
            "wind_speed": 11, "date": "2023/07/17"}
    ]
    },
    {"location_name": "Chile", "location_measurements": [
        {"temperature": 27.0, "humidity": 0.50,
            "wind_speed": 10, "date": "2023/07/21"},
        {"temperature": 25.7, "humidity": 0.45,
            "wind_speed": 8, "date": "2023/07/17"},
        {"temperature": 26.9, "humidity": 0.57,
            "wind_speed": 11, "date": "2023/07/23"},
        {"temperature": 26.0, "humidity": 0.65,
            "wind_speed": 12, "date": "2023/07/17"},
        {"temperature": 26.4, "humidity": 0.64,
            "wind_speed": 20, "date": "2023/07/21"},
        {"temperature": 26.6, "humidity": 0.60,
            "wind_speed": 7, "date": "2023/07/18"},
        {"temperature": 25.8, "humidity": 0.46,
            "wind_speed": 19, "date": "2023/07/19"},
        {"temperature": 25.3, "humidity": 0.46,
            "wind_speed": 12, "date": "2023/07/21"},
        {"temperature": 25.7, "humidity": 0.61,
            "wind_speed": 19, "date": "2023/07/23"},
        {"temperature": 25.1, "humidity": 0.49,
            "wind_speed": 15, "date": "2023/07/18"},
        {"temperature": 26.4, "humidity": 0.46,
            "wind_speed": 9, "date": "2023/07/20"},
        {"temperature": 25.8, "humidity": 0.55,
            "wind_speed": 13, "date": "2023/07/20"},
        {"temperature": 26.6, "humidity": 0.58,
            "wind_speed": 8, "date": "2023/07/22"},
        {"temperature": 26.5, "humidity": 0.61,
            "wind_speed": 5, "date": "2023/07/17"},
        {"temperature": 26.5, "humidity": 0.52,
            "wind_speed": 9, "date": "2023/07/18"},
        {"temperature": 25.8, "humidity": 0.59,
            "wind_speed": 14, "date": "2023/07/22"},
        {"temperature": 25.6, "humidity": 0.51,
            "wind_speed": 9, "date": "2023/07/20"},
        {"temperature": 25.0, "humidity": 0.51,
            "wind_speed": 17, "date": "2023/07/21"},
        {"temperature": 26.3, "humidity": 0.54,
            "wind_speed": 17, "date": "2023/07/17"},
        {"temperature": 25.7, "humidity": 0.49,
            "wind_speed": 10, "date": "2023/07/18"},
        {"temperature": 26.7, "humidity": 0.57,
            "wind_speed": 15, "date": "2023/07/23"},
        {"temperature": 25.5, "humidity": 0.62,
            "wind_speed": 11, "date": "2023/07/20"},
        {"temperature": 25.1, "humidity": 0.47,
            "wind_speed": 10, "date": "2023/07/18"},
        {"temperature": 25.1, "humidity": 0.45,
            "wind_speed": 16, "date": "2023/07/20"},
        {"temperature": 25.6, "humidity": 0.52,
            "wind_speed": 20, "date": "2023/07/17"},
        {"temperature": 26.0, "humidity": 0.52,
            "wind_speed": 9, "date": "2023/07/21"},
        {"temperature": 26.8, "humidity": 0.65,
            "wind_speed": 18, "date": "2023/07/21"},
        {"temperature": 25.4, "humidity": 0.65,
            "wind_speed": 5, "date": "2023/07/22"},
        {"temperature": 26.0, "humidity": 0.47,
            "wind_speed": 19, "date": "2023/07/22"},
        {"temperature": 26.7, "humidity": 0.47,
            "wind_speed": 15, "date": "2023/07/19"}
    ]
    },
    {"location_name": "Colombia", "location_measurements": [
        {"temperature": 25.1, "humidity": 0.49,
            "wind_speed": 12, "date": "2023/07/21"},
        {"temperature": 25.3, "humidity": 0.56,
            "wind_speed": 20, "date": "2023/07/18"},
        {"temperature": 26.9, "humidity": 0.62,
            "wind_speed": 14, "date": "2023/07/18"},
        {"temperature": 26.6, "humidity": 0.49,
            "wind_speed": 7, "date": "2023/07/17"},
        {"temperature": 25.9, "humidity": 0.46,
            "wind_speed": 8, "date": "2023/07/20"},
        {"temperature": 26.2, "humidity": 0.51,
            "wind_speed": 9, "date": "2023/07/21"},
        {"temperature": 25.2, "humidity": 0.50,
            "wind_speed": 13, "date": "2023/07/20"},
        {"temperature": 26.8, "humidity": 0.53,
            "wind_speed": 8, "date": "2023/07/19"},
        {"temperature": 25.8, "humidity": 0.49,
            "wind_speed": 9, "date": "2023/07/17"},
        {"temperature": 25.5, "humidity": 0.53,
            "wind_speed": 7, "date": "2023/07/19"},
        {"temperature": 26.7, "humidity": 0.45,
            "wind_speed": 13, "date": "2023/07/22"},
        {"temperature": 26.5, "humidity": 0.57,
            "wind_speed": 17, "date": "2023/07/18"},
        {"temperature": 26.9, "humidity": 0.54,
            "wind_speed": 8, "date": "2023/07/23"},
        {"temperature": 25.9, "humidity": 0.65,
            "wind_speed": 11, "date": "2023/07/22"},
        {"temperature": 26.9, "humidity": 0.64,
            "wind_speed": 16, "date": "2023/07/22"},
        {"temperature": 26.9, "humidity": 0.58,
            "wind_speed": 5, "date": "2023/07/20"},
        {"temperature": 26.7, "humidity": 0.65,
            "wind_speed": 17, "date": "2023/07/17"},
        {"temperature": 26.5, "humidity": 0.56,
            "wind_speed": 14, "date": "2023/07/23"},
        {"temperature": 25.7, "humidity": 0.52,
            "wind_speed": 18, "date": "2023/07/19"},
        {"temperature": 26.2, "humidity": 0.54,
            "wind_speed": 9, "date": "2023/07/22"},
        {"temperature": 26.8, "humidity": 0.53,
            "wind_speed": 6, "date": "2023/07/19"},
        {"temperature": 26.6, "humidity": 0.50,
            "wind_speed": 8, "date": "2023/07/19"},
        {"temperature": 25.3, "humidity": 0.45,
            "wind_speed": 16, "date": "2023/07/20"},
        {"temperature": 25.8, "humidity": 0.49,
            "wind_speed": 16, "date": "2023/07/20"},
        {"temperature": 26.9, "humidity": 0.60,
            "wind_speed": 6, "date": "2023/07/19"},
        {"temperature": 26.2, "humidity": 0.63,
            "wind_speed": 20, "date": "2023/07/19"},
        {"temperature": 25.8, "humidity": 0.59,
            "wind_speed": 18, "date": "2023/07/18"},
        {"temperature": 25.3, "humidity": 0.65,
            "wind_speed": 10, "date": "2023/07/19"},
        {"temperature": 25.8, "humidity": 0.56,
            "wind_speed": 16, "date": "2023/07/17"},
        {"temperature": 25.2, "humidity": 0.58,
            "wind_speed": 5, "date": "2023/07/17"}
    ]
    },
    {"location_name": "Mexico", "location_measurements": [
        {"temperature": 25.5, "humidity": 0.46,
            "wind_speed": 11, "date": "2023/07/21"},
        {"temperature": 26.4, "humidity": 0.53,
            "wind_speed": 8, "date": "2023/07/22"},
        {"temperature": 26.7, "humidity": 0.48,
            "wind_speed": 18, "date": "2023/07/18"},
        {"temperature": 25.4, "humidity": 0.58,
            "wind_speed": 9, "date": "2023/07/22"},
        {"temperature": 25.5, "humidity": 0.48,
            "wind_speed": 12, "date": "2023/07/17"},
        {"temperature": 27.0, "humidity": 0.46,
            "wind_speed": 14, "date": "2023/07/21"},
        {"temperature": 25.9, "humidity": 0.54,
            "wind_speed": 11, "date": "2023/07/21"},
        {"temperature": 25.2, "humidity": 0.59,
            "wind_speed": 10, "date": "2023/07/17"},
        {"temperature": 25.6, "humidity": 0.49,
            "wind_speed": 12, "date": "2023/07/21"},
        {"temperature": 26.2, "humidity": 0.53,
            "wind_speed": 20, "date": "2023/07/18"},
        {"temperature": 25.2, "humidity": 0.57,
            "wind_speed": 18, "date": "2023/07/22"},
        {"temperature": 25.8, "humidity": 0.54,
            "wind_speed": 11, "date": "2023/07/17"},
        {"temperature": 25.1, "humidity": 0.61,
            "wind_speed": 20, "date": "2023/07/22"},
        {"temperature": 25.1, "humidity": 0.65,
            "wind_speed": 11, "date": "2023/07/18"},
        {"temperature": 25.9, "humidity": 0.48,
            "wind_speed": 15, "date": "2023/07/18"},
        {"temperature": 25.6, "humidity": 0.50,
            "wind_speed": 5, "date": "2023/07/17"},
        {"temperature": 25.7, "humidity": 0.59,
            "wind_speed": 7, "date": "2023/07/23"},
        {"temperature": 26.7, "humidity": 0.46,
            "wind_speed": 13, "date": "2023/07/18"},
        {"temperature": 25.0, "humidity": 0.59,
            "wind_speed": 7, "date": "2023/07/17"},
        {"temperature": 26.5, "humidity": 0.61,
            "wind_speed": 16, "date": "2023/07/19"},
        {"temperature": 25.5, "humidity": 0.56,
            "wind_speed": 20, "date": "2023/07/19"},
        {"temperature": 25.2, "humidity": 0.58,
            "wind_speed": 11, "date": "2023/07/20"},
        {"temperature": 26.5, "humidity": 0.57,
            "wind_speed": 10, "date": "2023/07/18"},
        {"temperature": 25.9, "humidity": 0.63,
            "wind_speed": 11, "date": "2023/07/22"},
        {"temperature": 25.8, "humidity": 0.51,
            "wind_speed": 11, "date": "2023/07/20"},
        {"temperature": 25.6, "humidity": 0.48,
            "wind_speed": 15, "date": "2023/07/19"},
        {"temperature": 25.9, "humidity": 0.50,
            "wind_speed": 16, "date": "2023/07/23"},
        {"temperature": 26.4, "humidity": 0.54,
            "wind_speed": 5, "date": "2023/07/19"},
        {"temperature": 27.0, "humidity": 0.60,
            "wind_speed": 17, "date": "2023/07/19"},
        {"temperature": 25.3, "humidity": 0.64,
            "wind_speed": 16, "date": "2023/07/22"}
    ]
    },
    {"location_name": "Peru", "location_measurements": [
        {"temperature": 26.5, "humidity": 0.53,
            "wind_speed": 13, "date": "2023/07/19"},
        {"temperature": 25.1, "humidity": 0.59,
            "wind_speed": 18, "date": "2023/07/17"},
        {"temperature": 26.1, "humidity": 0.53,
            "wind_speed": 6, "date": "2023/07/21"},
        {"temperature": 26.3, "humidity": 0.45,
            "wind_speed": 12, "date": "2023/07/17"},
        {"temperature": 25.6, "humidity": 0.52,
            "wind_speed": 8, "date": "2023/07/20"},
        {"temperature": 25.6, "humidity": 0.52,
            "wind_speed": 16, "date": "2023/07/17"},
        {"temperature": 25.4, "humidity": 0.65,
            "wind_speed": 13, "date": "2023/07/20"},
        {"temperature": 25.7, "humidity": 0.46,
            "wind_speed": 11, "date": "2023/07/20"},
        {"temperature": 25.8, "humidity": 0.50,
            "wind_speed": 16, "date": "2023/07/20"},
        {"temperature": 25.4, "humidity": 0.58,
            "wind_speed": 18, "date": "2023/07/20"},
        {"temperature": 25.5, "humidity": 0.47,
            "wind_speed": 14, "date": "2023/07/23"},
        {"temperature": 25.7, "humidity": 0.50,
            "wind_speed": 19, "date": "2023/07/19"},
        {"temperature": 25.6, "humidity": 0.46,
            "wind_speed": 14, "date": "2023/07/22"},
        {"temperature": 25.7, "humidity": 0.61,
            "wind_speed": 8, "date": "2023/07/21"},
        {"temperature": 25.3, "humidity": 0.63,
            "wind_speed": 12, "date": "2023/07/21"},
        {"temperature": 26.8, "humidity": 0.62,
            "wind_speed": 9, "date": "2023/07/17"},
        {"temperature": 25.4, "humidity": 0.59,
            "wind_speed": 14, "date": "2023/07/23"},
        {"temperature": 25.2, "humidity": 0.62,
            "wind_speed": 6, "date": "2023/07/20"},
        {"temperature": 26.2, "humidity": 0.48,
            "wind_speed": 8, "date": "2023/07/17"},
        {"temperature": 26.3, "humidity": 0.54,
            "wind_speed": 20, "date": "2023/07/17"},
        {"temperature": 25.3, "humidity": 0.51,
            "wind_speed": 12, "date": "2023/07/17"},
        {"temperature": 26.8, "humidity": 0.46,
            "wind_speed": 11, "date": "2023/07/17"},
        {"temperature": 25.8, "humidity": 0.60,
            "wind_speed": 11, "date": "2023/07/22"},
        {"temperature": 26.2, "humidity": 0.52,
            "wind_speed": 16, "date": "2023/07/22"},
        {"temperature": 25.8, "humidity": 0.47,
            "wind_speed": 6, "date": "2023/07/22"},
        {"temperature": 25.2, "humidity": 0.53,
            "wind_speed": 18, "date": "2023/07/21"},
        {"temperature": 25.8, "humidity": 0.51,
            "wind_speed": 17, "date": "2023/07/23"},
        {"temperature": 25.3, "humidity": 0.62,
            "wind_speed": 13, "date": "2023/07/18"},
        {"temperature": 25.9, "humidity": 0.57,
            "wind_speed": 13, "date": "2023/07/18"},
        {"temperature": 25.6, "humidity": 0.61,
            "wind_speed": 15, "date": "2023/07/20"}
    ]
    },
    {"location_name": "United States", "location_measurements": [
        {"temperature": 26.7, "humidity": 0.48,
            "wind_speed": 13, "date": "2023/07/18"},
        {"temperature": 25.3, "humidity": 0.45,
            "wind_speed": 14, "date": "2023/07/17"},
        {"temperature": 26.5, "humidity": 0.52,
            "wind_speed": 14, "date": "2023/07/18"},
        {"temperature": 26.1, "humidity": 0.53,
            "wind_speed": 20, "date": "2023/07/23"},
        {"temperature": 26.2, "humidity": 0.60,
            "wind_speed": 16, "date": "2023/07/23"},
        {"temperature": 26.8, "humidity": 0.60,
            "wind_speed": 16, "date": "2023/07/22"},
        {"temperature": 25.3, "humidity": 0.49,
            "wind_speed": 15, "date": "2023/07/18"},
        {"temperature": 26.7, "humidity": 0.60,
            "wind_speed": 19, "date": "2023/07/23"},
        {"temperature": 26.6, "humidity": 0.58,
            "wind_speed": 16, "date": "2023/07/23"},
        {"temperature": 25.6, "humidity": 0.63,
            "wind_speed": 9, "date": "2023/07/23"},
        {"temperature": 26.5, "humidity": 0.50,
            "wind_speed": 7, "date": "2023/07/18"},
        {"temperature": 26.3, "humidity": 0.59,
            "wind_speed": 7, "date": "2023/07/20"},
        {"temperature": 26.3, "humidity": 0.65,
            "wind_speed": 18, "date": "2023/07/21"},
        {"temperature": 25.0, "humidity": 0.53,
            "wind_speed": 16, "date": "2023/07/18"},
        {"temperature": 25.2, "humidity": 0.45,
            "wind_speed": 20, "date": "2023/07/21"},
        {"temperature": 26.5, "humidity": 0.49,
            "wind_speed": 6, "date": "2023/07/23"},
        {"temperature": 25.3, "humidity": 0.62,
            "wind_speed": 8, "date": "2023/07/17"},
        {"temperature": 25.6, "humidity": 0.46,
            "wind_speed": 7, "date": "2023/07/21"},
        {"temperature": 25.0, "humidity": 0.64,
            "wind_speed": 19, "date": "2023/07/18"},
        {"temperature": 25.0, "humidity": 0.56,
            "wind_speed": 9, "date": "2023/07/21"},
        {"temperature": 25.6, "humidity": 0.60,
            "wind_speed": 6, "date": "2023/07/23"},
        {"temperature": 26.1, "humidity": 0.45,
            "wind_speed": 17, "date": "2023/07/20"},
        {"temperature": 25.7, "humidity": 0.56,
            "wind_speed": 8, "date": "2023/07/18"},
        {"temperature": 26.0, "humidity": 0.49,
            "wind_speed": 14, "date": "2023/07/22"},
        {"temperature": 25.8, "humidity": 0.52,
            "wind_speed": 7, "date": "2023/07/18"},
        {"temperature": 25.3, "humidity": 0.64,
            "wind_speed": 18, "date": "2023/07/23"},
        {"temperature": 25.9, "humidity": 0.47,
            "wind_speed": 16, "date": "2023/07/21"},
        {"temperature": 25.4, "humidity": 0.47,
            "wind_speed": 7, "date": "2023/07/19"},
        {"temperature": 25.0, "humidity": 0.58,
            "wind_speed": 9, "date": "2023/07/20"},
        {"temperature": 26.5, "humidity": 0.46,
            "wind_speed": 13, "date": "2023/07/18"}
    ]
    },
    {"location_name": "Venezuela", "location_measurements": [
        {"temperature": 26.0, "humidity": 0.48,
            "wind_speed": 16, "date": "2023/07/22"},
        {"temperature": 26.6, "humidity": 0.48,
            "wind_speed": 7, "date": "2023/07/18"},
        {"temperature": 26.9, "humidity": 0.54,
            "wind_speed": 18, "date": "2023/07/23"},
        {"temperature": 25.8, "humidity": 0.48,
            "wind_speed": 18, "date": "2023/07/17"},
        {"temperature": 26.2, "humidity": 0.61,
            "wind_speed": 11, "date": "2023/07/22"},
        {"temperature": 26.6, "humidity": 0.64,
            "wind_speed": 5, "date": "2023/07/18"},
        {"temperature": 26.5, "humidity": 0.54,
            "wind_speed": 16, "date": "2023/07/21"},
        {"temperature": 26.8, "humidity": 0.64,
            "wind_speed": 9, "date": "2023/07/21"},
        {"temperature": 26.4, "humidity": 0.52,
            "wind_speed": 20, "date": "2023/07/23"},
        {"temperature": 25.8, "humidity": 0.49,
            "wind_speed": 5, "date": "2023/07/21"},
        {"temperature": 25.1, "humidity": 0.52,
            "wind_speed": 19, "date": "2023/07/18"},
        {"temperature": 26.9, "humidity": 0.47,
            "wind_speed": 5, "date": "2023/07/23"},
        {"temperature": 25.6, "humidity": 0.46,
            "wind_speed": 5, "date": "2023/07/23"},
        {"temperature": 25.3, "humidity": 0.64,
            "wind_speed": 13, "date": "2023/07/21"},
        {"temperature": 26.3, "humidity": 0.53,
            "wind_speed": 17, "date": "2023/07/17"},
        {"temperature": 25.2, "humidity": 0.62,
            "wind_speed": 7, "date": "2023/07/23"},
        {"temperature": 26.6, "humidity": 0.62,
            "wind_speed": 8, "date": "2023/07/20"},
        {"temperature": 26.8, "humidity": 0.61,
            "wind_speed": 9, "date": "2023/07/21"},
        {"temperature": 25.0, "humidity": 0.65,
            "wind_speed": 20, "date": "2023/07/20"},
        {"temperature": 25.3, "humidity": 0.54,
            "wind_speed": 5, "date": "2023/07/20"},
        {"temperature": 26.6, "humidity": 0.60,
            "wind_speed": 6, "date": "2023/07/19"},
        {"temperature": 26.6, "humidity": 0.45,
            "wind_speed": 10, "date": "2023/07/23"},
        {"temperature": 26.6, "humidity": 0.45,
            "wind_speed": 9, "date": "2023/07/22"},
        {"temperature": 25.9, "humidity": 0.48,
            "wind_speed": 13, "date": "2023/07/23"},
        {"temperature": 25.7, "humidity": 0.47,
            "wind_speed": 10, "date": "2023/07/23"},
        {"temperature": 25.2, "humidity": 0.58,
            "wind_speed": 11, "date": "2023/07/20"},
        {"temperature": 26.2, "humidity": 0.48,
            "wind_speed": 6, "date": "2023/07/21"},
        {"temperature": 25.7, "humidity": 0.58,
            "wind_speed": 11, "date": "2023/07/21"},
        {"temperature": 25.8, "humidity": 0.54,
            "wind_speed": 16, "date": "2023/07/21"},
        {"temperature": 25.3, "humidity": 0.56,
            "wind_speed": 8, "date": "2023/07/22"}
    ]
    }
]


def convert_to_objects(countries_data, states_data, measurements_data):
    countries_list = []
    for country_data in countries_data:
        name = country_data["location_name"]
        capital = country_data["location_capital"]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currency"]
        language = country_data["main_language"]

        country_obj = Country(name, capital, population,
                              area, currency, language)
        countries_list.append(country_obj)

    states_list = []
    for state_data in states_data:
        country = state_data.get("location_name")
        for city in state_data["location_states"]:
            name = city.get("state_name")
            capital = city.get("state_capital")
            population = city.get("population")
            area = city.get("area")

            state_obj = State(country, name, capital, population, area)
            states_list.append(state_obj)

    measurements_list = []
    for measure_data in measurements_data:
        country = measure_data.get("location_name")
        for measure in measure_data["location_measurements"]:
            temperature = measure.get("temperature")
            humidity = round(measure.get("humidity")*100, 2)
            wind_speed = measure.get("wind_speed")
            date = measure.get("date")

            measure_obj = Measurement(
                country, temperature, humidity, wind_speed, date)
            measurements_list.append(measure_obj)
    return countries_list, states_list, measurements_list


def start():

    print("""
*==* Bienvenido a SKYNOW *==*
Cargando datos LOCALES...
""")
    countries_list, states_list, measurements_list = convert_to_objects(
        countries, states, weather)
    return countries_list, states_list, measurements_list
