import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, RaterForm, RaterLoginForm
from django.core.mail import EmailMessage
from rally import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
