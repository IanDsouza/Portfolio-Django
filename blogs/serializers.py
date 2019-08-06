from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('id', 'name', 'paradigm', 'image')

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['id', 'title','author','post','rank','image','like','comments']

class Skillerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class  ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True)
    class Meta:
        model = Project
        fields = ['id', 'title','start_date','end_date','discription','images']

class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic
        fields = '__all__'
