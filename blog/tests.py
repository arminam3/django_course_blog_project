from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth.models import User


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='ali', password='jfldkgdfhgdflfh')
        cls.post = Post.objects.create(title='this is created title',
                                        body='this is the body',
                                        author=cls.user,
                                        status=Post.STATUS_CHOICES[0][0]
                                        )

        cls.post2 = Post.objects.create(title='this is created title2',
                                        body='this is the body2',
                                        author=cls.user,
                                        status=Post.STATUS_CHOICES[1][0]
                                        )

    def test_post_list_url(self):
        response = self.client.get('/blog/postlist/')
        self.assertEqual(response.status_code, 200)

    def test_post__str(self):
        self.assertEqual(str(self.post), 'this is created title')

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        self.assertEqual(self.post.title, 'this is created title')
        self.assertEqual(self.post.body, 'this is the body')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.status, Post.STATUS_CHOICES[0][0])
        self.assertEqual(self.post2.status, Post.STATUS_CHOICES[1][0])

    def test_post_list_templates(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, 'this is created title')

    def test_post_detail_url(self):
        response = self.client.get(reverse('post_detail', args=[self.post.author.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_templates(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertContains(response, 'this is created title')

    def test_post_detail_error_404(self):
        response = self.client.get(reverse('post_detail', args=[657867]))
        self.assertEqual(response.status_code, 404)

    def test_post_list_template_used(self):
        response = self.client.get(reverse('post_detail', args=[self.post.author.id]))
        self.assertTemplateUsed(response, template_name='blog/post_detail.html')
        self.assertTemplateUsed(response, template_name='_base.html')

    def test_post_pup_check(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse("new_post"), {
            'title': 'new title',
            'body': 'new body',
            'author': self.user.id,
            'status': 'published',

        })
        self.assertEqual(response.status_code, 302)
    def test_post_delete_view(self):
        response = self.client.post(reverse('delete_post', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)

    def test_update_post_view(self):
        response = self.client.post(reverse('update_post', args=[self.post.id]), {
            'title': 'title updated',
            'body': 'body updated',
            'author':self.user.id,
            'status':'published'
        })

        self.assertEqual(response.status_code, 302)
