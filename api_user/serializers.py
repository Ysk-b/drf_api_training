from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import Profile, FriendRequest
# serializersは、モデルをJSON形式にシリアライズ（変換）するためのクラス
# 流れとしては urls.py -> views.py -> models.py -> serializers.py -> views.py -> urls.py
class User(serializers.ModelSerializer):
    class Meta:
        # get_user_model() -> 現在のユーザーモデルを取得
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # シリアライズ済のデータを基に新しいユーザーを作成
    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'nickName', 'userPro', 'created_on', 'img')
        extra_kwargs = {'userPro': {'read_only': True}}

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ('id', 'askFrom', 'askTo', 'approved')
        extra_kwargs = {'askFrom': {'read_only': True}}