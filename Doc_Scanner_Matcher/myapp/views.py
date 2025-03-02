from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .models import CreditRequest, Document
from django.contrib.auth.decorators import login_required
from .utils import reset_credits
from .utils import find_matches,ai_find_matches
from django.http import HttpResponse
from django.utils import timezone

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request,user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
    return render(request,'login.html')

def home(request):
    context = {
        'username': request.user.username  
    }
    return render(request,'home.html',context)

@login_required
def profile(request):
    profile = request.user.userprofile
    scans = Document.objects.filter(user=request.user)
    requests = CreditRequest.objects.filter(user=request.user)
    reset_credits()
    return render(request, 'profile.html', {
        'credits': profile.credits,
        'scans': scans,
        'requests': requests
    })
            

@login_required
def request_credits(request):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        CreditRequest.objects.create(user=request.user, requested_credits=amount)
        return redirect('profile')
    return render(request, 'creditsrequest.html')

@login_required
def admin_credits(request):
    if not request.user.is_staff:
        return redirect('profile')
    if request.method == 'POST':
        req_id = request.POST['request_id']
        action = request.POST['action']
        credit_req = CreditRequest.objects.get(id=req_id)
        if action == 'approve':
            credit_req.user.userprofile.credits += credit_req.requested_credits
            credit_req.status = 'approved'
            credit_req.user.userprofile.save()
        else:
            credit_req.status = 'denied'
        credit_req.save()
    requests = CreditRequest.objects.filter(status='pending')
    return render(request, 'admincredits.html', {'requests': requests})


@login_required
def scan_document(request):
    profile = request.user.userprofile
    if profile.credits < 1:
        return render(request, 'no_credits.html')
    if request.method == 'POST':
        file = request.FILES['file']
        content = file.read().decode('utf-8')  
        doc = Document.objects.create(user=request.user, file=file, content=content)
        profile.credits -= 1
        profile.save()
        return redirect('matches', doc_id=doc.id)
    return render(request, 'scan.html')



@login_required
def matches(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    matches = ai_find_matches(doc)
    return render(request, 'matches.html', {'doc': doc, 'matches': matches})

@login_required
def document_detail(request, doc_id):

    doc = get_object_or_404(Document, id=doc_id)
    return render(request, 'document_detail.html', {'doc': doc})

@login_required
def download_scan_history(request):
    
    scans = Document.objects.filter(user=request.user)

    content = f"Scan History for {request.user.username}\n\n"
    for scan in scans:
        content += f"Document: {scan.file.name}\n"
        content += f"Scanned At: {scan.uploaded_at}\n"
        content += "=" * 50 + "\n\n"

    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="scan_history_{request.user.username}.txt"'
    return response

