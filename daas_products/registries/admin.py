# daas_products/admin.py

from django.contrib import admin
from .models import Gender, Salutation, MaritalStatus, EducationLevel, Position, Specialisation, Region, Zone, Woreda, Kebele, DevelopmentAgent
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class GenderResource(resources.ModelResource):
    class Meta:
        model = Gender

class GenderAdmin(ImportExportModelAdmin):
    resource_class = GenderResource

admin.site.register(Gender, GenderAdmin)


class SalutationResource(resources.ModelResource):
    class Meta:
        model = Salutation

class SalutationAdmin(ImportExportModelAdmin):
    resource_class = SalutationResource

admin.site.register(Salutation, SalutationAdmin)


class MaritalStatusResource(resources.ModelResource):
    class Meta:
        model = MaritalStatus

class MaritalStatusAdmin(ImportExportModelAdmin):
    resource_class = MaritalStatusResource

admin.site.register(MaritalStatus, MaritalStatusAdmin)


class EducationLevelResource(resources.ModelResource):
    class Meta:
        model = EducationLevel

class EducationLevelAdmin(ImportExportModelAdmin):
    resource_class = EducationLevelResource

admin.site.register(EducationLevel, EducationLevelAdmin)


class PositionResource(resources.ModelResource):
    class Meta:
        model = Position

class PositionAdmin(ImportExportModelAdmin):
    resource_class = PositionResource

admin.site.register(Position, PositionAdmin)

class SpecialisationResource(resources.ModelResource):
    class Meta:
        model = Specialisation

class SpecialisationAdmin(ImportExportModelAdmin):
    resource_class = SpecialisationResource

admin.site.register(Specialisation, SpecialisationAdmin)

class RegionResource(resources.ModelResource):
    class Meta:
        model = Region

class RegionAdmin(ImportExportModelAdmin):
    resource_class = RegionResource

admin.site.register(Region, RegionAdmin)


class ZoneResource(resources.ModelResource):
    class Meta:
        model = Zone

class ZoneAdmin(ImportExportModelAdmin):
    resource_class = ZoneResource

admin.site.register(Zone, ZoneAdmin)


class WoredaResource(resources.ModelResource):
    class Meta:
        model = Woreda

class WoredaAdmin(ImportExportModelAdmin):
    resource_class = WoredaResource

admin.site.register(Woreda, WoredaAdmin)


class KebeleResource(resources.ModelResource):
    class Meta:
        model = Kebele

class KebeleAdmin(ImportExportModelAdmin):
    resource_class = KebeleResource

admin.site.register(Kebele, KebeleAdmin)


class DevelopmentAgentResource(resources.ModelResource):
    class Meta:
        model = DevelopmentAgent

class DevelopmentAgentAdmin(ImportExportModelAdmin):
    resource_class = DevelopmentAgentResource

admin.site.register(DevelopmentAgent, DevelopmentAgentAdmin)
