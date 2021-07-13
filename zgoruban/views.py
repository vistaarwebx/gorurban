from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zgoruban.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from rurban.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User

def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['usr']
        p = d['pass']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('admin_index')
        else:
            error = True
    d = {'error': error}
    return render(request, "login.html", d)

def FORGOT(request):
    error = False
    form = False
    udata = False
    if request.method == "POST":
        dd = request.POST
        name = dd["form"]
        if name == "submit email":
            e = dd['em']
            user = User.objects.filter(email = e)
            if user:
                form = True
                udata = user[0]
            else:
                error = True
        if name == 'submit pwd':
            p = dd ['pwd']
            c = dd ['cpwd']
            u = dd ['idd']
            user = User.objects.get(id=u)
            user.set_password(p)
            user.save()
            return redirect ('Login')
    d = {"form":form,"error":error,"udata":udata}
    return render(request,'forgot.html',d)

def LOGOUT(request):
    logout(request)
    return redirect('home')

def Home(request):
    if request.method == "POST":
        newsl = request.POST['newsletter']
        EMAIL_LETTERS.objects.create(mubmail=newsl)
    test = TESTIMONY.objects.all()
    fiv = GALLERY.objects.filter(Year="2021").order_by('-id')
    fou = GALLERY.objects.filter(Year="2020").order_by('-id')
    thre = GALLERY.objects.filter(Year="2019").order_by('-id')
    two = GALLERY.objects.filter(Year="2018").order_by('-id')
    neww = NEWSS.objects.all().order_by('-id')
    evee = EVENTSS.objects.all().order_by('-id')
    abo = BANNER_ABOUT.objects.all()
    cam = BANNER_CAMPS.objects.all()
    ana = BANNER_ANANTMANDI.objects.all()
    sto = BANNER_STORE.objects.all()
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    new = neww[:8]
    eve = evee[:8]
    fou1 = fou[:6]
    fou2 = fou[6:12]
    fou3 = fou[12:18]
    thre1 = thre[:6]
    thre2 = thre[6:12]
    thre3 = thre[12:18]
    two1 = two[:6]
    two2 = two[6:12]
    two3 = two[12:18]
    fi = fiv[:6]
    fi2 = fiv[6:12]
    fi3 = fiv[12:18]
    d = {"fi": fi,"fi2":fi2,"fi3":fi3,"fou1":fou1,"fou2":fou2,"fou3":fou3,"thre1":thre1,"thre2":thre2,"thre3":thre3,"two1":two1,"two2":two2,"two3":two3,"test":test,"new":new,"eve":eve,"abo":abo,"cam":cam,"ana":ana,"sto":sto,"zcmap":zcmap,"test":test}
    return render(request, 'index.html',d)

def CONTACT(request):
    if request.method == "POST":
        c = request.POST
        cname = c['first-name']
        clname = c['last-name']
        cemail = c['email']
        cmobile = c['phone']
        cmessage = c['message']
        email = 'tejendrapatel1998@gmail.com'
        subject = "Contact US Requests "
        content = "Prospectias"
        Contact.objects.create(fname=cname, lname=clname, mob=cmobile, email=cemail,message=cmessage)
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
        d = {'cname': cname, 'clname': clname, "cemail": cemail, "cmobile": cmobile, "cmessage": cmessage}
        html = get_template('email3.html').render(d)
        msg.attach_alternative(html, 'text/html')
        msg.send()
        return redirect('contact')
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"zcmap":zcmap}
    return render(request, 'contact.html',d)

def OPPURTUNITIES(request):
    if request.method == "POST":
        c = request.POST
        fna = c['fname']
        lna = c['lname']
        mobb = c['mob']
        emm = c['email']
        agg = c['age']
        roll = c['role']
        addd = c['add']
        mess = c['message']
        Oppurtunities.objects.create(fname=fna, lname=lna, mob=mobb, age=agg,email=emm, role=roll ,address=addd ,message=mess )
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"zcmap": zcmap}
    return render(request, 'oppurtunuties.html',d)

def CAMPS(request):
    mos = Go_Ruban_Motive.objects.all()
    cam = Camps.objects.all()
    mo = mos[:1]
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"mo":mo,"cam":cam,"zcmap": zcmap}
    return render(request, 'camps.html',d)



