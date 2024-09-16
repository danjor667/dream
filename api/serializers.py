from rest_framework import serializers, viewsets



from dreametrix.models import School




class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ('id',)
        write_only_fields = ('id',)


