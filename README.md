# lektor-google-analytics

This plugin adds support for Google analytics to Lektor.  

Once the plugin is enabled, a `generate_google_analytics` function 
is available which can include Google Analytics code in target `template` files.


## Enabling the Plugin

To enable the plugin add this to your project file:

```ini
[packages]
lektor-google-analytics = 0.1
```

## Configuring the Plugin

The plugin has a config file that is needed to inform it about your
website.  Just create a file named `google-analytics.ini` into your
`configs/` folder and configure the `GOOGLE_ANALYTICS` key with target 
property ID of form 'UA-abcdefgx-y':

```ini
GOOGLE_ANALYTICS = 'UA-abcdefgx-y'
; GOOGLE_ANALYTICS_PROPERTY = 'auto'
; LEGACY = 0
```

## In Templates

Now you can add a Google analytics code-snippet to any of your templates by 
just calling the `generate_google_analytics` function.

```html
<div class="ga-script">{{ generate_google_analytics() }}</div>
```

Optionally the function accepts a few arguemnts:

* Use `GOOGLE_ANALYTICS_PROPERTY` property to set it to include custom-built 
Google Analytics tracking code. By deafault, it is set to `auto`.

* Set `LEGACY` property to `1` to force using legacy `ga.js` code, 
which is not recommended unless you know what are you doing.
By default, it is `0` which means Google-recommended `analytics.js` code will
be used.
For more information, please refer to 
[Google-Analytics documentation](http://developers.google.com/analytics/devguides/collection/analyticsjs/).
