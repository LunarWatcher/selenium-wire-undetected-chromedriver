from seleniumwire_gpl import UndetectedChrome
from time import sleep

def test_requests_intercepted(uchrome: UndetectedChrome):
    uchrome.get("https://www.example.com")
    sleep(1)
    # page + favicon
    # I've observed up to 3 additional requests caused by google phoning home
    assert len(uchrome.requests) >= 2

    req = [ request for request in uchrome.requests  
        if "example.com" in request.url
    ]
    assert len(req) == 2
    page_req = [ request for request in req
        if "favicon" not in request.url
    ]
    assert len(page_req) == 1
    page_req = page_req[0]
    assert page_req.response is not None
    assert page_req.response.status_code == 200
    assert "This domain is for use in illustrative examples in documents" \
        in page_req.response.decompress_body().decode()
