import json
import urllib2

class Route(object):

    BASEURL = 'http://api.bestbuy.com/v1/'

    def __init__(self, settings):
        
        if type(settings) is dict:
            self.overwrite_defaults(settings)
        else:
            raise Exception('Settings must be passed as a dictionary')


    def overwrite_defaults(self, settings):

        for key,val in settings.iteritems():
            if self.settings.has_key(key):
                self.settings[key] = val


    def format_params(self, params):

        formatted_params = ''

        if type(params) is dict:
            for key,val in params.iteritems():
                formatted_params += '{param}={param_val}'.format(param=key, param_val=val)
            return formatted_params
        else:
            raise Exception('params must be in a dictionary')


    def get_full_url(self, endpoint):

        settings = self.get_settings()

        return Route.BASEURL + endpoint + settings


    def get_settings(self):

        settings = '?'
        count = 1

        for key,val in self.settings.iteritems():
            settings += '{setting}={setting_val}'.format(setting=key, setting_val=val)
            if count < len(self.settings):
                settings += '&'
            count += 1

        return settings


    def execute(self, url):

        try:
            response = urllib2.urlopen(url)
            data = response.read()
            return json.loads(data)
        except:
            raise Exception('malformed url: {url}'.format(url=url))

        