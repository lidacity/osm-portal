#!/usr/bin/python

import sys
import os

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

fields = {
	'refresh': "Время обновления",
	'coverage': "Покрытие",
	'author': "Автор",
	'authors': "Авторы",
}

# TODO: get these from GeoIP and/or from user selection
LAT = "53.92"
LON = "27.55"
ZOOM = "11"

#http://wowik.byethost7.com/routes/ru-ore/55.htm
#http://stat.latlon.org/
#https://osm.cupivan.ru/
#https://disaster.ninja/live/#id=862b38e7-f7e1-486f-81d3-05394662d7c0;position=25.268380854291763,53.83782195587909;zoom=8.434805551671564
#https://osmapa.pl/#lat=53.8856&lon=25.3226&z=14&m=os
#https://opentouchmap.org/
#http://tools.geofabrik.de/mc/#10/53.9313/25.4735&num=4&mt0=mapnik&mt1=geofabrik-basic-colour&mt2=mapnik-german&mt3=here-map
#http://geo.klein-computing.de/gpx_tool.html
#https://map.meurisse.org/
#https://maps.darksky.net/@temperature,52.616,28.828,7
#http://openwhatevermap.xyz/#11/53.8533/25.4196
#http://maps.stamen.com/toner/#13/53.8966/-334.6992
#https://print.get-map.org/new/
#http://fieldpapers.org/compose#3/25.40/-10.99
#https://orda.of.by/.map/?53.902253,27.561854&m=gm/17,osm/6,rkka/13,wig/13
#https://taginfo.openstreetmap.org/


