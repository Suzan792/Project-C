from paypal.standard.forms import PayPalPaymentsForm

from django import forms
from django.utils.html import format_html

class PayPalForm(PayPalPaymentsForm):
    form_action = "request_to_paypal/"
    image = "{% static '/paypal/paypal-button-white'%}"
    
    def render(self):
        return format_html(
            u"""
            <form action="{0}" method="post">
            {1}
            <input type="image" src="{2}" border="0" name="submit" alt="Buy it Now" />
            </form>
            """, 
            self.form_action, self.as_p(), self.image)
    