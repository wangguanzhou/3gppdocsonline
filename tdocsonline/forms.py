from django import forms

WORKGROUP_CHOICES = (
	('SA2', 'SA2'),
	('RAN2', 'RAN2'),
)

SA2_MEETING_CHOICES = (
	('118bis', '118bis'),
	('118', '118'),
	('117', '117'),
)

RAN2_MEETING_CHOICES = (
	('AH_NR1', 'AH_NR1'),
	('96', '96'),
	('95bis', '95bis'),
)


XGPP_MEETING_LIST = {
	'SA2': SA2_MEETING_CHOICES,
	'RAN2': RAN2_MEETING_CHOICES,
}

class TdocFilterForm(forms.Form):
	work_group = forms.ChoiceField(choices=(), label='', \
				 widget=forms.Select(attrs={'onchange': 'this.form.submit();',\
											'class': 'uk-select uk-form-width-small uk-form-small'}))
	meeting_no = forms.ChoiceField(choices=(), label='', \
				 widget=forms.Select(attrs={'class': 'uk-select uk-form-width-small uk-form-small'}))

	tdoc_source = forms.ChoiceField(choices=(), label='', \
				  widget=forms.Select(attrs={'class': 'uk-select uk-form-width-small uk-form-small'}))
	tdoc_agenda_item = forms.ChoiceField(choices=(), label='', \
				       widget=forms.Select(attrs={'class': 'uk-select uk-form-width-small uk-form-small'}))
	tdoc_workitem = forms.ChoiceField(choices=(), label='', \
				    widget=forms.Select(attrs={'class': 'uk-select uk-form-width-small uk-form-small'}))
	tdoc_release = forms.ChoiceField(choices=(), label='', \
				   widget=forms.Select(attrs={'class': 'uk-select uk-form-width-small uk-form-small'}))
	tdoc_type = forms.ChoiceField(choices=(), label='', \
				widget=forms.Select(attrs={'class': 'uk-select uk-form-width-small uk-form-small'}))


MEETING_REPORT_LIST = {
	'SA2': ['118bis',
			'118',
			'117',
			'116bis',
			'116',
			'115',
			'114',
			'113',
			],
	'RAN2':['',
			],
}
			
