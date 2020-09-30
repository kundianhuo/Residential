from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods

from .models import Community, User
from Residential import utils, settings
from .forms import CommunityModelForm
from django.core.paginator import Paginator


# Create your views here.
def list(request):
    name = request.GET.get("name", None)
    if name:
        nums = Community.objects.filter(state=True, name__contains=name).count()
    else:
        nums = Community.objects.filter(state=True).count()

    # 获取总页码
    pages = (nums - 1) // settings.PAGE_SIZE + 1;

    return render(request, "community/list.html", locals())


def list_data(request):
    communities = Community.objects.filter(state=True)

    if request.GET.get("name", None):
        communities = communities.filter(name__contains=request.GET.get("name"))

    communities = communities.order_by("-create_time").values()

    paginator = Paginator(communities, settings.PAGE_SIZE)

    page = paginator.page(request.GET.get("page", 1))

    # 获取总页数、和当前页的数据
    nums = communities.count()

    data = [obj for obj in page.object_list]

    return JsonResponse(data={"nums": nums, "communities": data, "pages": paginator.num_pages},
                        json_dumps_params={"ensure_ascii": True})


def add(request):
    if request.method == "GET":
        # 查询所有的管理员
        users = User.objects.values("username", "pk")

        return render(request, "community/add.html", locals())

    # 获取提交的所有数据
    form = CommunityModelForm(data=request.POST)

    if form.is_valid():
        # 设置小区的编码，自动生成、采用  XXX-YY-NNNNN
        form.instance.code = utils.community_code()

        # 设置状态 为 True
        form.instance.state = True

        form.save()

        return JsonResponse(data={"status": True, "info": "新增小区成功"})

    return JsonResponse(data={"status": False, "info": "参数错误、新增数据失败！"})


def update(request):
    if request.method == "GET":
        # 查询所有的管理员
        users = User.objects.values("username", "pk")

        # 查询 小区所有信息
        id = request.GET.get("id")

        community = Community.objects.get(pk=id)

        return render(request, "community/update.html", locals())

    # 获取要修改的小区
    community = Community.objects.get(pk=request.POST.get("id"))
    # 创建form
    # 获取提交的所有数据
    form = CommunityModelForm(data=request.POST, instance=community)
    if form.is_valid():
        # 设置小区的编码，自动生成、采用  XXX-YY-NNNNN

        # 设置状态 为 True
        form.instance.state = True
        form.save()

        return JsonResponse(data={"status": True, "info": "修改小区成功"})

    return JsonResponse(data={"status": False, "info": "参数错误、修改数据失败！"})


@csrf_exempt
def upload(request):
    # 获取上传的文件对象
    file = request.FILES.get("images")

    # 将文件写入到服务器中、并返回写入的路径
    path = utils.write_upload_img("community", file)

    # 返回结果
    return JsonResponse(data={"status": True, "image_name": path})


@csrf_exempt
@require_http_methods(["DELETE"])
def batch_del(request):
    # 获取 删除的的 Id (request.JSON 自己封装的 JsonRequestMiddleware中间键)
    ids = request.JSON

    from datetime import datetime
    # 删除数据
    Community.objects.filter(pk__in=ids).update(state=False, del_time=datetime.now())

    return JsonResponse(data={"status": True, "info": "删除成功"})


@csrf_exempt
@require_http_methods(["PUT"])
def status_update(request, pk, status):
    Community.objects.filter(pk=pk).update(status=status)

    return JsonResponse(data={"status": True, "info": "更改状态成功"})
