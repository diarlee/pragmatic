from django.shortcuts import render
from django.urls import reverse

from django.views.generic import CreateView, DeleteView

from commentApp.models import Comment
from commentApp.forms import CommentCreateForm
from articleApp.models import Article
from django.utils.decorators import method_decorator
from commentApp.decorators import comment_ownership_required
# Create your views here.

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'commentApp/create.html'

    def form_valid(self, form):

        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk':self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentApp/delete.html'

    def get_success_url(self):
        return reverse('articleApp:detail', kwargs={'pk': self.object.article.pk})

