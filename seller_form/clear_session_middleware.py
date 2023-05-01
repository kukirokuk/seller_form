class ClearSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Clear the session data on every page refresh
        request.session.flush()
        
        response = self.get_response(request)

        return response