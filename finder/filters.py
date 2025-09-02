import django_filters

from .models import Museum


class MuseumFilter(django_filters.FilterSet):
    class Meta:
        model = Museum
        fields = {
            'city': {'exact'},
            'name': {'icontains'},
            'category': {'icontains'},
            
            }

# = or __icontains= in url