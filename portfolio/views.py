from django.shortcuts import render
import smtplib
# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def thank(request):
    if request.method == 'POST':
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login("himon.choton@gmail.com", "Himonchoton@18")
        # message to be sent
        message = "Subject:  "+str(request.POST['subject'])+"\n\n\n\n Name = "+str(request.POST['name']) + "\n Emaiil = " +str(request.POST['email']) + "\n\n Message = " + str(request.POST['message']) 
        # sending the mail
        print(type(message))
        print(message)
        #message = "uhasiodhasioudasiuhdc iasnhdviaushvriaweuvnhriavnuhdiasdvas asiludvhasidjASDp vasjodvsadvd;as;dasl;dvas;vd;evlwojejqiweolwq;lasv;asd"
        s.sendmail("himon.choton@gmail.com", "himondas18@gmail.com", message)
        
        # terminating the session
        s.quit()
        return render(request, 'portfolio/thank.html')
    else:
        return render(request, 'portfolio/thank.html')