from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Retrusn a list of APIView freatures"""
        
        an_apiview = [
            'Users HTTP methods as functino (get, post, patch, put, delete',
            'Is similar to a traditional django view',
            'Gives you the most control over the app logic',
            'Is mapped manually to URLs',
        ]
        
        return Response({'message' : 'hello', 'an_apiview': an_apiview})
        