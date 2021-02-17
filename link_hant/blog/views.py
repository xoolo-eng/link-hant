from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog, Tags


class AllBlogs(ListView):
    model = Blog
    template_name = "blogs.html"
    paginate_by = 3

    def get_queryset(self):
        if self.request.GET.get("tag"):
            return self.model.objects.filter(tags__name=self.request.GET.get("tag"))
        return super().get_queryset()


class OneBlog(DetailView):
    model = Blog
    template_name = "blog.html"

    # def get_context_data(self, **kwargs):
        # # Call the base implementation first to get a context
        # context = super().get_context_data(**kwargs)
        # # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        # return context
