from django import forms


class AttendanceForm(forms.Form):

    student_name = forms.CharField(max_length=100)

    roll_number = forms.CharField(max_length=20)

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    status = forms.ChoiceField(
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent')
        ]
    )


class SearchForm(forms.Form):

    roll_number = forms.CharField(max_length=20)