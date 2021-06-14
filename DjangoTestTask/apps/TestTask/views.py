import os
from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from .models import Pic
from django.urls import reverse
from PIL import Image
from .forms import URLPicForm, SizeForm
from datetime import datetime
import requests


def index(request):
    all_pics = Pic.objects.order_by('-id')
    return render(request, 'TestTask/list.html', {'all_pics': all_pics})


def d(request, path):
    path = 'static/' + path
    if path:
        os.remove(path)
    return HttpResponseRedirect(reverse('TestTask:index'))


def add_pic(request):
    error = ''
    if request.method == 'POST':
        url_form = URLPicForm(request.POST)
        if request.FILES != {} and request.POST['url'] == '':
            blob_pic = request.FILES['pic'].read()
            name = str(request.FILES['pic'])
            try:
                with open('static/TestTask/img/' + name, 'wb') as file:
                    file.write(blob_pic)
                pic = Pic(pic='TestTask/img/' + name, name=name,
                          width=Image.open('static/TestTask/img/' + name).size[0],
                          height=Image.open('static/TestTask/img/' + name).size[1])
                pic.save()
                return HttpResponseRedirect(reverse('TestTask:exact_pic', args=(pic.id,)))
            except:
                os.remove('static/TestTask/img/' + name)
                error = 'Ваш файл не является изображением!'
        elif url_form.is_valid() and request.FILES == {}:
            remote_pic = requests.get(request.POST['url'])
            if remote_pic and "image" in remote_pic.headers['content-type']:
                url_form.save()
                pic = Pic.objects.order_by('-id')[0]
                file_name = str(datetime.now()).replace('.', '-').replace(':', '-') + '.' + \
                            remote_pic.headers['content-type'][6:]
                file = open('static/TestTask/temp/' + file_name, 'wb')
                file.write(remote_pic.content)
                file.close()
                pic.name = file_name
                pic.width = Image.open('static/TestTask/temp/' + file_name).size[0]
                pic.height = Image.open('static/TestTask/temp/' + file_name).size[1]
                pic.save()
                os.remove('static/TestTask/temp/' + file_name)
                return HttpResponseRedirect(reverse('TestTask:exact_pic', args=(pic.id,)))
            elif "image" not in remote_pic.headers['content-type']:
                error = 'Ваша ссылка - не ссылка на изображение!'
            else:
                raise Http404("Страница по вашей ссылке не найдена!")
        else:
            error = 'Некорректные данные!'
    else:
        url_form = URLPicForm()
    return render(request, 'TestTask/add_pic.html', {'url_form': url_form, 'error': error})


def pic_size(path):
    im = Image.open(path)
    width = im.size[0]
    height = im.size[1]
    return {'width': width, 'height': height}


def create_copy(pic):
    path = "static/TestTask/temp/" + str(datetime.now()).replace('.', '-').replace(':', '-') + pic.name
    if pic.pic:
        with open('static/' + pic.pic, 'rb') as file:
            with open(path, 'wb') as out:
                out.write(file.read())
    else:
        with open(path, 'wb') as file:
            file.write(requests.get(pic.url).content)
    return path


def exact_pic(request, pic_id):
    try:
        pic = Pic.objects.get(id=pic_id)
    except:
        raise Http404("Изображение не найдено!")
    error = ''
    try:
        if request.method == 'POST' and 'old_path' in request.POST:
            path = 'static/' + request.POST['old_path']
            print(path)
        if 'path' not in locals():
            path = create_copy(pic)
        if request.method == 'POST':
            form = SizeForm(request.POST)
            if request.POST['width'] != '' or request.POST['height'] != '':
                if int(request.POST['width']) != pic_size(path)['width'] and int(request.POST['height']) != \
                        pic_size(path)['height']:
                    if int(request.POST['width']) >= int(request.POST['height']):
                        width, height = pic.width, pic.height
                        new_width = int(request.POST['width'])
                        new_height = int(new_width * height / width)
                        im = Image.open(path)
                        im = im.resize((new_width, new_height), Image.ANTIALIAS)
                        im.save(path)
                        form = SizeForm({'width': new_width, 'height': new_height})
                        return render(request, 'TestTask/exact_pic.html', {'pic': pic, 'form': form, 'path': path[7:],
                                                                           'error': error})
                    else:
                        width, height = pic.width, pic.height
                        new_height = int(request.POST['height'])
                        new_width = int(new_height * width / height)
                        im = Image.open(path)
                        im = im.resize((new_width, new_height), Image.ANTIALIAS)
                        im.save(path)
                        form = SizeForm({'width': new_width, 'height': new_height})
                        return render(request, 'TestTask/exact_pic.html', {'pic': pic, 'form': form, 'path': path[7:],
                                                                           'error': error})
                elif int(request.POST['width']) != pic_size(path)['width']:
                    width, height = pic.width, pic.height
                    new_width = int(request.POST['width'])
                    new_height = int(new_width * height / width)
                    im = Image.open(path)
                    im = im.resize((new_width, new_height), Image.ANTIALIAS)
                    im.save(path)
                    form = SizeForm({'width': new_width, 'height': new_height})
                    return render(request, 'TestTask/exact_pic.html', {'pic': pic, 'form': form, 'path': path[7:],
                                                                       'error': error})
                elif int(request.POST['height']) != pic_size(path)['height']:
                    width, height = pic.width, pic.height
                    new_height = int(request.POST['height'])
                    new_width = int(new_height * width / height)
                    im = Image.open(path)
                    im = im.resize((new_width, new_height), Image.ANTIALIAS)
                    im.save(path)
                    form = SizeForm({'width': new_width, 'height': new_height})
                    return render(request, 'TestTask/exact_pic.html', {'pic': pic, 'form': form, 'path': path[7:],
                                                                       'error': error})
                else:
                    return render(request, 'TestTask/exact_pic.html', {'pic': pic, 'form': form, 'path': path[7:],
                                                                       'error': error})
            else:
                error = 'Введите корректные данные!'
                form = SizeForm({'width': pic_size(path)['width'], 'height': pic_size(path)['height']})
                return render(request, 'TestTask/exact_pic.html', {'pic': pic, 'form': form, 'path': path[7:],
                                                                   'error': error})
        else:
            form = SizeForm({'width': pic.width, 'height': pic.height})
            return render(request, 'TestTask/exact_pic.html', {'pic': pic, 'form': form, 'path': path[7:],
                                                               'error': error})
    except:
        error = 'Поля не могут быть пустыми и не могут содержать дробные числа!'
        form = SizeForm({'width': pic_size(path)['width'], 'height': pic_size(path)['height']})
        return render(request, 'TestTask/exact_pic.html', {'pic': pic, 'form': form, 'path': path[7:], 'error': error})
