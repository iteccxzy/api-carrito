# api-carrito


#Postman
Authorization type API Key
Key: Authorization
Value: Token a45s...

Get http://127.0.0.1:8000/articles/

get http://127.0.0.1:8000/detalle/1

Post http://127.0.0.1:8000/articles/
{
"marca": "rebook",
"modelo": "training",
"precio": 13000
}


Post http://127.0.0.1:8000/detalle/
{"article": 3,
"color": "gris",
"talle": 40,
"cantidad": 20}