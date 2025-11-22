from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'description', 'requirements',
            'location', 'salary', 'job_type', 'deadline'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g., Senior Backend Engineer',
                'class': 'w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all hover:border-blue-400'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe the role, responsibilities, tech stack, etc.',
                'class': 'w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all hover:border-blue-400'
            }),
            'requirements': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'List qualifications and skills required',
                'class': 'w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all hover:border-blue-400'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'e.g., Remote or Bangalore, IN',
                'class': 'w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all hover:border-blue-400'
            }),
            'salary': forms.TextInput(attrs={
                'placeholder': 'e.g., ₹12–18 LPA or $120k–$160k',
                'class': 'w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all hover:border-blue-400'
            }),
            'job_type': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all hover:border-blue-400'
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all hover:border-blue-400'
            }),
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Write your cover letter here...'}
            )
        }

class JobSearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Job title or keyword'}
    ))
    location = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Location'}
    ))
    category = forms.ChoiceField(required=False)
    job_type = forms.ChoiceField(
        required=False,
        choices=[('', 'All Types')] + Job.JOB_TYPE_CHOICES
    )

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary', 'job_type']