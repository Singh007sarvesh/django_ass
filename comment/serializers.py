from rest_framework import serializers
from comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
	# file = serializers.FileField(
 #        max_length=None, use_url=True,
 #    )
	comment = serializers.CharField(source='comment_text')
	class Meta:
		model = Comment
		# fields = '__all__'
		fields = ['commentID', 'comment', 'created_at','parent']

	def create(self, validated_data):
		return Comment.objects.create(**validated_data)