from rest_framework.serializers import CharField, ModelSerializer

from users.models import City, CustomUser
from weather.serializers import CitySerializer


class RegisterCustomUserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    native_city = CitySerializer()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'native_city')

    def create(self, validated_data):
        city_data = validated_data.pop('native_city')
        city_instance, _ = City.objects.get_or_create(city_name=city_data['city_name'])
        user = CustomUser.objects.create(native_city=city_instance, **validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user


class CustomUserSerializer(ModelSerializer):
    native_city = CitySerializer()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'native_city')

    def update(self, instance, validated_data):
        city = validated_data.pop('native_city')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if city:
            city_name = city.get('city_name')
            city_instance, _ = City.objects.get_or_create(city_name=city_name)
            instance.native_city = city_instance

        instance.save()
        return instance
