from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from django.contrib.auth.decorators import login_required
from .forms import VideoUploadForm

# Create your views here.

def home(request):
    videos = Video.objects.all()
    return render(request, 'video_app/home.html', {'videos': videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    videos = Video.objects.exclude(pk=pk)
    return render(request, 'video_app/video_detail.html', {
        'video': video,
        'videos': videos
    })


@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploader = request.user
            video.save()
            return redirect('video_app:video_detail', pk=video.pk)
    else:
        form = VideoUploadForm()
    return render(request, 'video_app/upload_video.html', {'form': form})