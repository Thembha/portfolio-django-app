from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileModelTests(TestCase):                                                                                        
    @classmethod                                                                                                          
    def setUpTestData(cls):                                                                                               
        User.objects.create()                                                                                                                                                                                   

    def test_profile(self):                                                                                    
        profile = User.objects.last().profile