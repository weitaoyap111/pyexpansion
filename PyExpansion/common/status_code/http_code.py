HTTP_100 = {"100": "Continue"}
HTTP_101 = {"101": "Switching Protocols"}
HTTP_102 = {"102": "Processing"}
HTTP_103 = {"103": "Early Hints"}

HTTP_1xx_OFFICIAL = dict()
HTTP_1xx_OFFICIAL.update(HTTP_100)
HTTP_1xx_OFFICIAL.update(HTTP_101)
HTTP_1xx_OFFICIAL.update(HTTP_102)
HTTP_1xx_OFFICIAL.update(HTTP_103)

HTTP_200 = {"200": "OK"}
HTTP_201 = {"201": "Created"}
HTTP_202 = {"202": "Accepted"}
HTTP_203 = {"203": "Non-Authoritative Information"}
HTTP_204 = {"204": "No Content"}
HTTP_205 = {"205": "Reset Content"}
HTTP_206 = {"206": "Partial Content"}
HTTP_207 = {"207": "Multi-Status"}
HTTP_208 = {"208": "Already Reported"}
HTTP_226 = {"226": "IM Used"}

HTTP_2xx_OFFICIAL = dict()
HTTP_2xx_OFFICIAL.update(HTTP_200)
HTTP_2xx_OFFICIAL.update(HTTP_201)
HTTP_2xx_OFFICIAL.update(HTTP_202)
HTTP_2xx_OFFICIAL.update(HTTP_203)
HTTP_2xx_OFFICIAL.update(HTTP_204)
HTTP_2xx_OFFICIAL.update(HTTP_205)
HTTP_2xx_OFFICIAL.update(HTTP_206)
HTTP_2xx_OFFICIAL.update(HTTP_207)
HTTP_2xx_OFFICIAL.update(HTTP_208)
HTTP_2xx_OFFICIAL.update(HTTP_226)

HTTP_300 = {"300": "Multiple Choices"}
HTTP_301 = {"301": "Moved Permanently"}
HTTP_302 = {"302": "Found"}
HTTP_303 = {"303": "See Other"}
HTTP_304 = {"304": "Not Modified"}
HTTP_305 = {"305": "Use Proxy"}
HTTP_306 = {"306": "Switch Proxy"}
HTTP_307 = {"307": "Temporary Redirect"}
HTTP_308 = {"308": "Permanent Redirect"}

HTTP_3xx_OFFICIAL = dict()
HTTP_3xx_OFFICIAL.update(HTTP_300)
HTTP_3xx_OFFICIAL.update(HTTP_301)
HTTP_3xx_OFFICIAL.update(HTTP_302)
HTTP_3xx_OFFICIAL.update(HTTP_303)
HTTP_3xx_OFFICIAL.update(HTTP_304)
HTTP_3xx_OFFICIAL.update(HTTP_305)
HTTP_3xx_OFFICIAL.update(HTTP_306)
HTTP_3xx_OFFICIAL.update(HTTP_307)
HTTP_3xx_OFFICIAL.update(HTTP_308)

HTTP_400 = {"400": "Bad Request"}
HTTP_401 = {"401": "Unauthorized"}
HTTP_402 = {"402": "Payment Required"}
HTTP_403 = {"403": "Forbidden"}
HTTP_404 = {"404": "Not Found"}
HTTP_405 = {"405": "Method Not Allowed"}
HTTP_406 = {"406": "Not Acceptable"}
HTTP_407 = {"407": "Proxy Authentication Required"}
HTTP_408 = {"408": "Request Timeout"}
HTTP_409 = {"409": "Conflict"}
HTTP_410 = {"410": "Gone"}
HTTP_411 = {"411": "Length Required"}
HTTP_412 = {"412": "Precondition Failed"}
HTTP_413 = {"413": "Payload Too Large"}
HTTP_414 = {"414": "URI Too Long"}
HTTP_415 = {"415": "Unsupported Media Type"}
HTTP_416 = {"416": "Range Not Satisfiable"}
HTTP_417 = {"417": "Expectation Failed"}
HTTP_418 = {"418": "I'm a teapot"}
HTTP_421 = {"421": "Misdirected Request"}
HTTP_422 = {"422": "Unprocessable Entity"}
HTTP_423 = {"423": "Locked"}
HTTP_424 = {"424": "Failed Dependency"}
HTTP_425 = {"425": "Too Early"}
HTTP_426 = {"426": "Upgrade Required"}
HTTP_428 = {"428": "Precondition Required"}
HTTP_429 = {"429": "Too Many Requests"}
HTTP_431 = {"431": "Request Header Fields Too Large"}
HTTP_451 = {"451": "Unavailable For Legal Reasons"}

