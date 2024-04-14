from django.forms import ModelForm

from app.models import Version

class CreatePatientModelForm(ModelForm):
    # validation should be here...

    class Meta:
        model = Version
        fields = '__all__'