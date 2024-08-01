from django.shortcuts import render
from django.views import View
from . comment import Comment
from . serializers.comment_serializer import CommentSerializer
from .serializers.model_serializer import ModelSerializerr
from django.http import HttpResponse

# Create your views here.

class CommentView(View):
    def get(self, request, *args, **kwargs):
        comment = Comment(email="esbonmigiro@gmail.com", content="I'm expert programmer")
        serialized_data = CommentSerializer(comment).data
        print(serialized_data)
        return render(request, 'comments.html', {"comment": serialized_data})

        
class SerializerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login_s.html')
    def post(self, request, *args, **kwargs):
        serializer = ModelSerializerr(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("saved successfully")
        return HttpResponse("Invalid serialzer")

        