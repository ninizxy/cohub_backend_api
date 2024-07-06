from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
import requests
import re
from bs4 import BeautifulSoup

def regular_string(s):
    return s.replace("\\u002F", "/").replace("\\u0026", "&")

def get_title_from_link(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    response = requests.get(link, headers=headers)
    response.encoding = 'utf-8'  # 确保正确的编码
    html = response.text

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 根据实际页面结构提取标题
    title_tag = soup.find('title')
    title = title_tag.text.strip() if title_tag else "未知标题"

    return title

def get_image_urls_from_meta_tags(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    response = requests.get(link, headers=headers)
    response.encoding = 'utf-8'  # 确保正确的编码
    html = response.text

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 提取 og:image 元标签中的图片链接
    # 转义特殊字符
    og_images = soup.find_all('meta', {'name': re.escape('og:image')})
    if og_images:
        image_urls = [img['content'] for img in og_images if 'content' in img.attrs][0]
    else:
        image_urls = ["N/A"]

    return image_urls

def get_description_from_meta_tags(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    response = requests.get(link, headers=headers)
    response.encoding = 'utf-8'  # 确保正确的编码
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    meta_description = soup.find('meta', {'name': 'description'})

    return meta_description['content'] if meta_description else "No description found"


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            title = get_title_from_link(link)
            description = get_description_from_meta_tags(link)
            image_url = get_image_urls_from_meta_tags(link)
            Note.objects.create(link=link, title=title, description=description, image_url=image_url)
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'link_analys/add_note.html', {'form': form})


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'link_analys/note_list.html', {'notes': notes})
