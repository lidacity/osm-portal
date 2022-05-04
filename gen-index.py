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
			{
				'name': "Кадастровая стоимость земель",
				'url': f"http://vl.nca.by/",
				'image': "nca_vl.png",
				'descr': "Кадастровая стоимость земель и налоговая база кадастрового агенства.",
				'author': "НКА",
				'coverage': "Беларусь",
			},
			{
				'name': "Публичная кадастровая карта",
				'url': f"https://map.nca.by/",
				'image': "nca.png",
				'descr': "Публичная кадастровая карта с большим количеством слоёв.",
				'author': "НКА",
				'coverage': "Беларусь",
			},
			{
				'name': "Мозаика данных ДЗЗ",
				'url': f"https://www.dzz.by/izuchdzz/",
				'image': "dzz.png",
				'descr': "Сведения о данных дистанционного зондирования Земли на территорию Республики Беларусь.",
				'author': "Государственный комитет по имуществу Республики Беларусь",
				'coverage': "Беларусь",
			},
			{
				'name': "Геопортал ЗИС",
				'url': f"https://gismap.by/next/",
				'image': "gismap.png",
				'descr': "Открытые данные геопортала ЗИС со слоями.",
				'author': "УП Проектный институт Белгипрозем",
				'coverage': "Беларусь",
			},
			{
				'name': "Госкартгеоцентр",
				'url': f"http://maps.by/demo/demo.html",
				'image': "maps_by.png",
				'descr': "Демокарта Беларуси.",
				'author': "Госкартгеоцентр",
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
				'image': "mapsurfer.png",
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
			{
				'name': "OSMapa",
				'url': f"https://osmapa.pl/#lat={LAT}&lon={LON}&z={ZOOM}&m=os",
				'image': "osmapa.png",
				'descr': "Польский вариант карты для Гармина.",
				'coverage': "Мир",
			},
			{
				'name': "Stamen Toner",
				'url': f"http://maps.stamen.com/toner/#{ZOOM}/{LAT}/{LON}",
				'image': "toner.png",
				'descr': "Чёрно-белая карта.",
				'coverage': "Мир",
			},
			{
				'name': "Touch Map",
				'url': f"https://opentouchmap.org/",
				'image': "opentouchmap.png",
				'descr': "Карта без лишнего.",
				'coverage': "Мир",
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
			{
				'name': "GPX Tool",
				'url': f"http://geo.klein-computing.de/gpx_tool.html",
				'image': "gpxtool.png",
				'descr': "Работа с координатами.",
				'coverage': "Вся планета",
				'author': "<a href='http://geo.klein-computing.de/'>Geo Tools, Pascal Klein</a>",
			},
			{
				'name': "Distance Calculator",
				'url': f"https://map.meurisse.org/",
				'image': "distance.png",
				'descr': "Работа с построением путей.",
				'coverage': "Вся планета",
			},
#
		],
	},

	{
		'caption': "Контроль качества",
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
			{
				'name': "Валидатор автодорог",
				'url': f"http://wowik.byethost7.com/routes/",
				'image': "wowik_routes.png",
				'descr': "Валидатор автодорог",
				'coverage': "Европа",
				'refresh': "Несколько раз в месяц",
				'authors': "iWowik",
			},
			{
				'name': "Список населенных мест",
				'url': f"http://wowik.byethost7.com/places/by/",
				'image': "wowik_places.png",
				'descr': "Валидатор населённых пунктов",
				'coverage': "Европа",
				'refresh': "Несколько раз в месяц",
				'authors': "iWowik",
			},
			{
				'name': "TagInfo",
				'url': f"https://taginfo.openstreetmap.org/",
				'image': "taginfo.png",
				'descr': "OpenStreetMap использует теги в виде ключ=значение для описания географических объектов. Taginfo собирает информацию об этих тегах из нескольких источников, чтобы помочь вам разобраться, что каждый тег означает и как применяется.",
				'coverage': "Весь мир",
				'refresh': "Ежедневно",
			},
			{
				'name': "Карта подъездов и номера квартир",
				'url': f"https://osm.cupivan.ru/entrance/#366/?z={ZOOM}&lat={LAT}&lon={LON}",
				'image': "entrance.png",
				'descr': "Валидатор подъездов. На данной карте можно посмотреть в каких подъездах не проставлены номера квартир, а также этажность и адрес на здании.",
				'coverage': "Весь мир",
				'refresh': "Онлайн",
				'authors': "CupIvan",
			},
			{
				'name': "Этажность зданий на карте",
				'url': f"https://osm.cupivan.ru/levels/#366/?z={ZOOM}&lat={LAT}&lon={LON}",
				'image': "levels.png",
				'descr': "Этажность зданий. Раскраска зданий по количеству этажей. Удобно смотреть где ещё не указаны этажи.",
				'coverage': "Весь мир",
				'refresh': "Онлайн",
				'authors': "CupIvan",
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
			{
				'name': "Disaster Ninja",
				'url': f"https://disaster.ninja/live/#position={LON},{LAT};zoom={ZOOM}",
				'image': "disaster_ninja.png",
				'descr': "В шестиугольниках показываются наиболее активные участники правок",
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
			{
				'name': "XYZ",
				'url': f"http://openwhatevermap.xyz/#{ZOOM}/{LAT}/{LON}",
				'image': "xyz.png",
				'descr': "Карта отображается из кусочков разных стилей.",
			},
			{
				'name': "Сравнение OSM с Народной картой",
				'url': f"https://osm.cupivan.ru/OSMvsNarod/",
				'image': "OSMvsNarod.png",
				'descr': "Сравнение с картой Яндекса. Двойная карта OSM / Яндекс. Поиск населённых пунктов и координаты городов в формате Википедии.",
				'author': "CupIvan",
			},
		],
	},

	{
		'caption': "Разное",
		'items': [
			{
				'name': "Dark Sky Map",
				'url': f"https://maps.darksky.net/@temperature,{LAT},{LON},{ZOOM}",
				'image': "dark_sky_map.png",
				'descr': "Погода.",
				'coverage': "Мир",
			},
			{
				'name': "Field Paprers",
				'url': f"http://fieldpapers.org/compose#{ZOOM}/{LAT}/{LON}",
				'image': "fieldpapers.png",
				'descr': "Сделать полевые материалы для печати.",
				'coverage': "Мир",
			},
			{
				'name': "Сгенерировать карту",
				'url': f"https://print.get-map.org/new/",
				'image': "MyOSMatic.png",
				'descr': "Это свободный веб-сервис, позволяющий генерировать карты городов с использованием данных OpenStreetMap. Сгенерированные карты доступны в форматах PNG, PDF и SVG, и готовы к распечатке.",
				'coverage': "Мир",
			},
		],
	},
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
