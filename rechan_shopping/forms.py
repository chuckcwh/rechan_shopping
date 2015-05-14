from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from rechan_shopping.models import Member, Contact, Tag, Product, Ads


class MemberForm(UserCreationForm):
    real_name = forms.CharField(required=True)

    class Meta:
        model = Member
        fields = ("username", "password1", "password2", "real_name", "email")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def save(self, commit=True):
        user = super(MemberForm, self).save(commit=commit)
        return user


class ContactForm(forms.Form):
    recipient = forms.CharField(required=True)
    tel = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = Contact
        fields = ("recipient", 'tel', 'address')


class TagForm(forms.Form):
    tag_name = forms.CharField()

    class Meta:
        model = Tag
        fields = ("tag_name")


class ProductForm(forms.Form):
    cat_choice = (
        ('Toys', 'Toys'),
        ('Candies', 'Candies'),
        ('Lucky_draw', 'Lucky_draw')
    )
    category = forms.ChoiceField(choices=cat_choice)
    name = forms.CharField(help_text='')
    brand = forms.CharField(help_text='')
    description = forms.CharField()
    tags = forms.ModelChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Product
        fields = ("category", "name", "brand", "description", "tags", "photo")


class AdsForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()

    class Meta:
        model = Ads
        fields = ("title", "description", "image")
