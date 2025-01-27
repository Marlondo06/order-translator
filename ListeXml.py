import json
import xmltodict

Liste = """
{
  "Haupt": {
  "orderReference": "32345423", 
  "currency": "EUR",
  "customerReference": "7788997",
  "orderDate": "2023-04-24T08:48:07",
   "shippingAddress": {
    "firstName": "Mia",
    "lastName": "Mustermann",
    "address1": "Hauptstr.",
    "address2": "1",
    "address3": "",
    "city": "Berlin",
    "zipCode": "10115",
    "countryCode": "DE"
    },
    "orderItems": [
    {
      "sku": "4251238918483",
      "name": "Silani"
    },
    {
      "sku": "4059117317163",
      "name": "Sarion"
    },
    {
      "sku": "4059117317163",
      "name": "Sarion"
    },
    {
      "sku": "4251200728256",
      "name": "Sanika"
    }
  ]
  }
}
"""

um = json.loads(Liste)
zw = xmltodict.unparse(um)
print(zw)

with open("test.json", "w") as json.data:
    json.dump(Liste, json.data, indent=4)