from rest_framework import serializers
from .models import Task

#Este archivo se encarga de serializar y deserializar la información del modelo Task

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)



class TaskSerializer(serializers.ModelSerializer):

    category = ChoiceField(choices=Task.CATEGORIES)

    class Meta:
        model = Task
        fields = '__all__'