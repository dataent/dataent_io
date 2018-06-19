<!-- add-breadcrumbs -->
# Adding Custom Domains to your Site

You can add **multiple custom domains** for your site, just run: 

	bench setup add-domain [desired-domain]

On running the command you will be asked for which site you want to set the custom domain for. 

You can also setup SSL for your custom domain by using the options: 

	--ssl-certificate [path-to-certificate]
	--ssl-certificate-key [path-to-certificate-key]

Example: 

	bench setup add-domain custom.epaas.com --ssl-certificate /etc/letsencrypt/live/epaas.cert --ssl-certificate-key /etc/letsencrypt/live/epaas.key

Domain configuration is stored in the respective site's site_config.json

	 "domains": [
	  {
	   "ssl_certificate": "/etc/letsencrypt/live/epaas.cert",
	   "domain": "epaas.com",
	   "ssl_certificate_key": "/etc/letsencrypt/live/epaas.key"
	  }
	 ],

**You will need to regenerate the nginx configuration by runnning `bench setup nginx` and reload the nginx service put your custom domain in effect**