HTTP_4xx_OFFICIAL = dict()
HTTP_4xx_OFFICIAL.update(HTTP_400)
HTTP_4xx_OFFICIAL.update(HTTP_401)
HTTP_4xx_OFFICIAL.update(HTTP_402)
HTTP_4xx_OFFICIAL.update(HTTP_403)
HTTP_4xx_OFFICIAL.update(HTTP_404)
HTTP_4xx_OFFICIAL.update(HTTP_405)
HTTP_4xx_OFFICIAL.update(HTTP_406)
HTTP_4xx_OFFICIAL.update(HTTP_407)
HTTP_4xx_OFFICIAL.update(HTTP_408)
HTTP_4xx_OFFICIAL.update(HTTP_409)
HTTP_4xx_OFFICIAL.update(HTTP_410)
HTTP_4xx_OFFICIAL.update(HTTP_411)
HTTP_4xx_OFFICIAL.update(HTTP_412)
HTTP_4xx_OFFICIAL.update(HTTP_413)
HTTP_4xx_OFFICIAL.update(HTTP_414)
HTTP_4xx_OFFICIAL.update(HTTP_415)
HTTP_4xx_OFFICIAL.update(HTTP_416)
HTTP_4xx_OFFICIAL.update(HTTP_417)
HTTP_4xx_OFFICIAL.update(HTTP_418)
HTTP_4xx_OFFICIAL.update(HTTP_421)
HTTP_4xx_OFFICIAL.update(HTTP_422)
HTTP_4xx_OFFICIAL.update(HTTP_423)
HTTP_4xx_OFFICIAL.update(HTTP_424)
HTTP_4xx_OFFICIAL.update(HTTP_425)
HTTP_4xx_OFFICIAL.update(HTTP_426)
HTTP_4xx_OFFICIAL.update(HTTP_428)
HTTP_4xx_OFFICIAL.update(HTTP_429)
HTTP_4xx_OFFICIAL.update(HTTP_431)
HTTP_4xx_OFFICIAL.update(HTTP_451)

HTTP_500 = {"500": "Server Internal Error"}
HTTP_501 = {"501": "Not Implemented"}
HTTP_502 = {"502": "Bad Gateway"}
HTTP_503 = {"503": "Service Unavailable"}
HTTP_504 = {"504": "Gateway Timeout"}
HTTP_505 = {"505": "HTTP Version Not Supported"}
HTTP_506 = {"506": "Variant Also Negotiates"}
HTTP_507 = {"507": "Insufficient Storage"}
HTTP_508 = {"508": "Loop Detected"}
HTTP_510 = {"510": "Not Extended"}
HTTP_511 = {"511": "Network Authentication Required"}

HTTP_5xx_OFFICIAL = dict()
HTTP_5xx_OFFICIAL.update(HTTP_500)
HTTP_5xx_OFFICIAL.update(HTTP_501)
HTTP_5xx_OFFICIAL.update(HTTP_502)
HTTP_5xx_OFFICIAL.update(HTTP_503)
HTTP_5xx_OFFICIAL.update(HTTP_504)
HTTP_5xx_OFFICIAL.update(HTTP_505)
HTTP_5xx_OFFICIAL.update(HTTP_506)
HTTP_5xx_OFFICIAL.update(HTTP_507)
HTTP_5xx_OFFICIAL.update(HTTP_508)
HTTP_5xx_OFFICIAL.update(HTTP_510)
HTTP_5xx_OFFICIAL.update(HTTP_511)

HTTP_STANDARD = dict()
HTTP_STANDARD.update(HTTP_1xx_OFFICIAL)
HTTP_STANDARD.update(HTTP_2xx_OFFICIAL)
HTTP_STANDARD.update(HTTP_3xx_OFFICIAL)
HTTP_STANDARD.update(HTTP_4xx_OFFICIAL)
HTTP_STANDARD.update(HTTP_5xx_OFFICIAL)