#https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services
objects = [
	{
		'caption': "Официальные рендеры",
		'items': [
			{
				'name': "Mapnik",
				'url': f"http://www.openstreetmap.org/?lat={LAT}&lon={LON}&zoom={ZOOM}&layers=M",
				'image': "mapnik.png",
				'descr': "Основной рендер OpenStreetMap. При этом самый быстрый - задержка между внесением изменений в карту и отрисовкой обычно не превышает нескольких минут.",
				'refresh': "Минуты",
				'coverage': "Вся планета",
			},
			{
				'name': "CyclOSM",
				'url': f"http://www.openstreetmap.org/?lat={LAT}&lon={LON}&zoom={ZOOM}&layers=Y",
				'image': "CyclOSM.png",
				'descr': "CyclOSM — это принципиально новая карта для велосипедистов, основанная на данных OpenStreetMap. Проект ставит своей целью — создание красивой и практичной карты для велосипедистов, независимо от их привычек и способностей.",
				'author': "<a href='https://cyclosm.org/'>cyclosm</a>",
				'refresh': "Несколько дней",
				'coverage': "Вся планета",
			},
			{
				'name': "Cycle Map",
				'url': f"http://www.openstreetmap.org/?lat={LAT}&lon={LON}&zoom={ZOOM}&layers=C",
				'image': "cyclemap.png",
				'descr': "Карта для велосипедистов с топографией и выделением веломаршрутов.",
				'refresh': "Несколько дней",
				'coverage': "Вся планета",
			},
			{
				'name': "Transport Map",
				'url': f"http://www.openstreetmap.org/?lat={LAT}&lon={LON}&zoom={ZOOM}&layers=T",
				'image': "transport_map.png",
				'descr': "Слой с маршрутами общественного транспорта.",
				'refresh': "Несколько дней",
				'coverage': "Вся планета",
			},
			{
				'name': "&Ouml;PNV-Karte",
				'url': f"http://www.xn--pnvkarte-m4a.de/?zoom={ZOOM}&lat={LAT}&lon={LON}",
				'image': "opnvkarte.png",
				'descr': "Сторонний рендер с маршрутами общественного транспорта.",
				'author': "<a href='http://xn--pnvkarte-m4a.de/'>&Ouml;PNV-Karte</a>",
				'refresh': "Раз в несколько дней",
				'coverage': "Вся планета",
			},
			{
				'name': "Humanitarian",
				'url': f"http://www.openstreetmap.org/?lat={LAT}&lon={LON}&zoom={ZOOM}&layers=H",
				'image': "humanitarian.png",
				'descr': "Этот стиль карты сосредоточен на ресурсах, полезных для гуманитарных организаций и граждан в целом в чрезвычайных ситуациях, выделяя POI, такие как водные ресурсы (колодцы, ручные насосы, пожарные гидранты ...), источники света, общественные здания, социальные здания, качество дорог и т.д. Используемые цвета светлые, поэтому люди могут распечатать их, а затем легко рисовать и писать поверх карты (это полезная функция для гуманитарных организаций для обновления информации на распечатанной карте в таких ситуациях, как землетрясение, например).",
				'refresh': "Несколько дней",
				'coverage': "Вся планета",
			},
		],
	},

	{
		'caption': "Беларусь",
		'items': [
			{
				'name': "OpenStreetMap.by",
				'url': f"http://openstreetmap.by/?lat={LAT}&lon={LON}&zoom={ZOOM}",
				'image': "osmby.png",
				'descr': "Рендер с продвинутым стилем.",
				'author': "<a href='http://www.openstreetmap.org/user/Kom%D1%8Fpa'>Komяpa</a>",
				'refresh': "Минуты",
				'coverage': "Вся планета",
			},
			{
				'name': "LatLon.org",
				'url': f"http://latlon.org/#{ZOOM}/{LAT}/{LON}?layers=L",
				'image': "latlon_buildings.png",
				'descr': "Рендер Беларуси на белорусском языке.",
				'refresh': "Реальное время",
				'author': "<a href='http://www.openstreetmap.org/user/Kom%D1%8Fpa'>Komяpa</a>",
				'coverage': "Беларусь",
			},
		],
	},

	{
		'caption': "Сторонние рендеры",
		'items': [
			{
				'name': "openstreetmap.ru",
				'url': f"http://www.openstreetmap.ru/#layer=BY&zoom={ZOOM}&lat={LAT}&lon={LON}",
				'image': "mapsurfer_hybrid.png",
				'descr': "Полупрозрачный слой с подписями для использования поверх спутниковых снимков и карт",
				'authors': "Maxim Rylov and Vitaly Chezganov",
				'coverage': "Вся планета",
			},
			{
				'name': "OpenStreetBrowser",
				'url': f"http://www.openstreetbrowser.org/?zoom={ZOOM}&lat={LAT}&lon={LON}",
				'image': "openstreetbrowser.png",
				'descr': "Карта с большим количеством накладываемых слоёв с различной информацией (общественный транспорт, заправки, питание, туризм и т.д.).",
				'coverage': "Европа (до 45° в.д.)",
			},
		],
	},

	{
		'caption': "Прокладка маршрутов",
		'items': [
			{
				'name': "OSRM",
				'url': f"http://map.project-osrm.org/?z={ZOOM}&center={LAT},{LON}",
				'image': "osrm.png",
				'descr': "Быстрая прокладка маршрутов по карте OSM.",
				'coverage': "Вся планета",
				'refresh': "Приблизительно раз в неделю (актуальность данных можно посмотреть нажав на кнопку с шестерёнкой)",
			},
		],
	},

	{
		'caption': "Инструменты контроля качества",
		'items': [
			{
				'name': "KeepRight!",
				'url': f"http://keepright.ipax.at/report_map.php?zoom={ZOOM}&lat={LAT}&lon={LON}",
				'image': "keepright.png",
				'descr': "Инструмент, помогающий выявить огромное количество топологических ошибок на карте, включая неправильно отмеченные объекты, отсутствие необходимых тэгов, несоединённые и самопересекающиеся дороги и т.д.",
				'coverage': "Вся планета",
				'refresh': "Примерно раз в неделю",
			},
			{
				'name': "WHO DID IT?!",
				'url': f"http://simon04.dev.openstreetmap.org/whodidit/?zoom={ZOOM}&lat={LAT}&lon={LON}",
				'image': "whodidit.png",
				'descr': "Мониторинг правок пользователей на выбранной территории.",
				'coverage': "Вся планета",
				'refresh': "Ежечасно",
			},
			{
				'name': "Geofabrik Tools/OSM Inspector", # TODO: нужно разбить на инструменты; для разных инструментов разный coverage
				'url': f"http://tools.geofabrik.de/osmi/?view=addresses&zoom={ZOOM}&lat={LAT}&lon={LON}",
				'image': "osminspector.png",
				'descr': "Набор инструментов для визуализации различных объектов и их отношений на карте. Включает инструменты, показывающие ошибки геометрии и тэгов, а также подробную визуализацию населённых пунктов, дорожной сети, адресации, границ, водоёмов, общественного транспорта.",
				'coverage': "Европа (до 45° в.д.)",
				'refresh': "Несколько дней",
				'authors': "<a href='http://www.geofabrik.de/'>Geofabrik GmbH</a>",
			},
		],
	},

	{
		'caption': "Информация по участникам OSM",
		'items': [
			{
				'name': "OSM Heat Map",
				'url': f"http://yosmhm.neis-one.org/",
				'image': "heatmap.png",
				'descr': "'Тепловая карта' правок пользователя",
				'coverage': "Вся планета",
				'author': "Pascal Neis",
			},
			{
				'name': "OoOC",
				'url': f"http://resultmaps.neis-one.org/oooc?zoom={ZOOM}&lat={LAT}&lon={LON}",
				'image': "oooc.png",
				'descr': "Карта, отображающая примерное положение и количество правок участников OSM",
				'coverage': "Вся планета",
				'author': "Pascal Neis",
			},
		],
	},

	{
		'caption': "Сравнение карт",
		'items': [
			{
				'name': "Geofabrik Tools/Map Compare",
				'url': f"http://tools.geofabrik.de/mc/?zoom={ZOOM}&lat={LAT}&lon={LON}",
				'image': "mapcompare.png",
				'descr': "Сервис для side-by-side сравнения карт. Кроме OSM поддерживает карты Google.",
				'authors': "<a href='http://www.geofabrik.de/'>Geofabrik GmbH</a>",
			},
		],
	},

	# TODO: добавить, как минимум: latlon, openorientingmap
	#
	# TODO: добавить все текстовые ресурсы (водный реестр, валидатор адресов от Лёши и т.д.)
	# TODO: добавить альтернативные проекты и карты (нужно?)
]

