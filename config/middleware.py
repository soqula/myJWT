# middleware.py
import logging
import time

per_logger = logging.getLogger('performance-logger')

class PerformanceMiddlware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # 前処理
        self.before_request(request)
        # ビューの処理
        response = self.get_response(request)
        # 後処理
        response = self.after_response(request, response)
        return response

    def before_request(self, request):
        start_time = time.time()
        request.start_time = start_time
        # per_logger.info(f'process_request:{request.get_full_path()}: {start_time}s')
        per_logger.info(f'bef_request:{request.get_full_path()}:')

    def after_response(self, request, response):
        response_time = round(time.time() - request.start_time,3)
        # print("after_response:" + str(response_time))
        per_logger.info(f'aft_response:{request.get_full_path()}: {response_time}s status:{response.status_code}')
        return response
