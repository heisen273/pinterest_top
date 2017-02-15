# pinterest_top

Как юзать: 

https://developers.pinterest.com/tools/api-explorer/

Здесь жмешь "Retrieve the pins on a Board", затем "Get Token": 

![alt tag](https://pp.vk.me/c639319/v639319490/7394/svWmq21aFI0.jpg) 


Токен нужно сохранить куда-нибудь, он нужен для скрипта. 
Перед запуском `pinterest.py` необходимо убедиться, что установлена библиотека requests:

`pip install requests`

Ок. Теперь запускаем скрипт:

`python pinterest.py`

Скрипт спросит у тебя твой токен и борду, с которой ты хочешь парсить пины. Как это выглядит:

```
anton$ python pinterest.py

enter access token:  AejohV0C3mI4tBPkRJ5V58p7RZtnFKNP6c7UTn1DyQ3mkoBEmQAAAAA

enter board:  f0xkid/antohin_board
[[u'https://www.pinterest.com/pin/169377635966593483/', 2], [u'https://www.pinterest.com/pin/169377635966593480/', 2], [u'https://www.pinterest.com/pin/169377635966593477/', 2]]
```

На выходе получаем комбинацию:
[PIN_LINK, N]

где 
```
PIN_LINK, – прямая ссылка на пин
N, - индекс популярности пина. Это сумма лайков, комментов и репинов конкретного пина. 
```

