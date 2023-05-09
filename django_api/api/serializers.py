from rest_framework import serializers
from api.models import Snippet,CATEGORIES_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    Name = serializers.CharField()
    Email_ID = serializers.CharField(style={'base_template':'textarea.html'})
    Phone_number = serializers.CharField()
    Subject = serializers.CharField()
    Categories = serializers.ChoiceField(choices=CATEGORIES_CHOICES,default = 'Car')
    Description = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name','instance.Name')
        instance.Email_ID = validated_data.get('Email_ID','instance.Email_ID')
        instance.Phone_number = validated_data.get('Phone_number','instance.Phone_number')
        instance.Subject = validated_data.get('Subject','instance.Subject')
        instance.Categories = validated_data.get('Categories','instance.Categories')
        instance.Description = validated_data.get('Description','instance.Description')
        instance.save()
        return instance
    
    class Meta:
        model = Snippet
        fields = ['Name','Email_ID','Phone_number','Subject','Categories','Description']