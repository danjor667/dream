from rest_framework import serializers, viewsets



from dreametrix.models import School, Admin


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ('id',)
        write_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["password", "email"]




