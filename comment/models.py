from django.db import models

# Create your models here.

class Comment(models.Model):
	commentID = models.AutoField(primary_key = True)
	comment_text = models.TextField()
	created_at = models.DateTimeField(null=False)
	updated_at = models.DateTimeField(null=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


	class Meta:
		db_table = "comment"

	# def __str__(self):
	# 	return self.comment_text
