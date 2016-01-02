# lektor-google-analytics


[![](https://img.shields.io/badge/License-BSD-blue.svg)]((https://opensource.org/licenses/BSD-3-Clause))

This plugin adds support for [Google analytics](http://www.google.com/analytics/) to [Lektor CMS](https://github.com/lektor/lektor).

Once the plugin is enabled, a `generate_google_analytics()` function
is available to be included in target `template` which automatically include Google-Analytics code in final HTML files rendered by `Lektor`.

## Basic Usage

### Enabling the Plugin

To enable the plugin add this to your project file:

```ini
[packages]
lektor-google-analytics = 0.1
```

### Configuring the Plugin

The plugin needs a config file with your `Google analytics` code in it.

Just create a file named `google-analytics.ini` into `./configs` folder in your Lektor project's base directory. And, put the `GOOGLE_ANALYTICS_ID` key with target
property ID of form `UA-XXXXXXXX-Y` which you obtained from:

```ini
GOOGLE_ANALYTICS_ID = UA-XXXXXXXX-Y
```

### Using in Templates

Now you can add a Google analytics code-snippet in your templates by
just calling the `generate_google_analytics` function in its <body> </body> tag as below.

```html
<div class="ga-script">{{ generate_google_analytics() }}</div>
```

That's it. All the `HTML` files that rendered from that template will include Google-Analytics code automatically.

------
### Advanced

* You can use `GOOGLE_ANALYTICS_PROPERTY` property to include your custom-built
Google Analytics tracking code. In that case, your `./configs/google-analytics.ini` will look like this:

```ini
GOOGLE_ANALYTICS_ID = UA-XXXXXXXX-Y
GOOGLE_ANALYTICS_PROPERTY = 'my custom code'
```

Don't use this property unless you know what are you doing.
By default, it is set to `auto`.

To go deeper than this, please refer to
[Google-Analytics documentation](http://developers.google.com/analytics/devguides/collection/analyticsjs/).


------
**Copyright** (c) 2015,  Khaled Monsoor
All rights reserved.

Licensed under [BSD](https://opensource.org/licenses/BSD-3-Clause) license.
