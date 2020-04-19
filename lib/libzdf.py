# -*- coding: utf-8 -*-

from libmediathek4 import lm4
import libzdfjsonparser as jsonParser
parser = jsonParser.parser()


#https://api.zdf.de/content/documents/zdf-startseite-100.json?profile=default
#https://api.zdf.de/content/documents/meist-gesehen-100.json?profile=teaser
#https://api.zdf.de/content/documents/meist-gesehen-100.json?profile=default
#https://api.zdf.de/content/documents/sendungen-100.json?profile=default
#api.zdf.de/search/documents?hasVideo=true&q=*&types=page-video&sender=ZDFneo&paths=%2Fzdf%2Fcomedy%2Fneo-magazin-mit-jan-boehmermann%2Ffilter%2C%2Fzdf%2Fcomedy%2Fneo-magazin-mit-jan-boehmermann&sortOrder=desc&limit=1&editorialTags=&sortBy=date&contentTypes=episode&exclEditorialTags=&allEditorialTags=false
#api.zdf.de/search/documents?hasVideo=true&q=*&types=page-video&sender=ZDFneo&paths=%2Fzdf%2Fnachrichten%2Fzdfspezial%2Ffilter%2C%2Fzdf%nachrichten%2Fzdfspezial&sortOrder=desc&limit=1&editorialTags=&sortBy=date&contentTypes=episode&exclEditorialTags=&allEditorialTags=false
#https://api.zdf.de/cmdm/epg/broadcasts?from=2016-10-28T05%3A30%3A00%2B02%3A00&to=2016-10-29T05%3A29%3A00%2B02%3A00&limit=500&profile=teaser
#https://api.zdf.de/cmdm/epg/broadcasts?from=2016-10-28T05%3A30%3A00%2B02%3A00&to=2016-10-29T05%3A29%3A00%2B02%3A00&limit=500&profile=teaser&tvServices=ZDF
#https://api.3sat.de/content/documents/zdf/programm?profile=video-app&maxResults=200&airtimeDate=2019-06-09T12:00:00.000Z&includeNestedObjects=true


