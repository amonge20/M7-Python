import json
datas = """
{
  "book": [
    {
      "title": "El señor de los anillos",
      "cover": "asda",
      "year": 1990,
      "pages": 200
    },
    {
      "title": "Harry Potter",
      "cover": "asda",
      "year": 2003,
      "pages": 200,
    },
    {
      "title": "asas",
      "cover": "asda",
      "year": 2001,
      "pages": "aasas"
    },
    {
      "title": "asas",
      "cover": "asda",
      "year": 2015,
      "pages": "aasas"
    }
  ]
}
"""""


with open("ejemplo.json", 'w') as file:
    json.dump(datas,file)