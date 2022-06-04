from django import forms
from .models import Question,Category

class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Question
        posts = Category.objects.order_by('id')
        fields = '__all__'
                
        # fields = ('status' ,'category_system' ,'category_detail','questioner','question_title','question_contents','answer')
        widgets = {
        #     'status': forms.TextInput(),
            # 'category_system': forms.ChoiceField,
        #     'category_detail': forms.TextInput(),
        #     'questioner': forms.TextInput(),
            # 'question_title': forms.TextInput(),
        #     'question_contents': forms.TextInput(),
        #     'answer': forms.TextInput(),
        }
        labels = {
            'status':'状態',
            'category_system':'大項目',
            'category_detail':'中項目',
            'questioner':'質問者',
            'question_title':'タイトル',
            'question_contents':'質問内容',
            'answer':'回答',
            'tags':'検索タグ',
        }

QuestionFormSet = forms.modelformset_factory(
    Question, form=QuestionForm, extra=1, max_num=10
)