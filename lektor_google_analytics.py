# -*- coding: utf-8 -*-
from markupsafe import Markup

from lektor.pluginsystem import Plugin
from lektor.context import get_ctx, url_to
from lektor.utils import htmlsafe_json_dump


SCRIPT = '''
<div id="ga-script"></div>
<script type="text/javascript">
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', '%(GOOGLE_ANALYTICS_ID)s', 'auto');
        ga('send', 'pageview');
</script>
'''


class GoogleAnalyticsPlugin(Plugin):
    name = u'Google Analytics'
    description = u'Adds Google Analytics to Lektor-generated website'

    # def get_google_config(self):
      #  configs = []
       # ctx = get_ctx()
        # if ga_property is None:
            # ga_property = 'auto'
        # if ga_property is not None:
            # configs.append('this.page.ga_property = %s;' %
                           # htmlsafe_json_dump(ga_property))

        # if ga_legacy is not None and int(ga_legacy) == 1:
            # configs.append('this.page.ga_legacy = 1')
        # else:
            # configs.append('this.page.ga_legacy = 0')
        # return ' '.join(configs)

    def on_setup_env(self, **extra):
        ga_property = self.get_config().get('GOOGLE_ANALYTICS_PROPERTY', 'auto')
        ga_legacy = self.get_config().get('GOOGLE_ANALYTICS_LEGACY', 0)
        google_analytics_id = self.get_config().get('GOOGLE_ANALYTICS_ID')

        if google_analytics_id is None:
            raise RuntimeError('GOOGLE_ANALYTICS_ID is not configured')

        def google_analytics():
            # config = self.get_google_config()
            return Markup(SCRIPT % {'GOOGLE_ANALYTICS_ID': google_analytics_id})

        self.env.jinja_env.globals['generate_google_analytics'] = google_analytics
