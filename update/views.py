from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
from . import forms
from . import models
from . import sshd
import os
import requests
import zipfile
import hashlib
import json


# Create your views here.


def index(request):
    return render(request, 'update/index.html', locals())


#解压缩patch包
def unzip_zipfile(file_dir):
    zipFile = zipfile.ZipFile(file_dir)
    try:
        for file in zipFile.namelist():
            zipFile.extract(file)
        zipFile.close()
        unzip_message = "解压成功"
    except:
        unzip_message = "解压失败"
    return unzip_message


#解压缩patch包方式2
def unzip_zip(file_dir):
	os.system("unzip -o {0}".format(file_dir))



#获取patch包信息，包括项目名，版本，目录名
def get_zip_name(file_dir):
    return (file_dir.split("_"))


#获取patch包下所有子目录文件名
def get_file_name(file_dir):
    list_file = []
    for root, dirs, files in os.walk(file_dir):
        for name in files:
            list_file.append(os.path.join(root, name))
    return list_file

#获取patch包下所有子目录文件名方式2
def get_txt_info(filedir):
    pass
    


#获取patch包下所有子目录名
def get_file_dir(file_dir):
        list_dir = []
        for root, dirs, files in os.walk(file_dir):
            for name in dirs:
                list_dir.append(os.path.join(root.replace(file_dir,file_dir.split("_")[2]), name))
        return list_dir


#下载发布文件
def download(url,patch_zip):
    #下载动作
    ret=os.system("wget -O {0} {1}".format(patch_zip,url))
    if ret == 0:
        download_message = "下载成功"
    else:
        download_message = "下载失败"
    #返回下载zip包名
    return download_message

#下载发布文件方式2
def request_download(url,patch_zip):
    r = requests.get(url)
    try:
        with open(patch_zip, "wb") as code:
            code.write(r.content)
        download_message = "下载成功"
    except:
        download_message = "下载失败"
    return download_message

#md5计算
def file_md5(filename):
    if os.path.isfile(filename):
        fp=open(filename,'rb')
        contents=fp.read()
        fp.close()
        return hashlib.md5(contents).hexdigest()
    else:
        print('file not exists')

#创建目录
def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...  ---")
		print("---  OK  ---")
 
	else:
		print("---  There is this folder!  ---")


