from django.db.models import Q
from rest_framework import generics, mixins

from postings.models import KhassidaPost
from .permissions import IsOwnerOrReadOnly
from .serializers import KhassidaPostSerializer


class KhassidaPostAPIView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = KhassidaPostSerializer
    #queryset                = KhassidaPost.objects.all()

    def get_queryset(self):
        qs = KhassidaPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(title__icontains=query)|
                    Q(file__icontains=query)
                    ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class KhassidaPostRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = KhassidaPostSerializer
    permission_classes      = [IsOwnerOrReadOnly]
    #queryset                = KhassidaPost.objects.all()

    def get_queryset(self):
        return KhassidaPost.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return KhassidaPost.objects.get(pk=pk)
