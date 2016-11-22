# -*- coding: utf-8 -*-
from django import forms

from forum.models import Article

error_messages = {
    'title': {
        'required': u'必须填写标题',
        'max_length': u'标题长度过长',
    },
    'content': {
        'required': u'必须填写内容',
    }
}


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 表单对应的model
        fields = ['title', 'content']


class ReplyForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea,
                              error_messages=error_messages.get('content'))
