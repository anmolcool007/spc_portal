from django.contrib import admin
from .models import JobAdvertisement, InternshipAdvertisement, InternshipOffer, JobOffer


@admin.register(JobAdvertisement)
class JobAdvertisementAdmin(admin.ModelAdmin):
    class Meta:
        model = JobAdvertisement
        fields = '__all__'


@admin.register(InternshipAdvertisement)
class InternshipAdvertisementAdmin(admin.ModelAdmin):
    class Meta:
        model = InternshipAdvertisement
        fields = '__all__'


@admin.register(InternshipOffer)
class InternshipOfferAdmin(admin.ModelAdmin):
    class Meta:
        model = InternshipOffer
        fields = '__all__'


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    class Meta:
        model = JobOffer
        fields = '__all__'
