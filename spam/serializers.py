from spam.models import Contact
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = '__all__'

    # def validate_email(self, email):
    #     if Contact.objects.filter(email=email).exists():
    #         raise serializers.ValidationError('Вы уже подписаны!')
    #     return email\

    def create(self, validated_data):
        if Contact.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError('Вы уже подписаны!')
        return super().create(validated_data)