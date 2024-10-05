from rest_framework import serializers # type: ignore
from .models import Student


#with ModelSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

# #without ModelSerializer
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255, validators=[starts_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=255)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance


#     #field level validation
        
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value

#     #object level validaton

#     def validate(self,data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
#             raise serializers.ValidationError('city must be ranchi')
#         return data
    

#     # validators
#     def starts_with_r(value):
#         if value[0].lower() != 'r':
#             raise serializers.ValidationError('Name should starts with R')