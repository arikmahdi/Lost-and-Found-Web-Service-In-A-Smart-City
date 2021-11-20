from django.contrib import admin

# Register your models here.

from .models import LostPet
admin.site.register(LostPet)

from .models import FoundPet
admin.site.register(FoundPet)

from .models import LostObject
admin.site.register(LostObject)

from .models import FoundObject
admin.site.register(FoundObject)


from .models import LostPerson
admin.site.register(LostPerson)

from .models import FoundPerson
admin.site.register(FoundPerson)