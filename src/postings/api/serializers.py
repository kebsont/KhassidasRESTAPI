from rest_framework import serializers

from postings.models import KhassidaPost


class KhassidaPostSerializer(serializers.ModelSerializer): # forms.ModelForm
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = KhassidaPost
        fields = [
            'url',
            'id',
            'user',
            'title',
            'category',
            'file',
            'coverImage',
            'timestamp',
        ]
        read_only_fields = ['id', 'user']

        #convert to json
        #validation for data passed
    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def validate_title(self, value):
        qs = KhassidaPost.objects.filter(title__iexact=value) # including instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value
