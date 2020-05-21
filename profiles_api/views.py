from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers



class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    print('in class')
    print('The Serializer Class value is ' + str(serializer_class))


    def get(self,request,format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'user HTTP Method as functions (get, Post, Patch, put, delete)',
            'is similar to a traditional View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=self.request.data)
        print(serializer)
        print('After Serializer')


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            print(name)
            age = serializer.validated_data.get('age')
            message = f'Hello {name}! Your Age is {age}'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request, pk=None):
        """Handle a partial update of an object"""
        return Response ({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response ({'method':'DELETE'})
