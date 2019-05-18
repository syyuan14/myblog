from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Category, Banner, Article, Tag, Link

# 首页


def index(request):
    allcategory = Category.objects.all()  # 用于导航栏文章类别
    banner = Banner.objects.filter(is_active=True)[0:4]  # 用以轮播图
    tui = Article.objects.filter(tui__id=1)[:3]  # 用以首页推荐
    allarticle = Article.objects.all().order_by('-id')[:9]  # 用以首页展示
    hot = Article.objects.all().order_by('views')[:9]  # 热门文章排行
    PopularReco = Article.objects.filter(tui__id=2)[:6]  # 热门推荐
    alltag = Tag.objects.all()  # 所有标签
    friendly_link = Link.objects.all()  # 友情链接
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'tui': tui,
        'allarticle': allarticle,
        'hot': hot,
        'PopularReco': PopularReco,
        "alltag": alltag,
        'friendly_link': friendly_link,
    }
    return render(request, 'index.html', context)

# 列表页


def list(request, lid):
    article_list = Article.objects.filter(category__id=lid)  # 获取当前文章类别的文章
    cname = Category.objects.get(id=lid)  # 获取当前类别的名字
    remen = Article.objects.filter(tui__id=2)[:5]  # 获取热门推荐文章
    allcategory = Category.objects.all()  # 获取所有的分类
    tags = Tag.objects.all()  # 获取所有的标签
    page = request.GET.get("page")  # 在url中获取当前页面数
    paginator = Paginator(article_list, 5)  # 对查询到的数据对象进行分页,设置超过五条数据就分页
    try:
        page_list = paginator.page(page)
    except PageNotAnInteger:
        page_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第一页内容
    except EmptyPage:
        # 如果用户输入的页数不在系统的页码列表中,显示最后一页
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'list.html', locals())
# 内容页


def show(request, sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 导航上的分栏
    tags = Tag.objects.all()  # 右侧的所有标签
    remen = Article.objects.filter(tui__id=2)[:5]  # 右侧热门推荐
    hot = Article.objects.all().order_by("?")[:10]  # 内容下面的您可能感兴趣文章,随机推荐
    previous_blog = Article.objects.filter(
        created_time__lt=show.created_time, category=show.category.id).last()
    next_blog = Article.objects.filter(
        created_time__gt=show.created_time, category=show.category.id).first()
    show.views = show.views + 1
    show.save()
    return render(request, "show.html", locals())

# 标签页
def tag(request, tag):
    article_list = Article.objects.filter(tags__name=tag)  # 获取当前文章类别的文章
    cname = Tag.objects.get(name=tag)  # 获取当前标签的名字
    remen = Article.objects.filter(tui__id=2)[:5]  # 获取热门推荐文章
    allcategory = Category.objects.all()  # 获取所有的分类
    tags = Tag.objects.all()  # 获取所有的标签
    page = request.GET.get("page")  # 在url中获取当前页面数
    paginator = Paginator(article_list, 5)  # 对查询到的数据对象进行分页,设置超过五条数据就分页
    try:
        page_list = paginator.page(page)
    except PageNotAnInteger:
        page_list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第一页内容
    except EmptyPage:
        # 如果用户输入的页数不在系统的页码列表中,显示最后一页
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'tags.html', locals())

# 搜索页
def search(request):
    ss = request.GET.get("search")#获取当前搜索关键词
    article_list = Article.objects.filter(title__icontains=ss)#获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get("page")
    tags = Tag.objects.all()
    paginator = Paginator(article_list,10)
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return render(request,'search.html',locals())
# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request,'page.html',locals())