with open("index.html.new", mode="w", encoding="utf-8", newline="\n") as f:
	print("<html><head><title>OSM::Portal: всё это - OpenStreetMap</title>", file=f)
	print("<meta http-equiv=\"Content-type\" value=\"text/html; charset=utf-8\">", file=f)
	print("<link rel=\"stylesheet\" media=\"screen\" href=\"osm-portal.css\">", file=f)
	print("</head>", file=f)
	print("<body>", file=f)

	print("<div id=\"switcher\">", file=f)

	num = 0
	for page in objects:
		if num == 0:
			print(f"<input type=\"radio\" name=\"selector\" id=\"radio{num}\" checked=\"checked\"/><label for=\"radio{num}\">{page['caption']}</label>", file=f)
		else:
			print(f"<input type=\"radio\" name=\"selector\" id=\"radio{num}\"/><label for=\"radio{num}\">{page['caption']}</label>", file=f)
		num += 1

	print("</div>", file=f)

	num = 0
	for page in objects:
		print(f"<div class=\"page\"><h1>{page['caption']}</h1>", file=f)

		for item in page['items']:
			has_data = False
			url = item['url']
			print(f"<div class=\"block\"><a href=\"{url}\"><h2>{item['name']}</h2></a>", file=f)

			if 'descr' in item:
				print("<div class=\"descr\">", file=f)
				print(f"<p>{item['descr']}</p>\n", file=f)
				print("</div>", file=f)

			for field in fields:
				if field in item:
					has_data = True
					break

			if has_data:
				print("<div class=\"descr\">", file=f)

				print("<ul>", file=f)
				for field in fields:
					if field in item:
						print(f"<li><b>{fields[field]}:</b> {item[field]}</li>", file=f)

				print("</ul>", file=f)

				print("</div>", file=f)

			print(f"<a href=\"{url}\"><img src=\"{item['image']}\"></a>", file=f)
			print("</div>", file=f)

		print("</div>", file=f)

	print("<script src=\"osm-portal.js\" type=\"text/javascript\"></script>", file=f)
	print("</body></html>", file=f)

os.rename("index.html.new", "index.html")