#获取待发布任务参数
def patchUpdate(request):
    local_project_form = forms.LocalProjectForm()
    url_form = forms.UpdateFileForm()
    if request.method == 'POST':
    #获取post参数
        local_id=request.POST.get('驻地')
        project_id=request.POST.get('项目')
    #通过post参数查询数据库数据，获取数据对象
        Value = models.local_project_ship.objects.values('last_version','path','backup_path').filter(local_name_id=local_id).filter(project_name_id=project_id)
        Ip = models.host.objects.values_list('name','ip').filter(host_local_id=local_id)
        Project_name = models.project.objects.values('alias_name').filter(id=project_id)
        Local_name = models.local.objects.values('alias_name').filter(id=local_id)
    #获取对象数据
        #获取驻地名和项目名
        list_project_name = list(Project_name)
        list_local_name = list(Local_name)
        project_name = list_project_name[0]['alias_name']
        local_name = list_local_name[0]['alias_name']
        #获取主机IP
        list_host_ip=list(Ip)
        #获取驻地项目信息：最新版本，路径，备份路径
        list_version_path=list(Value)
        #获取下载路径
        url = request.POST.get('升级文件地址')
        #获取下载文件名
        patch_zip = url.split("/")[-1]
        #数据库信息：
        local_info = local_name+"_"+project_name
        #文件信息：
        pkg_info = patch_zip.split("_")[0]+"_"+patch_zip.split("_")[1]+"_"+patch_zip.split("_")[2]
        #校验发布信息
        if local_info == pkg_info:
            check_message = '校验通过!'
            #执行下载任务
            download_message = request_download(url,patch_zip)
            #获取zip包解压目录名
            patch_dir = os.path.splitext(patch_zip)[0]
            #执行解压动作
            unzip_message = unzip_zipfile(patch_zip)
            #执行发布动作
            buckup_message = ''
            create_dir_action_message = ''
            overwrite_action_message = ''
            for ip in list_host_ip:
            #获取主机用户信息
                sshd_info = models.host.objects.values_list('ssh_user_name','ssh_passwd','ssh_port').filter(ip=ip[1])
                host_ssh_info = list(sshd_info)
                ssh_user_name = host_ssh_info[0][0]
                ssh_passwd = host_ssh_info[0][1]
                ssh_port = int(host_ssh_info[0][2])
            #判断是否存在 update.txt
            #获取待发布文件目录路径
                list_update_pkg = get_file_name(patch_dir)
                list_dir_pkg = get_file_dir(patch_dir)
            #快照路径
                snap_path = "snap/"
            #备份项目
                product_host_ip = ip[1]
                product_project_path = list_version_path[0]['path']+list_project_name[0]['alias_name']
                product_project_path_buckup = list_version_path[0]['backup_path']+list_project_name[0]['alias_name']+'_'+list_version_path[0]['last_version']
                buckup_action = "Processing... ssh {0} \"cp -ra {1} {2}\"\n".format(product_host_ip,product_project_path,product_project_path_buckup)
                buckup_message = buckup_message+buckup_action+'\n'
                order = "cp -ra {0} {1}".format(product_project_path,product_project_path_buckup)
                sshd.ssh_order(ip[1],ssh_port,ssh_user_name,ssh_passwd,order)
            #执行发布动作
                update_message = ''
                for k in range(len(list_dir_pkg)):
                    create_dir = list_version_path[0]['path']+list_dir_pkg[k]
                    create_dir_action = "Processing... ssh  {0} \"mkdir -p {1}\"\n".format(product_host_ip,create_dir)
                    create_dir_action_message = create_dir_action_message+create_dir_action+'\n'
                    snap_dir = snap_path+local_info+'/'+list_dir_pkg[k]
                    print(snap_dir)
                    mkdir(snap_dir)
                    order = "mkdir -p {0}".format(create_dir)
                    sshd.ssh_order(ip[1],ssh_port,ssh_user_name,ssh_passwd,order)
                for i in range(len(list_update_pkg)):
                    updateing_file = list_update_pkg[i]
                    product_overwrite_file = list_version_path[0]['path']+list_update_pkg[i].replace(patch_dir,list_project_name[0]['alias_name'])
                    snap_file = snap_path+local_info+'/'+list_update_pkg[i].replace(patch_dir,list_project_name[0]['alias_name'])
                    #下载现网文件
                    sshd.sftp_download(ip[1],ssh_port,ssh_user_name,ssh_passwd,product_overwrite_file,snap_file)
                    #比较文件MD5差异
                    snap_file_MD5 = file_md5(snap_file)
                    overwrite_file_MD5 =file_md5(updateing_file)
                    if snap_file_MD5 != overwrite_file_MD5:
                        overwrite_action = "Processing... scp {0} {1}:{2}\n".format(updateing_file,product_host_ip,product_overwrite_file)
                        overwrite_action_message = overwrite_action_message+overwrite_action+'\n'
                        sshd.sftp_upload(ip[1],ssh_port,ssh_user_name,ssh_passwd,updateing_file,product_overwrite_file)
                        update_message = update_message +'{0}升级完成'.format(updateing_file)+'\n'
                    else:
                        update_message = update_message +'{0}无变化'.format(updateing_file)+'\n'
            #记录发布信息（项目，路径，版本号）
            new_book = models.update_book()
            new_book.local = local_name
            new_book.host = list_host_ip
            new_book.project = project_name
            new_book.patch_file = patch_zip
            new_book.new_version = patch_dir.split("_")[3]
            new_book.last_version = list_version_path[0]
            new_book.save()
            #更新版本信息
            local_project_ship_id = models.local_project_ship.objects.values('id').filter(local_name_id =  local_id).filter(project_name_id =  project_id)
            t_version_update = models.local_project_ship.objects.get(id =  local_project_ship_id)
            t_version_update.last_version=patch_dir.split("_")[3]
            t_version_update.save()
            #增加历史版本
            history = models.history_version()
            history.local_project_ship_id = project_id
            history.version = patch_dir.split("_")[3]
            history.local_project = local_name+"_"+project_name
            history.save()
        else:
            check_message = '校验未通过！，选错驻地，项目，或者补丁包'
    else:        
        return render(request, 'update/patch.html', locals())
    return render(request, 'update/patch.html', locals())

#发布历史记录
def patch(request):
    if request.method == 'POST':
        local_json=eval(request.POST.get('info'))
        request_dict=json.dumps(local_json)
        print(local_json)
        new_book = models.update_book()
        new_book.local = local_json["local"]
        new_book.host = local_json["host"]
        new_book.project = local_json["project"]
        new_book.patch_file = local_json["patchfile"]
        new_book.new_version = local_json["new_version"]
        new_book.last_version = local_json["last_version"]
        new_book.save()
        resp = {'patch_info': request_dict}
    return HttpResponse(json.dumps(resp), content_type="application/json")

#获取历史发布记录
def getbookinfo(request):
    if request.method == 'GET':
        books = models.update_book.objects.all()
        resp = serializers.serialize("json", books)

    return HttpResponse(resp, content_type="application/json")

#获取主机信息
def gethostinfo(request):
    if request.method == 'GET':
        hosts = models.host.objects.select_related('host_local')
        json_list = []
        for host in hosts:
            #print(host.host_local.alias_name)
            json_dict_local = model_to_dict(host.host_local)
            a_name = json_dict_local['alias_name']
            l_name = json_dict_local['name']
            json_dict_host= model_to_dict(host)
            json_dict_host['alias_name'] = a_name
            json_dict_host['l_name'] = l_name
            json_list.append(json_dict_host)
    return HttpResponse(json.dumps(json_list), content_type="application/json")

#重启tomcat
def restart_tomcat(request):
    pass

def hotfix(request):
    return render(request, 'update/hotfix.html', locals())
