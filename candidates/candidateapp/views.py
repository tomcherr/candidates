from django.shortcuts import render


from django.shortcuts import render
from django.shortcuts import render, redirect  
from candidateapp.forms import candidateForm
from candidateapp.models import Candidatedirectory
def emp(request):  
    if request.method == "POST":  
        form = candidateForm(request.POST)  
        if form.is_valid() :  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = candidateForm() 
    return render(request,'index.html',{'form':form})  
def show(request):  
    candidates = Candidatedirectory.objects.all() 
    return render(request,"show.html",{'candidates':candidates})  
def edit(request, id):  
    candidate = Candidatedirectory.objects.get(id=id)  
    return render(request,'edit.html', {'candidate':candidate})  
def update(request, id):
    candidate = Candidatedirectory.objects.get(id=id)
    
    if request.method == 'POST':
        form = candidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect("/show")
    else:
        form = candidateForm(instance=candidate)  
    
    return render(request, 'edit.html', {'form': form, 'candidate': candidate})



def destroy(request, id):  
    candidate = Candidatedirectory.objects.get(id=id)  
    candidate.delete()  
    return redirect("/show")
