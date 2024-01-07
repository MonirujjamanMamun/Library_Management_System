from .models import BookReview
from django.core.validators import MaxValueValidator
from django import forms
from .models import BooksModel


class BooksForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        # fields = '__all__'
        exclude = ['borrower', 'borrow',]


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['rating']  # Add other fields if needed

    rating = forms.IntegerField(
        validators=[MaxValueValidator(5)],
        widget=forms.NumberInput(attrs={'min': 0, 'max': 5})
    )

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 0 or rating > 5:
            raise forms.ValidationError('Rating must be between 0 and 5.')
        return rating
