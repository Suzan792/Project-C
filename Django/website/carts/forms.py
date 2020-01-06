from paypal.standard.forms import PayPalPaymentsForm

from django import forms
from django.utils.html import format_html

class PayPalForm(PayPalPaymentsForm):
    form_action = "request_to_paypal/"
    
    def render(self):
        return format_html(
            u"""
            <form action="{0}" method="post">
            {1}
            <button class="btn btn-primary mb-2" type="submit">Checkout with PayPal</button>
            </form>
            """, 
            self.form_action, self.as_p())
    