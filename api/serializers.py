from rest_framework import serializers, viewsets



from dreametrix.models import School, User


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ('id',)
        write_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["password", "email"]


    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user





