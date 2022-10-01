def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(PostForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['author'].required = False