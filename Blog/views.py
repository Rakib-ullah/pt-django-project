from django.shortcuts import render

blogdata = [
    {
        "title": "ফ্রাঙ্কফুর্ট বইমেলা শুরু, থাকছে বাংলাদেশও",
        "content": "জার্মানির ফ্রাঙ্কফুর্টে বইমেলার ৭৫তম আসর বসছে। জার্মানি এবং সেই সঙ্গে বিশ্বের সাহিত্য ও সংস্কৃতিকে এগিয়ে"
                   " নিতে এই মেলার রয়েছে অপরিসীম অবদান",
        "author": "সরাফ আহমেদ",
        "post_datetime": " ১৯ অক্টোবর ২০২৩, ১৯: ০৩",

    }

]


def homepage(request):
    return render(request, "home.html", {"blogdata": blogdata})


def about(request):
    return render(request, "about.html", {"title": "about page"})
