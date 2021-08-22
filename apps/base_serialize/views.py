from django.shortcuts import render
from .serializers import CommentSerializer
from .models import Comment
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

# Create your views here.
def basic_serialize(request):
    comment = Comment(email='leila@example.com', content='foo bar')
    print(f"{comment=}")
    
    serializer = CommentSerializer(comment)
    print(f"{serializer.data=}")
    
    # Serialize into json
    json = JSONRenderer().render(serializer.data)
    print(f"{json=}") # binary

    # Deserialize
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream) 
    print(f"{data=}, {type(data)}")# python type


    return JsonResponse(serializer.data)