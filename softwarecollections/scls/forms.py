from django.forms import ModelForm, RadioSelect
from django.utils.translation import ugettext_lazy as _

from .models import SoftwareCollection

POLICY_CHOICES = tuple((s, s) for s in [
    '''**Developing** - this is just for my testing purposes and it probably does not work yet.
And if this works I will put here update soon, which will most likely break it.
    ''',
    '''**Quick and Dirty** - I made this collection just for myself and few
of my colleagues. Do not expect bug-fixes, security patches or any kind of support.
    ''',
    '''**Just Works** - I plan to use this collection very often. You may
expect bug-fixes here. But only if my time allows me.
    ''',
    '''**Professional** - I will maintain this collections regularly. All fixes
will be done in timely manner. And security fixes will be back-ported as soon
as possible.
    ''',
])

class CreateForm(ModelForm):

    class Meta:
        model = SoftwareCollection
        fields = ['username', 'name', 'policy']
        widgets = {
            'policy': RadioSelect(choices=POLICY_CHOICES),
        }

