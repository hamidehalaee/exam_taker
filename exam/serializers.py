from rest_framework import serializers
from .models import Exam, ExamTaker,User

class ExamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class authorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTaker
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user