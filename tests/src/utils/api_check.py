import http
import requests
from requests.exceptions import ConnectionError
import backoff


class ApiCheck:

    @backoff.on_predicate(backoff.fibo, max_value=10)
    @backoff.on_exception(backoff.expo, ConnectionError)
    def ping(self) -> bool:
        response = requests.get("http://api:8000" + '/api/v1/health/check')
        if response.status_code == http.HTTPStatus.OK:
            return True
        return False


ApiCheck().ping()