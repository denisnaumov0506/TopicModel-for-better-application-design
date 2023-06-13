from google_play_scraper import Sort, reviews, reviews_all
import csv
import logging
import json
from datetime import datetime

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

apps = [
    'youtube',
    'whatsapp',
    'telegram',
    'instagram',
    'tiktok',
    'com.zzkko',
    'com.snapchat.android',
    'com.amazon.avod.thirdpartyclient',
    'com.lemon.lvoverseas',
    'com.gamma.scan',
    'com.paypal.android.p2pmobile',
    'de.hafas.android.db',
    'com.ebay.kleinanzeigen',
    'de.dhl.paket',
    'com.sec.android.easyMover',
    'de.cellular.ottohybrid',
    'com.google.android.apps.translate',
    'de.ingdiba.bankingapp',
    'com.amazon.mShop.android.shopping',
    'com.duolingo',
    'com.starfinanz.mobile.android.pushtan',
    'com.scaleup.chatai',
    'com.disney.disneyplus',
    'fr.doctolib.www',
    'bloodpressure.bloodpressureapp.bloodpressuretracker',
    'com.starfinanz.smob.android.sfinanzstatus',
    'whale.vpn.free',
    'com.lidl.eci.lidlplus',
    'com.facebook.orca',
    'com.spotify.music',
    'com.facebook.katana',
    'com.teacapps.barcodescanner',
    'videoplayer.videodownloader.downloader',
    'com.whatsapp.w4b',
    'com.google.android.apps.walletnfcrel',
    'com.myklarnamobile',
    'com.pinterest',
    'com.azure.authenticator',
    'net.wrightflyer.le.reality',
    'com.ai.polyverse.mirror',
    'net.diflib.recorderx',
    'io.faceapp',
    'com.booking',
    'de.dm.meindm.android',
    'com.netflix.mediaclient',
    'com.goodreads',
    'com.google.android.apps.maps',
    'com.google.android.apps.subscriptions.red',
    'com.tinder',
    'com.dazn',
    'tv.twitch.android.app',
    'de.komoot.android',
    'com.bumble.app',
    'com.crunchyroll.crunchyroid',
    'com.yazio.android',
    'com.babbel.mobile.android.en',
    'com.microsoft.skydrive',
    'net.lovoo.android',
    'de.prosiebensat1digital.seventv',
    'com.badoo.mobile',
    'com.dropbox.android',
    'com.calimoto.calimoto',
    'com.fitbit.FitbitMobile',
    'sg.bigo.live',
    'me.fup.joyapp',
    'com.reddit.frontpage',
    'com.groundspeak.geocaching.intro',
    'com.discord',
    'com.nordvpn.android',
    'de.mobiletrend.lovidoo',
    'de.exaring.waipu',
    'de.spiegel.android.app.spon',
    'de.dwins.financeguru',
    'deezer.android.app',
    'com.sgiggle.production',
    'com.zattoo.player',
    'com.colt',
    'com.cbs.ca',
    'com.grindrapp.android',
    'com.netbiscuits.bild.android',
    'com.canva.editor',
    'com.azarlive.android',
    'com.blinkslabs.blinkist.android',
    'com.naver.linewebtoon',
    'com.iViNi.bmwhatLite',
    'com.tomtom.gplay.navapp',
    'com.kms.free',
    'us.zoom.videomeetings']

for app in apps:

    print(f'Scraping {app}...')

    result = reviews_all(
        app,
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
        filter_score_with=None, # defaults to None(means all score)
    )

    class DateTimeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return json.JSONEncoder.default(self, obj)

    filename = f'{app}_reviews_all.json'

    # Dump the scraped data into a JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4, cls=DateTimeEncoder)

    print(f'Scraping {app} finished!')


