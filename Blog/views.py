from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

blogdata = [
    {
        "title": "ফ্রাঙ্কফুর্ট বইমেলা শুরু, থাকছে বাংলাদেশও",
        "content": "জার্মানির ফ্রাঙ্কফুর্টে বইমেলার ৭৫তম আসর বসছে। জার্মানি এবং সেই সঙ্গে বিশ্বের সাহিত্য ও সংস্কৃতিকে এগিয়ে"
                   " নিতে এই মেলার রয়েছে অপরিসীম অবদান",
        "author": "সরাফ আহমেদ",
        "post_datetime": " ১৯ অক্টোবর ২০২৩, ১৯: ০৩",

    },
    {
        "title": "বিশ্ব বাজারে দ্বিতীয় সপ্তাহেও বেড়েছে জ্বালানি তেলের দাম",
        "content": "মধ্যপ্রাচ্যে হামাস-ইসরায়েলের সংঘাতের জেরে দ্বিতীয় সপ্তাহের "
                   "মতো মধ্যপ্রাচ্যের বাজারে বেড়েছে অপরিশোধিত জ্বালানি তেলের দাম। ",
        "author": "সরাফ বাণিজ্য ডেস্ক",
        "post_datetime": "২০ অক্টোবর ২০২৩, ১৭: ১৬ ",

    },

    {
        "title": "২৮ অক্টোবর বিএনপির পরিণতি হবে ১০ ডিসেম্বরের মতো: কাদের",
        "content": "২৮ অক্টোবর বিএনপির পরিণতি ১০ ডিসেম্বরের মতো হবে বলে মন্তব্য করেছেন আওয়ামী লীগের সাধারণ সম্পাদক ওবায়দুল কাদের। তিনি বলেন, "
                   "১০ ডিসেম্বর তারা গোলাপবাগ গরুর হাটের খাদে পড়েছিল, এবার কোথায় যাবে, সেটা দেখার অপেক্ষায়।",
        "author": "বিশেষ প্রতিনিধি, ঢাকা",
        "post_datetime": "২০ অক্টোবর ২০২৩, ১৮: ১৪",

    },

]


def homepage(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


class PostListview(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-post_datetime']


def about(request):
    return render(request, "about.html", {"title": "about page"})


class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_forms.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
