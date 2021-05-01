from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = {
            "review",
            "auccuracy",
            "communication",
            "cleanliness",
            "location",
            "check_in",
            "value",
        }