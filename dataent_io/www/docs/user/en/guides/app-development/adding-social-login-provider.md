<!-- add-breadcrumbs -->
# Adding Social Login Provider

This guide discusses how to add a social login provider to dataent via pull request.

### Add your provider in `SocialLoginKey.get_social_login_provider`

```
providers["Dataent"] = {
	"provider_name": "Dataent",
	"enable_social_login": 1,
	"custom_base_url": 1,
	"icon":"/assets/dataent/images/favicon.png",
	"redirect_url": "/api/method/dataent.www.login.login_via_dataent",
	"api_endpoint": "/api/method/dataent.integrations.oauth2.openid_profile",
	"api_endpoint_args":None,
	"authorize_url": "/api/method/dataent.integrations.oauth2.authorize",
	"access_token_url": "/api/method/dataent.integrations.oauth2.get_token",
	"auth_url_data": json.dumps({
		"response_type": "code",
		"scope": "openid"
	})
}
```

### Add provider key in exact same type case in options of `social_login_provider` select field on `Social Login Key` DocType. e.g. `Dataent`

Once the user adds a social login provider and enables it the `Authorization Code` is sent back by the provider api server on to the redirect_url mentioned on the same server. You will have to add a whitelisted method allowing guest access in `dataent.integrations.oauth2_logins`. e.g. `login_via_office365` 

There many implementations of OAuth 2.0 + OpenID Connect. Here we'll discuss two ways of accessing openid information.

#### User Creation via OpenID Profile Endpoint

example:

```
@dataent.whitelist(allow_guest=True)
def login_via_dataent(code, state):
	login_via_oauth2("dataent", code, state, decoder=json.loads)
```

#### User Creation via id_token

example:

```
@dataent.whitelist(allow_guest=True)
def login_via_office365(code, state):
	login_via_oauth2_id_token("office_365", code, state, decoder=json.loads)
```