def GALLERYS(request):
    fir = GALLERY.objects.filter(Year="2017")
    sec = GALLERY.objects.filter(Year="2018")
    thi = GALLERY.objects.filter(Year="2019")
    fou = GALLERY.objects.filter(Year="2020")
    fiv = GALLERY.objects.filter(Year="2021")
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"fir":fir,"sec":sec,"thi":thi,"fou":fou,"fiv":fiv,"zcmap": zcmap}
    return render(request, 'gallery.html',d)

def ABOUT(request):
    abo = About.objects.filter(heading="About Gorurban")
    his = About.objects.filter(heading="History Gorurban")
    obj = About.objects.filter(heading="Objective Gorurban")
    team = Team.objects.all()
    mcm = Camps.objects.all()
    zcmap = mcm[:3]

    d = {"abo":abo,"his":his,"obj":obj,"team":team,"zcmap": zcmap}
    return render(request, 'about.html',d)

def BLOGSS(request):
    blo = BLOGS.objects.all()
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"blo":blo,"zcmap": zcmap}
    return render(request, 'blogs.html',d)

def DEMO(request):
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"zcmap": zcmap}
    return render(request, 'video_header.html',d)

def EVENTS(request):
    fir = EVENTSS.objects.filter(Year="2017")
    sec = EVENTSS.objects.filter(Year="2018")
    thi = EVENTSS.objects.filter(Year="2019")
    fou = EVENTSS.objects.filter(Year="2020")
    fiv = EVENTSS.objects.filter(Year="2021")
    mcm = Camps.objects.all()
    zcmap = mcm[:3]

    d = {"fir": fir, "sec": sec, "thi": thi, "fou": fou, "fiv": fiv,"zcmap": zcmap}
    return render(request, 'events.html',d)

def NEWS(request):
    fir = NEWSS.objects.filter(Year="2017")
    sec = NEWSS.objects.filter(Year="2018")
    thi = NEWSS.objects.filter(Year="2019")
    fou = NEWSS.objects.filter(Year="2020")
    fiv = NEWSS.objects.filter(Year="2021")
    mcm = Camps.objects.all()
    zcmap = mcm[:3]

    d = {"fir": fir, "sec": sec, "thi": thi, "fou": fou, "fiv": fiv,"zcmap": zcmap}
    return render(request, 'news.html',d)

def TERMS_CONDITIONS(request):
    ter = TERMS_CONDITIONSs.objects.all()
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"ter": ter,"zcmap": zcmap}
    return render(request, 'terms_conditions.html',d)

def PRIVACY_POLICY(request):
    ter = PRIVACY_POLICYs.objects.all()
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"ter": ter,"zcmap": zcmap}
    return render(request, 'privacy_policy.html',d)

def PAYMENT_PROCEDURE(request):
    ter = PAYMENT_PROCEDUREs.objects.all()
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"ter": ter,"zcmap": zcmap}
    return render(request, 'payment_procedure.html',d)

##########        dynamic functions    ##############

def BLOG_SINGLE(request,blo_id):
    blosingle = BLOGS.objects.get(id=blo_id)
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"blosingle":blosingle,"zcmap": zcmap}
    return render(request, 'blog_dynamic.html',d)

def CAMPS_SINGLE(request,cmp_id):
    blosingle = Camps.objects.get(id=cmp_id)
    par = CAMPparticipants.objects.filter(imag=blosingle)
    gal = GALLERY.objects.filter(campname=blosingle)
    new = NEWSS.objects.filter(campname=blosingle)
    mcm = Camps.objects.all()
    zcmap = mcm[:3]
    d = {"blosingle": blosingle,"par":par,"gal":gal,"new":new,"zcmap": zcmap}
    return render(request, 'camps_dynamic.html',d)

###########      admin pannel        ########

def ADMIN_YOUTUBE(request):
 
    return render(request, 'admin_youtube.html')


