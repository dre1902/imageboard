from django import forms

class OpPostForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=20, required=False)
    name = forms.CharField(label='Name', max_length=20, required=False)
    text = forms.CharField(label='Post', max_length=2000)
    image = forms.ImageField()

class PostForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20, required=False)
    text = forms.CharField(label='Post', max_length=2000, required=False)
    image = forms.ImageField(required=False)

    # to allow text OR an image
    def clean(self):
        clean_data = super().clean()
        if not (clean_data.get('text') is not None or clean_data.get(image) is not None):
            raise ValidationError("Post requires text or an image.")
        return clean_data