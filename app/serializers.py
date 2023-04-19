from rest_framework import serializers

from .models import Position, Employee


class PositionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    position = serializers.CharField(max_length=20)
    department = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.position = validated_data['position']
        instance.department = validated_data['department']
        instance.save()
        return instance

def pos_chioces():
    position_choices = []
    for position in Position.objects.all():
        position_choices.append((position.id, position.position))
    return position_choices


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(max_length=50)
    birth_date = serializers.DateField()
    position = serializers.CharField(max_length=20)
    salary = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)



    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.birth_date = validated_data['birth_date']
        instance.position = validated_data['position']
        instance.salary = validated_data['salary']
        instance.save()
        return instance