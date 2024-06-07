from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework import status

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
