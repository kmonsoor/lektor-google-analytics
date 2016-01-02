# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from markupsafe import Markup

SCRIPT = '''
<div id="ga-script"></div>
<script type="text/javascript">
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
        ga('create', '%(GOOGLE_ANALYTICS_ID)s', '%(GOOGLE_ANALYTICS_PROPERTY)s');
        ga('send', 'pageview');
</script>
'''


class GoogleAnalyticsPlugin(Plugin):
    name = u'Google Analytics'
    description = u'adds support for Google Analytics to Lektor CMS'

    def on_setup_env(self):
        ga_property = self.get_config().get('GOOGLE_ANALYTICS_PROPERTY', 'auto')
        google_analytics_id = self.get_config().get('GOOGLE_ANALYTICS_ID')

        if google_analytics_id is None:
            raise RuntimeError('GOOGLE_ANALYTICS_ID is not configured. '
                               'Please configure it in '
                               '`./configs/google-analytics.ini` file')

        def google_analytics():
            return Markup(SCRIPT % {'GOOGLE_ANALYTICS_ID': google_analytics_id,
                                    'GOOGLE_ANALYTICS_PROPERTY': ga_property})

        self.env.jinja_env.globals['generate_google_analytics'] = google_analytics
