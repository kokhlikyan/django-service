from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        Prefetch(
            "client",
            to_attr="client",
            queryset=Client.objects.all().only("company_name", "user__email"),
        )
    )
    serializer_class = SubscriptionSerializer
