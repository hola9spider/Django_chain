from rest_framework import serializers
from app1.models import App

class AppSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = App
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    def create(self, validated_data):
        return App.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos',instance.linenos)
        instance.language = validated_data.get('language',instance.language)
        instance.style = validated_data.get('style',instance.style)
        instance.save()
        return instance


