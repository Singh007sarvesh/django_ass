from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import HttpResponse, JsonResponse
from comment.models import Comment
from . import serializers
from django.core import serializers as cs
from rest_framework import status
import json
import datetime
# Create your views here.

class CommentView(APIView):
    
    # View to list all comments.

    def get(self, request, format=None):
        """
        Return a list of all comments.
        """
        comment = list(Comment.objects.values())
        return JsonResponse(comment, safe=False, status=status.HTTP_200_OK)

    # Create Comment
    def post(self, request, format=None):
    	data = json.loads(request.body)
    	current_datetime = datetime.datetime.now()
    	data['created_at'] = current_datetime
    	if data['commentID'] != '':
    		data['parent'] = int(data['commentID'])
    		comment = serializers.CommentSerializer(data=data)
    		if comment.is_valid(raise_exception=True):
    			comment.validated_data
    			comment.save()
    		return JsonResponse({'id':comment.data['commentID'],'comment':comment.data['comment']}, 
	    		status=status.HTTP_201_CREATED)
    	else:
	    	comment = serializers.CommentSerializer(data=data)
	    	if comment.is_valid(raise_exception=True):
	    		comment.validated_data
	    		comment.save()
	    	return JsonResponse({'id':comment.data['commentID'],'comment':comment.data['comment']}, 
	    		status=status.HTTP_201_CREATED)

    # update comment value based on id
    def put(self, request, id, format=None):
    	data = json.loads(request.body)
    	current_datetime = datetime.datetime.now()
    	db_res = Comment.objects.filter(pk=id).update(comment_text=data['comment'], updated_at=current_datetime)
    	if db_res !=0:
    		return JsonResponse({"commentID":id,"comment":data['comment']}, status=status.HTTP_200_OK)
    	else:
    		return JsonResponse({'response':'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)

   	# delete comment value based on id 
    def delete(self, request, id, format=None):
    	db_res = Comment.objects.filter(pk=id).delete()
    	if db_res[0] != 0:
    		return JsonResponse({'response':'Deleted Successfully'}, status=status.HTTP_200_OK)
    	else:
    		return JsonResponse({'response':'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
