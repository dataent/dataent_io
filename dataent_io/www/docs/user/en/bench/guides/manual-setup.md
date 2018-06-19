<!-- add-breadcrumbs -->
# Manual Setup

Manual Setup
--------------

Install pre-requisites,

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [MariaDB](https://mariadb.org/)
* [Redis](http://redis.io/topics/quickstart)
* [WKHTMLtoPDF with patched QT](http://wkhtmltopdf.org/downloads.html) (required for pdf generation)

[Installing pre-requisites on OSX](https://github.com/dataent/bench/wiki/Installing-Bench-Pre-requisites-on-MacOSX)

Install bench as a *non root* user,

		git clone https://github.com/dataent/bench bench-repo
		sudo pip install -e bench-repo

Note: Please do not remove the bench directory the above commands will create


Migrating from existing installation
------------------------------------

If want to migrate from EPAAS version 3, follow the instructions [here](https://github.com/dataent/bench/wiki/Migrating-from-EPAAS-version-3)

If want to migrate from the old bench, follow the instructions [here](https://github.com/dataent/bench/wiki/Migrating-from-old-bench)


Basic Usage
===========

* Create a new bench

	The init command will create a bench directory with dataent framework
	installed. It will be setup for periodic backups and auto updates once
	a day.

		bench init dataent-bench && cd dataent-bench

* Add apps

	The get-app command gets and installs dataent apps. Examples:
	
	- [epaas](https://github.com/dataent/epaas)
	- [epaas_shopify](https://github.com/dataent/epaas_shopify)
	- [paypal_integration](https://github.com/dataent/paypal_integration)
	
	bench get-app epaas https://github.com/dataent/epaas

* Add site

	Frappé apps are run by dataent sites and you will have to create at least one
	site. The new-site command allows you to do that.

		bench new-site site1.local

* Start bench

	To start using the bench, use the `bench start` command

		bench start

	To login to Frappé / EPAAS, open your browser and go to `localhost:8000`

	The default user name is "Administrator" and password is what you set when you created the new site.


Setting Up EPAAS
==================

To install EPAAS, simply run:
```
bench install-app epaas
```

You can now either use `bench start` or [setup the bench for production use](setup-production.html)



