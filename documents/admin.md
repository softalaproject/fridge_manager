## <a id="start"></a>Django admin creation & usage

### Shortcuts:

[Admin UI usage](#admin-ui)
<br>
<br>
<br>

**1 Make your admin login creditentals to .env file** (`remember add .env to .gitignore`)

![](dotenv_example.jpg)**location <app_root>/.env**
<br/>
<br/>

**2 Adding docker-compose.yml `python <app_root>/manage.py createsuperuser --no-input` script command**

![](compose.yml_example.jpg)

**3 Git add changes, commit & push**


**4 Go into deployed admin interface & test login creditentals working**


**5 Remove or comment createsuperuser script from docker-compose.yml**
<br>

****

**<a id="admin-ui"></a>6 Admin UI usage & functionalities:**
<br>

![](suBaseView.jpg)

    Once you have registered your app or apps with admin it appears under Authentication & authorization in own section.
    You can add or change existing objects from here in this case fridges.
<br>

**Add fridges view:**

    Defaults helps adding & creating own case sensitive values for fridges. 
    After done with inputs press save button & it should notify your recent creation.

**Change existing fridges view:**

    Again same values appears while editing your app objects.
    Once decided new relevant values press save button and djnago seds notification for you succeeded edit.  

**Delete fridges view:**


    Select "Delete selected fridges" from shown dropdown. Then when decide you're done press go-button. 
    Django should throw warning & ask confirm action. 

[Return to start of document](#start)