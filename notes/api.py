from rest_framework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperlinkedModelSerializer):
  def create(self, validate_data):
    user = self.context['request'].user

    note = Note.objects.create(user=user, **validate_data)
    return note
  
  class Meta:
    model = Note 
    fields = ('title', 'content')

class NoteViewSet(viewsets.ModelViewSet):
  serializer_class = NoteSerializer
  queryset = Note.objects.all()