from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    category = serializers.CharField()
    price = serializers.IntegerField()
    rating = serializers.FloatField()

    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid")
        return data