from django import forms
from .models import Question

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['author', 'text']

        widgets={
            'author': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition resize-none', 'placeholder': 'Enter your name (optional)' }),

            'text': forms.Textarea(attrs={'class': 'px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition resize-none w-full h-40', 'placeholder': 'Enter your question here...'}),

        }