HTTP_419 = {"419": "Page Expired (Laravel Framework)"}
HTTP_420 = {"420": "Method Failure (Spring Framework)"}
# HTTP_420 = {"420": "Enhance Your Calm (Twitter)"}
HTTP_430 = {"430": "Request Header Fields Too Large (Shopify)"}
HTTP_450 = {"450": "Blocked by Windows Parental Controls (Microsoft)"}
HTTP_498 = {"498": "Invalid Token (Esri)"}
HTTP_499 = {"499": "Token Required (Esri)"}
HTTP_509 = {"509": "Bandwidth Limit Exceeded (Apache Web Server/cPanel)"}
HTTP_529 = {"529": "Site is overloaded (Qualys)"}
HTTP_530 = {"530": "Site is frozen (Pantheon Systems)"}
HTTP_598 = {"598": "(Informal convention) Network read timeout error"}
HTTP_599 = {"599": "Network Connect Timeout Error"}
HTTP_440 = {"440": "Login Time-out (IIS)"}
HTTP_449 = {"449": "Retry With (IIS)"}
HTTP_451 = {"451": "Redirect (IIS)"}
HTTP_444 = {"444": "No Response (nginx)"}
HTTP_494 = {"494": "Request header too large (nginx)"}
HTTP_495 = {"495": "SSL Certificate Error (nginx)"}
HTTP_496 = {"496": "SSL Certificate Required (nginx)"}
HTTP_497 = {"497": "HTTP Request Sent to HTTPS Port (nginx)"}
# HTTP_499 = {"499": "Client Closed Request"}
HTTP_520 = {"520": "Web Server Returned an Unknown Error (Cloudflare)"}
HTTP_521 = {"521": "Web Server Is Down (Cloudflare)"}
HTTP_522 = {"522": "Connection Timed Out (Cloudflare)"}
HTTP_523 = {"523": "Origin Is Unreachable (Cloudflare)"}
HTTP_524 = {"524": "A Timeout Occurred (Cloudflare)"}
HTTP_525 = {"525": "SSL Handshake Failed (Cloudflare)"}
HTTP_526 = {"526": "Invalid SSL Certificate (Cloudflare)"}
HTTP_527 = {"527": "Railgun Error (Cloudflare)"}
# HTTP_530 = {"530": "returned along with a 1xxx error (Cloudflare)"}
HTTP_460 = {"460": "Client closed the connection with the load balancer before the idle timeout period elapsed. (AWS)"}
HTTP_463 = {"463": "The load balancer received an X-Forwarded-For request header with more than 30 IP addresses. (AWS)"}
HTTP_464 = {"464": "Incompatible protocol versions between Client and Origin server. (AWS)"}
HTTP_561 = {"561": "Unauthorized (AWS)"}
HTTP_110 = {"110": "Response is Stale"}
HTTP_111 = {"111": "Revalidation Failed"}
HTTP_112 = {"112": "Disconnected Operation"}
HTTP_113 = {"113": "Heuristic Expiration"}
HTTP_199 = {"199": "Miscellaneous Warning"}
HTTP_214 = {"214": "Transformation Applied"}
HTTP_299 = {"299": "Miscellaneous Persistent Warning"}

HTTP_NOT_STANDARD = dict()
HTTP_NOT_STANDARD.update(HTTP_419)
HTTP_NOT_STANDARD.update(HTTP_420)
# HTTP_420 = {"420": "Enhance Your Calm (Twitter)"}
HTTP_NOT_STANDARD.update(HTTP_430)
HTTP_NOT_STANDARD.update(HTTP_450)
HTTP_NOT_STANDARD.update(HTTP_498)
HTTP_NOT_STANDARD.update(HTTP_499)
HTTP_NOT_STANDARD.update(HTTP_509)
HTTP_NOT_STANDARD.update(HTTP_529)
HTTP_NOT_STANDARD.update(HTTP_530)
HTTP_NOT_STANDARD.update(HTTP_598)
HTTP_NOT_STANDARD.update(HTTP_599)
HTTP_NOT_STANDARD.update(HTTP_440)
HTTP_NOT_STANDARD.update(HTTP_449)
HTTP_NOT_STANDARD.update(HTTP_451)
HTTP_NOT_STANDARD.update(HTTP_444)
HTTP_NOT_STANDARD.update(HTTP_494)
HTTP_NOT_STANDARD.update(HTTP_495)
HTTP_NOT_STANDARD.update(HTTP_496)
HTTP_NOT_STANDARD.update(HTTP_497)
# HTTP_499 = {"499": "Client Closed Request"}
HTTP_NOT_STANDARD.update(HTTP_520)
HTTP_NOT_STANDARD.update(HTTP_521)
HTTP_NOT_STANDARD.update(HTTP_522)
HTTP_NOT_STANDARD.update(HTTP_523)
HTTP_NOT_STANDARD.update(HTTP_524)
HTTP_NOT_STANDARD.update(HTTP_525)
HTTP_NOT_STANDARD.update(HTTP_526)
HTTP_NOT_STANDARD.update(HTTP_527)
# HTTP_530 = {"530": "returned along with a 1xxx error (Cloudflare)"}
HTTP_NOT_STANDARD.update(HTTP_460)
HTTP_NOT_STANDARD.update(HTTP_463)
HTTP_NOT_STANDARD.update(HTTP_464)
HTTP_NOT_STANDARD.update(HTTP_561)
HTTP_NOT_STANDARD.update(HTTP_110)
HTTP_NOT_STANDARD.update(HTTP_111)
HTTP_NOT_STANDARD.update(HTTP_112)
HTTP_NOT_STANDARD.update(HTTP_113)
HTTP_NOT_STANDARD.update(HTTP_199)
HTTP_NOT_STANDARD.update(HTTP_214)
HTTP_NOT_STANDARD.update(HTTP_299)