class libzdf(lm4):
	def __init__(self):
		lm4.__init__(self)
		self.defaultMode = 'libZdfListMain'

		self.modes.update({
			'libZdfListMain':self.libZdfListMain,
			'libZdfListShows':self.libZdfListShows,
			'libZdfListVideos':self.libZdfListVideos,
			'libZdfListChannel':self.libZdfListChannel,
			'libZdfListChannelDateVideos':self.libZdfListChannelDateVideos,
			'libZdfListPage':self.libZdfListPage,
			'libZdfListSport':self.libZdfListSport,
			})

		self.searchModes = {
			'libZdfListSearch': self.libZdfListSearch,
		}

		self.playbackModes = {
			'libZdfPlay':self.libZdfPlay,
			'libZdfPlayById':self.libZdfPlayById,
			}

		parser.baseApi = self.baseApi
		parser.userAgent = self.userAgent
		parser.tokenUrl = self.tokenUrl
		parser.API_CLIENT_ID = self.API_CLIENT_ID
		parser.API_CLIENT_KEY = self.API_CLIENT_KEY

	def libZdfListMain(self):
		l = []
		l.append({'metadata':{'name':self.translation(32031)}, 'params':{'mode':'libZdfListPage','url':f'{self.baseApi}/content/documents/meist-gesehen-100.json?profile=default'}, 'type':'dir'})
		#l.append({'metadata':{'name':self.translation(32031)}, 'params':{'mode':'libZdfListPage','url':f'{self.baseApi}/content/documents/filter-meist-gesehen-100.json?profile=page-video_episode_vod&limit=50'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32132)}, 'params':{'mode':'libZdfListShows'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32133)}, 'params':{'mode':'libZdfListChannel'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32134)}, 'params':{'mode':'libZdfListPage', 'url':f'{self.baseApi}/search/documents?q=%2A&contentTypes=category'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32139)}, 'params':{'mode':'libMediathekSearch', 'searchMode':'libZdfListSearch'}, 'type':'dir'})
		return {'items':l,'name':'root'}
		"""
		l = []
		l.append({'_name':translation(31031), 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/content/documents/meist-gesehen-100.json?profile=default'})
		l.append({'_name':'Sporttest1', 'mode':'libZdfListSport', '_type': 'dir', 'url':baseApi+'/content/documents/zdf/sport?profile=navigation'})
		l.append({'_name':'Sporttest1Frauenfussball', 'mode':'libZdfListSport', '_type': 'dir', 'url':baseApi+'/content/documents/fifa-frauen-wm-2019-spiele-in-voller-laenge-100.json?profile=default'})
		l.append({'_name':'Sporttest2', 'mode':'libZdfListSport', '_type': 'dir', 'url':baseApi+'/content/documents/leichtathletik-wm-live-livestream-ergebnisse-zeitplan-100.json?profile=default'})
		l.append({'_name':'Sporttest3 ALLE LIVESTREAMS', 'mode':'libZdfListSport', '_type': 'dir', 'url':baseApi+'/content/documents/SCMS_6f8a3ea6-d778-4bdc-9042-82c6e438a7be.json?profile=default'})
		l.append({'_name':'Sporttest4 Leichta', 'mode':'libZdfListSport', '_type': 'dir', 'url':baseApi+'/content/documents/SCMS_6528733f-d1d9-41a4-9bdd-a88c9d100f05.json?profile=default'})
		l.append({'_name':'Sporttest5 Leichta', 'mode':'libZdfListSport', '_type': 'dir', 'url':baseApi+'/content/documents/leichtathletik-wm-live-livestream-ergebnisse-zeitplan-100.json?profile=default'})
		l.append({'_name':translation(31032), 'mode':'libZdfListShows', '_type': 'dir'})
		l.append({'_name':translation(31033), 'mode':'libZdfListChannel', '_type': 'dir'})
		l.append({'_name':translation(31034), 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/search/documents?q=%2A&contentTypes=category'})
		l.append({'_name':'TEST', 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/content/documents/serien-100.json?profile=default&contentTypes=topic'})
		l.append({'_name':'TEST2', 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/content/documents/zdf/serien/serien-bereich-100.json?profile=default&maxResults=2&limit=2& =brand'})
		l.append({'_name':'TEST3', 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/cmdm/brands/0ec8a12b-3dca-4fa9-ad54-2893317fdac3?profile=default'})
		#l.append({'_name':'TEST42', 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/search/documents?q=%2A&contentTypes=brand&paths=%2Fzdf%2Fserien%2F&limit=50'})
		l.append({'_name':'TEST43', 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/search/documents?q=%2A&contentTypes=teaserCategory&paths=%2Fzdf%2Fserien%2F&limit=10'})
		l.append({'_name':'TEST4', 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/search/documents?q=%2A&profile=teaser&paths=%2Fzdf%2Fserien%2F&limit=50'})
		l.append({'_name':'TEST5', 'mode':'libZdfListPage', '_type': 'dir', 'url':baseApi+'/search/documents?q=%2A&paths=%2Fzdf%2Fserien%2F&limit=50'})
		
		l.append({'_name':translation(31039), 'mode':'libZdfSearch',   '_type': 'dir'})
		return l"""
		
	def libZdfListShows(self):
		if 'uri' in self.params:
			return parser.getAZ(self.params['uri'])
		else:
			return parser.getAZ()
				
	def libZdfListPage(self):
		return parser.parsePage(self.params['url'])

	def libZdfListSport(self):
		return
		"""
		l = libZdfListPage()
		for item in l:
			homeTeam,guestTeam = item['_name'].replace(u' in voller Länge','').split(u' - ')
			item['_type'] = 'sport'
			item['_customprops'] = {}

			item['_customprops']['rightTeamName'] = guestTeam
			item['_customprops']['rightTeamScore'] = ''
			item['_customprops']['rightTeamIcon'] = ''
			item['_customprops']['leftTeamName'] = homeTeam
			item['_customprops']['leftTeamScore'] = ''
			item['_customprops']['leftTeamIcon'] = ''
			item['_customprops']['date'] = ''
		return l"""
		
	def libZdfListVideos(self):
		return parser.getVideos(self.params['url'])

	def libZdfPlay(self):
		return parser.getVideoUrl(self.params['url'])
		
	def libZdfPlayById(self):
		return parser.getVideoUrlById(self.params['id'])
		
	def libZdfListChannel(self):
		l = []
		for channel in self.channels:
			l.append({'metadata':{'name':channel}, 'params':{'mode':'libMediathekListDate','subParams':f'{{"mode":"libZdfListChannelDateVideos","channel":"{channel}"}}'}, 'type':'dir'})
		return {'items':l,'name':'libZdfListChannel'}
		
	def libZdfListChannelDateVideos(self):
		self.params['url'] = f"{self.baseApi}/cmdm/epg/broadcasts?from={self.params['yyyymmdd']}T00%3A00%3A00%2B02%3A00&to={self.params['yyyymmdd']}T23%3A59%3A59%2B02%3A00&limit=500&profile=teaser&tvServices={self.params['channel']}"
		return self.libZdfListPage()
		
	def libZdfListSearch(self,searchString):
		self.params['url'] = f'{self.baseApi}/search/documents?q={searchString}'
		return self.libZdfListPage()
			
	def libZdfGetVideoHtml(self,url):
		pass
		#import re
		#response = libMediathek.getUrl(url)
		#return parser.getVideoUrl(re.compile('"contentUrl": "(.+?)"', re.DOTALL).findall(response)[0])
