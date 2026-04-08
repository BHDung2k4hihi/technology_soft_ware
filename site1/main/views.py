import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Name


def home(request):
    submitted_name = None
    greeting = None

    # danh sách lời chào
    greetings = [
        'Xin chào!',
        'Chúc bạn một ngày tốt lành!',
        'Rất vui được gặp bạn!',
        'Hãy giữ nụ cười nhé!',
        'Chào bạn đến với trang của tôi!',
    ]

    if request.method == 'POST':
        name_input = request.POST.get('name')

        if name_input:
            # lưu vào DB
            Name.objects.create(name=name_input)

            submitted_name = name_input
            greeting = random.choice(greetings)

            # 👉 tránh reload form bị gửi lại
            return redirect('home')

    # lấy danh sách tên
    names = Name.objects.all().order_by('-created_at')
    total_names = names.count()

    # random background
    backgrounds = [
        'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'linear-gradient(135deg, #ff7e5f 0%, #feb47b 100%)',
        'linear-gradient(135deg, #43cea2 0%, #185a9d 100%)',
        'linear-gradient(135deg, #ff6a00 0%, #ee0979 100%)',
        'linear-gradient(135deg, #00c6ff 0%, #0072ff 100%)',
        'linear-gradient(135deg, #f7971e 0%, #ffd200 100%)',
        'linear-gradient(135deg, #5f2c82 0%, #49a09d 100%)',
        'linear-gradient(135deg, #ff5f6d 0%, #ffc371 100%)',
        'linear-gradient(135deg, #36d1dc 0%, #5b86e5 100%)',
    ]

    page_background = random.choice(backgrounds)

    return render(request, 'main/home.html', {
        'names': names,
        'total_names': total_names,
        'submitted_name': submitted_name,
        'greeting': greeting,
        'page_background': page_background,
    })


# ===== DELETE =====
def delete_name(request, id):
    name = get_object_or_404(Name, id=id)
    name.delete()
    return redirect('home')  