def ADMIN_INDEX(request):
    li = [ ]
    em1 = EMAIL_LETTERS.objects.all()
    for i in em1:
        li.append(i.mubmail)
    if request.method == "POST":
        if 'new' in request.POST:
            c = request.POST
            subject = c['sub']
            imgg = c['img']
            content = c['msg']
            email = li
            # Contact.objects.create(fname=cname, lname=clname, mob=cmobile, email=cemail,message=cmessage)
            msg = msg = EmailMultiAlternatives(subject, content, EMAIL_HOST_USER,email)
            d = {'subject': subject, "imgg": imgg, "content": content}
            html = get_template('email.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('admin_index')
        elif 'pos' in request.POST:
            imgg = request.FILES['imagg']
            EMIMG.objects.create(imagess=imgg )
            return redirect('admin_index')
    podd =  EMIMG.objects.latest('id')
    opps = Oppurtunities.objects.all().order_by('-id')
    cons = Contact.objects.all().order_by('-id')
    cam = Camps.objects.all().order_by('-id')
    opp = opps[:5]
    con = cons[:5]
    emp = Team.objects.all()
    d = {"opp":opp,"con":con,"emp":emp,"cam":cam,"podd":podd}
    return render(request, 'admin_index.html',d)

def ADMIN_CONTACT(request):
    con = Contact.objects.all()
    d = {"con":con}
    return render(request, 'admin_contact.html',d)

def ADMIN_OPPORTUNITIES(request):
    opp = Oppurtunities.objects.all()
    d = {"opp":opp}
    return render(request, 'admin_oppurtunities.html',d)

def ADMIN_MAIl(request):
    li = [ ]
    em1 = EMAIL_LETTERS.objects.all()
    for i in em1:
        li.append(i.mubmail)
    if request.method == "POST":
        if 'em' in request.POST:
            c = request.POST
            email = c['emi']
            subject = c['sub']
            imgg = c['img']
            content = c['msg']
            # Contact.objects.create(fname=cname, lname=clname, mob=cmobile, email=cemail,message=cmessage)
            msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
            d = {'email': email, 'subject': subject, "imgg": imgg, "content": content}
            html = get_template('email.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('admin_mail')
        elif 'new' in request.POST:
            c = request.POST
            subject = c['sub']
            imgg = c['img']
            content = c['msg']
            email = li
            # Contact.objects.create(fname=cname, lname=clname, mob=cmobile, email=cemail,message=cmessage)
            msg = msg = EmailMultiAlternatives(subject, content, EMAIL_HOST_USER,email)
            d = {'subject': subject, "imgg": imgg, "content": content}
            html = get_template('email.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('admin_mail')
        
    return render(request, 'admin_mail.html')

def ADMIN_ABOUT(request):
    abo = About.objects.get(id=1)
    abo2 = About.objects.get(id=2)
    abo3 = About.objects.get(id=3)
    emp = Team.objects.all()
    if request.method == "POST":
        if 'about' in request.POST:
            c = request.POST
            hedd = c['head']
            parr = c['para']
            imgg = request.FILES['img']
            abow = About.objects.filter(id=1)
            abow.update(heading=hedd,paragraph=parr,image1=imgg)
            return redirect('admin_about')
        elif 'history' in request.POST:
            c = request.POST
            hedd = c['head']
            parr = c['para']
            imgg = request.FILES['img']
            abow = About.objects.filter(id=2)
            abow.update(heading=hedd,paragraph=parr,image1=imgg)
            return redirect('admin_about')
        elif 'objective' in request.POST:
            c = request.POST
            hedd = c['head']
            parr = c['para']
            imgg = request.FILES['img']
            abow = About.objects.filter(id=3)
            abow.update(heading=hedd,paragraph=parr,image1=imgg)
            return redirect('admin_about')
        elif 'team' in request.POST:
            c = request.POST
            nam = c['head']
            mobi = c['mob']
            imgg = request.FILES['img']
            idobbb = c['dobb']
            emaill = c['emai']
            desi = c['desig']
            Team.objects.create(name=nam,mobile=mobi,image1=imgg,dob=idobbb,email=emaill,designation=desi)
            return redirect('admin_about')
    d = {"emp":emp,"abo":abo,"abo2":abo2,"abo3":abo3}
    return render(request, 'admin_about.html',d)

def ADMIN_HOME(request):
    if request.method == "POST":
        if 'testi' in request.POST:
            c = request.POST
            nam = c['cat']
            posit = c['head']
            imgg = request.FILES['img']
            detai = c['det']
            face = c['fb']
            linkedi = c['link']
            insta = c['inst']
            twitt = c['twit']
            TESTIMONY.objects.create(name=nam,position=posit,image=imgg,Detail=detai,facebook=face,linkedin=linkedi,instagram=insta,twitter=twitt)
            return redirect('admin_home')

        elif 'bann' in request.POST:
            c = request.POST
            posit = c['about']
            bans = BANNER_ABOUT.objects.filter(id = 1)
            bans.update(Discription=posit)
            return redirect('admin_home')
    test = TESTIMONY.objects.all()
    ban = BANNER_ABOUT.objects.get(id = 1)
    d = {"test":test,"ban":ban}      
    return render(request, 'admin_home.html',d)

def ADMIN_HOME2(request):
    if request.method == "POST":
        if 'testi' in request.POST:
            c = request.POST
            nam = c['cat']
            posit = c['head']
            imgg = request.FILES['img']
            detai = c['det']
            face = c['fb']
            linkedi = c['link']
            insta = c['inst']
            twitt = c['twit']
            TESTIMONY.objects.create(name=nam,position=posit,image=imgg,Detail=detai,facebook=face,linkedin=linkedi,instagram=insta,twitter=twitt)
            return redirect('admin_home2')

        elif 'bann' in request.POST:
            c = request.POST
            posit = c['about']
            bans = BANNER_CAMPS.objects.filter(id = 1)
            bans.update(Discription=posit)
            return redirect('admin_home2')
    test = TESTIMONY.objects.all()
    ban = BANNER_CAMPS.objects.get(id = 1)
    d = {"test":test,"ban":ban}      
    return render(request, 'admin_home2.html',d)

def ADMIN_HOME3(request):
    if request.method == "POST":
        if 'testi' in request.POST:
            c = request.POST
            nam = c['cat']
            posit = c['head']
            imgg = request.FILES['img']
            detai = c['det']
            face = c['fb']
            linkedi = c['link']
            insta = c['inst']
            twitt = c['twit']
            TESTIMONY.objects.create(name=nam,position=posit,image=imgg,Detail=detai,facebook=face,linkedin=linkedi,instagram=insta,twitter=twitt)
            return redirect('admin_home3')

        elif 'bann' in request.POST:
            c = request.POST
            posit = c['about']
            bans = BANNER_ANANTMANDI.objects.filter(id = 1)
            bans.update(Discription=posit)
            return redirect('admin_home3')
    test = TESTIMONY.objects.all()
    ban = BANNER_ANANTMANDI.objects.get(id = 1)
    d = {"test":test,"ban":ban}      
    return render(request, 'admin_home3.html',d)

def ADMIN_HOME4(request):
    if request.method == "POST":
        if 'testi' in request.POST:
            c = request.POST
            nam = c['cat']
            posit = c['head']
            imgg = request.FILES['img']
            detai = c['det']
            face = c['fb']
            linkedi = c['link']
            insta = c['inst']
            twitt = c['twit']
            TESTIMONY.objects.create(name=nam,position=posit,image=imgg,Detail=detai,facebook=face,linkedin=linkedi,instagram=insta,twitter=twitt)
            return redirect('admin_home4')

        elif 'bann' in request.POST:
            c = request.POST
            posit = c['about']
            bans = BANNER_STORE.objects.filter(id = 1)
            bans.update(Discription=posit)
            return redirect('admin_home4')
    test = TESTIMONY.objects.all()
    ban = BANNER_STORE.objects.get(id = 1)
    d = {"test":test,"ban":ban}      
    return render(request, 'admin_home4.html',d)

def ADMIN_CAMPS(request):
    if request.method == "POST":
        if 'cpma' in request.POST:
            c = request.POST
            cname = c['cmpp']
            dayy = c['day']
            strdte = c['strda']
            dimg = request.FILES['img']
            sdeta = c['det']
            text = c['about']
            Camps.objects.create(camp_name=cname,no_of_days=dayy,date=strdte,image=dimg,detail=sdeta,content=text)
    camp = Camps.objects.all()
    d = {"camp":camp}
    return render(request, 'admin_camps.html',d)

def ADMIN_NEWS(request):
    if request.method == "POST":
        campna = request.POST['cam']
        nyear = request.POST['year']
        nimg = request.FILES['img']
        fir = Camps.objects.get(camp_name=campna)
        fir.content = campna
        fir.save()
        NEWSS.objects.create(Year=nyear, image=nimg)
    camp = Camps.objects.all()
    fir = NEWSS.objects.filter(Year="2018")
    sec = NEWSS.objects.filter(Year="2018")
    thi = NEWSS.objects.filter(Year="2019")
    fou = NEWSS.objects.filter(Year="2020")
    fiv = NEWSS.objects.filter(Year="2021")
    d = {"fir": fir, "sec": sec, "thi": thi, "fou": fou, "fiv": fiv,"camp":camp}
    return render(request, 'admin_news.html',d)

def ADMIN_GALLERY(request):
    if request.method == "POST":
        campna = request.POST['cam']
        nyear = request.POST['year']
        nimg = request.FILES['img']
        fir = Camps.objects.get(camp_name=campna)
        fir.content = campna
        fir.save()
        GALLERY.objects.create(Year=nyear,image=nimg)
    camp = Camps.objects.all()
    fir = GALLERY.objects.filter(Year="2018")
    sec = GALLERY.objects.filter(Year="2018")
    thi = GALLERY.objects.filter(Year="2019")
    fou = GALLERY.objects.filter(Year="2020")
    fiv = GALLERY.objects.filter(Year="2021")
    d = {"fir": fir, "sec": sec, "thi": thi, "fou": fou, "fiv": fiv,"camp":camp}
    return render(request, 'admin_gallery.html',d)

def ADMIN_BLOGS(request):
    if request.method == "POST":
        bcat = request.POST['cat']
        bhead = request.POST['head']
        bimg = request.FILES['img']
        bdet = request.POST['det']
        btxt = request.POST['txt']
        btag = request.POST['tag']
        BLOGS.objects.create(category=bcat,Heading=bhead,image1=bimg,Detail=bdet,Discription=btxt,tags=btag)
    bl = BLOGS.objects.all()
    d = {"bl":bl}
    return render(request, 'admin_blogs.html',d)

def ADMIN_EVENTS(request):
    if request.method == "POST":
        campna = request.POST['cam']
        nyear = request.POST['year']
        nimg = request.FILES['img']
        fir = Camps.objects.get(camp_name=campna)
        fir.content = campna
        fir.save()
        EVENTSS.objects.create(Year=nyear, image=nimg)
    camp = Camps.objects.all()

    fir = EVENTSS.objects.filter(Year="2018")
    sec = EVENTSS.objects.filter(Year="2018")
    thi = EVENTSS.objects.filter(Year="2019")
    fou = EVENTSS.objects.filter(Year="2020")
    fiv = EVENTSS.objects.filter(Year="2021")
    d = {"fir": fir, "sec": sec, "thi": thi, "fou": fou, "fiv": fiv,"camp":camp}
    return render(request, 'admin_events.html',d)


#####     admin delete ####

def ADMIN_GALLERY_DELETE(request,del_id):
    GALLERY.objects.get(id=del_id).delete()
    return redirect('admin_gallery')

def ADMIN_NEWS_DELETE(request,del_id):
    NEWSS.objects.get(id=del_id).delete()
    return redirect('admin_news')

def ADMIN_EVENTS_DELETE(request,del_id):
    EVENTSS.objects.get(id=del_id).delete()
    return redirect('admin_events')

def ADMIN_BLOGS_DYNAMICC_DELETE(request,del_id):
    BLOGS.objects.get(id=del_id).delete()
    return redirect('admin_blogs')

def ADMIN_TEAM_DELETE(request,del_id):
    Team.objects.get(id=del_id).delete()
    return redirect('admin_about')

def ADMIN_TESTIMONY_DELETE(request,del_id):
    TESTIMONY.objects.get(id=del_id).delete()
    return redirect('admin_home')

def ADMIN_CAMPS_DELETE(request,del_id):
    Camps.objects.get(id=del_id).delete()
    return redirect('admin_camps')

def ADMIN_PARTICPANT_DELETE(request,del_id):
    CAMPparticipants.objects.get(id=del_id).delete()
    return redirect('admin_camps')



    ####  admin dynamic functions  #####

def ADMIN_BLOGS_DYNAMICC(request,bdy_id):
    blosingle = BLOGS.objects.get(id=bdy_id)
    d = {"blosingle":blosingle}
    return render(request, 'admin_blogs_dynamic.html',d)

def ADMIN_CAMPS_DYNAMICC(request,camp_id):
    if request.method == "POST":
        campna = request.POST['nam']
        nyear = request.POST['des']
        nimg = request.FILES['img']
        blosing = Camps.objects.get(id=camp_id)
        CAMPparticipants.objects.create(imag = blosing, image1=nimg,designation=nyear,name=campna)
    
    blosingle = Camps.objects.get(id=camp_id)
    par = CAMPparticipants.objects.filter(imag=blosingle)
    d = {"blosingle":blosingle,"par":par}
    return render(request, 'admin_camps_dynamic.html',d)


