import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse
from .models import *
from django.core.paginator import Paginator


def index(request):
    dict = {
        'Header': {
            'status': 0,
            'msg': '查询成功'
        },
        'Content': {
        }
    }

    if request.method == 'GET':

        blogclass = []

        classx = Category.objects.values('id', 'name')

        for jsonx in classx:
            blogclass.append(jsonx)

        dict['Content'] = {'blogclass': blogclass}

        return JsonResponse(dict)
    else:
        dict['Header']['status'] = 101
        dict['Header']['msg'] = '参数错误'

        return JsonResponse(dict)

# def overall_situation():
#     # 顶部导航栏...
#     top_class_list = Category.objects.all()  # 获取所有的博客分类...
#     top_tag_list = Tag.objects.all()  # 获取所有的博客标签...
#
#     # 侧边导航栏
#     side_notice = Custom.objects.values('values').filter(name='公告').first()  # 获取自定义变中名字为公告的对象
#     side_new_blog_list = Blog.objects.values('title', 'id').order_by('-pub')[:5]  # 获取所有的博客目录按时间排序...
#     side_hot_reading_list = Blog.objects.values('title', 'id').order_by('-views')[:5]  # 获取所有的博客目录按阅读量排序...
#     side_new_comment_list = Comment.objects.all().order_by('-pub')[:3]  # 获取最新的前5条评论...
#
#     return {
#         'top_class_list': top_class_list,
#         'top_tag_list': top_tag_list,
#         'side_notice': side_notice,
#         'side_new_blog_list': side_new_blog_list,
#         'side_hot_Reading_list': side_hot_reading_list,
#         'side_new_Comment_list': side_new_comment_list,
#     }
#
#
# # 博客首页...
# def blog_home(request):
#     # 分页功能...
#     page = request.GET.get('page')
#     blog_list = Blog.objects.all().order_by('-pub')  # 获取所有博客按时间排序...
#     blog_list = Paginator(blog_list, 4)  # 定义每页显示的数量...
#     blog_list = blog_list.get_page(page)
#
#     data = {
#         'blog_list': blog_list,
#     }
#     data.update(overall_situation())
#
#     # 传递参数到固定页面...
#     return render(request, 'blog/blog_home.html', data)


# # 博客详情...
# def blog_details(request, blog_id):
#     # 检查异常...
#     try:
#         # 获取固定的blog_id的对象...
#         blog = Blog.objects.get(id=blog_id)
#         blog.increase_views()
#     except Blog.DoesNotExist:
#         raise Http404('博客已被删除或丢失!')
#
#     if request.method == 'GET':
#
#     else:
#         # 验证当前是否已登陆...
#         if request.user.is_authenticated:
#             # 请求方法为Post时，执行下面方法...
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 comment_count = Comment.objects.filter(blog_id=blog_id).count()  # 获取固定blog_id的评论数量...
#                 floor = comment_count + 1  # 给评论数加1做到盖楼效果...
#                 cleaned_data = form.cleaned_data
#                 cleaned_data['blog'] = blog
#                 Comment.objects.create(**cleaned_data,
#                                        name=request.user.username,
#                                        email=request.user.email,
#                                        floor=floor)
#         else:
#             return redirect('/accounts/login/')
#
#     blog_tag = Tag.objects.filter(blog=blog.id).values('name'),  # 获取固定blog_id的标签...
#     blog_comments = blog.comment_set.all().order_by('-pub'),  # 获取评论列表按时间排序...
#
#     data = {
#         'blog': blog,
#         'blog_tag': blog_tag,
#         'blog_comments': blog_comments,
#         'form': form,
#     }
#     data.update(overall_situation())
#
#     # 传递参数到固定页面...
#     return render(request, 'blog/blog_details.html', data)
#
#
# # 博客标签列表...
# def blog_tag_list(request, tag_id):
#     # 分页功能...
#     page = request.GET.get('page')
#     blog_list = Blog.objects.filter(tag=tag_id).order_by('-pub')  # 获取固定tag_id的博客...
#     blog_list = Paginator(blog_list, 4)  # 定义每页显示的数量...
#     blog_list = blog_list.get_page(page)
#
#     blog_tag = Tag.objects.values('name').filter(id=tag_id).first()  # 获取固定tag_id的标签...
#
#     data = {
#         'blog_list': blog_list,
#         'blog_tag': blog_tag,
#     }
#     data.update(overall_situation())
#
#     # 传递参数到固定页面...
#     return render(request, 'blog/blog_tag.html', data)
#
#
# # 博客分类列表...
# def blog_category_list(request, category_id):
#     # 分页功能
#     page = request.GET.get('page')
#     blog_list = Blog.objects.filter(category=category_id).order_by('-pub')  # 获取固定category_id的博客...
#     blog_list = Paginator(blog_list, 4)  # 定义每页显示的数量...
#     blog_list = blog_list.get_page(page)
#
#     data = {
#         'blog_list': blog_list,
#     }
#     data.update(overall_situation())
#
#     # 传递参数到固定页面...
#     return render(request, 'blog/blog_category.html', data)
