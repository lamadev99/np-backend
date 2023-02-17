from rest_framework import serializers
from api.models import *

class WriterPorfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        fields = ["url","fname", "lname", "bio", "image", "fUrl", "tUrl", "iUrl"]
        
class NewsSerializer(serializers.HyperlinkedModelSerializer):
    slug=serializers.ReadOnlyField()
    class Meta:
        model=News
        fields="__all__"

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    cId=serializers.ReadOnlyField()
    class Meta:
        model=Comment
        fields="__all__"

class NewsSubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    nsId=serializers.ReadOnlyField()
    class Meta:
        model=NewsSubscription
        fields="__all__"