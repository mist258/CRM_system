from rest_framework import serializers

from .models import CommentsModel


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentsModel
        fields = ('id',
                  'text',
                  'order',
                  )

        read_only_fields = ('id',
                            'created_at',
                            'order',
                            )
        