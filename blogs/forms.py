from django import forms

from .models import Blog, UserSettings

class BlogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'A title for your blog...'})
        self.fields['title'].label = False
        self.fields['subdomain'].widget.attrs.update({'placeholder': 'Preferred subdomain...'})
        self.fields['subdomain'].label = False

    class Meta:
        model = Blog
        fields = ('title', 'subdomain')


class DashboardCustomisationForm(forms.ModelForm):
    dashboard_styles = forms.CharField(
        widget=forms.Textarea(),
        label="Dashboard styles",
        required=False,
        help_text="Change the way your dashboard looks and feels with CSS."
    )

    dashboard_footer = forms.CharField(
        widget=forms.Textarea(),
        label="Dashboard footer content",
        required=False,
        help_text="Add scripts and other footer content to your dashboard."
    )

    class Meta:
        model = UserSettings
        fields = ('dashboard_styles', 'dashboard_footer')


class NavForm(forms.ModelForm):
    nav = forms.CharField(
        label="Nav",
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}),
        help_text='''<span>Add navigation links in
                    <a href='https://herman.bearblog.dev/markdown-cheatsheet/#links' target='_blank'>
                        markdown
                    </a>
                    <br>
                    [Home](/) [About me](/about-me/) [Blog](/blog/)
                    <br>
                    To add a page to the nav menu set the link value to the link of a published post or page</span>
                    ''',
        required=False,
    )

    class Meta:
        model = Blog
        fields = ('nav',)


class StyleForm(forms.ModelForm):
    custom_styles = forms.CharField(
        label="Edit theme CSS",
        widget=forms.Textarea(),
        required=False,
        help_text="Ensure styling caters to existing dark mode CSS."
    )

    class Meta:
        model = Blog
        fields = ('custom_styles', )


class AdvancedSettingsForm(forms.ModelForm):
    analytics_active = forms.BooleanField(
        label="Collect analytics",
        required=False,
        help_text="Disable to not collect read analytics"
    )

    fathom_site_id = forms.CharField(
        max_length=20,
        required=False,
        help_text="<span>More in-depth analytics using <a href='https://usefathom.com/ref/GMAGWL' target='_blank'>Fathom</a>.</span>"
    )

    robots_txt = forms.CharField(
        widget=forms.Textarea(),
        label="robots.txt content",
        required=False,
        help_text="This will be appended to the mandatory robots.txt content. View yours at example.bearblog.dev/robots.txt"
    )

    class Meta:
        model = Blog
        fields = ('analytics_active', 'fathom_site_id', 'blog_path', 'rss_alias', 'robots_txt')


class AnalyticsForm(forms.ModelForm):
    fathom_site_id = forms.CharField(
        max_length=20,
        required=False,
        help_text="8 upper-case characters"
    )

    class Meta:
        model = Blog
        fields = ('fathom_site_id',)


class PostTemplateForm(forms.ModelForm):
    post_template = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 20, 'cols': 40, 'placeholder': "title: \nmeta_description: \n___\nHello world!"}),
        required=False,
        label='',
        help_text="This will pre-populate on all new posts. Separate header and body content with ___ (3 underscores)."
    )

    class Meta:
        model = Blog
        fields = ('post_template',)
