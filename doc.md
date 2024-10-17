# Robobyke Project
## OAuth
* Read the documentation [here](https://developer.squareup.com/docs/oauth-api/overview)
### Flows
* There are code and PKCE (Proof Key for Code Exchange flows)
* PKCE is the appropriate option for clients that cannot safely store secrets in the application
* The following terms are used within any of both flows
    * Authorization code - A code that is returned when calling the Authorize endpoint. This code is used to redeem an access token and a refresh token.
    * Access token - A token that grants access to a client's resources and has some privileges attached to it. Access tokens expire after a certain amount of time.
    * Refresh token - A token that is used to generate more access tokens. 
        * If you use the PKCE flow, refresh tokens are single-use tokens and expire after 90 days.
