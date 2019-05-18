1.首页
2.类别页
3.搜索页
4.博客文章展示页
5.按标签显示页
urlpatterns = [
  url(r'',views.index,name='index'),#首页展示
  url(r'^category-<int:lid>.html',views.category,name='category'),#按类别展示
  url(r'^show-<int:sid>.html',views.show,name='show'),#展示文章内容
  url(r'^tag/',views.tag,name='tags'),#标签列表页
  url(r'^s/',views.search,name='search')
]
