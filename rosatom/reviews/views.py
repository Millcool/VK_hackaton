from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from .rating import rating_for_text, predict_pos_neg
from .models import User

def index_page(request):
    return render(request, 'index.html')

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            # perform sentiment analysis on the text to determine rating and positivity
            rating = rating_for_text()
            positive = predict_pos_neg()
            print(rating,positive)
            review = Review(text=text, rating=rating, positive=positive)
            review.save()
            return redirect('review')
    else:
        form = ReviewForm()
    if request.method == 'GET':
        form = ReviewForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data['text']
            # perform sentiment analysis on the text to determine rating and positivity
            rating = rating_for_text()
            positive = predict_pos_neg()
            review = Review(text=text, rating=rating, positive=positive)
            review.save()
            return redirect('review')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})
def user_table(request):
    users = User.objects.all()
    return render(request, 'user_table.html', {'users': users})