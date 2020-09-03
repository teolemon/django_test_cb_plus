from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as u


def validate_digit_length(gtin):
    if not (len(str(gtin)) == 13): 
    	raise ValidationError(u"gtin must be 13 digits.",params={'gtin': gtin})
