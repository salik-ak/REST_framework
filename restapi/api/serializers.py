from rest_framework import serializers
from .models import CustomUser



  

class UserRegister(serializers.ModelSerializer):

    password2=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = CustomUser
        fields=["password","email","username","phone","dob","password2"]

    def save(self):
        reg=CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            phone=self.validated_data['phone'],
            dob=self.validated_data['dob'],
            # profile_picture=self.validated_data['profile_picture'],
            )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg