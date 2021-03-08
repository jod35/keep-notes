from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages


from .models import Note

class HomePageView(View):

    template_name='index.html'


    def get(self,request,*args,**kwargs):
        notes=Note.objects.all()

        context={
            'notes':notes
        }
        return render(request,self.template_name,context)


    def post(self,request,*args,**kwargs):
        data=request.POST

        title=data.get('title')
        note=data.get('note')

        new_note=Note(title=title,note=note)

        new_note.save()

        messages.success(request,"Note Created")

        return redirect('notes:home')


class NoteDeleteView(View):
    def get(self,request,id,*args,**kwargs):
        note_to_delete=Note.objects.filter(id=id).first()

        note_to_delete.delete()

        messages.warning(request,"Note Deleted")

        return redirect('notes:home')

class NoteUpdateView(View):
    template_name='update.html'

    def get(self,request,id,*args,**kwargs):
        note_to_update=Note.objects.filter(id=id).first()

        context={
            'note':note_to_update
        }

        return render(request,self.template_name,context)

    def post(self,request,id,*args,**kwargs):
        note_to_update=Note.objects.filter(id=id).first()

        data=request.POST

        updated_title=data.get('title')
        updated_note=data.get('note')

        note_to_update.title=updated_title
        note_to_update.note=updated_note

        note_to_update.save()

        messages.info(request,'Note Updated')

        return redirect('notes:home')




