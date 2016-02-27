from django import forms
from django.forms.formsets import BaseFormSet
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from .models import CustomUser, Item, Category, ItemPhoto
from .models import CONDITION_OF_ITEM, WAY_OF_DEAL


from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


User = get_user_model()

# # Apply summernote to specific fields.
# class SomeForm(forms.Form):
#     foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea


class ItemPhotoForm(forms.ModelForm):

    class Meta:
        model = ItemPhoto
        exclude = ('item',)

class ItemForm(forms.ModelForm):

    category = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                          queryset=Category.objects.all())

    vendor = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                    queryset=User.objects.all())

    deal_way = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=WAY_OF_DEAL)

    condition = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=CONDITION_OF_ITEM)

    class Meta:
        model = Item
        exclude = ('created_at', 'updated_at', )



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'nickname')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'nickname', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

# class ItemPhotoFormset(BaseFormSet):
#
#