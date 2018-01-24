from django.forms import ClearableFileInput


class ChangedClearableFileInput(ClearableFileInput):
    template_name = 'users/forms/widgets/clearable_file_input.html'
