from django import forms
from django.core import validators  #inbuilt validators from django recommended to be used instead of creating yourself
from secondApp.models import Webpage, Topic, AccessRecord

def check_for_z(value):

    if value.lower()[0] == 'z':
        raise forms.ValidationError('Z named users not allowed')


class CommentForm(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10), check_for_z])
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label='Enter the email again')

    def clean_botcatcher(self):
        ## clean_particular fieldName to create validation function for that field

        botcatcher = self.cleaned_data['botcatcher']
        print('bot crawling the web page')
        if len(botcatcher) > 0:
            raise forms.ValidationError('Gotcha Bot!!')
        return botcatcher

    def clean(self):
        ### to  clean the entire form fields at once###
        all_clean = super().clean()
        email = all_clean['email']
        vemail = all_clean['verifyEmail']

        if email != vemail:
            raise forms.ValidationError('Emails do not match')


class add_webpage_form(forms.ModelForm):
    # topic = forms.CharField(validators=[validators.MaxLengthValidator(3)])
    # url = forms.URLField(validators=[validators.URLValidator])
    # name = forms.CharField(validators=[validators.MaxLengthValidator(3)])

    class Meta:
        model = Webpage
        fields = '__all__'
