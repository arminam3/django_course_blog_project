from django.shortcuts import render,redirect, get_object_or_404, reverse
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import NewPostForm, UpdatePostForm



class PostListView(generic.ListView):
    # model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return  Post.objects.filter(status='published').order_by('-date_edit')

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(generic.CreateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_new_post.html'
    # success_url = '/blog/newpost/'

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'blog/post_update_post.html'
    form_class = UpdatePostForm


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete_post.html'
    success_url = reverse_lazy("post_list")
    # def get_success_url(self):
    #     return reverse('post_list')



# def post_list_view(request):
#     post_list = Post.objects.filter(status='published').order_by('-date_edit')
#     context = {
#         "post_list": post_list
#     }
#     return render(request, 'blog/post_list.html', context)

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     context = {
#         "post": post
#     }
#     return render(request, 'blog/post_detail.html', context)


# def new_post_view(request):
#     if request.method == "POST":
#         new_post_form = NewPostForm(request.POST)
#         if new_post_form.is_valid():
#             new_post = new_post_form.save()
#             return redirect("post_list")
#
#     else:
#         new_post_form = NewPostForm()
#     context = {
#         'new_post_form':  new_post_form,
#     }
#
#     return render(request, 'blog/post_new_post.html', context)



# def update_post_view(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     post_form = UpdatePostForm(request.POST or None,instance=post)
#     if post_form.is_valid():
#         print("is_valid")
#         post_form.save()
#         return redirect(reverse("post_detail", args=[post.id]))
#     context={
#         "post_form": post_form,
#         "post": post
#     }
#     print("not valid")
#     return render(request, "blog/post_update_post.html", context)


# def delete_post_view(request, pk):
#     post=get_object_or_404(Post, id=pk)
#     print(request.method)
#     if request.method =="POST":
#         post.delete()
#         return redirect("post_list")
#     else:
#         return render(request, 'blog/post_delete_post.html',{'post':post})





