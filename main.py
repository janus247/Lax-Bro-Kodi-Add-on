import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'Live TV')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
    url = build_url({'mode': 'folder_one', 'foldername': 'Live & Upcoming Action'})
    li = xbmcgui.ListItem('Live Action', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Live_Action.png')
    li.setProperty('fanart_image', 'special://home/addons/plugin.video.laxbro/fanart.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'folder_two', 'foldername': 'Archived Action'})
    li = xbmcgui.ListItem('Archived Action', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Archived_Action.png')
    li.setProperty('fanart_image', 'special://home/addons/plugin.video.laxbro/fanart.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder_one':
    foldername = args['foldername'][0]
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Patriot_League_Live.m3u'
    li = xbmcgui.ListItem('College Lax Sesh', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Live.png')
    li.setProperty('fanart_image', 'special://home/addons/plugin.video.laxbro/fanart.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)	
	
	
elif mode[0] == 'folder_two':
    foldername = args['foldername'][0]
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/2015_NCAA_T.m3u'
    li = xbmcgui.ListItem('2015 NCAA Lacrosse Championship Tournament', iconImage='special://home/addons/plugin.video.laxbro/resources/media/NCAA.png')
    li.setProperty('fanart_image', 'https://bigtennetworks.files.wordpress.com/2015/05/usatsi_8580510.jpg?w=912&h=652')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/2015_MCLA_T.m3u'
    li = xbmcgui.ListItem('2015 MCLA Lacrosse Championship Tournament', iconImage='special://home/addons/plugin.video.laxbro/resources/media/MCLA.png')
    li.setProperty('fanart_image', 'http://cdn.laxallstars.com/wp-content/uploads/2015/06/unnamed-23.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
   
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Army.m3u'
    li = xbmcgui.ListItem('Army NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Army.png')
    li.setProperty('fanart_image', 'http://www.sports-logos-screensavers.com/user/Army_Black_Knights2.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/BostonU.m3u'
    li = xbmcgui.ListItem('Boston University NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Boston.png')
    li.setProperty('fanart_image', 'http://laborunionreport.com/wp-content/uploads/2015/02/Boston-University-Terriers.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Bucknell.m3u'
    li = xbmcgui.ListItem('Bucknell NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Bucknell.png')
    li.setProperty('fanart_image', 'http://content.sportslogos.net/logos/30/624/full/2442.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Colgate.m3u'
    li = xbmcgui.ListItem('Colgate NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Colgate.png')
    li.setProperty('fanart_image', 'http://www.sports-logos-screensavers.com/user/Colgate_Raiders.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Holy_Cross.m3u'
    li = xbmcgui.ListItem('Holy Cross NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Holy.png')
    li.setProperty('fanart_image', 'http://image.cdnllnwnl.xosnetwork.com/pics33/0/AL/ALLBPZTGRZVWJRQ.20150805200419.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Lafayette.m3u'
    li = xbmcgui.ListItem('Lafayette NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Lafayette.png')
    li.setProperty('fanart_image', 'https://s.graphiq.com/sites/default/files/5636/media/images/Lafayette_Leopards_NCAA_Football_3963863.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
		
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Lehigh.m3u'
    li = xbmcgui.ListItem('Lehigh NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Lehigh.png')
    li.setProperty('fanart_image', 'http://content.sportslogos.net/logos/32/727/full/wt5ggswfh4dmynrwe0ah.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Loyola.m3u'
    li = xbmcgui.ListItem('Loyola NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Loyola.png')
    li.setProperty('fanart_image', 'http://www.loyola.edu/~/media/undergraduate/images2014/greyhound-pride/athletics_1366x768.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Navy.m3u'
    li = xbmcgui.ListItem('Navy NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Navy.png')
    li.setProperty('fanart_image', 'http://wallpapergoo.com/wp-content/uploads/2015/06/Navy-Wallpaper-1F44.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Towson.m3u'
    li = xbmcgui.ListItem('Towson NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Towson.png')
    li.setProperty('fanart_image', 'https://s3.amazonaws.com/internet-retail-connection-category-images/555d6ede629387.95775763.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Hofstra.m3u'
    li = xbmcgui.ListItem('Hofstra NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Hofstra.png')
    li.setProperty('fanart_image', 'https://makingbabygrand.files.wordpress.com/2010/11/hofstra_logo.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/NEC.m3u'
    li = xbmcgui.ListItem('Northeast Conference Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/NE10.png')
    li.setProperty('fanart_image', 'http://www.sacredheartpioneers.com/fanCenter/NEC_primary.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/SLC.m3u'
    li = xbmcgui.ListItem('MCLA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/MCLAreg.png')
    li.setProperty('fanart_image', 'https://i.ytimg.com/vi/0UbNSSdtkK4/maxresdefault.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    
    url = 'https://raw.githubusercontent.com/janus247/Lax-Bro-Entertainment/master/M3U%20files/Big%20Ten.m3u'
    li = xbmcgui.ListItem('Bonus BIG TEN NCAA Lacrosse', iconImage='special://home/addons/plugin.video.laxbro/resources/media/Big10.png')
    li.setProperty('fanart_image', 'http://cdn.fansided.com/wp-content/blogs.dir/229/files/2014/10/ncaa-football-michigan-penn-state.jpg')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
